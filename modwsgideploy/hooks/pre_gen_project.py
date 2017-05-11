import os
#os.path.basename(os.path.dirname(os.path.realpath(__file__)))
#workfolder=os.path.dirname(os.path.realpath(__file__))
workfolder=os.getcwd()
#workfolder=os.path.dirname(__file__)

try:
    choice2 = input('Project folder ['+str(workfolder) +']:')
    if choice2=='':
        print(workfolder)
    else:
        print(choice2)
except NameError:
    choice2 = raw_input('Project folder ['+str(workfolder) +']:')
    if choice2=='':
        print(workfolder)
    else:
        print(choice2)
import pdb; pdb.set_trace()

if choice2=='':
    print(workfolder)
else:
    workfolder=choice2
#current_folder=os.path.dirname(os.path.realpath(__file__))
if "{{cookiecutter.framework_to_deploy}}"==1:
    default_folder='/usr/local/pyramid'
elif "{{cookiecutter.framework_to_deploy}}"==2:
    default_folder='/usr/local/django'

Context={}
Context["cookiecutter"]= {
            'workfolder':workfolder
            }
Context["workfolder"]= 'ggggg'
context={}
context["workfolder"]= 'ggggg'
extra_context={'project_name2': 'TheGreatest'}
#from cookiecutter.main import cookiecutter
#cookiecutter(
#            'modwsgideploy',
#                extra_context={'workfolder': workfolder}
#                )
