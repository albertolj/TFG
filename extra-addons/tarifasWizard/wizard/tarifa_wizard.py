# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TarifaWizard(models.TransientModel):
    _name = 'tarifa_wizard'
    _description = "Confirmar un pedido por debajo de la tarifa"

    order_id = fields.Many2one('sale.order', string='Sale Order', required=True)

    def action_confirm_tarifa(self):
        self.order_id.write({'state': 'waiting', 'date_order': fields.Datetime.now()})

    @api.model
    def default_get(self, fields):
        result = super(TarifaWizard, self).default_get(fields)
        ord_id = self.env.context.get('order_id')
        if self.env.context.get('order_id'):
            result.update({
                'order_id': ord_id
            })
        return result
        
        