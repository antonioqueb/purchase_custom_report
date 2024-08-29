{
    'name': 'Purchase Custom Report',
    'version': '1.0',
    'category': 'Purchases',
    'summary': 'Replace the default Purchase Order report with a customized one and add a direct print button',
    'description': 'Replace the default Purchase Order report with a customized one.',
    'depends': ['purchase'],
    'data': [
        'views/view_purchase_order_form_inherit.xml',  # Botón personalizado en la vista de formulario
        'views/purchase_order_report_view.xml',       # Acción del reporte personalizado
        'report/purchase_order_template.xml',         # Plantilla personalizada del reporte
    ],
    'installable': True,
    'application': False,
}
