# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Country(models.Model):
    _name = "crm2.country"
    _description = "Country"
    _order = "id asc"
    _rec_name = 'country_name'
    _sql_constraints = [
                        ('field_unique', 
                        'unique(country_name)',
                        'Choose another value - it has to be unique!')
    ]
    country_name = fields.Char(string = 'Country', required = True)

                
                    

    
    