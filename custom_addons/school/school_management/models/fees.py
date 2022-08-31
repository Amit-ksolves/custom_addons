from odoo import models, fields

class StudentFees(models.Model):
    _name = "student.fees"
    _description = "Student Fees"

    name = fields.Many2one('school.student', string='Student ID')
    student = fields.Char(string='Student Name', related='name.student_name')
    # st_class = fields.Char(string='Class', related='name.student_class')
    pay_date = fields.Date(string='Date')
    # total_fees = fields
    fee_ids = fields.One2many('fee.structure', 'fees_id', string='Total Fees')

class FeeStructure(models.Model):
    _name = "fee.structure"
    _description = "Fee Structure"

    name = fields.Integer(string='Serial No.')
    pay_date = fields.Date(string='Date')
    fees = fields.Float(string="Fees")
    fees_id = fields.Many2one('student.fees', string='Fee Paid')
