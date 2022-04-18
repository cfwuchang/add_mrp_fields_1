# -*- coding: utf-8 -*-
{
    'name': 'add_mrp_field',
    'category': 'add_mrp_field',
    'description': """
            add_mrp_field
            """,
    'author': 'CodeFire Technologies',
    'website': 'https://www.codefire.org/',
    'version': '14.0.1.1',
    'license': 'AGPL-3',
    'images': ['static/description/odoo-free.jpg'],
    'depends': [
        'mrp',
    ],
    "data": [
        "views/sale_bom.xml",
        "views/sale_bom_list.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
