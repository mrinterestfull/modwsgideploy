=============
modwsgideploy
=============


.. image:: https://img.shields.io/pypi/v/modwsgideploy.svg
        :target: https://pypi.python.org/pypi/modwsgideploy

.. image:: https://img.shields.io/travis/lszyba1/modwsgideploy.svg
        :target: https://travis-ci.org/lszyba1/modwsgideploy

.. image:: https://readthedocs.org/projects/modwsgideploy/badge/?version=latest
        :target: https://modwsgideploy.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/lszyba1/modwsgideploy/shield.svg
        :target: https://pyup.io/repos/github/lszyba1/modwsgideploy/
        :alt: Updates
.. image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
        :target: https://gitter.im/dataassistant-co/modwsgideploy


Deployment using mod_wsgi and apache. Below instructions will tell you how to quickly deploy your pyramid app using libapache2-mod-wsgi-py3.

Install modwsgideploy
---------------------

PYPI
~~~~

You can install modwsgideploy from PyPi::

 pip install modwsgideploy

Done.

Run modwsgideploy
------------------

Go into your python application project folder and type in::

 modwsgideploy


Example
-------

Here is a typical installation, from start to finish on Debian Linux. You might have to use you OS specific commands for installing apache.

The steps are:
1) Install apache and modwsgi
2) Setup virtual environment and install you web application written in pyramid,etc
3) Install modwsgideploy and run the modwsgideploy command above to generate all the configuration files.
4) Tweak apache/ .conf and .wsgi settings to fit your needs or use default settings.
5) Check if everything is running properly.

In this case I will install apache using tools available from my Linux operating system::

 apt-get install apache2
 apt-get install libapache2-mod-wsgi-py3
 virtualenv -p python3 --no-site-packages /usr/local/pyramid/env_py3
 source /usr/local/pyramid/env_py3/bin/activate
 pip install modwsgideploy

 Go into you app and run modwsgideploy command::

 cd myapp
 modwsgideploy

You should see an apache2 folder like this inside 'myapp'::

 myapp
 |-- apache2
 |   |-- .python-eggs
 |   |-- README.txt
 |   |-- myapp.conf
 |   |-- myapp.wsgi
 |   `-- test.wsgi

.. image:: https://raw.githubusercontent.com/lszyba1/modwsgideploy/master/docs/gif/tty.gif
        :target: https://github.com/lszyba1/modwsgideploy

1. Read the README.txt
2. myapp.conf is a apache2 configuration file that you need to copy into your apache2 configuration folder after all the settings are set.
3. myapp.wsgi is an modwsgi script that is called from myapp apache2 file
4. test.wsgi is a test script that you can call to see if you modwsgi was properly installed and working.

Edit myapp.conf file to change any paths and/or apache configurations. Then copy to apache2 folder in /etc/apache2/sites-available/.

On Debian Linux operating system I copy this file to::

 cp ./apache2/myapp.conf /etc/apache2/sites-available/

Enable the website. On my OS its::

 a2ensite myapp.conf
 /etc/init.d/apache restart

Done

Feedback
--------

If you have a useful sample wsgi script or apache config that you would like to share, please sent it https://gitter.im/dataassistant-co/modwsgideploy

Help
----

If you need help or would like to discuss: Go To: https://gitter.im/dataassistant-co/modwsgideploy


Release Notes
-------------
3.18.19
* Allow to change the subdomain name vs project name
* Fix bug that might cause apache2 error: Name duplicates previous WSGI daemon definition. bug#1_.
  .. _bug#1: https://github.com/lszyba1/modwsgideploy/issues/1

3.5.25
* Python3 Support
* Upgrade to new subsystem. Use cookiecutter
* Use post_gen_project.py to add additional functionality.
* ask_more_questions(question=None)
