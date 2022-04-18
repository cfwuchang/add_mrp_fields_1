from odoo import api, fields, models, tools, _

class Bom(models.Model):
    _inherit = 'mrp.bom.line'

    x_category = fields.Char(string=u'产品类别',related='product_id.categ_id.name')
