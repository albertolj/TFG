# -*- coding: utf-8 -*-
{
    'name': "Tarifas Restrictivas",

    'description': """
        Cuando una persona que no sea el administrador intente vender un producto por debajo de la tarifa,
        se genera un nuevo estado en las ventas llamado "pendiente de aprobación" para que solo un administrador 
        pueda confirmar ese pedido de venta.
    """,


    'category': 'Uncategorized',
    'version': '0.1',

    'license' : 'LGPL-3' ,
    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'product','equipoDeVentas'],

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
