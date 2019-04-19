from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import random

class ExampleOrm(models.Model):
    _inherit = 'example.orm'


    def create_orm_line(self):
        eol = self.env['example.orm.line']
        eol.create({
            'name' : 'Created via Button',
            'detail' : random.randint(12, 16),
            'example_id' : self.id,
        })

    def new_records(self):
        temp_array = []

        # Basic If Conditional
        if self.title:
            temp_name = self.title
        else:
            temp_name = 'Logitech'

        # One Liner
        temp_name = self.title if self.title else 'Logitech'

        for i in range(0, self.records_to_add):
            value = {
                'detail': 'Kelipatan %s by %s' % (self.records_to_add, temp_name),
                'amount': random.randint(1, 6) * 1000,
            }
            temp_array.append((0, 0, value))

        self.write({
            'line_ids' : temp_array,
        })

    def break_one_record(self):
        line_docs = self.line_ids
        if line_docs:
            baris_pertama_doc = line_docs[0]
            baris_pertama_doc.example_id = False

    def delete_one_record(self):
        line_docs = self.line_ids
        if line_docs:
            baris_pertama_doc = self.line_ids[-1]

            self.write({
                'line_ids': [
                    (3, baris_pertama_doc.id)
                    ],
            })
            # Task A :
            # Delete dari amount yang paling kecil
            orm_line_docs = self.line_ids.sorted(lambda x: -x.amount)
            # Silahkan dilanjutkan ..

    def break_all_record(self):
        line_docs = self.line_ids
        for line_doc in line_docs:
            line_doc.example_id = False

    def link_one_record(self):
        search_query = [('example_id', '=', False)]
        line_doc = self.env['example.orm.line'].search(search_query, limit=1)
        if not line_doc:
            raise UserError('Line sudah ke link semua')
        self.write({
            'line_ids': [(4, line_doc.id)]
        })


    def link_all_nganggur_record(self):
        line_obj = self.env['example.orm.line']
        search_query = [('example_id','=',False),]
        nganggur_docs = self.env['example.orm.line'].search(search_query)


        # Task B :
        # Link semua 'nganggur' record dengan Dokumen ini 

        # Silahkan dilanjutkan ..

