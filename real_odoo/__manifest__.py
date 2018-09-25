# -*- coding: utf-8 -*-
{
    'name': "REAL Odoo",
    'summary': "Install some modules ",
    'description': """
        Install some modules.
    """,
    'author': "REAL Solutions S.A.",
    'website': "http://www.real.lu",
    'category': 'Uncategorized',
    'version':  '11.0.1.0.0',
    # any module necessary for this one to work correctly
    # sudo pip install -U pip setuptools
    # module non odoo a copier dans /odoo-build-env/odoo-version10-develop/src/addons:
    #                   mass_edit  : git clone https://github.com/OCA/server-tools.git
    #                   mass_excel : git clone -b 9.0-develop http://gitlab.real.net:8181/odoo-commons/mass_export.git

    'depends': [
        'web_enterprise',
    ],
    'data': [
        'views/assets.xml',
    ],
}
