from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class CafeOrder(models.Model):
    # Original
    # _name = 'cafe.order'
    # _inherit = ['mail.thread']

    # Existing
    _name = 'cafe.order'
    _inherit = ['mail.thread', 'cafe.order']

    state = fields.Selection(track_visibility='onchange')