# -*- coding: utf-8 -*-

# standard python modules
import logging, random, threading, time, traceback

# pip
try:
    from pip.operations.freeze import freeze
    from pip.utils import get_installed_distributions
except:
    from pip._internal.operations.freeze import freeze
    from pip._internal.utils.misc import get_installed_distributions

# odoo
from odoo import models, fields, api, _
from odoo.exceptions import UserError

# real
from real.environment.util import find_path
# local modules

_logger = logging.getLogger(__name__)
class RealBase(models.TransientModel):
    '''
    just a transient node to access common functionality
    '''
    _name = 'real.base'
    @api.model
    def requirements_txt(self):
        '''
        return dependencies in requirements.txt format like the output
        of "pip freeze"
        '''
        # the packages to skip is magic but is what 'pip freeze' uses
        # when called from the command line
        requirements = freeze(skip=['wheel', 'argparse', 'python', 'distribute',
            'wsgiref', 'setuptools', 'pip'])
        requirements_txt = '\n'.join(requirements) + '\n'
        return requirements_txt

    @api.model
    def installed_distributions(self):
        '''
        return the output of "pip list" to see or compare versions of installed packages
        '''
        packages = get_installed_distributions()

        installed_distributions = []
        for package in packages:
            installed_distributions.append({
                    'project_name': package.project_name,
                    'version': package.version,
                    'egg_name': package.egg_name(),
                    'location': package.location,
            })

        return installed_distributions

    @api.model
    def odoo_conf(self):
        '''
        return odoo.conf file content
        '''
        # walk up to the root and find odoo.conf
        odoo_conf_path = find_path('etc/odoo.conf')
        odoo_conf_file = open(odoo_conf_path)
        odoo_conf = odoo_conf_file.read()
        return odoo_conf
