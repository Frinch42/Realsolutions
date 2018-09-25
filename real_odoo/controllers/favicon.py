# -*- coding: utf-8 -*-
# Copyright 2018 REal Solutions s.a. <http://www.real.lu>

# Odoo
from odoo import http
from odoo.tools import config
from odoo.tools.misc import file_open

class Favicon(http.Controller):
    @http.route('/real_odoo/favicon', type='http', auth="none")
    def favicon(self):
        instance_type = config.get('instance_type', 'develop')
        customer_module = config.get('customer_module', 'real_odoo')
        for extension, favicon_mimetype in [
                ('png', 'image/png'),
                ('ico', 'image/x-icon'),
                ('gif', 'image/gif'),
                ('svg', 'image/svg+xml'),
            ]:
            try:
                favicon_path = '%s/static/src/img/favicon-%s.%s' % \
                        (customer_module, instance_type, extension)
                favicon_file = file_open(favicon_path, 'rb')
            except IOError:
                continue
            break
        else:
            favicon_path = 'web/static/src/img/favicon.ico'
            favicon_file = file_open(favicon_path, 'rb')
            favicon_mimetype = 'image/x-icon'
        favicon_data = favicon_file.read()

        print('found favicon path', favicon_path) 

        response = http.request.make_response(favicon_data, [
                ('Content-Type', favicon_mimetype)
        ])
        return response
