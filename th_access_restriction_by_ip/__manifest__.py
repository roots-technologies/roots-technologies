# -*- coding: utf-8 -*-
{
    'name': "Restriction d'accès par IP",
    'summary': """L'utilisateur peut accéder à son compte uniquement à partir de l'adresse IP spécifiée""",
    'version': '0.1',
    'description': """L'utilisateur peut accéder à son compte uniquement à partir de l'adresse IP spécifiée""",
    'author': 'ROOTS-TECHNOLOGIES',
    'company': 'ROOTS-TECHNOLOGIES',
    'website': 'https://www.roots-technologies.com',
    'category': 'Roots',
    'depends': ['base', 'mail'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/allowed_ips_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

