Deployment using mod_wsgi and apache. Below instructions will tell you how to quickly deploy your turbogears2 app using mod_wsgi.

Install modwsgideploy
---------------------

PYPI
~~~~

You can install modwsgideploy from PyPi::

 easy_install modwsgideploy

Done.

Source Install
~~~~~~~~~~~~~~

You also have a choice of getting the source and installing it.
You should use this in a virtual environment, for example::

 virtalenv --no-site-packages BASELINE
 source BASELINE/bin/activate

Install [:Bazaar:] if its not already installed on your system::

 easy_install bzr

Branch out the code. This will pull all the revision history. If you want just the recent one use checkout::

 bzr branch https://code.launchpad.net/~szybalski/modwsgideploy/trunk/ modwsgideploy_code

Install it::

 cd modwsgideploy_code/trunk
 python setup.py develop

Run modwsgi_deploy 
------------------

Go into your python application project folder and type in::

 paster modwsgi_deploy


Example
-------

Here is a typical installation, from start to finish on Debian Linux. You might have to use you OS specific commands for installing apache. 

The steps are:
1) Install apache and modwsgi
2) Setup virtual environment and install tg2
3) Create tg2 app 'myapp'
4) Install modwsgideploy and tweak wsgi settings to fit your needs or use default settings.
5) Check if everything is running properly.

In this case I will install apache using tools available from my Linux operating system::

 aptitude install apache2
 aptitude install libapache2-mod-wsgi
 virtualenv --no-site-packages BASELINE
 source BASELINE/bin/activate
 easy_install -i http://www.turbogears.org/2.0/downloads/current/index tg.devtools
 paster quickstart myapp
 
Install modwsgideploy::

 easy_install modwsgideploy

Go into you app and run modwsgi_deploy command::

 cd myapp
 paster modwsgi_deploy

You should see an apache folder like this inside 'myapp'::

 myapp
 |-- apache
 |   |-- README.txt
 |   |-- myapp
 |   |-- myapp.wsgi
 |   `-- test.wsgi
 

1. Read the README.txt
2. myapp is a apache configuration file that you need to copy into your apache configuration folder after all the settings are set.
3. myapp.wsgi is an modwsgi script that is called from myapp apache file
4. test.wsgi is a test script that you can call to see if you modwsgi was properly installed and working.

Edit myapp file to change any paths and/or apache configurations. Then copy to apache folder. 

On my operating system I copy this file to::

 cp ./apache/myapp /etc/apache2/sites-available/

Enable the website. On my OS its::

 a2ensite myapp
 /etc/init.d/apache restart

Done

Feedback
--------

If you have a useful sample wsgi script or apache config that you would like to share, please sent it to Turbogears mailing list.   

