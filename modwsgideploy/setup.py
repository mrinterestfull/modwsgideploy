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


#Needed to add to package_data
def add_to_package_data(pkg, roots):
    """Generic function to find package_data.
    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.
    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}



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
    #package_data=add_to_package_data("{{cookiecutter.folder_name}}")
    #This causes to be included in bdist, vs Manifest.in only gets included in sdist
    # data_files=[('{{cookiecutter.folder_name}}', ['*']),
    #               ('config', ['cfg/data.cfg']),
    #               ('/etc/init.d', ['init-script'])],
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
