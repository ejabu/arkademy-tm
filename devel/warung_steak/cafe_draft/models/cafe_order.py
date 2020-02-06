from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class CafeOrder(models.Model):
    _inherit = 'cafe.order'

    note = fields.Char(string='Note')

    customer = fields.Char(readonly=True, states={'draft': [('readonly', False)]})

    def set_open(self):
        for doc in self:
            nama_baru = self.env['ir.sequence'].next_by_code('cafe.order.sequence')
            doc.name = nama_baru
            doc.state = 'open'
            



    