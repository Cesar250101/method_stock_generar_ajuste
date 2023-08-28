# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class AjustesInventario(models.Model):
    _inherit = 'stock.inventory'
    
    @api.multi
    def genera_productos(self):
        if not self.line_ids:
            product_ids=self.env['product.product'].search([('type','=','product')])
            model_stock_inventoty_line=self.env['stock.inventory.line']
            for i in product_ids:
                model_stock_inventoty_line=self.env['stock.inventory.line'].search([('product_id','=',i.id)],limit=1)
                values={
                    'product_id':i.id,
                    'product_uom_id':i.uom_id.id,
                    'location_id':self.location_id.id,
                    'theoretical_qty':0,
                    'product_qty':0,
                    'inventory_id':self.id
                }
                if not model_stock_inventoty_line:
                    model_stock_inventoty_line.create(values)
                else:
                    model_stock_inventoty_line.write(values)
        else:
            raise Warning("Para esta opción no deben existir productos en la actual toma de inventario!")
        return

    