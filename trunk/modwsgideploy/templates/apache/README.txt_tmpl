#1. Create production.ini configuration file 
cp development.ini production.ini
#Edit production.ini and delete the port settings. Default is 80.

#2. Change or check the apache settings file.
#Edit /usr/local/turbogears/${package}/apache/${package} and make sure it has the necessary apache configurations you need.
#Copy {$package} apache config file to apache folder.
cp /usr/local/turbogears/${package}/apache/${package} /etc/apache2/sites-available/${package}

#3.Check if permissions are the same as other apache sites usually (root:root)

ls -l /etc/apache2/sites-available/
#You shoud see
#total 16
#-rw-r--r-- 1 root root  950 2008-08-08 13:06 default
#-rw-r--r-- 1 root root 7366 2008-08-08 13:06 default-ssl
#-rw-r--r-- 1 root root 1077 2008-11-08 12:38 ${package}

#4.Enable your site.
a2ensite ${package}

#5. Check if your project has proper permissions, usually apache user. (Example: www-data:www-data). If it doesn't don't forget to change it.
ls -l /usr/local/turbogears/mainweb/apache/
#total 16
#-rw-r--r-- 1 www-data www-data 1077 2008-11-26 22:35 ${package}
#-rw-r--r-- 1 www-data www-data 2319 2008-11-26 23:25 ${package}.wsgi
#-rw-r--r-- 1 www-data www-data  594 2008-11-26 22:35 README.txt
#-rw-r--r-- 1 www-data www-data  538 2008-11-26 22:35 test.wsgi

#6.Reload apache
/etc/init.d/apache2 reload


#You are done. Your application should be working. Check the access.log, warn.log, and error.log in /var/log/apache to see if there are any errors. 
