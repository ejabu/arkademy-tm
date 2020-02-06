from odoo import models, fields, api

class TokoStruk(models.Model):
    _name = 'toko.struk'

    name = fields.Char(string='No Struk')

    detail = fields.Text(string='Detail Belanja')

    price_total = fields.Float(compute='get_price_total', store=True, string='Price Total')

    pegawai_id = fields.Many2one(comodel_name='toko.pegawai', string='Kasir')

    line_ids = fields.One2many(
        comodel_name='toko.struk.line',
        inverse_name='struk_id',
        string='Detail Jual',
        )

    state = fields.Selection([
            ('draft', 'Draft'),
            ('open', 'Open'),
        ], string='Status', default='draft')

    def set_open(self):
        for doc in self:
            doc.state = 'open'


    @api.depends('line_ids')
    def get_price_total(self):
        for doc in self:
            temp_price = 0
            for line_id in doc.line_ids:
                temp_price += line_id.price_total
            doc.price_total = temp_price
    
