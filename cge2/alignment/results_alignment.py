# Created by Alfred Ferrer Florensa
"""Contains objects to contain the results of an alignment"""

import os
import sys


class Hit_alignment(dict):

    def __init__(self, template, software, data):

        self.template_hit = template
        self.software = software
        self.data = {}

    def __dict__(self):

        return self.data

    def __str__(self):

        return self.template_hit
