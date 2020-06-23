# -*- coding: utf-8 -*-
from odoo import api, models, modules, fields, _
from odoo.exceptions import ValidationError
from datetime import datetime
import json

class HrLoBulletin(models.Model):
    _name = 'hr.lotbulletin'
    _description = 'Ajouter la fonctionnalté de lot de bulletion'

    name = fields.Char(
        string='Nom du lot de bulletion',
        required=True,

    )
    date_from = fields.Date(
        string='Date de début',
        required=True,

    )
    date_to = fields.Date(
        string='Date de fin',
        required=True,

    )
    credit_note = fields.Boolean(
        string='Avoir',

    )

    bulletin_ids = fields.One2many(
        'hr.payslip',
        'my_run',
        string='Bulletins de paie',
    )
    journal_id = fields.Many2one(
        'account.journal',
        string='Journal de paie',

    )
    date_comptable = fields.Date(
         string='Date comptable',

         default=datetime.today().strftime('%Y-%m-%d'),
     ) 
    def genere_payslips(self):
        employee_ids = self.env['hr.employee'].search([])
        payslip_ids = self.env['hr.payslip'].search([('my_run','=',self.id)])
        # raise ValidationError(_(len(payslip_ids)))
        for p in payslip_ids:
            p.unlink()
        for el in employee_ids:
            vals = {
                'name' : 'Bulletin de paie de ' + el.name + ' pour ' + self.date_to.strftime('%B-%Y'),
                'my_run' : self.id,
                'employee_id' : el.id,
                'date_from' : self.date_from,
                'date_to': self.date_to,
                'contract_id': el.contract_id.id,
                'struct_id': el.contract_id.struct_id.id,  
            }
            self.env['hr.payslip'].create(vals)

    def confim_all_payslip(self):
        for el in self.bulletin_ids:
            el.action_payslip_done()

    def cancel_all_payslip(self):
        for el in self.bulletin_ids:
            el.action_payslip_cancel()

    def draft_all_payslip(self):
        for el in self.bulletin_ids:
            el.action_payslip_draft()

    def calculer_salaire(self):
        for el in self.bulletin_ids:
            el.compute_sheet()

    def comtabiliser_paie(self):
        # line = self.bulletin_ids[0].line_ids[0].salary_rule_id
        move_lines = []
        for b in self.bulletin_ids:
            for line in b.line_ids:
                if line.compte_debit_id.id == False and line.compte_credit_id.id == False:
                    move_lines.append(
                        (0, 0, {
                        'name': line.name,
                        'debit': line.total, 
                        'credit': 0,
                        'account_id': line.salary_rule_id.compte_debit_id.id,
                        'partner_id': None,
                        }),
                    )

                    move_lines.append(
                    (0, 0, {
                        'name': line.name,
                        'debit': 0, 
                        'credit': line.total,
                        'account_id': line.salary_rule_id.compte_credit_id.id,
                        'partner_id': None,
                        }),
                    )

        vals = {
            'date': self.date_comptable,
            'ref': self.name,
            'journal_id': self.journal_id.id,
            'line_ids' : move_lines,
        }
        raise ValidationError(_(move_lines))
        self.env['account.move'].create(vals)


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'
    _description = 'Ajouter un champs au bulletion de paie'

    my_run =  fields.Many2one(
        'hr.lotbulletin',
        string='Lot de bulletion de paie',
        ondelete='cascade',
    )