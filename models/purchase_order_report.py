from odoo import models

class PurchaseOrderReport(models.Model):
    _inherit = 'purchase.order'

    def action_print_purchase_order_custom(self):
        # Obtenemos el objeto de la empresa actual
        company_data = self.env.user.company_id
        
        # Añadimos 'company_data' al contexto antes de generar el reporte
        return self.env.ref('purchase_custom_report.action_report_purchase_order_custom').with_context(
            disable_report_customization=True,
            company_data=company_data  # Pasamos el objeto 'company' al contexto con un nombre diferente
        ).report_action(self)
