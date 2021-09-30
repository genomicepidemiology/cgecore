# Created by Alfred Ferrer Florensa
"""Contains objects for reading alignment files"""

import gzip
import io
import pandas as pd
import signal
import sys
from cge2.alignment.Hit import Hit, BlastHit, KMAHit
from cge2.alignment.file import _Parse_File
from Bio.Blast.NCBIXML import parse as BioXMLParse
from cge2.alignment.translate_hits import Translate_Hits


class Iterator_XMLFile(_Parse_File):

    def __init__(self, path):

        _Parse_File.__init__(self, path)
        self.iterator_XML = BioXMLParse(self.file)

    def __iter__(self):

        return self

    def __next__(self):
        _Parse_File.opened_file(self)
        recordblast = next(self.iterator_XML)
        recorddict = recordblast.__dict__
        queryID = recorddict["query"]
        if recordblast.alignments:
            record_alignments = recorddict.pop("alignments")
            description_alignments = recorddict.pop("descriptions")
            for n_aln in record_alignments:
                hsps_aln = n_aln.__dict__.pop("hsps")
                for hsp in hsps_aln:
                    hit = BlastHit(file_type="xml")
                    hit = Iterator_XMLFile.assign_BlastHit(hit, queryID,
                                                           n_aln.__dict__,
                                                           hsp.__dict__)
                    return hit
        else:
            hit = BlastHit(file_type="xml", empty=True)
            hit = Iterator_XMLFile.assign_BlastHit(hit, queryID)
            return hit

    @staticmethod
    def assign_BlastHit(hit, queryid, aln_info=None, hsp_info=None):
        hit["queryID"] = queryid
        if not hit.empty:
            hit["templateID"] = aln_info["hit_id"]
            for key, value in hsp_info.items():
                key = Translate_Hits.translate_keys(key,
                                                    Translate_Hits.BLAST_XML_HSP)
                hit[key] = value
        return hit


class Iterator_BlastSepFile(_Parse_File):

    def __init__(self, path, separator, comment_lines=False,
                 header=["qseqid", "sseqid", "pident", "length", "mismatch",
                         "gapopen", "qstart", "qend", "sstart", "send",
                         "evalue", "bitscore"]):
        self.header = header
        self.software = "blastn"
        if separator == "comma":
            self.separator = ","
            self.file_type = "csv"
        elif separator == "tab":
            self.separator = "\t"
            self.file_type = "tsv"
        else:
            raise ValueError("The separator of the blast results file has to "
                             "be 'comma' or 'tab'.")

        if separator == "comma" and comment_lines:
            raise TypeError("The option of comment_lines is only available "
                            "for tab separated files")
        self.comment_lines = comment_lines

        _Parse_File.__init__(self, path)

    def __repr__(self):

        return "Iterator_TabFile(%s)" % self.path

    def __str__(self):

        return self.path

    def __iter__(self):

        return self

    def __next__(self):
        entry_line = True
        _Parse_File.opened_file(self)
        while entry_line:
            line = self.file.readline()
            if line == "":
                entry = None
                _Parse_File.close(self)
                raise StopIteration("The iterator has arrived to the end of "
                                    "the file")
            elif self.comment_lines and line.startswith("#"):
                line_split = line.rstrip().split(" ")
                if line_split[1] == "Query:":
                    query_entry = line_split[-1]
                elif line_split[-1] == "found":
                    if line_split[1] == "0":
                        entry = {"qseqid": query_entry}
                        hit = BlastHit(data=entry,
                                       empty=True,
                                       file_type=self.file_type)
                        hit = Iterator_BlastSepFile.assign_BlastHit(hit, entry)
                        return hit

            else:
                line_split = line.rstrip().replace(" ",
                                                   "").split(self.separator)
                if len(line_split) != len(self.header):
                    raise IndexError("Length of line (%s)is not equal to"
                                     " header (%s). Check if you have chosen "
                                     "the right separator." % (len(line_split),
                                                               len(self.header)
                                                               ))
                hit = BlastHit(file_type=self.file_type, empty=False)
                hit = Iterator_BlastSepFile.assign_BlastHit(hit, line_split,
                                                            header=self.header)
                entry_line = False
        return hit

    @staticmethod
    def assign_BlastHit(hit, data, header=None):
        if isinstance(data, dict):
            for key, value in data.items():
                key = Translate_Hits.translate_keys(key,
                                                    Translate_Hits.BLAST_TSV)
                hit[key] = value
        elif isinstance(data, list):
            if len(data) != len(header):
                raise IndexError("Length of line (%s)is not equal to"
                                 " header (%s). Check if you have chosen "
                                 "the right separator." % (len(data),
                                                           len(header)
                                                           ))
            for n_feat in range(len(data)):
                value = data[n_feat]
                key = Translate_Hits.translate_keys(header[n_feat],
                                                    Translate_Hits.BLAST_TSV)
                hit[key] = value
        else:
            raise TypeError("Data has to be list or dictionary")

        return hit
