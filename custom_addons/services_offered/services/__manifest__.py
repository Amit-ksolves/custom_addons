{
    'name': 'services',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'services',
    'depends': ['base', 'sale', 'report_xlsx'],
    'application': True,

    'data': [
        'security/ir.model.access.csv',
        # 'wizard/',
        'view/services_offered_view.xml',
    ],
}


