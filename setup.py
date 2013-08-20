#!python
from ez_setup import use_setuptools
use_setuptools()

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='Django-PostBox',
    version='0.1',
    packages=['PostBox'],
    install_requires = [
        'Django == 1.5.1',
        'MySQL-python == 1.2.3',
        ],
    dependency_links = [
        'thirdparty',
        ],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to share feedback within a team.',
    long_description=README,
    author='Antony M S J',
    author_email='antony_sakkariaz@dell.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Team Members',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    )
