from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string='Patient Name', required=True)
    age = fields.Integer(string='Age')
    doctor_name = fields.Char(string='Doctor Name')
    discharge = fields.Boolean(string='Discharged')
    appointment_date = fields.Date(string='Today date')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Others')], )
    # bill = fields.Float(string='Total Bill')
    responsible_id = fields.Many2one('res.partner', string='Responsible')
    note = fields.Text(string='Description')
    # appointment_count = fields.Integer('', string='Appointment Count')
    state = fields.Selection([('confirm', 'Confirm')])
    # @api.depends('')
    # def _compute_appointment_count(self):
    #

    @api.onchange('responsible_id')
    def _onchange_responsible_id(self):
        self.note = self.responsible_id.name

    @api.constrains('appointment_date')
    def _check_date(self):
        for record in self:
            if record.appointment_date and record.appointment_date < fields.Date.today():
                raise ValidationError("Please enter present or upcoming dates!" % self.appointment_date)
#validation error put in place of print


    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'Normal'
        res = super(HospitalPatient, self).create(vals)
        return res

    def action_view_appointment(self):
        return {
            'name': 'Appointment',
            'res_model': 'hospital.appointment',
            'view_mode': 'list,form',
            'context': {},
            'target': 'current',
            'type': 'ir.actions.act_window',
        }

    def action_confirm(self):
        self.state = 'confirm'
        for rec in self:
        #     #odoo search method
            patients = self.env['hospital.patient'].search([])
            print('patients.....', patients)
            male_patients = self.env['hospital.patient'].search([('gender', '=', 'male')])
            print('male_patients....', male_patients)
            #
            # #odoo search_count method
            patient_count = self.env['hospital.patient'].search_count([])
            print('patient_count....', patient_count)

            # #odoo browse method
            # browse_result = self.env['hospital.patient'].browse([2, 1])
            # print('browse_result....', browse_result)
            # if browse_result.exists():
            #     print('Existing')
            # else:
            #     print('Noooo')
            #
            # #odoo create method
            # vals = {
            #     'name': 'Raja',
            #     'age': '45',
            # }
            # create_record = self.env['hospital.patient'].create(vals)
            # print('create_record.....', create_record)
            #
            # #odoo update method
            # record_to_update = self.env['hospital.patient'].browse(3)
            # if record_to_update.exists():
            #     vals: {
            #         'name': 'Rahul'
            #     }
            #     record_to_update.write(vals)
            #
            # #odoo copy
            # record_to_copy = self.env['hospital.patient'].browse(22)
            # record_to_copy.copy()
            #
            # # odoo unlink
            # record_to_copy = self.env['hospital.patient'].browse(2)
            # record_to_copy.unlink()
