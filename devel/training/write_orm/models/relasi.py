from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ExampleOrm(models.Model):
    _inherit = 'example.orm'

    line_ids = fields.One2many('example.orm.line', 'example_id', 'Line')

class ExampleOrmLine(models.Model):
    _inherit = 'example.orm.line'

    example_id = fields.Many2one('example.orm', 'Example ID', ondelete='cascade')
