# -*- coding: utf-8 -*-
from odoo import http
#
#
# class AbcApiDevelop(http.Controller):
#     @http.route('/abc/api/develop',  auth='public', website=False, type='http', methods=['GET'])
#     def index(self, **kw):
#         sum = int(kw['a']) + int(kw['b'])
#         sub = int(kw['a']) - int(kw['b'])
#         mul = int(kw['a']) * int(kw['b'])
#         div = int(kw['a']) / int(kw['b'])
#
#         return "Sum: "+str(sum)+"\n"+"Sub: "+str(sub)+"\n"+"Mul: "+str(mul)+"\n"+"Div: "+str(div)


class AbcApiDevelop(http.Controller):
    @http.route('/abc/api/contact/develop',  auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        contacts = http.request.env['res.partner'].sudo().search([])
        contacts_list = []
        for x in contacts:
            contacts_list.append({

                'Contact':x.type,
                'Job Position':x.function,
                'Email':x.email,
                'Phone':x.phone,


            })

        return contacts_list

#CRM CUstomer API

class AbcApiDevelop(http.Controller):
    @http.route('/abc/api/crm/develop',  auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        crm = http.request.env['crm.lead'].sudo().search([])
        customer_list = []
        for x in crm:
            customer_list.append({

                'Customer':x.partner_id,
                'Sales Team':x.team_id,
                'Email':x.email_from,
                'Phone':x.phone,


            })

        return customer_list


#CRM Pipeline

class AbcApiDevelop(http.Controller):
    @http.route('/abc/api/crm/pip/develop',  auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        crm = http.request.env['crm.lead'].sudo().search([])
        contact = []
        for x in crm:
            contact.append({

                'Company Name':x.partner_name,
                'Contact Name':x.contact_name,
                'Website':x.website,
                'Address':x.street,


            })

        return contact

#Add Api CRM

class AbcApiDevelop(http.Controller):
    @http.route('/abc/api/crm/add/develop',  auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        http.request.env['crm.lead'].sudo().create(kw)
        return kw
# import logging
# _logger = logging.getLogger(__name__)

#Add contact Api

class AbcApiDevelop(http.Controller):
    @http.route('/abc/api/contact/add/develop',  auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        # _logger.info(kw)
        http.request.env['res.partner'].sudo().create(kw)
        return kw

#contact update Api

class AbcApiDevelop(http.Controller):
    @http.route('/abc/api/contact/update/develop', auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
       user = http.request.env['res.partner'].sudo().search([('id','=',kw['id'])])
       user.write({
           'name':kw['name'],
           'email':kw['email'],
           'phone': kw['phone'],
           'mobile': kw['mobile'],
           'website': kw['website'],

       })

       return kw














