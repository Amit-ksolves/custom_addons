from odoo import models, fields

class ClassTeacher(models.Model):
    # _inherit = "hr.employee"
    _name = "class.teacher"
    _description = "Class Teacher"

    teacher_id = fields.Many2one(string='Teacher Name')
    subject_ids = fields.One2many(string='Subject')
    # class_ids = fields.Many2many(string='Class')
    # exam_ids = fields.Many2many(string='Exam')
