#!/usr/bin/env python
import sys
import os

try:
    from setuptools import setup, find_packages
except ImportError:
    sys.exit(
        "We need the Python library setuptools to be installed. "
        "Try runnning: python -m ensurepip"
    )


with open("README.md", 'r') as f:
    long_description = f.read()

with open("cgecore2/__init__.py", 'r') as f:
    for l in f:
        if l.startswith('__version__'):
            version = l.split('=')[1].strip().strip('"')

setup(
    name='cgecore2',
    version=version,
    description='Center for Genomic Epidemiology Core Module',
    long_description=long_description,
    license="Apache License, Version 2.0",
    author='Center for Genomic Epidemiology',
    author_email='food-cgehelp@dtu.dk',
    url="https://bitbucket.org/genomicepidemiology/cge_core_module/src/2.0",
    packages=['cgecore2'],
)
