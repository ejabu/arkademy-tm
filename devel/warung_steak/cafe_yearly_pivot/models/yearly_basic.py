from odoo import api, fields, models, tools

class YearlyBasic(models.Model):
    _name = "yearly.basic"
    _auto = False


    produk_id = fields.Many2one('cafe.produk', string='Produk')
    quantity = fields.Integer(string='Quantity')
    price_total = fields.Float(string='Price Total')

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'yearly_basic')
        self._cr.execute("""
            create or replace view yearly_basic as (
                SELECT
                    min(ol.id) as id,
                    ol.produk_id as produk_id,
                    ol.quantity as quantity,
                    ol.price_total as price_total
                FROM cafe_order_line ol
                GROUP BY
                    ol.produk_id,
                    ol.quantity,
                    ol.price_total
        )""")
