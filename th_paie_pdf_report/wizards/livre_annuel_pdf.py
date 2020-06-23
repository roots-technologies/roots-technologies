# -*- coding: utf-8 -*-

from odoo import models, api, _, fields
from odoo.exceptions import ValidationError
from math import *
from datetime import *

class PrintPayrollReport(models.TransientModel):
	_name = 'print.paieannuel.report'

	date_debut = fields.Date(string="Date de débuit")
	date_fin = fields.Date(string="Date de fin")

	def print_report(self):
		data = {}
		head_ids = []
		for rule in self.env['hr.salary.rule'].search([]):
			head_ids.append([rule.name,rule.code])

		employee_payroll_report = []
		employee_ids = self.env['hr.employee'].search([])
		for employee in employee_ids:
			vals = {
				'employee_id': employee.id,
				'employee_name' : employee.name,
			}
			employee_payroll_report.append(vals)

		raise ValidationError(_(employee_payroll_report))
		
		for employee_id in employee_payroll_report:
			employee_payslip_ids = self.env['hr.payslip'].search([('employee_id','=',employee_id['employee_id'])])
			payslip_lines = []
			for payslip in employee_payslip_ids:
				if payslip.date_from.strftime('%Y') == self.date_debut.strftime('%Y') and payslip.date_to.strftime('%Y') == self.date_fin.strftime('%Y'):
					for line in payslip.line_ids:
						vals = {
							'code' : line.code,
							'nom' : line.name,
							'total' : line.total,
						}
						payslip_lines.append(vals)

			employee_head_ids = []

			for head in head_ids:
				vals = {
					'code' : head[1],
					'nom' : head[0],
					'total' : 0,
				}
				employee_head_ids.append(vals)

			for head in employee_head_ids:
				total = 0
				for line in payslip_lines:
					if head['code'] == line['code']:
						total += line['total']

				head['total'] = total

			employee_id['lines'] = employee_head_ids

		total = []
		sous_total = 0
		for h in head_ids:
			for p in employee_payroll_report:
				for l in p['lines']:
					if h[1] == l['code']:
						sous_total += l['total']
			total.append(sous_total)
			sous_total=0
			
		total_name = {
			'employee_id': '10',
			'employee_name' : 'Total',
		}
		vals_total = []
		for t in range(0,len(total)):
			lines_total ={				
				'code' : head_ids[t][1],
				'name' : head_ids[t][0],
				'total' : total[t],
			}
			vals_total.append(lines_total)


		total_name['lines'] = vals_total

		employee_payroll_report.append(total_name)


		#Traitement par lot de 7
		nombre_de_chiffre = len(employee_payroll_report)
		nombre_par_page = 6
		nombre_de_page = int(ceil(nombre_de_chiffre/nombre_par_page))

		toute_les_liste_a_traiter = []

		index = 0

		for i in range(0, nombre_de_page):
			liste_a_traiter =[]
			for c in employee_payroll_report:
				if employee_payroll_report.index(c) >= index and employee_payroll_report.index(c) < index + nombre_par_page:
					liste_a_traiter.append(c)
			index += nombre_par_page
			toute_les_liste_a_traiter.append(liste_a_traiter)

		data['heads'] = head_ids
		data['list_report'] =employee_payroll_report
		data['toute_les_liste_a_traiter'] = toute_les_liste_a_traiter
		data['nombre_employee'] = len(self.env['hr.employee'].search([]))
		data['annee'] = self.date_debut.strftime('%Y')
		return self.env.ref('th_paie_pdf_report.paie_annuel_pdf_view_report').report_action(self, data=data)