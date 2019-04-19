from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class CafeOrderLine(models.Model):
    _inherit = 'cafe.order.line'

    # order_id = fields.Many2one(ondelete='set null')
    order_id = fields.Many2one(ondelete='cascade')