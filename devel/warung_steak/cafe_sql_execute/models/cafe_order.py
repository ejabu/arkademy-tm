from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class CafeOrder(models.Model):
    _inherit = 'cafe.order'

    def query_order_line(self):
        # A. Get Data
        query_sql = """
            SELECT 
                ol.produk_id, 
                ol.quantity,
                ol.price,
                ol.price_total
            FROM 
                cafe_order_line as ol
            WHERE
                ol.order_id = %s
        """ % (self.id)

        self._cr.execute(query_sql)
        result_rows = self._cr.dictfetchall()
        
        # B. Result in Popup
        if self._context.get('popup'):
            raise UserError(str(result_rows))

        # C. Result as return value
        return result_rows            
        