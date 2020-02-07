from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StatSatuLine(models.Model):
    _name = 'stat.satu.line'

    name = fields.Char(string='Nama')
    value = fields.Integer(string='Value')

    stat_id = fields.Many2one(
        comodel_name='stat.satu',
        string='Stat Terkait'
    )
