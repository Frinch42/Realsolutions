from odoo import _, api, fields, models, tools

class RealOdooTool(models.TransientModel):
    '''
    a wizard to show the result of an action in an overlay to be clicked
    '''
    _name = 'real.odoo.tool'

    @api.model
    def config_get(self, key, default=None):
        '''
        get value from odoo.conf
        '''
        value = tools.config.get(key, default)

        return value

    @api.model
    def drop_view_if_exists(self, model_name):
        model_proxy = self.env[model_name]
        tools.drop_view_if_exists(self.env.cr, model_proxy._name)

    @api.model
    def set_state(self, model_name, ids, state):
        model_proxy = self.env[model_name]
        self.env.cr.execute("update %s set state = '%s' where id in (%s);" % \
                (model_proxy._table, state, ','.join([str(id) for id in ids])))
        return False
