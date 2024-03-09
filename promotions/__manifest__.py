# -*- coding: utf-8 -*-
{
    'name': "Promociones",

    'summary': """
        Módulo de gestión de promociones para proyecto final""",

    'description': """
        Este módulo se encarga de gestionar promociones y descuentos
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
    'depends': ['product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/pro.xml'
    ],
    'application' : True,
    'installable' : True
}