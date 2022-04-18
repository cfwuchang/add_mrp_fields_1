from odoo import api, fields, models, tools, _

class List(models.Model):
    _inherit = 'stock.move'
    
    x_category= fields.Char(string=u'类别',related='product_id.categ_id.name')
    x_material= fields.Char(string=u'领料人')
    x_date= fields.Datetime(string=u'领料时间')
    x_remark= fields.Char(string=u'备注')
    
    
