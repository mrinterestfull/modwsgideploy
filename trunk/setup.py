from setuptools import setup, find_packages
import sys, os

version = '0.4.12'

setup(name='modwsgideploy',
      version=version,
      description="Deploy Turbogears2 or Pylons via apache and modwsgi.",
      long_description="""\
Templates builds a wsgi file and apache config file that user puts in apache and runs the app in few simple steps.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='apache mod_wsgi turbogears pylons deploy script',
      author='Lukasz Szybalski',
      author_email='szybalski@gmail.com',
      url='http://lucasmanual.com/mywiki/modwsgideploy',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "cheetah>=2.0" ,
        "pastescript>=1.0", 
        # -*- Extra requirements: -*-
      ],
      entry_points="""
        [paste.global_paster_command]
        modwsgi_deploy = modwsgideploy.commands:ModwsgiCommand
      """,
      )
