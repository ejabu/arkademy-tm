from odoo import models, fields

class TokoPegawai(models.Model):
    _name = 'toko.pegawai'

    name = fields.Char(string='Nama Pegawai')
    alamat = fields.Text(string='Alamat')
    tahun_masuk = fields.Integer(string='Tahun Masuk')
    indeks_prestasi = fields.Float(string='Indeks Prestasi')
    
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    waktu_bangun = fields.Datetime(string='Waktu Bangun Tidur')
    gender = fields.Selection([
        ('l', 'Laki-laki'),
        ('p', 'Perempuan'),
    ], string='Gender')
    
    is_part_time = fields.Boolean(string='Part Time')

    struk_ids = fields.One2many(comodel_name='toko.struk', inverse_name='pegawai_id', string='Riwayat Jual')
