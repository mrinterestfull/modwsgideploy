try:
    choice = input('You said Y to subdomain').lower()
except NameError:
    choice = raw_input('You said Y to subdomain').lower()

print(choice)

import os
#os.path.basename(os.path.dirname(os.path.realpath(__file__)))
workfolder=os.path.dirname(os.path.realpath(__file__))
#workfolder=os.path.dirname(__file__)

try:
    choice2 = input('Is this the project location? Press Enter if yes, otherwise enter a new path: '+str(workfolder))
    if choice2=='':
        print(workfolder)
    else:
        print(choice2)
except NameError:
    choice2 = input('Is this the project location? Press Enter if yes, otherwise enter a new path: '+str(workfolder))
    if choice2=='':
        print(workfolder)
    else:
        print(choice2)
#current_folder=os.path.dirname(os.path.realpath(__file__))
