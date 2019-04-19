from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class CatalogWizard(models.TransientModel):

    _name = 'catalog.wizard'

    catalog_type = fields.Selection(
        selection=[
            ('makanan', 'Makanan'),
            ('minuman', 'Minuman'),
            ],
        string='Catalog Type',
        required=True
        )

    def process_wizard(self):
        search_query = [('tipe', '=', self.catalog_type)]
        produk_docs = self.env['cafe.produk'].search(search_query)
        return self.env.ref('cafe_print_popup.cafe_produk_print').report_action(produk_docs)
