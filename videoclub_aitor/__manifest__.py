# -*- coding: utf-8 -*-
{
    'name': "Videoclub",

    'summary': """
        Pelis y mucho más""",

    'description': """
        Módulo de videoclub para SGE
    """,

    'author': "Aitor Clemente Ramos",
    'website': "https://www.yourcompany.com",
    'images': ['static/description/icon.png'],
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/videoclub_security.xml',
        'security/ir.model.access.csv',
        'views/videoclub.xml'
    ],
    'application' : True,
    'installable' : True
}