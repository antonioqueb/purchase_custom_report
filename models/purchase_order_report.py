from odoo import models, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_print_purchase_order_custom(self):
        return self.env.ref('purchase_custom_report.action_report_purchase_order_custom').report_action(self)

class PurchaseOrderReport(models.AbstractModel):
    _name = 'report.purchase_order_custom'
    _description = 'Custom Purchase Order Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['purchase.order'].browse(docids)
        _logger.info("Docs: %s", docs)
        return {
            'doc_ids': docids,
            'doc_model': 'purchase.order',
            'docs': docs,
            'currency_id': docs.currency_id,
            'formatLang': self.env['ir.qweb'].formatLang,
        }

