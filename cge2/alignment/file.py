# Created by Alfred Ferrer Florensa
"""Contains objects for reading files"""

import os
import sys
import gzip
import signal
from cge2.utils import FormatFile


class FileError(Exception):
    """Raised when trying to read a file that do not exists"""

    def __init__(self, file_path):
        """Initialize."""
        self.file_path = file_path

    def __str__(self):
        """Format the error as a string"""
        str_error = "Non-zero return code when trying to read %d file, as  %s" % (self.file_path, self.returncode)
        return str_error

    def __repr__(self):
        """Represent error as a string"""
        return "FileError(%i, %s, %s, %s)" % (
            self.returncode,
            self.file_path
        )


class _File:
    """Generic interface for taking information from files"""

    def __init__(self, file_path, is_empty=None, compression=None):
        self.file_path = file_path
        self.is_empty = is_empty
        self.compression = compression

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


class _Parse_File(object):
    """A generator that iterates through a CC-CEDICT formatted file, returning
    a tuple of parsed results (Traditional, Simplified, Pinyin, English)"""

    def __init__(self, path, is_gzip=False):
        self.path = path
        if is_gzip:
            self.file = gzip.open(path, "rt")
        else:
            self.file = open(path, "r")
        signal.signal(signal.SIGINT, self.signal_term_handler)

    def signal_term_handler(self, signal, frame):
        """ Make sure to close handle if app closes prematurely """
        try:
            print("Closing CGEFile...")
            self.close()
        except ValueError:
            pass
        sys.exit()

    def opened_file(self):
        if self.file.closed:
            raise IOError("File is closed")

    def close(self):
        self.file.close()
        print("CGEFile closed!")


class ResultFile(_File):

    def __init__(
        self,
        name,
        output,
        read_method=None,
        extension="",
        compression=None,
    ):
        self.name = name
        if output is None:
            output = ""
        file_path = output + extension
        self.extension = extension
        self.read_method = read_method

        _File.__init__(self, file_path=file_path, compression=compression)

    def __str__(self):
        return self.file_path

    def __repr__(self):
        return "%s(file=%s, compression=%s, read_method=%s)" % (
                self.name.capitalize(), self.file_path, self.compression,
                self.read_method)

    def read(self, **kwargs):

        _File.define_file(self)
        if self.read_method is None:
            return None
        else:
            return self.read_method(self.file_path)

    def dump_json(self):
        pass
