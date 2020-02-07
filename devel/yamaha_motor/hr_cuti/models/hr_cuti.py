from odoo import models, fields, api
from odoo.exceptions import UserError


class HrCuti(models.Model):
    _name = 'hr.cuti'

    name = fields.Char(
        string='Pengajuan Cuti',
        copy=False,
        readonly=True,
        default=lambda self: self.get_name())

    def get_name(self):
        nama_baru = self.env['ir.sequence'].next_by_code('hr.cuti.sequence')
        return nama_baru

    note = fields.Text(string='Note')
    karyawan_id = fields.Many2one(
        comodel_name='hr.karyawan',
        string='Karyawan Terkait',
        default=lambda self: self.get_this_karyawan(),
        readonly=True,
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User Terkait',
        default=lambda self: self.get_this_user(),
        readonly=True,
    )

    def get_this_karyawan(self):
        search_query = [('user_id', '=', self.env.user.id)]
        karyawan_doc = self.env['hr.karyawan'].search(search_query, limit=1)
        karyawan_id = karyawan_doc.id
        return karyawan_id

    def get_this_user(self):
        user_id = self.env.user.id
        return user_id

    date_from = fields.Date(string='Date From', default=fields.Date.today())
    date_to = fields.Date(string='Date To')
    quantity = fields.Integer(string='Quantity')
    group_todo = fields.Char(string='Group Todo', readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', 'Waiting'),
        ('done', 'Done'),
    ], string='Status', default='draft')

    @api.model_create_multi
    def create(self, vals_list):
        created_docs = super(HrCuti, self).create(vals_list)
        for doc in created_docs:
            doc.validate_allocation({})
        return created_docs


    def write(self, vals):
        if vals.get('quantity'):
            self.validate_allocation(vals)
        super(HrCuti, self).write(vals)

    def validate_allocation(self, vals):

        search_query = [('user_id', '=', self.user_id.id)]
        karyawan_doc = self.env['hr.karyawan'].search(search_query, limit=1)
        jatah = karyawan_doc.jatah_cuti
        request = vals.get('quantity', self.quantity)
        if not request or jatah > request:
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

    def set_confirm(self):
        for doc in self:
            if self.user_has_groups('hr_cuti.group_cuti_manager'):
                vals = {
                    'group_todo': 'hr_director',
                }
                doc.write(vals)
            if self.user_has_groups('hr_cuti.group_cuti_director'):
                vals = {
                    'group_todo': False,
                    'state': 'done',
                }
                doc.write(vals)
