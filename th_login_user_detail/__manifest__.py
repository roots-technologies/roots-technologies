# -*- coding: utf-8 -*-
{
    'name': "Détails de connexion un utilisateur Odoo",
    'version': '0.1',
    'summary': """Détails de l'utilisateur et adresse IP de connexion""",
    'description': """Ce module enregistre les informations de connexion de l'utilisateur""",
    'author': "Roots-Technologies",
    'company': "Roots-Technologies",
    'maintainer': 'Roots-Technologies',
    'website': "https://www.roots-Technologies.com",
    'category': 'Roots',
    'depends': ['base'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/login_user_views.xml'],
    'demo': [],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
