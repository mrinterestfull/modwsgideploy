print({{cookiecutter}})
context={{cookiecutter}}
print(context)
from mako.template import Template
from mako.lookup import TemplateLookup

import os
workfolder=os.getcwd()

#mylookup = TemplateLookup(directories=[workfolder], module_directory='/tmp/mako_modules')
mylookup = TemplateLookup(directories=[workfolder])

def serve_template(templatename, **kwargs):
        mytemplate2 = mylookup.get_template(templatename)
        print('rendering' + templatename)
        #print(mytemplate2.render(**kwargs))
        return mytemplate2.render(**kwargs)


for myfolder in os.walk(workfolder):
    for mytemplate in myfolder[2]:
        newtemplate=serve_template(mytemplate,**context)
        print(os.path.join(myfolder[0],mytemplate))
        f=open(os.path.join(myfolder[0],mytemplate),'w')
        f.write(newtemplate)
        f.close()




import pdb;pdb.set_trace()
