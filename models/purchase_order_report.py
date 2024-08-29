from odoo import models

class PurchaseOrderReport(models.Model):
    _inherit = 'purchase.order'

    def action_print_purchase_order_custom(self):
        # Llamamos directamente al reporte sin abrir la interfaz de branding
        return self.env.ref('purchase_custom_report.action_report_purchase_order_custom').with_context(disable_report_customization=True).report_action(self)
