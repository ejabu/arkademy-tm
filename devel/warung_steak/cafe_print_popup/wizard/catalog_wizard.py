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
        required=True,
    )

    def process_wizard(self):
        search_query = [
            ('tipe', '=', self.catalog_type),
            ('is_aktif', '=', True),
        ]
        produk_docs = self.env['cafe.produk'].search(search_query)
        report_xml_id = self.env.ref('cafe_print_popup.cafe_produk_print')
        vals = report_xml_id.report_action(produk_docs)
        # return vals

        return {
            'type': 'ir.actions.report',
            'name': 'Cafe Produk',
            'report_type': 'qweb-html',
            'report_file': False,
            'report_name': 'cafe_print_popup.cafe_produk_template',
            'data': None,
            'context': {
                'active_ids': produk_docs.ids,
                'lang': 'en_US',
                'tz': 'Europe/Brussels',
                'uid': 1,
            },
        }
