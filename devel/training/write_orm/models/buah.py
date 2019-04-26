from odoo import models, fields, api

class BuahMangga(models.Model):
    _name = 'buah.mangga'

    name = fields.Char(string='Jenis Mangga')
    warna = fields.Char(string='Warna')





    @api.multi
    def create_buah_mangga(self):
        self.env['buah.mangga'].create({
            'name': 'Mangga',
            'warna': 'Emas',
        })








    @api.multi
    def create_buah_mangga_simple(self):
        self.create({
            'name': 'Mangga',
            'warna': 'Hijau Kuning',
        })
        






    @api.multi
    def create_buah_jeruk(self):
        import random
        pilihan_warna = ['Hijau', 'Kuning', 'Orange', 'Hijau Kemerahan']
        index_warna = random.randint(0, 3)
        warna_jeruk = pilihan_warna[index_warna]

        self.env['buah.jeruk'].create({
            'name': 'Jeruk',
            'warna': warna_jeruk,
        })
        
    

class BuahJeruk(models.Model):
    _name = 'buah.jeruk'

    name = fields.Char(string='Jenis Jeruk')
    warna = fields.Char(string='Warna')