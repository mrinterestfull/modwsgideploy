#Created by modwsgideploy script for {{cookiecutter.package_name}}


#Debian:  ${package_folder}/${package_name}

# Make sure apache2 user owns ${package_name}.wsgi and can write to ${workfolder}/.python-eggs.
# This are the only two file it needs to own.
# The rest of the folders and your source code can be owned by other user.
# Debian: chown -R www-data:www-data ${workfolder}/${package_name}.wsgi
# Debian: chown -R www-data:www-data '${workfolder}/.python-eggs'


#
import os
os.environ['PYTHON_EGG_CACHE'] = '${workfolder}/.python-eggs'

from pyramid.paster import get_app, setup_logging
ini_path = '${package_folder}/${package_name}/${deployment_prod_or_dev}'
setup_logging(ini_path)
application = get_app(ini_path, 'main')


#[Optional] If you want to test modwsgi only, uncomment section 3 in your ${workfolder}/${package_name}.conf
