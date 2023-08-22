{
    'name' : 'CRM TESTING 2',
    'author' : 'Ken',
    'sequence': 15,
    'summary': 'Track leads and close opportunities',
    'depends' : ['base', 'mail'],
    'data' : [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/crm_leads_view.xml',
        'views/crm_account_manager_view.xml',
        'views/crm_acquisition_manager_view.xml',
        'views/crm_country_view.xml',
        'views/crm_partner_category_view.xml',
        'views/crm_partner_type_view.xml',
    ]
}