#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')

requires = [
        'pyyaml==3.13',
        'slackclient==1.3.0',
        'redis==2.10.6',
        'json2html==1.0.0',
        'pytest==4.0.1'
]

def get_version():
    return "1.0.0"

setup(
    name="hambot",
    version=get_version(),
    author="Equinox",
    description="",
    long_description=open('README.md').read(),
    url="https://bitbucket.org/equinoxfitness/hambot",
    scripts=[],
    license="TBD",
    packages=find_packages(exclude=["tests*"]),
    install_requires=requires,
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    dependency_links=[
        "git+https://bitbucket.org/equinoxfitness/datacoco3.core.git#egg=cocore-1.0.0",
        "git+https://bitbucket.org/equinoxfitness/datacoco3.cloud.git#egg=cocloud-1.0.0",
        "git+https://bitbucket.org/equinoxfitness/datacoco3.utils.git@feature/python#egg=coutils-1.0.0",
        "git+https://bitbucket.org/equinoxfitness/datacoco3.db.git@DATPLAT-391/replace-pymssql-to-pytds#egg=codb-1.0.0"
    ]
)