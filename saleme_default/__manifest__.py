##############################################################################
#
#    Copyright (C) 2020  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   le agregamos esto
##############################################################################

{
    'name': 'saleme',
    'version': '15.0.1.0.0',
    'category': 'Project',
    'summary': "Customization for saleme",
    'author': "Ing. Gabriela Rivero",
    'website': 'http://github.com/regaby/module-repo',
    'license': 'AGPL-3',
    'depends': ['website_sale', 'sale_management', 'stock'],
    'installable': True,

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    'port': '8069',

    'git-repos': [
        'https://github.com/regaby/cl-saleme.git',
        'https://github.com/aamaral2020/AlmacenSaleme_241122 -b main',
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo regaby/odoo-ce:15.0',
        'postgres postgres:10.1-alpine',
    ]
}
