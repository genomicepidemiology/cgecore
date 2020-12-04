# Created by Alfred Ferrer Florensa
"""Contains objects for reading """

import os
import sys
import gzip
import pandas as pd
from cge2.applications.file import _File
from cge2.applications.KMA.alignment_files import Read_Alignment


class KMA_ResultFile(_File):

    def __init__(
        self,
        name,
        output,
        read_method=None,
        extension="",
    ):
        self.name = name
        if output is None:
            output = ""
        file_path = output + extension
        self.extension = extension
        self.read_method = read_method
        self.file_path = file_path

        _File.__init__(self, file_path=file_path)

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


class Parse_File(object):
    """A generator that iterates through a CC-CEDICT formatted file, returning
    a tuple of parsed results (Traditional, Simplified, Pinyin, English)"""

    def __init__(self, path):
        self.path = path


class Parse_ResFile(Parse_File):
    """Create iterator for a .res file"""

    def __init__(self, path):
        self.header = None

        Parse_File.__init__(self, path)

    def __iter__(self):
        with open(self.path) as f:
            for line in f:
                if line.startswith("#"):
                    self.header = line.replace("#", "").rstrip().split("\t")
                else:
                    line_split = line.rstrip().split("\t")
                    if len(line_split) != len(self.header):
                        raise IndexError("Length of line is not equal to"
                                         " header")
                    entry = {self.header[i]: line_split[i]
                             for i in range(len(self.header))}
                    yield entry


class Parse_MatrixFile(Parse_File):
    """Create iterator for a .res file"""

    def __init__(self, path):

        Parse_File.__init__(self, path)

    def __iter__(self):
        gene_df = None
        gene_name = None
        gene_df = None
        with gzip.open(self.path, "rt", newline="\n") as f:
            for line in f:
                if line.startswith("#"):
                    if gene_df is not None:
                        dict_gene = {gene_name: gene_df}
                        yield dict_gene
                    gene_name = line.replace("#", "").rstrip()
                    gene_df = pd.DataFrame(columns=["Nucl", "A", "C", "G",
                                                    "T", "N", "-"])
                elif line in ['\n', '\r\n', '']:
                    continue
                else:
                    split_line = line.rstrip().split("\t")
                    row_series = pd.Series(data=split_line, index=["Nucl",
                                                                   "A", "C",
                                                                   "G", "T",
                                                                   "N", "-"])
                    gene_df = gene_df.append(row_series, ignore_index=True)
            dict_gene = {gene_name: gene_df}
            yield dict_gene


class Iterator_KMA:

    def __init__(self, file="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.res"):
        self.res_file = file

    def read_res(self, file_open):
        while True:
            data = file_open.readline()
            if not data:
                break
            yield data

    def files_iterate(self):

        with open(self.res_file, 'r') as res_open:
            res_data = self.read_res(res_open)
        yield res_data
