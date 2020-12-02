# Created by Alfred Ferrer Florensa
"""Contains objects for reading alignment files"""

import gzip
import io
import pandas as pd
from Bio import SeqIO


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
