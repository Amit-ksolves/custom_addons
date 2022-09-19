{
    'name': 'real_estate',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'real estate Software',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',

    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        # 'views/estate_owners_view.xml',
        # 'report/property_report.xml',
        'wizard/estate_price_view.xml',
        'data/estate_sequence_view.xml',
        'data/estate_cron_view.xml',
    ],
}
