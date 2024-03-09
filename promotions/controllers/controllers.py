# -*- coding: utf-8 -*-
# from odoo import http


# class Promotions(http.Controller):
#     @http.route('/promotions/promotions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/promotions/promotions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('promotions.listing', {
#             'root': '/promotions/promotions',
#             'objects': http.request.env['promotions.promotions'].search([]),
#         })

#     @http.route('/promotions/promotions/objects/<model("promotions.promotions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('promotions.object', {
#             'object': obj
#         })
