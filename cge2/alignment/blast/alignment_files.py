# Created by Alfred Ferrer Florensa
"""Contains objects for reading alignment files"""

import gzip
import io
import pandas as pd
import signal
import sys
from cge2.alignment.results_alignment import Feature_hit, Hit_Alignment
from cge2.alignment.Hit import Hit, BlastHit, KMAHit
from cge2.alignment.file import _Parse_File
from Bio.Blast.NCBIXML import parse as BioXMLParse


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
        if recordblast.alignments:
            record_alignments = recorddict.pop("alignments")
            description_alignments = recorddict.pop("descriptions")
            for n_aln in record_alignments:
                hsps_aln = n_aln.__dict__.pop("hsps")
                for hsp in hsps_aln:
                    data = {}
                    data.update(recorddict)
                    data.update(n_aln.__dict__)
                    data.update(hsp.__dict__)
                    hit = BlastHit(data=data, file="xml")
                    return hit
        else:
            data = recorddict
            hit = BlastHit(data=data, file="xml", empty=True)
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
        elif separator == "tab":
            self.separator = "\t"
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
                                       file="tsv")
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
                hit = BlastHit(file="tsv",
                               data=dict(zip(self.header, line_split)),
                               empty=False)
                entry_line = False
        return hit

if __name__ == '__main__':
    iter = Iterator_XMLFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino5.xml")
    for i in iter:
        if i.empty is False:
            print(i)
