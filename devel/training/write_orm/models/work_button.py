from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ExampleOrm(models.Model):
    _inherit = 'example.orm'


    def create_orm_line(self):
        eol = self.env['example.orm.line']

        if self.title:
            temp_name = self.title
        else:
            temp_name = 'Arkademy'

        eol.create({
            'name' : 'via Create Method',
            'detail' : 'Made by %s' % (self.title),
            'example_id' : self.id,
        })



    def new_records(self):
        temp_array = []

        for i in range(0, self.records_to_add):
            value = {
                'name' : 'via Write Method',
                'detail': 'Kelipatan %s' % (self.records_to_add),
                'amount': 1000,
            }
            temp_array.append((0, 0, value))

        self.write({
            'line_ids' : temp_array,
        })





    def break_one_record(self):
        if len(self.line_ids) > 0:
            baris_pertama_doc = self.line_ids[0]

            baris_pertama_doc.example_id = False





    def delete_one_record(self):

        if self.line_ids:
            baris_pertama_doc = self.line_ids[-1]

            self.write({
                'line_ids': [
                    (3, baris_pertama_doc.id)
                ]
            })





    def break_all_record(self):
        line_docs = self.line_ids
        for line_doc in line_docs:
            line_doc.example_id = False








    def link_one_record(self):

        # Contoh Get All ID
        all_docs = self.env['example.orm.line'].search([])
        
        # Contoh Get Nganggur IDS
        nganggur_docs = self.env['example.orm.line'].search(
            [('example_id', '=', False)]
        )

        # Get satu Nganggur ID
        search_query = [('example_id', '=', False)]
        nganggur_doc = self.env['example.orm.line'].search(search_query, limit=1)


        if not nganggur_doc:
            raise UserError('Line sudah ke link semua')
        self.write({
            'line_ids': [(4, nganggur_doc.id)]
        })


    def link_all_nganggur_record(self):
        line_obj = self.env['example.orm.line']
        search_query = [('example_id','=',False),]
        nganggur_docs = self.env['example.orm.line'].search(search_query)

        # Continue here .. :

