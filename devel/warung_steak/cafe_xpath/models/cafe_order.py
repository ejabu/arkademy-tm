from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class CafeOrder(models.Model):
    _inherit = 'cafe.order'

    note_text = fields.Text(string='Note')


class CafeOrderLine(models.Model):
    _inherit = 'cafe.order.line'

    matang_id = fields.Many2one('cafe.matang', string='Matang')

    # matang_ids = fields.Many2many(
    #     related="produk_id.matang_ids",
    #     string='Matang'
    #     )
    

