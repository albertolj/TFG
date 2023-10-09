# -*- coding: utf-8 -*-
{
    'name': "Tarifas Wizard",

    'description': """
        Cuando una persona que no sea el administrador intente vender un producto por debajo de la tarifa,
        se genera un nuevo estado en las ventas llamado "pendiente de aprobación" para que solo un administrador 
        pueda confirmar ese pedido de venta.
    """,



    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/boton_confirmar_tarifa.xml',
        'wizard/tarifa_wizard_view.xml'
    ],
    # only loaded in demonstration mode

    'application': True,
    'installable': True,
    'auto_install': False
}
