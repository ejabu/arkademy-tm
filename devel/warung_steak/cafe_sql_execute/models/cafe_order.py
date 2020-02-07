from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import requests

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
        # if self._context.get('popup'):
        #     raise UserError(str(result_rows))

        # C. Result as return value
        print('Flag Here')
        response = requests.get('https://pandi.id/stats/stats.json')
        if self._context.get('popup'):
            raise UserError(str(response.content))

            my_json = response.content.decode('utf8').replace("'", '"')

            json.loads(my_json)
        
        print('Flag Here')
        return result_rows            
        