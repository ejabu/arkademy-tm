from odoo import models, fields, api

class CafeMatang(models.Model):
    _name = 'cafe.matang'

    name = fields.Char(string='Jenis Kematangan')
