from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move"

    account_custom_lines = fields.One2many('account.custom.line', 'account_custom_id', string='Account')
    # partner_id = fields.Many2one('res.partner')

class AccountCustomLine(models.Model):
    _name = "account.custom.line"
    _description = "Account Custom Line"

    name = fields.Char(string='Description')
    account_custom_id = fields.Many2one('account.move', string='Account Custom')
    product_id = fields.Many2one('product.template', string='Product')
    quantity = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
    tax_ids = fields.Many2many('account.tax', string='Taxes')
    price_subtotal = fields.Float(string='Subtotal')
