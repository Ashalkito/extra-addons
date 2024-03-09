# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Clasificacion(models.Model):
    _name = 'promotions.clasificacion'
    _description = 'Clasificación de Promoción'

    name = fields.Char('Nombre', required=True, help='Nombre de la clasificación de promoción')
    descripcion = fields.Text('Descripción', help='Descripción de la clasificación de promoción')

class Promocion(models.Model):
    _name = 'promotions.promocion'
    _description = 'Promoción'

    name = fields.Char('Nombre', size=30, required=True, help='Nombre de la promoción')
    descripcion = fields.Char('Descripción', size=300, help='Descripción de la promo')
    descuento = fields.Float('Descuento')
    fechainicio = fields.Date('Fecha de inicio')
    imagen = fields.Binary('Imagen')

    clasificacion_id = fields.Many2one('promotions.clasificacion', string='Clasificación', required=True)

    
    # Campos calculados
    pequeno = fields.Char(compute='_descuento_pequeno', store=True) 
    mediano = fields.Char(compute='_descuento_mediano', store=True) 
    grande = fields.Char(compute='_descuento_grande', store=True) 

    @api.depends('descuento')
    def _descuento_pequeno(self):
        for record in self:
            if record.descuento < 10:
                record.pequeno = "Pequeño"
            else:
                record.pequeno = ""

    @api.depends('descuento')
    def _descuento_mediano(self):
        for record in self:
            if 10 <= record.descuento <= 20:
                record.mediano = "Mediano"
            else:
                record.mediano = ""

    @api.depends('descuento')
    def _descuento_grande(self):
        for record in self:
            if record.descuento > 20:
                record.grande = "Grande"
            else:
                record.grande = ""


class ProductosPromocion(models.Model):
    _inherit = 'product.template' #Herencia

    descuento = fields.Float('Descuento')
    promocion_id = fields.Many2one('promotions.promocion', string='Promoción')

    @api.onchange('promocion_id', 'descuento')
    def _onchange_promocion_descuento(self):
        for product in self:
            if product.promocion_id and product.promocion_id.descuento:
                # Si hay una promoción seleccionada con descuento, se iguala el descuento del producto al de la promoción
                product.descuento = product.promocion_id.descuento
            else:
                # Si no hay promoción seleccionada con descuento, se establece el descuento del producto en 0
                product.descuento = 0
            
            # Se actualiza el list_price en función del nuevo descuento
            product.list_price = product._get_precio_con_descuento()

    def _get_precio_con_descuento(self):
        # Calcula el precio con descuento según el descuento del producto
        return self.list_price * (1 - (self.descuento / 100))

