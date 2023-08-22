# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountManager(models.Model):
    _name = "crm2.account_manager"
    _description = "Account Manager"
    _order = "id desc"
    _rec_name = 'full_name'

    first_name = fields.Char(string = 'First Name', required = True)
    last_name = fields.Char(string = 'Last Name')
    full_name = fields.Char(compute = '_compute_full_name')
    is_active = fields.Boolean(default = True)
    
    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for rec in self:
            if type(rec.first_name) != bool and type(rec.last_name) != bool:
                self.full_name = f'{rec.first_name} {rec.last_name}'
            elif type(rec.first_name) != bool and type(rec.last_name) == bool:
                self.full_name = rec.first_name
            else:
                self.full_name = ''
                
                    

    
    