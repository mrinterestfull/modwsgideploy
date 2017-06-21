#Created by modwsgideploy script for {{cookiecutter.package_name}}


#Debian:  ${package_folder}/${package_name}

# Make sure apache2 user owns ${package_name}.wsgi and can write to ${workfolder}/.python-eggs.
# This are the only two file it needs to own.
# The rest of the folders and your source code can be owned by other user.
# Debian: chown www-data:www-data ${workfolder}/${package_name}.wsgi
# Debian: chown -R www-data:www-data '${workfolder}/.python-eggs'


#
import os
os.environ['PYTHON_EGG_CACHE'] = '${workfolder}/.python-eggs'


% if framework_to_deploy=='pyramid':
#=================WSGI File for Pyramid=====================================
from pyramid.paster import get_app, setup_logging
ini_path = '${package_folder}/${deployment_prod_or_dev}'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
% endif

% if framework_to_deploy=='trac':
#===================WSGI File for trac====================================
#os.environ['TRAC_ENV'] = '/home/trac/trac'
os.environ['PKG_RESOURCES_CACHE_ZIP_MANIFEST'] = '1'

import trac.web.main
def application(environ, start_response):
  environ['trac.env_path'] = '${package_folder}'
  return trac.web.main.dispatch_request(environ, start_response)
% endif


% if framework_to_deploy=='django':
#====================WSGI File for Django ==============================
#For more information on this file, see
#https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "${package_name}.settings")
application = get_wsgi_application()
% endif
