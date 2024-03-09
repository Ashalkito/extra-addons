# -*- coding: utf-8 -*-
# from odoo import http


# class VideoclubAitor(http.Controller):
#     @http.route('/videoclub_aitor/videoclub_aitor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/videoclub_aitor/videoclub_aitor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('videoclub_aitor.listing', {
#             'root': '/videoclub_aitor/videoclub_aitor',
#             'objects': http.request.env['videoclub_aitor.videoclub_aitor'].search([]),
#         })

#     @http.route('/videoclub_aitor/videoclub_aitor/objects/<model("videoclub_aitor.videoclub_aitor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('videoclub_aitor.object', {
#             'object': obj
#         })
