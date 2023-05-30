# -*- coding: utf-8 -*-
{
    'name': "extra4847933",

    'summary': "Gestión de un gimnasio",

    'description': "Módulo para la gestión de un gimnasio",

    'author': "Judith Alende Martínez",
    'website': "ead.murciaeduca.es",

    'category': 'gestión gimnasio',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
