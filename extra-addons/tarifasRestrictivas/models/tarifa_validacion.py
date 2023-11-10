# -*- coding: utf-8 -*-

from datetime import timedelta
from itertools import groupby
from markupsafe import Markup
import logging

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.fields import Command
from odoo.osv import expression
from odoo.tools import float_is_zero, format_amount, format_date, html_keep_url, is_html_empty
from odoo.tools.sql import create_index

from odoo.addons.payment import utils as payment_utils
import logging

_logger = logging.getLogger(__name__)

class tarifasExcepcion(models.Model):
    _inherit = 'sale.order'
    state = fields.Selection(selection_add=[('waiting', 'Pendiente de aprobación')])
    
        
    def action_confirm(self):

        for line in self.order_line:
            if (not(self.env.user.has_group('sales_team.group_sale_manager')) and not(self.env.user.has_group('equipoDeVentas.group_supervisor'))):
                tarifa = self.pricelist_id.get_product_price(line.product_id, line.product_uom_qty, self.partner_id)
                if (line.price_unit < tarifa):
                    return{
                        "type": "ir.actions.act_window",
                        "res_model": "tarifa_wizard",
                        "views": [[False, "form"]],
                        "target": "new",
                        "context": {'order_id': self.id}
                    }
            
        super(tarifasExcepcion, self).action_confirm()

    
            