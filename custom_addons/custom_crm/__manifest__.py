{
    'name': 'custom_contacts',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'next Version Contacts',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',

    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/custom_contacts_view.xml',
        'wizard/wiz_blacklist_view.xml',
    ],
}
