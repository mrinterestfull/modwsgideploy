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


test_requirements = [
            # TODO: put package test requirements here
            ]


setup(
    name='modwsgideploy',
    version=version,
    keywords='apache2 mod_wsgi turbogears pyramid deploy script',
    author='Lukasz Szybalski',
    author_email='szybalski@gmail.com',
    url='http://lucasmanual.com/mywiki/modwsgideploy',
    description="Deploy Pyramid via apache2 and modwsgi.",
    long_description=readme,
    license='BSD',
    #packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    packages=[
                 'modwsgideploy',
                     ],
    package_dir={'modwsgideploy':
                         'modwsgideploy'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        #"cheetah>=2.0" ,
        #"pastescript>=2.0",#Moving to cookiecutter
        "cookiecutter>=1.5",
        "mako",
        'Click>=6.0',
        # -*- Extra requirements: -*-
    ],
    entry_points={
        'console_scripts':[
             'modwsgideploy=modwsgideploy.cli:main'
            #'hello=modwsgideploy:say_hello'
        ],
    },
    classifiers=[ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements

    #"""
    #    [paste.global_paster_command]
    #    modwsgi_deploy = modwsgideploy.commands:ModwsgiCommand
    #""",
    )
