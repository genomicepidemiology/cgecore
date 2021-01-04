# Created by Alfred Ferrer Florensa
"""Contains objects for reading """

import os
import sys
import gzip
import signal
import pandas as pd
from cge2.applications.file import _File
from cge2.applications.KMA.alignment_files import Read_Alignment
import cge2.applications.KMA.alignment_files as alignment_files


class KMA_alignment_old:

    def __init__(self, output_path, files):
        self.output_path = output_path

        self.KMA_FILES = {
            "Result": KMA_ResultFile("Result", output_path, extension=".res",
                                     read_method=Read_Alignment.read_resfile),
            "Fragments": KMA_ResultFile("Fragments", output_path,
                                        extension=".frag.gz",
                                        read_method=Read_Alignment.read_fragfile),
            "Consensus": KMA_ResultFile("Consensus", output_path,
                                        extension=".fsa",
                                        read_method=Read_Alignment.read_consfile),
            "Alignment": KMA_ResultFile("Alignment", output_path,
                                        extension=".aln",
                                        read_method=Read_Alignment.read_alnfile),
            "Matrix": KMA_ResultFile("Matrix", output_path,
                                     extension=".mat.gz",
                                     read_method=Read_Alignment.read_matrixfile),
            "Mapstat": KMA_ResultFile("Mapstat", output_path,
                                      extension=".mapstat",
                                      read_method=Read_Alignment.read_mapstatfile),
            "Frag_Raw": KMA_ResultFile("Frag_Raw", output_path,
                                       extension=".frag_raw.gz",
                                       read_method=Read_Alignment.read_rawfragfile),
            "VCF": KMA_ResultFile("VCF", output_path, extension=".vcf.gz",
                                  read_method=Read_Alignment.read_vcffile),
            "Sparse": KMA_ResultFile("Sparse", output_path, extension=".spa",
                                     read_method=Read_Alignment.read_spafile),
                            }
        if not isinstance(files, list):
            files = [files]
        self.list_files = []
        self._init_files(files)
        self.kma_readfiles = {}
        self.data_alignment = {"db_hits": {}, "data": {}}

    def _init_files(self, files):
        len_f = len(files)
        for n_f in range(len_f):
            self.__setitem__(n_f, files[n_f])

    def __len__(self):
        return(len(self.list_files))

    def _check_Sparse(self):
        if "Sparse" in self.list_files and self.__len__() > 1:
            raise IndexError("File 'Sparse' is a unique result file. It "
                             "cannot be read with other files")

    def __setitem__(self, index, value):
        if value in self.KMA_FILES:
            file_result = self.KMA_FILES[value]
        else:
            raise IndexError("Name file '%s' not part of the KMA "
                             "Alignment: %" % (value,
                                               ", ".join(self.KMA_FILES.keys())
                                               ))
        if index == self.__len__():
            self.list_files.append(file_result)
        elif index < self.__len__():
            self.list_files[index] = file_result
        else:
            raise IndexError("list assignment index out of range")
        self._check_Sparse()

    def __getitem__(self, index):
        return(self.list_files[index])

    def __str__(self):
        return self.output_path

    def __repr__(self):
        return "KMA_alignment(" + self.output_path + ")"


class KMA_ResultFile(_File):

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

    def read(self):

        _File.define_file(self)
        if self.read_method is None:
            return None
        else:
            return self.read_method(self.file_path)


class KMA_alignment:

    def __init__(self, output_path, files):
        self.output_path = output_path

        self.KMA_FILES = {
            "Result": KMA_ResultFile("Result", output_path, extension=".res",
                                     read_method=alignment_files.Iterator_ResFile),
            "Fragments": KMA_ResultFile("Fragments", output_path,
                                        extension=".frag.gz",
                                        read_method=alignment_files.Parse_FragFile),
            "Consensus": KMA_ResultFile("Consensus", output_path,
                                        extension=".fsa",
                                        read_method=alignment_files.Parse_ConsensusFile),
            "Alignment": KMA_ResultFile("Alignment", output_path,
                                        extension=".aln",
                                        read_method=alignment_files.Parse_AlignmentFile),
            "Matrix": KMA_ResultFile("Matrix", output_path,
                                     extension=".mat.gz",
                                     read_method=alignment_files.Parse_MatrixFile),
            "Mapstat": KMA_ResultFile("Mapstat", output_path,
                                      extension=".mapstat",
                                      read_method=alignment_files.Iterator_MapstatFile),
            "Frag_Raw": KMA_ResultFile("Frag_Raw", output_path,
                                       extension=".frag_raw.gz",
                                       read_method=alignment_files.Parse_FragFile),
            "VCF": KMA_ResultFile("VCF", output_path, extension=".vcf.gz",
                                  read_method=alignment_files.Parse_VCFFile),
            "Sparse": KMA_ResultFile("Sparse", output_path, extension=".spa",
                                     read_method=alignment_files.Parse_SPAFile),
                            }
        if not isinstance(files, list):
            files = [files]
        self.list_files = []
        self._init_files(files)

    def _init_files(self, files):
        len_f = len(files)
        for n_f in range(len_f):
            self.__setitem__(n_f, files[n_f])

    def __len__(self):
        return(len(self.list_files))

    def _check_Sparse(self):
        if "Sparse" in self.list_files and self.__len__() > 1:
            raise IndexError("File 'Sparse' is a unique result file. It "
                             "cannot be read with other files")

    def __setitem__(self, index, value):
        if value in self.KMA_FILES:
            file_result = self.KMA_FILES[value]
        else:
            raise IndexError("Name file '%s' not part of the KMA "
                             "Alignment: %" % (value,
                                               ", ".join(self.KMA_FILES.keys())
                                               ))
        if index == self.__len__():
            self.list_files.append(file_result)
        elif index < self.__len__():
            self.list_files[index] = file_result
        else:
            raise IndexError("list assignment index out of range")
        self._check_Sparse()

    def __getitem__(self, index):
        return(self.list_files[index])

    def __str__(self):
        str_lst = []
        for file in self.list_files:
            str_lst.append(str(file))
        return ", ".join(str_lst)

    def __repr__(self):
        repr_lst = []
        for file in self.list_files:
            repr_lst.append("%s=%s" % (file.name, file.file_path))

        return "KMA_alignment(" + ", ".join(repr_lst) + ")"


class Iterate_KMAFiles:

    def __init__(self, output_path, files):

        KMAfiles = KMA_alignment(output_path, files)
        self.files_kma = files
        self.iter_KMAFiles = {}
        for files in KMAfiles:
            self.iter_KMAFiles[files.name] = files.read()

    def __iter__(self):

        return self

    def __next__(self):
        iter_true = True
        gene_output = {}
        while iter_true:
            for kma_file in self.files_kma:
                gene_output[kma_file] = next(self.iter_KMAFiles[kma_file])
            iter_true = False
        return gene_output
