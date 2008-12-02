from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='modwsgideploy',
      version=version,
      description="Template that helps to deploy via mod_wsgi and apache.",
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
          # -*- Extra requirements: -*-
      ],
      entry_points="""
        [paste.paster_create_template]
        modwsgideploy = modwsgideploy.modwsgideploy:FrameworkTemplate
      # -*- Entry points: -*-
      """,
      )
