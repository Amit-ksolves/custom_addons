from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    pick_custom_lines = fields.One2many('stock.custom.line', 'pick_custom_id', string='Stock Pick')

class StockCustomLine(models.Model):
    _name = "stock.custom.line"
    _description = "Stock Custom Line"

    name = fields.Char(string='Description')
    pick_custom_id = fields.Many2one('stock.picking', string='Stock Pick Line')
    product_id = fields.Many2one('product.template', string='Product')
    quantity = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
    tax_ids = fields.Many2many('account.tax', string='Taxes')
    price_subtotal = fields.Float(string='Subtotal')
