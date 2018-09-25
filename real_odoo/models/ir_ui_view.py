# -*- coding: utf-8 -*-
from odoo import api, models
from odoo.tools import config

class View(models.Model):
    _inherit = 'ir.ui.view'

    @api.model
    def render(self, values=None, engine='ir.qweb'):
        if values is None:
            values = {}
        instance_type = config.get('instance_type', 'develop')
        values['instance_type'] = instance_type

        customer_module = config.get('customer_module', 'real_odoo')
        if customer_module != None:
            values['customer_module'] = customer_module

        return super(View, self).render(values=values, engine=engine)

