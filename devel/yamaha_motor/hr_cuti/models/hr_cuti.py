from odoo import models, fields, api
from odoo.exceptions import UserError


class HrCuti(models.Model):
    _name = 'hr.cuti'

    name = fields.Char(string='Pengajuan Cuti', copy=False)

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User Terkait',
        default=lambda self: self.get_this_user(),
        readonly=True,
    )

    def get_this_user(self):
        user_id = self.env.user.id
        return user_id

    date_from = fields.Date(string='Date From', default=fields.Date.today())
    date_to = fields.Date(string='Date To')
    quantity = fields.Integer(string='Quantity')
    state = fields.Selection([
            ('draft', 'Draft'),
            ('waiting', 'Waiting'),
            ('done', 'Done'),
        ], string='Status', default='draft')

    def write(self, vals):
        self.validate_allocation(vals)
        super(HrCuti, self).write(vals)

    def validate_allocation(self, vals):

        search_query = [('user_id', '=', self.user_id.id)]
        karyawan_doc = self.env['hr.karyawan'].search(search_query, limit=1)
        jatah = karyawan_doc.jatah_cuti
        request = vals.get('quantity', self.quantity)
        if jatah > request:
            return True
        else:
            raise UserError('Mohon maaf tidak bisa ..')


    def set_waiting(self):
        for doc in self:
            vals = {
                'state': 'waiting',
                'group_todo': 'hr_manager',
            }
            doc.write(vals)
    
    group_todo = fields.Char(string='Group Todo')
