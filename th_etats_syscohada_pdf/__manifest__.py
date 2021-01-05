# -*- coding: utf-8 -*-
{
    'name': 'Etats syscohada en pdf',
    'version': '0.2.0',
#     'price': 315.99,
    'currency': 'EUR',
    'license': 'AGPL-3',
    'summary': """
       Imprimer les états de base sysohada au format pdf
    """,
    'category': 'Tools',
    'author': 'ZEN ROOTS-TECHNOLOGIES',
    'maintainer': 'ZEN ROOTS-TECHNOLOGIES',
    'company': 'ZEN ROOTS-TECHNOLOGIES',
    'website': 'https://roots-technologies.com',
    'depends': ['base', 'account', ],
    'data': [
        'wizards/imprimer_bilan.xml',
        'wizards/compte_resultat.xml',
        'wizards/flux_tresorerie.xml',
        'views/report_bilan_view.xml',
        'views/report_compte_resultat_view.xml',
        'views/report_flux_tresorerie_view.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
