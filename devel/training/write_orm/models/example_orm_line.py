from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ExampleOrmLine(models.Model):
    _name = 'example.orm.line'
    # _order = 'amount desc'

    name = fields.Char(string='Struk Pembayaran',
        default=lambda self: self.env['ir.sequence'].next_by_code('example.orm.line.default'))

    def get_name_new(self):
        nama_baru = self.env['ir.sequence'].next_by_code('example.orm.line.app')
        return nama_baru

    name_new = fields.Char(string='APP Code', default=get_name_new)

    detail = fields.Char('Detail')
    amount = fields.Monetary('Amount')

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        default=lambda self: self.env.user.company_id.currency_id.id)




