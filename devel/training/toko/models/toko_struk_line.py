from odoo import models, fields

class TokoStrukLine(models.Model):
    _name = 'toko.struk.line'

    name = fields.Char(string='Nama Produk')
    quantity = fields.Integer(string='Quantity')
    price = fields.Float(string='Price')
    price_total = fields.Float(string='Price Total')

    struk_id = fields.Many2one('toko.struk', string='Struk')
    