# Created by Alfred Ferrer Florensa
"""Contains objects for reading """

import os
import sys
import gzip
import signal
import pandas as pd
from cge2.alignment.file import _File, _ResultFile
from cge2.alignment.blast.alignment_files import Read_Alignment
import cge2.alignment.blast.alignment_files as alignment_files


class BLASTN_alignment:

    def __init__(self, output_path, files):
        self.output_path = output_path

        self.BLASTN_FILES = {
            "XML":
            _ResultFile("XML", output_path, extension=".xml",
                        read_method=alignment_files.Iterator_XMLFile),
            "TSV":
            _ResultFile("TSV", output_path, extension=".tsv",
                        read_method=alignment_files.Iterator_BlastSepFile),
            "CSV":
            _ResultFile("CSV", output_path, extension=".csv",
                        read_method=alignment_files.Iterator_BlastSepFile),
            "TSV_extra":
            _ResultFile("TSV_extra", output_path, extension=".tsv",
                        read_method=alignment_files.Iterator_BlastSepFile),

                            }
        if not isinstance(files, str):
            raise TypeError("The name of the file has to be a string")
        elif files not in self.BLASTN_FILES:
            raise KeyError("The name of the file has to be: XML, TSV, CSV or "
                           "TSV_extra.")

        self.file = self.BLASTN_FILES[file]

    def __str__(self):

        return str(file)

    def __repr__(self):

        repr_lst = "%s=%s" % (file.name, file.file_path)
        return "BLASTN_alignment(" + str(repr_lst) + ")"


class Iterator_KMAAlignment:

    def __init__(self, output_path, template_files, output_files):
        self.output_path = output_path
        self.beginnig = True
        self.output_files = output_files
        self.template_files = template_files
        self.aln_pos = 0
        self.iter_dataset = None

    def __iter__(self):

        return self

    def __next__(self):
        hit_template = None
        if self.iter_dataset is None:
            dataset_file = self.output_path + self.output_files[self.aln_pos]
            self.iter_dataset = Iterate_KMAFiles(output_path=dataset_file,
                                                 files=self.template_files)
        while hit_template is None:
            try:
                hit_template = next(self.iter_dataset)
            except StopIteration:
                self.aln_pos += 1
                dataset_file = (self.output_path
                                + self.output_files[self.aln_pos])
                self.iter_dataset = Iterate_KMAFiles(output_path=dataset_file,
                                                     files=self.template_files)

        return hit_template
