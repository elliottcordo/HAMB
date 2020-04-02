#!/usr/bin/env python

"""
setuptools install script.
"""
import os
import re
from setuptools import setup, find_packages

requires = [
    "datacoco-core==0.1.1",
    "datacoco-cloud==0.1.9",
    "datacoco-db==0.1.7",
    "datacoco-email-tools==0.1.3",
    "datacoco-ftp-tools==0.1.3",
    "datacoco-secretsmanager==0.1.4",
    "pyyaml==5.1",
    "slackclient==1.3.0",
    "redis==2.10.6",
    "json2html==1.0.0",
    "pytest==4.0.1",
]

def get_version():
    version_file = open(os.path.join("hamb", "__version__.py"))
    version_contents = version_file.read()
    return re.search('__version__ = "(.*?)"', version_contents).group(1)

setup(
    name="hamb",
    version=get_version(),
    author="Equinox Fitness",
    description="",
    long_description=open("README.rst").read(),
    url="https://github.com/equinoxfitness/HAMB",
    license="TBD",
    packages=find_packages(exclude=["tests*"]),
    install_requires=requires,
    scripts=['bin/hamb'],
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
)
