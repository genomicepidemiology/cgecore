# Created by Alfred Ferrer Florensa
"""Contains objects to contain HIT"""

import os
import sys
from .translate_hits import Translate_Hits


class Feature_Hit:

    def __init__(self, value=None, set=False):
        self.value = value
        self.set = set

    def __str__(self):
        return "%s" % self.value


class Hit(dict):

    def __init__(self, software=None, empty=False):

        self.software = software
        if isinstance(empty, bool):
            self.empty = empty
        else:
            raise TypeError("Empty variable has to be a boolean")
        self._init_hit()

    def __setitem__(self, i, y):
        if i in self:
            if self[i].set is True and self[i] != y:
                raise KeyError("The object Hit cannot change the value of %s "
                               "to %s because is already %s (%s)" % (
                                i, y, self[i], self[i].set))
            else:
                self._setparam(i, y)
        else:
            if isinstance(y, Feature_Hit):
                super(Hit, self).__setitem__(i, y)
            else:
                super(Hit, self).__setitem__(i,  Feature_Hit(value=y,
                                                             set=True))

    def _setdefault(self, key, value=None):
        self[key] = value

    def _setparam(self, key, value):
        self[key].value = value
        self[key].set = True

    def _init_hit(self):

        self._setdefault("queryID", Feature_Hit())
        self._setdefault("templateID", Feature_Hit())
        self._setdefault("query_identity", Feature_Hit())
        self._setdefault("template_identity", Feature_Hit())
        self._setdefault("template_length", Feature_Hit())
        self._setdefault("template_start_aln", Feature_Hit())
        self._setdefault("template_end_aln", Feature_Hit())
        self._setdefault("query_aln", Feature_Hit())	#Consensus sequence for KMA
        self._setdefault("template_aln", Feature_Hit())
        self._setdefault("evalue", Feature_Hit())
        self._setdefault("aln_length", Feature_Hit())
        self._setdefault("query_coverage", Feature_Hit())
        self._setdefault("template_coverage", Feature_Hit())


class BlastHit(Hit):

    def __init__(self, software="blast", data=None, empty=False,
                 file_type=None):
        super().__init__(software=software, empty=empty)
        if not isinstance(file_type, str):
            raise TypeError("File type has to be a string")
        self.extension = file_type
        self._init_blasthit(file_type)
        if data is not None:
            if isinstance(data, dict):
                self.incorporate_data(data)
            else:
                raise TypeError("Data must be in dict format")

    def __str__(self):
        if self["templateID"].value is not None:
            string_hit = "BLASTHit on %s (" % self["templateID"]
            for key, value in self.items():
                if value.set:
                    string_hit += "%s: %s, " % (key, value)
            string_hit = string_hit[:-2]
            string_hit += ")"
        elif self["queryID"].value is not None:
            string_hit = "No Hit by %s" % self["queryID"]
        else:
            string_hit = "No Hit"
        return string_hit

    def __repr__(self):
        repr_hit = "{"
        for key, value in self.items():
            repr_hit += "%s: %s, " % (key, value)
        repr_hit += "}"
        return repr_hit

    def incorporate_data(self, data):

        for key, value in data.items():
            self[key] = value

    def _init_blasthit(self, file):
        self._setdefault("query_start_aln", Feature_Hit())
        self._setdefault("query_end_aln", Feature_Hit())
        self._setdefault("bitscore", Feature_Hit())
        self._setdefault("raw_score", Feature_Hit())
        # Calculate?
        self._setdefault("n_identity", Feature_Hit())   # IS this the same as template_consensusSUm
        self._setdefault("mismatches", Feature_Hit())   #E qual to snps?
        self._setdefault("n_pos_matches", Feature_Hit())
        self._setdefault("pos_matches", Feature_Hit())
        self._setdefault("gapopen", Feature_Hit())
        self._setdefault("gaps", Feature_Hit())
        self._setdefault("frames", Feature_Hit())
        self._setdefault("query_frames", Feature_Hit())
        self._setdefault("template_frames", Feature_Hit())
        self._setdefault("btop", Feature_Hit())
        self._setdefault("template_taxids", Feature_Hit())
        self._setdefault("template_scie_name", Feature_Hit())
        self._setdefault("template_common_name", Feature_Hit())
        self._setdefault("template_blast_name", Feature_Hit())
        self._setdefault("template_superkingdom", Feature_Hit())
        self._setdefault("template_title", Feature_Hit())
        self._setdefault("all_template_title", Feature_Hit())
        self._setdefault("template_strand", Feature_Hit())
        self._setdefault("query_coverage_hsp", Feature_Hit())
        self._setdefault("db_number", Feature_Hit())
        self._setdefault("db_length", Feature_Hit())
        self._setdefault("hsp_length", Feature_Hit())
        self._setdefault("effective_space", Feature_Hit())

        if file == "xml":
            self._setdefault("kappa", Feature_Hit())
            self._setdefault("lambda", Feature_Hit())
            self._setdefault("effective_space", Feature_Hit())
            self._setdefault("entropy", Feature_Hit())
            self._setdefault("match_symbols", Feature_Hit())
        elif file == "tsv" or file == "csv":
            self._setdefault("query_coverage_once", Feature_Hit())
        else:
            raise TypeError("File with blast info has to be xml, csv or tsv."
                            " The file format provided is %." % file)


class KMAHit(Hit):

    def __init__(self, software="kma", data=None, empty=False, file_type=None):
        super().__init__(software=software, empty=empty)
        self.extension = file_type
        self._init_kmahit()

    def _init_kmahit(self):
        self._setdefault("conclave_score", Feature_Hit())
        self._setdefault("depth", Feature_Hit())
        self._setdefault("q_value", Feature_Hit())
        self._setdefault("p_value", Feature_Hit())
        self._setdefault("fragments", Feature_Hit())
        self._setdefault("reads_maped", Feature_Hit())
        self._setdefault("fragments_mapped", Feature_Hit())
        self._setdefault("mapScoreSum", Feature_Hit())
        self._setdefault("template_coveredPos", Feature_Hit())
        self._setdefault("template_consesusSum", Feature_Hit())
        self._setdefault("bpTotal", Feature_Hit())  # Coverage?
        self._setdefault("depth_variance", Feature_Hit())
        self._setdefault("nucHigh_depth_variance", Feature_Hit())
        self._setdefault("depth_max", Feature_Hit())
        self._setdefault("snps", Feature_Hit())
        self._setdefault("insertions", Feature_Hit())
        self._setdefault("deletions", Feature_Hit())
        self._setdefault("matrix", Feature_Hit())

    def _merge_files(self, hit):
        if isinstance(self.extension, str):
            self.extension = [self.extension]
        elif isinstance(self.extension, list):
            pass
        elif self.extension is None:
            self.extension = []
        else:
            raise TypeError(("The hits file that is being merged to is neither"
                            " a string or a list (%s)") % self.extension)

        if isinstance(hit.extension, str):
            if hit.extension in self.extension:
                raise ValueError(("The Hits information is coming from same "
                                 "files"))
            else:
                self.extension.append(hit.extension)
        elif isinstance(hit.extension, list):
            for hit_file in hit.extension:
                if hit_file in self.extension:
                    raise ValueError(("The Hits information is coming from "
                                      "same files"))
            self.extension.extend(hit.extension)
        elif hit.extension is None:
            if self.extension:
                self.extension = self.extension
            else:
                self.extension = None
        else:
            raise TypeError(("The hits file that is being merged is neither "
                            "a string or a list (%s)%s" % (hit.extension, hit))
                            )

    def __str__(self):
        if self["templateID"].value is not None:
            string_hit = "KMAHit on %s (" % self["templateID"]
            for key, value in self.items():
                if value.set:
                    string_hit += "%s: %s, " % (key, value)
            string_hit = string_hit[:-2]
            string_hit += ")"
        elif self["queryID"].value is not None:
            string_hit = "No Hit by %s" % self["queryID"]
        else:
            string_hit = "No Hit"
        return string_hit

    def __repr__(self):
        if self["templateID"] is not None:
            string_hit = "KMAHit on %s (" % self["templateID"]
            for key, value in self.items():
                string_hit += "%s: %s, " % (key, value)
            string_hit = string_hit[:-1]
            string_hit += ")"
        else:
            string_hit = "No hit"
        return string_hit

    def merge(self, hit):

        self._merge_files(hit)

        for key, values in hit.items():
            if values.set:
                self._setparam(key, values)
            else:
                pass
