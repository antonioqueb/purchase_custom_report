from odoo import models, api

class PurchaseOrderReport(models.Model):
    _inherit = 'purchase.order'

    def action_print_purchase_order_custom(self):
        return self.env.ref('purchase_custom_report.action_report_purchase_order_custom').report_action(self)

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['purchase.order'].browse(docids)
        company_data = self.env.user.company_id
        return {
            'doc_ids': docids,
            'doc_model': 'purchase.order',
            'docs': docs,
            'company_data': company_data,  # Pasamos el objeto 'company' al contexto con un nombre diferente
        }
