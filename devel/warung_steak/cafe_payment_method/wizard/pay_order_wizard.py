from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PayOrderWizard(models.TransientModel):
    _inherit = 'pay.order.wizard'

    payment_method = fields.Selection(
        selection=[
            ('cash', 'Cash'),
            ('card', 'Card'),
            ],
        string='Payment Method')

    payment_ref = fields.Char(string='Payment Ref')
