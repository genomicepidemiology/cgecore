# Created by Alfred Ferrer Florensa
"""Contains objects for reading alignment files"""

import gzip
import io
import pandas as pd
from Bio import SeqIO
import signal
import sys


class Read_Alignment:

    @staticmethod
    def read_resfile(file_path):
        """Conjunction of functions that read the results (*.res) file"""
        res_dataframe = pd.read_csv(file_path, sep="\t", skip_blank_lines=True)
        res_df = res_dataframe.rename(columns={'#Template': 'Template'})
        res_df.set_index("Template", drop=False, inplace=True,
                         verify_integrity=True)
        return res_df.to_dict("index")

    @staticmethod
    def read_fragfile(file_path):
        """Conjunction of functions that read the results (*.frag.gz) file"""

        fragment_dict = {}
        try:
            frag_dataframe = pd.read_csv(file_path, sep="\t", compression="gzip",
                                         skip_blank_lines=True, na_filter=True)
        except pd.errors.EmptyDataError:
            return fragment_dict

        frag_dataframe.dropna(how="all", inplace=True)
        if len(frag_dataframe.columns) == 9:
            frag_dataframe.columns = ["query_seq", "eq_mapped", "aln_score",
                                      "start_aln", "end_aln", "template",
                                      "query_name", "cut1", "cut2"]
        elif len(frag_dataframe.columns) == 7:
            frag_dataframe.columns = ["query_seq", "eq_mapped", "aln_score",
                                      "start_aln", "end_aln", "template",
                                      "query_name"]
        else:
            raise KeyError("Fragments file %s has not 7 or 9 columns" % file_path)
        for template, data in frag_dataframe.groupby("template", as_index=False):
            fragment_dict[template] = data.reset_index(drop=True)
        return fragment_dict

    @staticmethod
    def read_consfile(file_path):
        """Conjunction of functions that read the results (*.fsa) file"""
        consensus_dict = {}
        consensus_file = SeqIO.to_dict(SeqIO.parse(file_path, "fasta"))
        for cons_seq in consensus_file:
            consensus_dict[cons_seq] = str(consensus_file[cons_seq].seq)
        return(consensus_dict)

    @staticmethod
    def read_alnfile(file_path):
        """Conjunction of functions that read the results (*.aln) file"""
        alignment_dict = {}
        with open(file_path, "r") as file_open:
            previous_line = None
            entry_hit = None
            for line in file_open:
                if line.startswith("#") and previous_line is None:
                    if entry_hit is not None:
                        alignment_dict[entry_hit]["template_seq"] = "".join(alignment_dict[entry_hit]["template_seq"])
                        alignment_dict[entry_hit]["alignment_seq"] = "".join(alignment_dict[entry_hit]["alignment_seq"])
                        alignment_dict[entry_hit]["query_seq"] = "".join(alignment_dict[entry_hit]["query_seq"])
                    entry_hit = line.replace("# ", "").rstrip()
                    alignment_dict[entry_hit] = {"template_seq": [],
                                                 "alignment_seq": [],
                                                 "query_seq": []}
                    previous_line = "Header"
                elif line.startswith("template:"):
                    temp_seq = str(line.split("\t")[-1].rstrip())
                    alignment_dict[entry_hit]["template_seq"].append(temp_seq)
                    previous_line = "Template"
                elif previous_line == "Template":
                    aln_seq = str(line.split("\t")[-1].rstrip())
                    alignment_dict[entry_hit]["alignment_seq"].append(aln_seq)
                    previous_line = "Alignment"
                elif line.startswith("query:"):
                    query_seq = str(line.split("\t")[-1].rstrip())
                    alignment_dict[entry_hit]["query_seq"].append(query_seq)
                    previous_line = "query"
                else:
                    previous_line = None
        if entry_hit in alignment_dict:
            alignment_dict[entry_hit]["template_seq"] = "".join(alignment_dict[entry_hit]["template_seq"])
            alignment_dict[entry_hit]["alignment_seq"] = "".join(alignment_dict[entry_hit]["alignment_seq"])
            alignment_dict[entry_hit]["query_seq"] = "".join(alignment_dict[entry_hit]["query_seq"])
        else:
            pass

        return alignment_dict

    @staticmethod
    def read_matrixfile(file_path):
        matrix_dict = {}
        with gzip.open(file_path, "rt", newline="\n") as gzipfile:
            for line in gzipfile:
                line = line.rstrip()
                if line.startswith("#"):
                    gene_name = line.replace("#", "")
                    matrix_dict[gene_name] = pd.DataFrame(columns=["Nucl",
                                                                   "A", "C",
                                                                   "G", "T",
                                                                   "N", "-"])
                elif line in ['\n', '\r\n', '']:
                    continue
                else:
                    split_line = line.split("\t")
                    row_series = pd.Series(data=split_line, index=["Nucl",
                                                                   "A", "C",
                                                                   "G", "T",
                                                                   "N", "-"])
                    matrix_dict[gene_name] = matrix_dict[gene_name].append(
                                                            row_series,
                                                            ignore_index=True)
        dict_result = {}
        for i in matrix_dict:
            dict_result[i] = matrix_dict[i].to_dict("index")
        return matrix_dict

    @staticmethod
    def read_mapstatfile(file_path):
        map_file = open(file_path, "r")
        line_n = 0
        data = {}
        for line in map_file:
            if line.startswith("##"):
                data[line.rstrip().split("\t")[0].split(" ")[-1]] = line.rstrip().split("\t")[-1]
                line_n += 1
            else:
                break
        mapstat_dict = {}
        mapstat_dict["Mapstat_Data"] = data
        mapstat_dataframe = pd.read_csv(file_path, sep="\t",
                                        skiprows=range(line_n),
                                        skip_blank_lines=True)
        mapstat_df = mapstat_dataframe.rename(columns={'# refSequence':
                                                       'refSequence'})
        mapstat_df.set_index("refSequence", drop=False, inplace=True,
                             verify_integrity=True)
        mapstat_dict.update(mapstat_df.to_dict("index"))
        return mapstat_dict

    @staticmethod
    def read_rawfragfile(file_path):
        pass

    @staticmethod
    def read_vcffile(file_path):
        vcf_dataframe = {}
        with gzip.open(file_path, 'rt') as f:
            lines = [l for l in f if not l.startswith('##')]
        vcf_df = pd.read_csv(io.StringIO(''.join(lines)),
                             dtype={'#CHROM': str, 'POS': int, 'ID': str,
                                    'REF': str, 'ALT': str,
                                    'QUAL': str, 'FILTER': str, 'INFO': str},
                             sep='\t', skip_blank_lines=True
                             ).rename(columns={'#CHROM': 'CHROM'})
        for template, data in vcf_df.groupby("CHROM", as_index=False):
            vcf_dataframe[template] = data.reset_index(drop=True)
        return vcf_dataframe

    @staticmethod
    def read_spafile(file_path):
        spa_df = pd.read_csv(file_path, sep="\t", skip_blank_lines=True)
        spa_df = spa_df.rename(columns={'#Template': 'Template'})
        spa_df.set_index("Template", drop=False, inplace=True,
                         verify_integrity=True)
        return spa_df.to_dict("index")

class Parse_File(object):
    """A generator that iterates through a CC-CEDICT formatted file, returning
    a tuple of parsed results (Traditional, Simplified, Pinyin, English)"""

    def __init__(self, path, gzip=False):
        self.path = path
        if gzip:
            self.file = gzip.open(path, "rt", newline="\n")
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


class Iterator_ResFile(Parse_File):
    """Create iterator for a .res file"""

    def __init__(self, path):
        self.header = None

        Parse_File.__init__(self, path)

    def __repr__(self):

        return "Iterator_ResFile(%s)" % self.path

    def __str__(self):

        return self.path

    def __iter__(self):

        return self

    def __next__(self):
        entry_line = True
        Parse_File.opened_file(self)
        while entry_line:
            line = self.file.readline()
            if line == "":
                entry = None
                Parse_File.close(self)
                raise StopIteration("The iterator has arrived to the end of "
                                    "the file")
            elif line.startswith("#"):
                self.header = line.replace("#",
                                           "").rstrip().replace(" ",
                                                                "").split("\t")
            else:
                line_split = line.rstrip().replace(" ", "").split("\t")
                if len(line_split) != len(self.header):
                    raise IndexError("Length of line is not equal to"
                                     " header")
                entry = {}
                for i in range(len(self.header)):
                    try:
                        value_entry = float(line_split[i])
                    except ValueError:
                        value_entry = line_split[i]
                    entry[self.header[i]] = value_entry
                entry_line = False
        return entry


class Iterator_MapstatFile(Parse_File):

    def __init__(self, path):
        self.header = None

        Parse_File.__init__(self, path)

    def get_info(self):
        info = {}
        if not self.file.closed:
            file_open = open(self.path, 'r')
        else:
            file_open = self.file
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

        return self

    def __next__(self):
        entry_line = True
        Parse_File.opened_file(self)
        while entry_line:
            line = self.file.readline()
            if line == "":
                entry = None
                Parse_File.close(self)
                raise StopIteration("The iterator has arrived to the end of "
                                    "the file")
            elif line.startswith("## "):
                pass
            elif line.startswith("#"):
                self.header = line.replace("#",
                                           "").rstrip().replace(" ",
                                                                "").split("\t")
            else:
                line_split = line.rstrip().replace(" ", "").split("\t")
                if len(line_split) != len(self.header):
                    raise IndexError("Length of line is not equal to"
                                     " header")
                entry = {}
                for i in range(len(self.header)):
                    try:
                        value_entry = float(line_split[i])
                    except ValueError:
                        value_entry = line_split[i]
                    entry[self.header[i]] = value_entry
                entry_line = False
        return entry


class Parse_ResFile(Parse_File):
    """Create generator for a .res file"""

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
