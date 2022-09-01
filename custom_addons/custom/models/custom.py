from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_lines = fields.One2many('custom.sale.line', 'sale_id', string='Custom Sale Line')
    partner_id = fields.Many2one('res.partner')

class SaleInvoiceAdvance(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def create_invoices(self):
        res = super(SaleInvoiceAdvance, self).create_invoices()

        active_id = self._context.get('active_id')
        if active_id:
            order_id = self.env['sale.order'].browse(active_id)
            custom_order = self.env['account.move'].search([('invoice_origin', '=', 'order_id.name')])
            for rec in order_id.sale_lines:
                data ={
                     'account_custom_id': custom_order.id, 'product_id': rec.product_id.id, 'name': rec.name,
                        'quantity': rec.quantity, 'price_unit': rec.price_unit, 'price_subtotal': rec.price_subtotal
                    }
                print(custom_order.id)
                print(data)
                account_line = self.env['account.custom.line'].create(data)
                print(account_line)
        return res

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


class CustomSaleLine(models.Model):
    _name = "custom.sale.line"
    _description = "Custom Sale Line"

    name = fields.Char(string='Description')
    sale_id = fields.Many2one('sale.order', string='Sale Order')
    product_id = fields.Many2one('product.template', string='Product')
    quantity = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
    tax_ids = fields.Many2many('account.tax', string='Taxes')
    price_subtotal = fields.Float(string='Subtotal')
