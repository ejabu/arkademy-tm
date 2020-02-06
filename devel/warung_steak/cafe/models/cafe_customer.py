from odoo import models, fields, api


class CafeCustomer(models.Model):
    _name = 'cafe.customer'

    name = fields.Char(string='Nama')
    address_ids = fields.One2many(
        comodel_name='cafe.customer.address',
        inverse_name='customer_id',
        string='Address',
    )

    category = fields.Char(string='Category')
    phone = fields.Char(string='Phone')
    gender = fields.Selection([
            ('l', 'Laki-laki'),
            ('p', 'Perempuan'),
        ], string='Gender')

class CafeCustomerAddress(models.Model):
    _name = 'cafe.customer.address'

    name = fields.Char(string='Short Name')
    address = fields.Text(string='Alamat')
    is_main = fields.Boolean(string='Main')
    customer_id = fields.Many2one(
        comodel_name='cafe.customer',
        string='Customer'
    )

    _sql_constraints = [
        ('only_one_main', 'unique(is_main, customer_id)', 'Alamat Main harus satu')
    ]
