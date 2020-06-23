# -*- coding: utf-8 -*-

from odoo import models, api, _, fields
from odoo.exceptions import ValidationError
from math import *
from datetime import *

class PrintPayrollReport(models.TransientModel):
	_name = 'print.payrollpdf.report'

	date_debut = fields.Date(string="Date de débuit")
	date_fin = fields.Date(string="Date de fin")

	def print_report(self):
		data = {}

		heads_list = []
		heads = self.env['hr.salary.rule'].search([('active', 'in', (True, False))], order='sequence asc')
		list = []
		for head in heads:
			list = [head.name, head.code]
			heads_list.append(list)

		payslip_ids=self.env['hr.payslip'].search([('date_from','=',self.date_debut),('date_to','=',self.date_fin)])
		list_report = []
		for payslip in payslip_ids:
			vals = {
				'employee_id': payslip.employee_id,
				'employee_name' : payslip.employee_id.name,
				'date_from':payslip.date_from.strftime('%B %Y'),
				# 'matricule' : payslip.employee_id.matricule,
			}
			

			lines_list = []
			for line in payslip.line_ids:
				lines ={
					
					'code' : line.code,
					'name' : line.name,
					'total' : line.total,
				}
				lines_list.append(lines)

			
			vals['lines'] = lines_list
			list_report.append(vals)

		# totoal générle

		total = []
		sous_total = 0
		for h in heads_list:
			for p in payslip_ids:
				for l in p.line_ids:
					if h[1] == l.code:
						sous_total += l.total
			total.append(sous_total)
			sous_total=0
			
		total_name = {
			'employee_id': '10',
			'employee_name' : 'Total',
			'date_from':'',
			'matricule' :''
		}
		vals_total = []
		for t in range(0,len(total)):
			lines_total ={				
				'code' : heads_list[t][1],
				'name' : heads_list[t][0],
				'total' : total[t],
			}
			vals_total.append(lines_total)


		total_name['lines'] = vals_total

		list_report.append(total_name)


		#traitement par lot de 7

		nombre_de_chiffre = len(list_report)
		nombre_par_page = 7
		nombre_de_page = int(ceil(nombre_de_chiffre/nombre_par_page))

		toute_les_liste_a_traiter = []


		index = 0

		for i in range(0, nombre_de_page):
			liste_a_traiter =[]
			for c in list_report:
				if list_report.index(c) >= index and list_report.index(c) < index + nombre_par_page:
					liste_a_traiter.append(c)
			index += nombre_par_page
			toute_les_liste_a_traiter.append(liste_a_traiter)


		# Data a envoyer au template d'imprission
		data['heads'] = heads_list
		data['list_report'] =list_report
		data['toute_les_liste_a_traiter'] = toute_les_liste_a_traiter
		data['total_general'] = total
		data['nombre_employee'] = len(payslip_ids)

		return self.env.ref('th_paie_pdf_report.payroll_pdf_view_report').report_action(self, data=data)