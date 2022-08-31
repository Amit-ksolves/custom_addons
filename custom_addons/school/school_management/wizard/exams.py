from odoo import fields, models, api

class StudentExams(models.Model):
    _name = "student.exams"

    name = fields.Many2one('school.student', string="Student ID")
    sub = fields.Char(string='Subjects')
    time = fields.Datetime(string='Date & Time')
    # exam_ids = fields.One2many('student.subjects', 'sub_id', string='Subject Mark')

