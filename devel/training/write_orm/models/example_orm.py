from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ExampleOrm(models.Model):
    _name = 'example.orm'
    _rec_name = 'id'

    title = fields.Char('Title')

    records_to_add = fields.Integer('Records to Add', default=2)
