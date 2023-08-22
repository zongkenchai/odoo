# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class PartnerType(models.Model):
    _name = "crm2.partner_type"
    _description = "Partner Type"
    _order = "id asc"
    _rec_name = 'type'
    _sql_constraints = [
                        ('field_unique', 
                        'unique(type)',
                        'Choose another value - it has to be unique!')
    ]
    
    
    type = fields.Char(string = 'Type', required = True)

                
                    

    
    