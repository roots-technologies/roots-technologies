# -*- coding: utf-8 -*-
{
    'name' : 'Champs de rubriques de paie',
    'version' : '1.2.0',
    'license' : 'AGPL-3',
    'summary' : """
       Ajout des champs de rubriques de paie
    """,
    'category' : 'Tools',
    'author' : 'ZEN ROOTS-TECHNOLOGIES',
    'maintainer' : 'ZEN ROOTS-TECHNOLOGIES',
    'company': 'ZEN ROOTS-TECHNOLOGIES',
    'website' : 'https://roots-technologies.com',
    'depends' : ['base','hr','hr_payroll',],
    'data' : [
        'security/ir.model.access.csv',
        'views.xml',
        'data/data.xml',
        'reports/bulletin_paie.xml',
    ],

    'installable' : True,
    'application' : False,
    'auto_install' : False,
}
