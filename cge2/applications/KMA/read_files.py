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
                    yield {entry["Template"]: entry}


class Parse_MatrixFile(Parse_File):
    """Create iterator for a .mat file"""

    def __init__(self, path):

        Parse_File.__init__(self, path)

    def __iter__(self):
        template_df = None
        template_name = None
        with gzip.open(self.path, "rt", newline="\n") as f:
            for line in f:
                if line.startswith("#"):
                    if template_df is not None:
                        dict_template = {template_name: template_df}
                        yield dict_template
                    template_name = line.replace("#", "").rstrip()
                    template_df = pd.DataFrame(columns=["Nucl", "A", "C", "G",
                                                        "T", "N", "-"])
                elif line in ['\n', '\r\n', '']:
                    continue
                else:
                    split_line = line.rstrip().split("\t")
                    row_series = pd.Series(data=split_line, index=["Nucl",
                                                                   "A", "C",
                                                                   "G", "T",
                                                                   "N", "-"])
                    template_df = template_df.append(row_series,
                                                     ignore_index=True)
            dict_template = {template_name: template_df}
            yield dict_template


class Parse_AlignmentFile(Parse_File):
    """Create iterator for .aln file"""

    def __init__(self, path):
        Parse_File.__init__(self, path)

    def __iter__(self):
        with open(self.path, "r") as file_open:
            previous_line = None
            entry_hit = None
            alignment_entry = {}
            for line in file_open:
                if line.startswith("#") and previous_line is None:
                    if entry_hit is not None:
                        alignment_entry["template_seq"] = "".join(alignment_entry["template_seq"])
                        alignment_entry["alignment_seq"] = "".join(alignment_entry["alignment_seq"])
                        alignment_entry["query_seq"] = "".join(alignment_entry["query_seq"])
                        yield {entry_hit: alignment_entry}
                    entry_hit = line.replace("# ", "").rstrip()
                    alignment_entry = {"template_seq": [],
                                       "alignment_seq": [],
                                       "query_seq": []}
                    previous_line = "Header"
                elif line.startswith("template:"):
                    temp_seq = str(line.split("\t")[-1].rstrip())
                    alignment_entry["template_seq"].append(temp_seq)
                    previous_line = "Template"
                elif previous_line == "Template":
                    aln_seq = str(line.split("\t")[-1].rstrip())
                    alignment_entry["alignment_seq"].append(aln_seq)
                    previous_line = "Alignment"
                elif line.startswith("query:"):
                    query_seq = str(line.split("\t")[-1].rstrip())
                    alignment_entry["query_seq"].append(query_seq)
                    previous_line = "query"
                else:
                    previous_line = None
            if entry_hit is not None:
                alignment_entry["template_seq"] = "".join(alignment_entry["template_seq"])
                alignment_entry["alignment_seq"] = "".join(alignment_entry["alignment_seq"])
                alignment_entry["query_seq"] = "".join(alignment_entry["query_seq"])
                yield {entry_hit: alignment_entry}
            else:
                yield {}


class Parse_ConsensusFile(Parse_File):
    """Create iterator for .fsa file"""

    def __init__(self, path):

        Parse_File.__init__(self, path)

    def __iter__(self):
        with open(self.path, "r") as file_open:
            template_name = None
            template_seq = []
            for line in file_open:
                if line.startswith("#"):
                    if template_name is not None:
                        template_str = "".join(template_seq)
                        yield {template_name: template_str}
                    template_name = line.replace("#", "").rstrip()
                    template_seq = []
                else:
                    template_seq.append(line.rstrip())
            if template_name is not None:
                template_str = "".join(template_seq)
                yield {template_name: template_str}
            else:
                yield {}


class Parse_VCFFile(Parse_File):
    """Create iterator for .vcf file"""

    def __init__(self, path):

        Parse_File.__init__(self, path)

    def get_info(self):
        info = {}
        with gzip.open(self.path, 'rt') as file_open:
            for line in file_open:
                if line.startswith("##"):
                    line_split = line.replace("##", "").rstrip().split("=")
                    if len(line_split) == 2:
                        info[line_split[0]] = line_split[1]
                    else:
                        if line_split[0] not in info:
                            info[line_split[0]] = {}
                        new_value = []
                        for i in range(len(line_split[1:])-1):
                            new_element = line_split[1:][i].replace('<', '').split(",")
                            new_value.extend(new_element)
                        new_value.append(line_split[-1].replace('>', ''))
                        dict_value = dict(zip(new_value[::2], new_value[1::2]))
                        info[line_split[0]].update({dict_value["ID"]:
                                                    dict_value})
                else:
                    break
        return info

    def __iter__(self):
        with gzip.open(self.path, 'rt') as file_open:
            template_name = None
            template_df = pd.DataFrame()
            for line in file_open:
                if line.startswith("##"):
                    pass
                elif line.startswith("#"):
                    header = line.replace("#", "").rstrip().split("\t")
                else:
                    line_vcf = line.rstrip().split("\t")
                    if template_name == line_vcf[0]:
                        template_df = template_df.append(
                                        pd.Series(data=line_vcf, index=header),
                                        ignore_index=True)
                    else:
                        if template_name is not None:
                            yield {template_name: template_df}
                        template_name = line_vcf[0]
                        template_df = pd.DataFrame([line_vcf], columns=header)
        yield {template_name: template_df}


class Parse_SPAFile(Parse_File):

    def __init__(self, path):

        Parse_File.__init__(self, path)

    def __iter__(self):
        with open(self.path, 'r') as file_open:
            for line in file_open:
                if line.startswith("#"):
                    header = line.replace("#", "").rstrip().split("\t")
                else:
                    line_split = line.rstrip().split("\t")
                    entry = {header[i]: line_split[i]
                             for i in range(len(header))}
                    yield {entry["Template"]: entry}


class Parse_MapstatFile(Parse_File):

    def __init__(self, path):

        Parse_File.__init__(self, path)

    def get_info(self):
        info = {}
        with open(self.path, 'r') as file_open:
            for line in file_open:
                if line.startswith("##"):
                    split_line = line.replace("## ", "").rstrip().split("\t")
                    if len(split_line) != 2:
                        raise TypeError("The information line of Mapstat does"
                                        " not follow the normal format (%)" %
                                        (line))
                    info[split_line[0]] = split_line[1]
                else:
                    break
        return info

    def __iter__(self):
        with open(self.path, 'r') as file_open:
            for line in file_open:
                if line.startswith("# "):
                    header = line.replace("# ", "").rstrip().split("\t")
                elif line.startswith("## "):
                    pass
                else:
                    line_split = line.rstrip().split("\t")
                    entry = {header[i]: line_split[i]
                             for i in range(len(header))}
                    yield {entry["refSequence"]: entry}


class Parse_FragFile(Parse_File):

    def __init__(self, path):

        Parse_File.__init__(self, path)

    def __iter__(self):
        template_df = pd.DataFrame()
        template_name = None
        header = None
        with gzip.open(self.path, 'rt') as file_open:
            for line in file_open:
                line_frag = line.rstrip().split("\t")
                if line_frag[5] == template_name:
                    template_df = template_df.append(pd.Series(data=line_frag,
                                                               index=header),
                                                     ignore_index=True)
                else:
                    if template_name is not None:
                        yield {template_name: template_df}
                    if len(line_frag) == 7:
                        header = ["query_seq", "eq_mapped", "aln_score",
                                  "start_aln", "end_aln", "template",
                                  "query_name"]
                    elif len(line_frag) == 9:
                        header = ["query_seq", "eq_mapped", "aln_score",
                                  "start_aln", "end_aln", "template",
                                  "query_name", "cut1", "cut2"]
                    else:
                        raise KeyError("Fragment file is does has not 7 or 9 "
                                       "columns")
                    template_name = line_frag[5]
                    template_df = pd.DataFrame([line_frag], columns=header)
        yield {template_name: template_df}


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
