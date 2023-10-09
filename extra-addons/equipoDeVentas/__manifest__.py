# -*- coding: utf-8 -*-
{
    'name': "Equipo de Ventas",

    'description': """
        Grupos de seguridad
    """,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'crm'],

    # always loaded
    'data': [
        
        'security/groups_security.xml',
        'security/rules_security.xml',
        'views/ventas_form.xml',
        'views/crm_form.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False
}
