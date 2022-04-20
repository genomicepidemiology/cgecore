# Breaking changes!

We will update to version 2.0. It is completely different from the current version 1.5.7 and all external code using this and older
versions will break if attempting to use the 2.0 and above, unchanged.
To maintain legacy functionality, use version [1.5.7](https://bitbucket.org/genomicepidemiology/cge_core_module/commits/tag/1.5.7).

# cge_core_module

Core module for the Center for Genomic Epidemiology

This module contains classes and functions needed to run the service wrappers and pipeline scripts

The pypi project can be found here:
https://pypi.org/project/cgecore/

# How to update:
1. Make changes to the modules
2. Bump the version number accordingly in cgecore/__init__.py
3. Install package locally
4. Test the changes locally (for both python2 and python3)
5. Distribute to Pypi

# Install package locally
python2 setup.py install

python3 setup.py install

# Distribute to PyPi
python3 setup.py sdist bdist_wheel

twine upload dist/*

*deprecated:*
~~python setup.py sdist upload -r pypi~~
