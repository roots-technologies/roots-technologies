# -*- coding: utf-8 -*-
from odoo import models, api, fields, _
from odoo.exceptions import ValidationError
import re


class FluxTresorerieWizards(models.TransientModel):
    _name = 'flux.tresorerie'

    date_fin = fields.Date(
        string="A la date du",
        default=fields.date.today(),
    )
    est_comptabilise = fields.Boolean(
        string="Inclure les écritures non comptabilisées"
    )

    def imprimer_compte_resultat(self):
        data = {}
        state = 'posted'
        if self.est_comptabilise == True:
            state = 'draft'
        liste_ecriture_comptable_n_1 = []
        liste_ecriture_comptable_n = []
        date_n_1 = str(self.date_fin.year-1) + '-12-31'
        # écriture de l'année n-1
        ecriture_comptable_anne_n_1 = self.env['account.move.line'].search(
            [('date', '<=', date_n_1)])
        for e in ecriture_comptable_anne_n_1:
            if e.move_id.state == state or e.move_id.state == 'posted':
                vals = {
                    'account_id': e.account_id.code,
                    'credit': e.credit,
                    'debit': e.debit,
                    'balance': e.balance,
                }
                liste_ecriture_comptable_n_1.append(vals)
        # ecriture de l'anne n
        ecriture_comptable_anne_n = self.env['account.move.line'].search(
            [('date', '<=', self.date_fin)])
        for e in ecriture_comptable_anne_n:
            if e.move_id.state == state or e.move_id.state == 'posted':
                vals = {
                    'account_id': e.account_id.code,
                    'credit': e.credit,
                    'debit': e.debit,
                    'balance': e.balance,
                }
                liste_ecriture_comptable_n.append(vals)

        actif_circulant_hao = 0
        actif_circulant_hao_amortissement = 0

        # variation de stock
        variation_de_stocks = 0
        variation_de_stocks_de_marchandises = 0
        variation_de_stocks_de_matieres_premieres_et_fournitures_liees = 0
        variation_de_stocks_d_autres_approvisionnements = 0

        for ecriture in ecriture_comptable_anne_n_1:
            if re.match('^485', ecriture['account_id']) or re.match('^488', ecriture['account_id']):
                actif_circulant_hao += ecriture['balance']

            if re.match('^498', ecriture['account_id']):
                actif_circulant_hao_amortissement += ecriture['balance']

            # variation de stock
            if re.match('^6031', ecriture['account_id']):
                variation_de_stocks_de_marchandises += ecriture['balance']

            if re.match('^6032', ecriture['account_id']):
                variation_de_stocks_de_matieres_premieres_et_fournitures_liees += ecriture['balance']

            if re.match('^6033', ecriture['account_id']):
                variation_de_stocks_d_autres_approvisionnements += ecriture['balance']

        variation_de_stocks = variation_de_stocks_de_marchandises + \
            variation_de_stocks_de_matieres_premieres_et_fournitures_liees + \
            variation_de_stocks_d_autres_approvisionnements

        data['actif_circulant_hao_net'] = actif_circulant_hao + \
            actif_circulant_hao_amortissement

        # variation de stock
        data['variation_de_stocks'] = variation_de_stocks
        return self.env.ref('th_etats_syscohada_pdf.flux_tresorerie_pdf_view_report').report_action(self, data=data)
