#modwsgi script for ${package}

#1.Point to this script in you apache config file.
#Default location for all apps is:
#Debian:  /usr/local/turbogears/${package}

#2. Make sure apache user own the folder.
#Debian: chown -R www-data:www-data /usr/local/turbogears/${package}

#3.[Optional]If using modwsgi with virtualenv uncomment next few lines which will point to your virtualenv setup. 
#Make sure root owns the virtualenv folder. Example:(root:root)

import sys

#Using virtual enviroment. Uncomment next line.
#prev_sys_path = list(sys.path)

#Default location for virtualenv should be '/usr/local/pythonenv/BASELINE'. Create it using:
#mkdir /usr/local/pythonenv
#virtualenv --no-site-packages /usr/local/pythonenv/BASELINE


##Uncomment next 2 lines:
#import site. 
#site.addsitedir('/usr/local/pythonenv/BASELINE/lib/python2.5/site-packages')

##Move just added item to the front of the python system path. 
##Not needed if modwsgi>=3.0. Uncomment next 6 lines.
#new_sys_path = []
#for item in list(sys.path):
#    if item not in prev_sys_path:
#        new_sys_path.append(item)
#        sys.path.remove(item)
#sys.path[:0] = new_sys_path 


#4. Your website file location.
import os, sys
sys.path.append('/usr/local/turbogears/${package}')

#5. Set the environment variable PYTHON_EGG_CACHE to an appropriate directory where the Apache user has write permission and into which it can unpack egg files.
os.environ['PYTHON_EGG_CACHE'] = '/usr/local/turbogears/${package}/python-eggs'

#6.[Optional]If you want to enable logging you need to initialize logging. You also need to setup logger handlers in you production.ini. When done uncomment next two lines.
#from paste.script.util.logging_config import fileConfig
#fileConfig('/usr/local/turbogears/${package}/production.ini')

#7.[Not needed] Referance Only. 
#Pylons framework provides the paste.deploy.loadapp() function for constructing a WSGI application stack based on a specific configuration file.
#import pylons
#pylons.config.update({"server.webpath":"/${package}"})

#8. Load you application production.ini file.
from paste.deploy import loadapp
application = loadapp('config:/usr/local/turbogears/${package}/production.ini')


#9.[Optional] If you want to test modwsgi only, uncomment section 3 in you /usr/local/turbogears/${package}/apache/${package}.
