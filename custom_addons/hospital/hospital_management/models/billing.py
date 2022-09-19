from odoo import api, fields, models

class HospitalBilling(models.Model):
    _name = "hospital.billing"
    _description = "Hospital Billing"

    name = fields.Char(string='ID name')
    # patient_id = fields.Many2one('hospital.patient', string='Patient Name')
    bill = fields.Integer(string='Hospital Bill')
    expenses = fields.Integer(string='Other Expenses')







