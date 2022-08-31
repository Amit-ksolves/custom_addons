from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_lines = fields.One2many('custom.order.line', 'custom_id')
    partner_id = fields.Many2one('res.partner')

    # sample_lines = fields.One2many('wiz.sale.order.line', 'sample_id')

    # def action_confirm(self):
    #     for rec in self:
    #         # company = self.env['sale.order'].search([])
    #         # print('companies---', company)
    #
    #         # browse_result = self.env['sale.order'].browse()
    #         # print('browse_result---', browse_result)
    #         # if browse_result.exists():
    #         #     print("Existing")
    #         # else:
    #         #     print("NOOOOOO")
    #         vals = {
    #             'name': 'S03687',
    #             'partner_id': 'KTTT',
    #             'validity_date': '08/20/2022'}
    #         create_record = self.env['sale.order'].create(vals)
    #         print('create_record---', create_record)
    #
    #         record_update = self.env['sale.order'].browse()
    #         if record_update.exists():
    #             vals = {
    #                 'validity_date': '08/28/2022',
    #             }
    #             record_update.write(vals)


class CustomOrderLine(models.Model):
    _name = "custom.order.line"
    _description = "Custom Order Line"

    name = fields.Text(string='Description')
    custom_id = fields.Many2one('sale.order')
    product_id = fields.Many2one('product.template', string='Product')
    quantity = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
    tax_ids = fields.Many2many('account.tax', string='Taxes')
    price_subtotal = fields.Float(string='Subtotal')
