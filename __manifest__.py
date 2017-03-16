# -*- coding: utf-8 -*-
{
    'name': "Contact's marital status",
    'category': 'CRM',
    'version': '10.0.1.0.0',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ["partner_contact_personal_information_page"],
    'description': """
Contact's marital status
========================
* Adds a new model for storing different marital statuses and links partners to it

""",
    'data': [
        'views/res_partner.xml',
        'security/ir.model.access.csv'
    ],
    "license": "AGPL-3",
    'installable': True
}
