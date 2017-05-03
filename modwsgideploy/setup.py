#Gets setuptools
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys, os

version = '0.4.20'

readme=long_description=open("README.txt").read()

setup(
    name='modwsgideploy',
    version=version,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='apache mod_wsgi turbogears pylons deploy script',
    author='Lukasz Szybalski',
    author_email='szybalski@gmail.com',
    url='http://lucasmanual.com/mywiki/modwsgideploy',
    description="Deploy Turbogears2 or Pylons via apache and modwsgi.",
    long_description=readme,
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
