"""Paster Commands, for use modwsgideploy project

The command(s) listed here are for use with Paste to enable easy creation of
various mowsgideploy files..

Currently available commands:

    modwsgi_deploy
"""

import os
import sys

from paste.script.command import Command, BadCommand
from paste.script.filemaker import FileOp
from paste.script.copydir import copy_dir


#Needed to manipulate egg information
from paste.script import pluginlib

def can_import(name):
    """Attempt to __import__ the specified package/module, returning True when
    succeeding, otherwise False"""
    try:
        __import__(name)
        return True
    except ImportError:
        return False

def validateName(name):
    """Validate that the name for the layer isn't present on the
    path already"""
    if not name:
        # This happens when the name is an existing directory
        raise BadCommand('Please give the name of a layer.')
    # 'setup' is a valid controller name, but when paster controller is ran
    # from the root directory of a project, importing setup will import the
    # project's setup.py causing a sys.exit(). Blame relative imports
    if name != 'setup' and can_import(name):
        raise BadCommand(
            "\n\nA module named '%s' is already present in your "
            "PYTHON_PATH.\nChoosing a conflicting name will likely cause "
            "import problems in\nyour controller at some point. It's "
            "suggested that you choose an\nalternate name, and if you'd "
            "like that name to be accessible as\n'%s', add a route "
            "to your projects config/routing.py file similar\nto:\n"
            "    map.connect('%s', controller='my_%s')" \
            % (name, name, name, name))
    return True

class ModwsgiCommand(Command):
    """Create a modwsgi apache configuration.

    The ModwsgiController command will create the standard apache template file.

    Example usage::

        yourproj% paster modwsgi_deploy
        Creating yourproj/yourproj/controllers/foos.py
        Creating yourproj/yourproj/tests/functional/test_foos.py

    If you'd like to have controllers underneath a directory, just include
    the path as the controller name and the necessary directories will be
    created for you::

        yourproj% paster geo-controller admin/foos
        Creating yourproj/controllers/admin
        Creating yourproj/yourproj/controllers/admin/foos.py
        Creating yourproj/yourproj/tests/functional/test_admin_foos.py
    """
    summary = __doc__.splitlines()[0]
    usage = '\n' + __doc__

    min_args = 0
    max_args = 1
    group_name = 'TurboGears2'

    default_verbosity = 3

    parser = Command.standard_parser(simulate=True)
    parser.add_option('--no-test',
                      action='store_true',
                      dest='no_test',
                      help="Don't create the test; just the controller")
    parser.add_option('-o', '--output-dir',
                      dest='output_dir',
                      metavar='DIR',
                      default='.',
                      help="Write put the directory into DIR (default current directory)")
    def command(self):
        """Main command to create a modwsgi configuration files"""
        #Output directory is current folder unless specified vi output command.
        output_dir = os.path.join(self.options.output_dir, 'apache')
        #Input where the templates are at.
        input_dir= source_filename = os.path.join(os.path.dirname(__file__), 'templates/apache')
        #Finding directory that has egg info
        egg_info_dir = pluginlib.find_egg_info_dir(os.getcwd())
        #Name of the module
        plugins= os.path.splitext(os.path.basename(egg_info_dir))[0]
        #print os.path.splitext(os.path.basename(egg_info_dir))[0]
        dist_name= pluginlib.get_distro(plugins)
        vars={}
        #If PKG-INFO exists read it and add it to vars
        if dist_name.has_metadata('PKG-INFO'):
            data=dist_name.get_metadata('PKG-INFO')
            for add_info in pluginlib.parse_lines(data):
                (key,value) = add_info.split(':',1)
                vars[key]=value
        #Add package names
        vars['project']=plugins
        vars['package']=plugins
        vars['egg']=pluginlib.egg_name(str(dist_name))
        
        #Copy my template direcotry to destination.
        copy_dir(input_dir, output_dir, vars, verbosity=1, simulate=False, use_cheetah=True)
        print 'Thank you for using modwsgideploy!'
        print 'Please read README.txt in apache folder.'
        print 'Made in Chicago, USA'

