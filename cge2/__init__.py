#!/usr/bin/env python
"""
The CGE functions module
"""
from .applications import command
from .applications.KMA import kma_application


#####################
__version__ = "2.0.0"
__all__ = [
    "application"]

# Initiate Shared Objects
# debug = Debug()
# proglist = programlist_obj()
