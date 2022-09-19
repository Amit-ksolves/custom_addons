from odoo import api, fields, models

class HospitalAppointment(models.TransientModel):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"

    name = fields.Char(string='Order Reference', readonly=True, default=lambda self:('New'))
    # patient_ids = fields.Many2many('hospital.patient', string='Patient Name', related='doctor_id.name')
    doctor_id = fields.Many2one('hospital.patient', string='Doctor Name')
    date_appointment = fields.Date(string='Date')
    date_checkup = fields.Datetime(string='Checkup Time')

    def test_recordset(self):
        for rec in self:
            print("Odoo ORM: Record Set Operation")
            partners = self.env['res.partner'].search([])
            print("Mapped partners...", partners.mapped('name'))
            print("Sorted partners...", partners.sorted(lambda o: o.create_date))
            print("Filtered partners...", partners.filtered(lambda o: o.name))


class HospitalMedicine(models.Model):
    _name = "hospital.medicine"
    _description = "Hospital Medicine"

    name = fields.Char('Medicine')             #for inline view
    # qty = fields.Integer('Quantity')
    # usage = fields.Integer('Usage Months')

