from odoo import models, fields


class SpanishName(models.Model):
    _inherit = 'product.template'

    spanish_name = fields.Char(string='Spanish Name')
