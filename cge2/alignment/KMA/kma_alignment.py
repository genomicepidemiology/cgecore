# Created by Alfred Ferrer Florensa
"""Contains objects for reading """

import os
import sys
import json
from cge2.alignment.file import _File
from cge2.alignment.KMA.alignment_files import Read_Alignment
from cge2.alignment.Hit import KMAHit


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

    ## Philip is annoying and did some SAM output that goes to stout :)

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
            "Frag_Raw":KMA_ResultFile("Frag_Raw", output_path,
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

    def read(self, json_dump=False):
        db_hits = {}
        meta_data = {}
        for res_file in self.list_files:
            file_output = res_file.read()
            for hit_template in file_output:
                if hit_template == res_file.name + "_Data":
                    meta_data[hit_template] = file_output[hit_template]
                else:
                    if res_file is self.list_files[0]:
                        db_hits[hit_template] = {}
                        db_hits[hit_template][res_file.name] = file_output[hit_template]
                    else:
                        db_hits[hit_template].update(
                            {res_file.name: file_output[hit_template]})
        if json_dump:
            KMA_alignment.dump_json(json_dump, db_hits)
        return iter(db_hits), meta_data

    @staticmethod
    def dump_json(path, dict_hits):
        for hit in dict_hits:
            for result_file in dict_hits[hit].keys():
                if result_file in ["Fragments", "VCF", "Matrix"]:
                    dict_hits[hit][result_file] = dict_hits[hit][result_file].to_dict("index")
        with open(path, 'w') as fp:
            json.dump(dict_hits, fp)
