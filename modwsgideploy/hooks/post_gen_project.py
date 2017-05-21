import os
#os.path.basename(os.path.dirname(os.path.realpath(__file__)))
#workfolder=os.path.dirname(os.path.realpath(__file__))
#workfolder=os.path.dirname(__file__)
context={{cookiecutter}}

workfolder=os.getcwd()

try:
    choice2 = input('Project Folder ['+str(workfolder) +']:')
    if choice2=='':
        print(workfolder)
    else:
        print(choice2)
except NameError:
    choice2 = raw_input('Project Folder ['+str(workfolder) +']:')
    if choice2=='':
        print(workfolder)
    else:
        print(choice2)
#import pdb; pdb.set_trace()

if choice2=='':
    print(workfolder)
else:
    workfolder=choice2
context['workfolder']=workfolder

#current_folder=os.path.dirname(os.path.realpath(__file__))
if "{{cookiecutter.framework_to_deploy}}"==1:
    default_folder='/usr/local/pyramid'
elif "{{cookiecutter.framework_to_deploy}}"==2:
    default_folder='/usr/local/django'
else:
    default_folder='.'
context['default_folder']=default_folder


from mako.template import Template
from mako.lookup import TemplateLookup

import os
workfolder=os.getcwd()

#mylookup = TemplateLookup(directories=[workfolder], module_directory='/tmp/mako_modules')
mylookup = TemplateLookup(directories=[workfolder])

def serve_template(templatename, **kwargs):
        mytemplate2 = mylookup.get_template(templatename)
        print('rendering: ' + templatename)
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
    f=open(os.path.join(workfolder,file_name),'w')
    f.write(newtemplate)
    f.close()

file_name= context['package_name']+'.wsgi'
save_template(workfolder,file_name,context)

file_name= context['package_name']+'.conf'
save_template(workfolder,file_name,context)

file_name= 'README.txt'
save_template(workfolder,file_name,context)


#import pdb;pdb.set_trace()
