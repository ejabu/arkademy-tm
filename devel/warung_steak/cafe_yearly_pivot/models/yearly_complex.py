from odoo import api, fields, models, tools

class YearlyComplex(models.Model):
    _name = "yearly.complex"
    _auto = False


    produk_id = fields.Many2one('cafe.produk', string='Produk')
    quantity = fields.Integer(string='Quantity')
    price_total = fields.Float(string='Price Total')
    date_order = fields.Date(string='Date Order')
    
    tipe_produk = fields.Selection([
            ('makanan', 'Makanan'),
            ('minuman', 'Minuman'),
        ], string='Tipe')
    
    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'yearly_complex')
        self._cr.execute("""
            create or replace view yearly_complex as (
                SELECT
                    min(ol.id) as id,
                    ol.produk_id as produk_id,
                    ol.quantity as quantity,
                    ol.price_total as price_total,
                    co.date_order as date_order,
                    cp.tipe as tipe_produk
                FROM cafe_order_line ol
                    LEFT JOIN cafe_order co on (co.id=ol.order_id)
                    LEFT JOIN cafe_produk cp on (cp.id=ol.produk_id)
                GROUP BY
                    ol.produk_id,
                    ol.quantity,
                    ol.price_total,
                    co.date_order,
                    cp.tipe
        )""")
