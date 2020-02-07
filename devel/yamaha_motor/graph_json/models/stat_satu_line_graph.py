from odoo import models, fields, api, _
from odoo import tools
from odoo.exceptions import UserError


class StatSatuLineGraph(models.Model):
    _name = 'stat.satu.line.graph'
    _auto = False

    name = fields.Char(string='Name')
    value = fields.Integer(string='Value')

    @api.model_cr
    def init(self):
        # self._cr.execute("DROP TABLE IF EXISTS stat_satu_line_graph")
        tools.drop_view_if_exists(self._cr, 'stat_satu_line_graph')
        self._cr.execute("""
            create or replace view stat_satu_line_graph as (
                SELECT
                    row_number() OVER () AS id,
                    doc.name as name,
                    doc.value as value
                FROM 
                    stat_satu_line doc
                WHERE
                    doc.stat_id = (
                        SELECT
                            id
                        FROM
                            stat_satu
                        ORDER BY 
                            write_date DESC 
                        LIMIT 1
                    )
        )""")
