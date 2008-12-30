http://lucasmanual.com/mywiki/modwsgideploy


   1. Install
   2. Get source
   3. Run modwsgi_deploy
   4. Example

Install

    *

      Install modwsgideploy from PyPi. 

easy_install modwsgideploy

Get source

    * You also have an option to get the source code.
    * You should use this in a virtul enviroment 

virtalenv --no-site-packages BASELINE
source BASELINE/bin/activate

    *

      Install Bazaar if its not already installed on your system. 

easy_install bzr

    * Branch out the code. This will pull all the revision history. If you want just the recent one use checkout. 

bzr branch https://code.launchpad.net/~szybalski/modwsgideploy/trunk/ modwsgideploy_code

    * Install it 

cd modwsgideploy_code/trunk
python setup.py develop

Run modwsgi_deploy

    * Go into your python application project folder and type in: 

paster modwsgi_deploy

Example

    * Here is a typical installation, from start to finish.
    * [Optional]If you don't have tg app ready here is how you create one.
    * Install apache, modwsgi, setup virtual enviroment, install tg2, create tg2 app 'myapp'. In this case I will install apache using tools available from my Linux operating system. 

aptitude install apache2
aptitude install libapache2-mod-wsgi
virtualenv --no-site-packages BASELINE
source BASELINE/bin/activate
easy_install -i http://www.turbogears.org/2.0/downloads/1.9.7b2/index/ tg.devtools
paster quickstart myapp

    * Install modwsgideploy 

easy_install modwsgideploy

    * Go into you app and run modwsgi_deploy command 

cd myapp
paster modwsgi_deploy

    * You should see an apache folder like this inside you 'myapp': 

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
   5. Edit myapp file to change any paths or apache configurations
   6. Copy to apache folder. On my operating system it is in: 

cp ./myapp /etc/apache2/sites-available/

    * Enable the website. On my OS its: 

a2ensite myapp
/etc/init.d/apache restart

