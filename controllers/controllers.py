# -*- coding: utf-8 -*-
from odoo import http

# class MethodStokGenerarAjuste(http.Controller):
#     @http.route('/method_stok_generar_ajuste/method_stok_generar_ajuste/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_stok_generar_ajuste/method_stok_generar_ajuste/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_stok_generar_ajuste.listing', {
#             'root': '/method_stok_generar_ajuste/method_stok_generar_ajuste',
#             'objects': http.request.env['method_stok_generar_ajuste.method_stok_generar_ajuste'].search([]),
#         })

#     @http.route('/method_stok_generar_ajuste/method_stok_generar_ajuste/objects/<model("method_stok_generar_ajuste.method_stok_generar_ajuste"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_stok_generar_ajuste.object', {
#             'object': obj
#         })