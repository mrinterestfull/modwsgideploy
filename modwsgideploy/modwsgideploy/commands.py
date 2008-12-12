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

import pylons.util as util

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
        """Main command to create a tg.ext.geo controller"""
        output_dir = os.path.join(self.options.output_dir, 'apache')
        input_dir= source_filename = os.path.join(os.path.dirname(__file__), 'templates/apache')
        print self.args
        from paste.script import pluginlib
        egg_info_dir = pluginlib.find_egg_info_dir(os.getcwd())
        plugins= os.path.splitext(os.path.basename(egg_info_dir))[0]
        print os.path.splitext(os.path.basename(egg_info_dir))[0]
        dist_name= pluginlib.get_distro(plugins)
        if dist_name.has_metadata('PKG-INFO'):
            data=dist_name.get_metadata('PKG-INFO')
            for add_info in pluginlib.parse_lines(data):
                print add_info
        
        vars = {'project': plugins,
                'package': plugins,
                'egg': pluginlib.egg_name(str(dist_name)),
                }

        print 'var',vars
        print 'outdir',output_dir
        copy_dir(input_dir, output_dir, vars, verbosity=5, simulate=False, use_cheetah=True)

        return
        try:
            #fileOp = FileOp(source_dir=os.path.join(
            #    os.path.dirname(__file__), 'templates'))
            #try:
            #    print 'args', self.args
            #    name, directory = fileOp.parse_path_name_args(self.args[0])
            #except Exception ,e:
            #    print e
            #    raise BadCommand('No egg_info directory was found')

            # Check the name isn't the same as the package
            base_package = FileOp.find_dir('controllers', True)[0]
            if base_package.lower() == name.lower():
                raise BadCommand(
                    'Your controller name should not be the same as '
                    'the package name %r.' % base_package)

            # validate the name
            name = name.replace('-', '_')
            validateName(name)
            
            # Setup the controller
            fullname = os.path.join(directory, name)
            controller_name = util.class_name_from_module_name(
                name.split('/')[-1])
            if not fullname.startswith(os.sep):
                fullname = os.sep + fullname
            testname = fullname.replace(os.sep, '_')[1:]

            # set test file name
            #fullName = os.path.join(directory, name)
            #if not fullName.startswith(os.sep):
            #    fullName = os.sep + fullName
            #testName = fullName.replace(os.sep, '_')[1:]

            # set template vars
            #modName = name
            #fullModName = os.path.join(directory, name)
            #contrClass = util.class_name_from_module_name(name)
            #modelClass = util.class_name_from_module_name(singularName)
            #modelTabObj = name + '_table'

            # setup the controller
            fileOp.template_vars.update(
                {'name': controller_name,
                 'fname': os.path.join(directory, name),
                 'package':base_package,
                 })
            fileOp.copy_file(template='apache.wsgi_tmpl',
                         dest=os.path.join('apache', directory),
                         filename=name)
            if not self.options.no_test:
                fileOp.copy_file(template='test_apache.wsgi_tmpl',
                             dest=os.path.join('tests', 'functional'),
                             filename='test_' + testName)

        except BadCommand, e:
            raise BadCommand('An error occurred. %s' % e)
        except:
            msg = str(sys.exc_info()[1])
            raise BadCommand('An unknown error occurred. %s' % msg)


