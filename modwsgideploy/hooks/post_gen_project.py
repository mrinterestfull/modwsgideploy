import os
#os.path.basename(os.path.dirname(os.path.realpath(__file__)))
#workfolder=os.path.dirname(os.path.realpath(__file__))
#workfolder=os.path.dirname(__file__)
context={{cookiecutter}}

def ask_more_questions(question=None):
    try:
        output = raw_input(question)
        #output = input(question)
    except NameError:
        output = input(question)
        #output = raw_input(question)
    return output
#import pdb; pdb.set_trace()

#Getting the folder we are working at
workfolder=os.getcwd()
package_folder=os.path.abspath(os.path.join(workfolder,'../'))

#ask about workfolder
ask_workfolder=ask_more_questions(question='package_folder ['+str(package_folder) +']:')
if not ask_workfolder=='':
    package_folder=ask_workfolder
context['package_folder']=package_folder

#Where this program is creating conf and wsgi files.
context['wsgi_folder']=workfolder
context['workfolder']=workfolder
context['user_name']=os.getlogin()
context['static']=os.path.join('/',context['mount_point'],'static')

#ask about workfolder
# ask_virtualenv=ask_more_questions('Virtual environment path: /envProject Folder ['+str(workfolder) +']:')
# if ask_workfolder=='':
#     print(workfolder)
# else:
#     workfolder=ask_workfolder
# context['workfolder']=workfolder

#Ask about virtualenv
# virtual_environment_path=ask_more_questions('virtual_environment_path: /usr/local/{{cookiecutter.framework_to_deploy}}/env_py3: ')
# context['virtual_environment_path']=(virtual_environment_path or '/usr/local/{{cookiecutter.framework_to_deploy}}/env_py3')

#pyramid
if context['framework_to_deploy']=='pyramid':
    deployment_prod_or_dev=ask_more_questions(question='deployment_prod_or_dev: [development.ini] or production.ini :')
    context['deployment_prod_or_dev']=(deployment_prod_or_dev or 'development.ini')
#print(context['framework_to_deploy'])


#current_folder=os.path.dirname(os.path.realpath(__file__))
# if "{{cookiecutter.framework_to_deploy}}"=='pyramid':
#     default_folder='/usr/local/pyramid'
# elif "{{cookiecutter.framework_to_deploy}}"=='django':
#     default_folder='/usr/local/django'
# else:
#     default_folder='/usr/local/{{cookiecutter.package_name}}.'
# context['default_folder']=default_folder


from mako.template import Template
from mako.lookup import TemplateLookup

import os
workfolder=os.getcwd()

#mylookup = TemplateLookup(directories=[workfolder], module_directory='/tmp/mako_modules')
mylookup = TemplateLookup(directories=[workfolder],strict_undefined=True)

def serve_template(templatename, **kwargs):
        mytemplate2 = mylookup.get_template(templatename)
        #print('Rendering: ' + templatename)
        #print(mytemplate2.render(**kwargs))
        return mytemplate2.render(**kwargs)

#This loops through a files in a workfolder. I need more testing to confirm the work folder is where I think it is.
#For now I'm changing to below where I explicily render the template by name.
# for myfolder in os.walk(workfolder):
#     for mytemplate in myfolder[2]:
#         newtemplate=serve_template(mytemplate,**context)
#         print(os.path.join(myfolder[0],mytemplate))
#         f=open(os.path.join(myfolder[0],mytemplate),'w')
#         f.write(newtemplate)
#         f.close()
#

#Render each template explicily
def save_template(workfolder=None,file_name=None,context=None):
    newtemplate=serve_template(file_name,**context)
    print('Saving: '+workfolder+'/'+file_name)
    f=open(os.path.join(workfolder,file_name),'w')
    f.write(newtemplate)
    f.close()

#print(context['use_virtualhost'])
#print(context['host_as_subdomain'])
file_name= context['package_name']+'.wsgi'
save_template(workfolder,file_name,context)

file_name= context['package_name']+'.conf'
save_template(workfolder,file_name,context)

file_name= 'README.txt'
save_template(workfolder,file_name,context)

#print('\nThank you for deploying with modwsgideploy')
#print('\nBuild in Chicago, IL United States of America')
#print('''\nIf you have an idea that will make other peoples' life better and you need a partner. Reach out to us: parnter@dataassistant.co''')

print('''
===============================================================================
Documentation:          http://lucasmanual.com/mywiki/modwsgideploy
Mod-wsgi Mailing List:  https://groups.google.com/forum/#!forum/modwsgi
Modwsgideploy Chat:  https://gitter.im/dataassistant-co/modwsgideploy
Welcome to modwsgideploy.  Build a web that make other people's life better.
===============================================================================

Change directory into your newly created folder.
    cd {{cookiecutter.folder_name}}

Copy the {{cookiecutter.package_name}}.conf to Apache2 sites-available folder (Debian/Ubuntu).
    cp {{cookiecutter.package_name}}.conf /etc/apache2/sites-available/

Enable the new apache2 site
    a2ensite {{cookiecutter.package_name}}

You can change the owner of the wsgi and .python-eggs folder to apache owner.
    chown www-data:www-data {{cookiecutter.package_name}}.wsgi
    chown www-data:www-data .python-eggs

Reload Apache2:
    services apache2 reload

Watch the error log and go visit your site.
    tail -f /var/log/apache2/error.log   #(CTRL +c to get out)

Run your project at full speed.
''')
