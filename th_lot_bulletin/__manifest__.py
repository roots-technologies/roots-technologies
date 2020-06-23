# -*- coding: utf-8 -*-
{
	'name': 'Lot des Bulletins de Paie',
	'version': '1.0',
	'summary': 'Générer le bulletin de paie',
	'category': 'Tools',
	'author': 'Thomas ATCHA',
	'maintainer': 'ROOTS-TECHNOLOGIES',
	'company': 'ROOTS-TECHNOLOGIES',
	'website': 'https://www.roots-technologies.com',
	'depends': ['base','hr_payroll','hr','account'],
	'data': [
		'views/lot_view.xml',
		'security/ir.model.access.csv',
	],
	'images': [],
	'license': 'AGPL-3',
	'installable': True,
	'application': False,
	'auto_install': False,
}