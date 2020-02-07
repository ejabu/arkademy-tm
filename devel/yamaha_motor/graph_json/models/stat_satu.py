import requests
import json
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StatSatu(models.Model):
    _name = 'stat.satu'

    name = fields.Char(string='Name')
    line_ids = fields.One2many(
        comodel_name='stat.satu.line',
        inverse_name='stat_id',
        string='Data',
    )

    def request(self):
        response = requests.get('https://pandi.id/stats/stats.json')
        my_json = response.content.decode('utf8').replace("'", '"')
        vals = json.loads(my_json)
        registered_total_details = vals.get('registered_total_details')
        return registered_total_details

    def create_new(self):
        payload = self.request()

        # 1. Create Doc First
        vals = {
            'name': fields.Datetime.now()
        }
        doc = self.env['stat.satu'].create(vals)

        # 2. Isi One2many
        for key, value in payload.items():
            print(key, value)
            item_vals = {
                'name': key,
                'value': value,
            }
            doc.write({
                'line_ids': [
                    (0, 0, item_vals)
                ]
            })

    def edit_existing(self):
        payload = self.request()

        # 1. Use This Doc
        doc = self

        # 2. Hapus isi One2many
        doc.write({
            'line_ids': [
                (5, 0)
            ]
        })

        # 3. Isi One2many
        for key, value in payload.items():
            print(key, value)
            item_vals = {
                'name': key,
                'value': value,
            }
            doc.write({
                'line_ids': [
                    (0, 0, item_vals)
                ]
            })
