from odoo import models, fields, api

class CafeOrderLine(models.Model):
    _name = 'cafe.order.line'
    
    produk_id = fields.Many2one('cafe.produk', string='Produk')
    quantity = fields.Integer(string='Quantity', default=1)
    price = fields.Float(string='Price')
    price_total = fields.Float(string='Price Total', compute='get_price_total', store=True,)

    order_id = fields.Many2one('cafe.order', string='Order')

    @api.onchange('produk_id')
    def get_price(self):
        self.price = self.produk_id.price
    
    @api.onchange('quantity')
    def validate_qty(self):
        if self.quantity <= 0:
            # Task A : Set jadi 1
            return {
                'warning': {
                    'title': 'Cek Kembali Kolom Quantity',
                    'message': 'Jumlah pembelian harus lebih besar daripada 0',
                }
            }
    
    @api.depends('quantity', 'price')
    def get_price_total(self):
        # self.price_total = self.quantity * self.price

        for doc in self:
            doc.price_total = doc.quantity * doc.price
    
    
