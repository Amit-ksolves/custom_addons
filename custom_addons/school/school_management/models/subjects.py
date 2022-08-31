from odoo import models, fields

class StudentSubjects(models.Model):
    _name = "student.subjects"
    _description = "Student Subjects"

    student_id = fields.Many2one('school.student', string='Student')
    # student1_id = fields.Many2one(string='')
    marks = fields.Integer(string='Marks')
    # result_id = fields.One2many(string='')






