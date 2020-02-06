from odoo import models, fields

class CafePegawai(models.Model):
    _name = 'cafe.pegawai'

    name = fields.Char(string='Nama Karyawan', required=True)
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

    image = fields.Binary('Image')

    filename_ktp = fields.Char(string='Filename KTP')
    file_ktp = fields.Binary('Kartu Tanda Penduduk')

    filename_kk = fields.Char(string='Filename KK')
    file_kk = fields.Binary('Kartu Keluarga')
