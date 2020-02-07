from odoo import models, fields, api


class HrCuti(models.Model):
    _name = 'hr.cuti'

    name = fields.Char(string='Pengajuan Cuti')

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User Terkait',
        default=lambda self: self.get_this_user(),
        readonly=True,
    )

    def get_this_user(self):
        user_id = self.env.user.id
        return user_id
