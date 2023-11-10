# -*- coding: utf-8 -*-
{
    'name': "Equipo de Ventas",

    'description': """
        En este módulo se han creado dos grupos de seguridad nuevos para las ventas, llamados "operadores" y "supervisores".
        Estos grupos van vinculados a los equipos de ventas, siendo el supervisor el lider del equipo y los operadores los miembros del equipo.
        Y se han modificado los permisos de los usuarios para que solo puedan las ventas y oportunidad de su equipo, mientras que el supervisor también puedas editarlas.
    """,

    'version': '1',

    'license': 'LGPL-3',
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

    'application': True,
    'installable': True,
    'auto_install': False
}
