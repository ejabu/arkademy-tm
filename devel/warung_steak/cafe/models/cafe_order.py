from odoo import models, fields, api

class CafeOrder(models.Model):
    _name = 'cafe.order'

    name = fields.Char(string='Nomor Struk', default="/", readonly="1")
    
    customer = fields.Char(string='Customer')

    pegawai_id = fields.Many2one('cafe.pegawai', string='Pelayan')

    date_order = fields.Date(string='Date Order', default=fields.Date.today())

    state = fields.Selection([
            ('draft', 'Draft'),
            ('open', 'Open'),
        ], string='Status', default='draft')


    line_ids = fields.One2many(
        comodel_name='cafe.order.line',
        inverse_name='order_id',
        string='Line',
        )

    amount_total = fields.Float(compute='_compute_total', string='Total', store=True)
    
    @api.multi
    @api.depends('line_ids')
    def _compute_total(self):
        for order_doc in self:
            amount_total = sum(order_doc.line_ids.mapped('price_total'))
            order_doc.amount_total = amount_total
    