#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read()

config = {
    'name' : 'pelican-ab',
    'version' : '0.2.4',
    'packages' : find_packages(),
    'author' : 'Mr. Senko',
    'author_email' : 'atodorov@mrsenko.com',
    'license' : 'BSD',
    'description' : 'Support A/B testing for Pelican',
    'long_description' : long_description,
    'url' : 'https://github.com/MrSenko/pelican-ab',
    'keywords' : ['A/B testing', 'Pelican'],
    'classifiers' : [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    'zip_safe' : False,
    'install_requires' : ['pelican', 'jinja-ab>=0.3.0'],
}

setup(**config)
