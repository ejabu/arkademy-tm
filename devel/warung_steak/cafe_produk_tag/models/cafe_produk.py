from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class CafeProduk(models.Model):
    _inherit = 'cafe.produk'

    matang_ids = fields.Many2many(
        comodel_name='cafe.matang',
        string='Level Matang',
        )
