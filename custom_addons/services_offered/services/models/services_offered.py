from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    service_lines = fields.One2many('services.offered', 'service_id', string='Service Lines')

class ServicesOffered(models.Model):
    _name = "services.offered"
    _description = "Services Offered"

    name = fields.Char(string='Description')
    service_id = fields.Many2one('sale.order', string='Service Id')
    product_id = fields.Many2one('product.template', string='Products')
    quantity = fields.Integer(string='Quantity')
    tax_id = fields.Many2many(string='Taxes')
    price_unit = fields.Float(string='Unit Price')
    subtotal = fields.Float(string='Subtotal')
