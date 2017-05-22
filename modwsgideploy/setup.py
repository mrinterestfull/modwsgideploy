#Gets setuptools
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys, os

version = '3.5.21'

readme=long_description=open("README.rst").read()

setup(
    name='modwsgideploy',
    version=version,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='apache2 mod_wsgi turbogears pyramid deploy script',
    author='Lukasz Szybalski',
    author_email='szybalski@gmail.com',
    url='http://lucasmanual.com/mywiki/modwsgideploy',
    description="Deploy Pyramid, Turbogears2 Trac via apache2 and modwsgi.",
    long_description=readme,
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        #"cheetah>=2.0" ,
        #"pastescript>=2.0",#Moving to cookiecutter
        "cookiecutter>=1.5",
        "mako"
        # -*- Extra requirements: -*-
    ],
    entry_points={
        'console_scripts':[
            'hello=modwsgideploy:say_hello'
        ],
    }

    #"""
    #    [paste.global_paster_command]
    #    modwsgi_deploy = modwsgideploy.commands:ModwsgiCommand
    #""",
    )
