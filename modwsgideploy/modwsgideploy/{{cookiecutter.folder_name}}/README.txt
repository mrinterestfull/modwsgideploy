#We are about to deploy your ${framework_to_deploy} application.

#Please review your {{cookiecutter.package_name}}.conf

#To deploy on Debian/Ubuntu please read this conf file then:
#cp ${workfolder}/${package_name}.conf /etc/apache2/sites-available/${package_name}.conf
#a2ensite ${package_name}.conf

ls -l /etc/apache2/sites-available/
#You should see
#total 16
#-rw-r--r-- 1 root root  950 2008-08-08 13:06 default
#-rw-r--r-- 1 root root 7366 2008-08-08 13:06 default-ssl
#-rw-r--r-- 1 root root 1077 2008-11-08 12:38 ${package_name}


# Make sure apache2 user owns ${package_name}.wsgi and can write to ${workfolder}/.python-eggs.
# This are the only two file it needs to own.
# The rest of the folders and your source code can be owned by other user.
# Debian: chown www-data:www-data ${workfolder}/${package_name}.wsgi
# Debian: chown -R www-data:www-data '${workfolder}/.python-eggs'



#Reload apache
/etc/init.d/apache2 reload


#You are done. Your application should be working. Check the access.log, warn.log, and error.log in /var/log/apache to see if there are any errors.


#You Requested:
{{ cookiecutter | jsonify }}

${context.__dict__}


FAQ:
What is .python-eggs folder for?

The Python eggs directory is different to cache directories where individual py
files have their pyc files placed. The Python eggs directory is specifically
related to where Python packages distributed as an egg are expanded so they can
be used at runtime.
Wherever you put it, it needs to be a directory that the user that your code
runs as under Apache can write to.

Can I rename my conf file? My program is is being overwritten by another?

You can rename the file to something like 002-${package_name}.conf
Apache uses the number scheme to load files in sites-enabled so if you have
a main app running at 000-default.conf your 002-${package_name} would be loaded
next. You can change the order by changing the number.

Why should I user virtual environment: virtualenv -p python3 ${virtual_environment_path}?

Its a common practice to use your own environment for your package(s). The system
is not being affected by you installing upgrading or adding additional packages.
If at any point you have issues, you can easily re-created the environment. If you
were not using the virtual environment, your host linux system could potentially
get damaged by you upgrading python packages. The second benefit is that other
webapps will not interfere with your virtual environment.

Do I use embeded mode?
Embeded mode is for big websites with a lot of memory and visitors.
As of version 0.4.16 deamon mode is default and it should be used on Linux.
Visit modwsgi mailing list if you are getting some major traffic and you are concerned
with possible performance. Don't forget to adjust # of threads, and/or increase memory.



#Left over from prior version. No longer needed and depreciated. (DONT USE)
#############################
prev_sys_path = list(sys.path)

import site
site.addsitedir('/usr/local/pythonenv/BASELINE/lib/python2.5/site-packages')

\#Move just added item to the front of the python system path.
\#Not needed if modwsgi>=3.0. Uncomment next 6 lines.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

#Set the environment variable PYTHON_EGG_CACHE to an appropriate directory where the Apache user has write permission and into which it can unpack egg files.
os.environ['PYTHON_EGG_CACHE'] = '/usr/local/turbogears/${package_name}/python-eggs'

#If you want to enable logging you need to initialize logging. You also need to setup logger handlers in your production.ini. When done uncomment next two lines.
#from paste.script.util.logging_config import fileConfig
#fileConfig('/usr/local/turbogears/${package_name}/production.ini')

###############################
