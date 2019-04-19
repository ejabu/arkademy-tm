from odoo import models, fields

class CafeProduk(models.Model):
    _name = 'cafe.produk'

    kode = fields.Char(string='Kode Produk', size=6, )
    name = fields.Char(string='Nama Produk')
    price = fields.Float(string='Price')
    tipe = fields.Selection([
            ('makanan', 'Makanan'),
            ('minuman', 'Minuman'),
        ], string='Tipe')
    is_aktif = fields.Boolean(string='Aktif')

    _sql_constraints = [
        ('kode_uniq', 'unique(kode)', 'Nomor Kode harus unik !')
    ]
    