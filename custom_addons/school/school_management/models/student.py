from odoo import models, fields

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"

    student_lines = fields.One2many('student.subjects', string='Student ID')
    student_name = fields.Char(string='Student Name')
    gender = fields.Selection([('male', 'Boy'), ('female', 'Girl')], string='Gender')
    class_lines = fields.One2many('student.class', string='Class')
    # subject_ids = fields.Many2many('student.subjects', string='Subjects')
    # exam_ids = fields.Many2many()
    # percent = fields.Float(string='Percent Obtained', computed='')

    def action_confirm(self):
        for rec in self:
            student = self.env['school.student'].search([])
            print("Students.........", student)
