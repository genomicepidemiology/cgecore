# Created by Alfred Ferrer Florensa
"""Contains objects to contain the results of an alignment"""

import os
import sys


class Hits:

    def __init__(self):
        self.hits_db = []

    def __iter__(self):
        return self.hits_db

    def __next__(self):
        pass
