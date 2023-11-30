# -*- coding: utf-8 -*-
{
    'name': "Purchase extended VZ",

    'summary': "VZ Tech technical test",

    'description': """
        This test consists of adding new fields and views in a model existing Odoo.
    """,

    'author': "Juan Salazar",
    'website': "https://ansaju.itch.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_extended_view_tree.xml',
        'views/purchase_extended_view_tree_kpis.xml',
        'views/purchase_extended_view_tree_order.xml',
        'views/purchase_extended_view_form.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

