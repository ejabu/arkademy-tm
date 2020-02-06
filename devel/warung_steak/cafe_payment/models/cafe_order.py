from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class CafeOrder(models.Model):
    _inherit = 'cafe.order'

    state = fields.Selection(selection_add=[("paid", "Paid")])

    
    def buka_wizard(self):
        # Hands On : Pass Context ke Popup

        return {
            'type': 'ir.actions.act_window',
            'name': 'Popup',
            'res_model': 'pay.order.wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
    