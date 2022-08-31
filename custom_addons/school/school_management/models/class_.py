from odoo import models, fields

class StudentClass(models.Model):
    _name = "student.class"
    _description = "Student Class"

    class_id = fields.Many2one('school.student', string='Class')
    # sub_ids = fields.Many2many(string='Subject')
    # exam_ids = fields.One2many(string='Exam')
