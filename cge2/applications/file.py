# Created by Alfred Ferrer Florensa
"""Contains objects for reading files"""

import os
import sys
import subprocess
from cge2.utils import FormatFile


class FileError(Exception):
    """Raised when trying to read a file that do not exists"""

    def __init__(self, file_path):
        """Initialize."""
        self.file_path = file_path

    def __str__(self):
        """Format the error as a string"""
        str_error = "Non-zero return code when trying to read %d file, as %s" % (self.file_path, self.returncode)
        return str_error

    def __repr__(self):
        """Represent error as a string"""
        return "FileError(%i, %s, %s, %s)" % (
            self.returncode,
            self.file_path
        )


class _File:
    """Generic interface for taking information from files"""

    def __init__(self, file_path):
        self.file_path = file_path
        self.is_empty = None
        self.compression = None

    def define_file(self):

        if not os.path.isfile(self.file_path):
            raise OSError("File %s does not exists" % (self.file_path))

        self.compression = FormatFile.is_gzipped(self.file_path)

        if not os.access(self.file_path, os.R_OK):
            raise OSError("File's %s permissions do not allow to read it")

    def __str__(self):
        """TODO: Truncated files"""
        self.define_file()

        return self.file_path

    def __repr__(self):
        """Represent file as a string"""
        self.define_file()
        return "File(file=%s, compression=%s)" % (self.file_path,
                                                  self.compression)
