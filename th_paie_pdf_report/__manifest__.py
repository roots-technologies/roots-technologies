# -*- coding: utf-8 -*-
{
    'name' : 'Rapport de paie en PDF',
    'version' : '1.2.0',
    'license' : 'AGPL-3',
    'summary' : """
       Imprimer le livre de paie mensuel en pdf
    """,
    'category' : 'Tools',
    'author' : 'ZEN ROOTS-TECHNOLOGIES',
    'maintainer' : 'ZEN ROOTS-TECHNOLOGIES',
    'company': 'ZEN ROOTS-TECHNOLOGIES',
    'website' : 'https://roots-technologies.com',
    'depends' : ['base','hr_payroll'],
    'data' : [
        'reports/report_view.xml',
        'reports/report_livre_annuel.xml',
        'wizards/payroll_pdf_report.xml',
        'wizards/livre_annuel_pdf.xml',
    ],

    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
