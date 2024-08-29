from odoo import models

class PurchaseOrderReport(models.Model):
    _inherit = 'purchase.order'

    def action_print_purchase_order_custom(self):
        # Obtenemos el objeto de la empresa actual
        company = self.env.user.company_id
        
        # Añadimos 'company' al contexto antes de generar el reporte
        return self.env.ref('purchase_custom_report.action_report_purchase_order_custom').with_context(
            disable_report_customization=True,
            company=company  # Pasamos el objeto 'company' al contexto
        ).report_action(self)
