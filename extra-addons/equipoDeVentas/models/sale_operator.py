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
_logger = logging.getLogger(__name__)

class SaleOperator(models.Model):
    _inherit = 'sale.order'

    def write(self,vals):
        _logger.info('grupo operator: %s, User Id del pedido: %s, User Id: %s', self.env.user.has_group('equipoDeVentas.group_operators'), self.user_id, self.env.user.id)
        if self.env.user.has_group('equipoDeVentas.group_operators') and  (self.user_id.id!=self.env.user.id or self.user_id.id==False ):
            raise ValidationError('No puedes editar los pedidos que son de otro usuario. Por favor habla con su administrador')
        else:
            return super(SaleOperator, self).write(vals)
