# -*- coding: utf-8 -*-
from odoo import models, fields, api

class VideoclubCategoria(models.Model):
    _name = 'videoclub.categoria'
    _description = 'Categoría de Película'

    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
    pelis_id = fields.One2many('videoclub.pelis', 'categoria_id', string='Categoría')

class compania_cinematografica(models.Model):
    #_name = 'res.partner' --no hace falta
    _inherit = 'res.partner'
    premiada = fields.Boolean(default='false')
    
class VideoclubPelis(models.Model):
    _name = 'videoclub.pelis'
    _description = 'Película'

    # Campos
    titulo = fields.Char('Título', size=30, required=True, help='Nombre de la película')
    director = fields.Char('Director', size=30, required=False, help='Director de la película', default='')
    clasificacion = fields.Selection([('TP', 'Todos los Públicos'), ('men12', 'Menores de 12 años'), ('may18', 'Mayores 18 años')], string='Clasificación', default='TP')
    presupuesto = fields.Integer('Presupuesto')
    fechaestreno = fields.Date('Fecha de Estreno')
    imagen = fields.Binary('Imagen')
    categoria_id = fields.Many2one('videoclub.categoria', string='Categoría')
    #Nueva relación Relación en las pelis
    compania = fields.Many2one('res.partner')

    # Campos calculados
    subvencionado = fields.Integer(compute='_valor_subvencion', store=True) # Se subvenciona el 30% de la película
    invertido = fields.Integer(compute='_valor_inversion', store=True) # Se invierte el 70% de la película
    millonario = fields.Boolean(compute='_es_millonario', store=True) # Verdadero si el presupuesto es mayor a un millón de euros

    @api.depends('presupuesto')
    def _valor_subvencion(self):
        for record in self:
            record.subvencionado = record.presupuesto * 0.3

    @api.depends('presupuesto')
    def _valor_inversion(self):
        for record in self:
            record.invertido = record.presupuesto * 0.7

    @api.depends('presupuesto')
    def _es_millonario(self):
        for record in self:
            record.millonario = record.presupuesto > 1000000  # 1 millón de euros


    