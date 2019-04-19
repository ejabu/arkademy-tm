from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class PayOrderWizard(models.TransientModel):

    _name = 'pay.order.wizard'

    amount_total = fields.Float(string='Amount Total')
    payment_amount = fields.Float(string='Payment Amount')
    payment_return = fields.Float(string='Payment Return')

    def process_wizard(self):
        # Hands On : Validasi Payment Amount

        ids_to_change = self._context.get('active_ids')
        active_model = self._context.get('active_model')
        doc_ids = self.env[active_model].browse(ids_to_change)


        # Task A: Open -> Paid
        # -------------------- 
        # Silahkan dilanjutkan