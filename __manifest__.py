{
    'name': 'Purchase Custom Report',
    'version': '1.0',
    'category': 'Purchases',
    'summary': 'Custom Purchase Order Report',
    'description': 'Replace the default Purchase Order report with a customized one.',
    'depends': ['purchase'],
    'data': [
        'views/purchase_order_report_view.xml',
        'report/purchase_order_template.xml',
    ],
    'installable': True,
    'application': False,
}
