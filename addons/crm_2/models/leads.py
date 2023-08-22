# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import pendulum

class Leads(models.Model):
    _name = "crm2.leads"
    _description = "Leads"
    _order = "id desc"
    _rec_name = 'leads_name_1'
    _inherit = ['mail.thread']
           
    leads_name_1 = fields.Char(string = 'Partner Name 1', required = True, tracking = True)
    leads_name_2 = fields.Char(string = 'Partner Name 2', tracking = True)
    affiliate_id = fields.Integer(string = 'Partner ID', tracking = True)
    
    fk_acquisition_manager = fields.Many2one('crm2.acquisition_manager', string = 'Acquisition Manager', required = True, tracking = True)
    fk_account_manager = fields.Many2one('crm2.account_manager', string = 'Account Manager', tracking = True)
    fk_country = fields.Many2one('crm2.country', string = 'Country', required = True, tracking = True)
    fk_partner_category = fields.Many2one('crm2.partner_category', string = 'Partner Category', required = True, tracking = True)
    fk_partner_type = fields.Many2one('crm2.partner_type', string = 'Partner Type', required = True, tracking = True)
    status = fields.Selection([
        ('lead', '1. Lead'), ('follow_up', '2. Follow Up'), ('conversation', '3. Conversation'),
        ('sign_up', '4. Sign Up'), ('kick_off', '5. Kick Off'), ('rejected', '6. Rejected')
    ], required = True, default = 'lead', tracking = True)
    
    status_start_date = fields.Datetime(string = 'Status Start Date', readonly = True)
    @api.model
    def create(self, vals):
        vals['status_start_date'] = self.env.cr.now()
        res = super(Leads, self).create(vals)
        return res
    
    
    @api.onchange('status')
    def _compute_custom(self):
        if self._origin.status:
            print(self.env.cr.now(), self.status_start_date)
            prev_status = self._origin.status
            new_status = self.status
            prev_status_start_date = self.status_start_date
            self.status_start_date = self.env.cr.now()
            time_difference_in_seconds = ((self.status_start_date - prev_status_start_date).total_seconds())
            time_difference_in_minutes = time_difference_in_seconds/60
            time_difference_in_hours = time_difference_in_minutes/60
            time_difference_in_days = time_difference_in_hours/24
            


        # print(self.status.__dir__())
        # for rec in self:
        #     print(rec.status)
        #     print(rec.__dict__())
        # print(self.__dir__())
        
    # acq_manager = fields.Selection([
    #         ('louise', 'Loise'), ('ken', 'Ken'), ('test', 'Test')
    #     ], required = True, tracking = True, string = 'ACQ Manager')
    
    
    # partner_country = fields.Selection([
    #         ('malaysia', 'Malaysia'), ('singapore', 'Singapore'), ('indonesia', 'Indonesia'),
    #         ('thailand', 'Thailand'), ('philippines', 'Philippines'), ('vietnam', 'Vietnam'),
    #         ('others', 'Others')
    #     ], required = True, tracking = True, string = 'Partner Country')
    
    
    # @api.model
    # def default_get(self, fields):
    #     res = super(HospitalPatient, self).default_get(fields)
    #     res['note'] = 'NEW Patient Created'
    #     return res

    # name = fields.Char(string='Name', required=True, tracking=True)
    # reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
    #                         default=lambda self: _('New'))
    # age = fields.Integer(string='Age', tracking=True)
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('other', 'Other'),
    # ], required=True, default='male', tracking=True)
    # note = fields.Text(string='Description')
    # state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
    #                           ('done', 'Done'), ('cancel', 'Cancelled')], default='draft',
    #                          string="Status", tracking=True)
    # responsible_id = fields.Many2one('res.partner', string="Responsible")
    # appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    # image = fields.Binary(string="Patient Image")
    # appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string="Appointments")

    # def _compute_appointment_count(self):
    #     for rec in self:
    #         appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])
    #         rec.appointment_count = appointment_count

    # def action_confirm(self):
    #     for rec in self:
    #         rec.state = 'confirm'

    # def action_done(self):
    #     for rec in self:
    #         rec.state = 'done'

    # def action_draft(self):
    #     for rec in self:
    #         rec.state = 'draft'

    # def action_cancel(self):
    #     for rec in self:
    #         rec.state = 'cancel'

    # @api.model
    # def create(self, vals):
    #     if not vals.get('note'):
    #         vals['note'] = 'New Patient'
    #     if vals.get('reference', _('New')) == _('New'):
    #         vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
    #     res = super(HospitalPatient, self).create(vals)
    #     return res

    # @api.constrains('name')
    # def check_name(self):
    #     for rec in self:
    #         patients = self.env['hospital.patient'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
    #         if patients:
    #             raise ValidationError(_("Name %s Already Exists" % rec.name))

    # @api.constrains('age')
    # def check_age(self):
    #     for rec in self:
    #         if rec.age == 0:
    #             raise ValidationError(_("Age Cannot Be Zero .. !"))

    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         name = '[' + rec.reference + '] ' + rec.name
    #         result.append((rec.id, name))
    #     return result

    # def action_open_appointments(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Appointments',
    #         'res_model': 'hospital.appointment',
    #         'domain': [('patient_id', '=', self.id)],
    #         'context': {'default_patient_id': self.id},
    #         'view_mode': 'tree,form',
    #         'target': 'current',
    #     }