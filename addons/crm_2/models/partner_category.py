# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class PartnerCategory(models.Model):
    _name = "crm2.partner_category"
    _description = "Partner Category"
    _order = "id asc"
    _rec_name = 'category_name'
    _sql_constraints = [
                        ('field_unique', 
                        'unique(category_name)',
                        'Choose another value - it has to be unique!')
    ]
    category_name = fields.Char(string = 'Category', required = True)

                
                    

    
    