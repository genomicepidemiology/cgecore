# Created by Alfred Ferrer Florensa
"""Contains objects to contain HIT"""

import os
import sys
from .translate_hits import BLAST_XML


class Hit(dict):

    def __init__(self, software=None, data=None, empty=False, file=None):

        self.software = software
        if isinstance(empty, bool):
            self.empty = empty
        else:
            raise TypeError("Empty variable has to be a boolean")
        self.file = file
        self._init_hit()

    def _init_hit(self):

        self["queryID"] = None
        self["templateID"] = None
        self["query_identity"] = None
        self["template_identity"] = None
        self["template_length"] = None
        self["template_start_aln"] = None
        self["template_end_aln"] = None
        self["query_aln"] = None	#Consensus sequence for KMA
        self["template_aln"] = None
        self["evalue"] = None
        self["aln_length"] = None
        self["query_coverage"] = None
        self["template_coverage"] = None




class BlastHit(Hit):

    def __init__(self, software="blast", data=None, empty=False, file=None):
        super().__init__(software=software, data=data, empty=empty, file=file)
        self._init_blasthit(file)
        self.file = file
        if data is not None:
            if isinstance(data, dict):
                self.incorporate_data(data)
            else:
                raise TypeError("Data must be in dict format")

    def _init_blasthit(self, file):
        self["query_start_aln"] = None
        self["query_end_aln"] = None
        self["bitscore"] = None
        self["raw_score"] = None
        # Calculate?
        self["n_identity"] = None   #IS this the same as template_consensusSUm
        self["mismatches"] = None   #Equal to snps?
        self["n_pos_matches"] = None
        self["pos_matches"] = None
        self["gapopen"] = None
        self["gaps"] = None
        self["frames"] = None
        self["query_frames"] = None
        self["template_frames"] = None
        self["btop"] = None
        self["template_taxids"] = None
        self["template_scie_name"] = None
        self["template_common_name"] = None
        self["template_blast_name"] = None
        self["template_superkingdom"] = None
        self["template_title"] = None
        self["all_template_title"] = None
        self["template_strand"] = None
        self["query_coverage_hsp"] = None
        self["db_number"] = None
        self["db_length"] = None
        self["hsp_length"] = None
        self["effective_space"] = None

        if file == "xml":
            self["kappa"] = None
            self["lambda"] = None
            self["effective_space"] = None
            self["entropy"] = None
            self["match_symbols"] = None
        elif file == "tsv":
            self["query_coverage_once"] = None
        else:
            raise ValueError("File where blast info has to be xml or tsv")

    def incorporate_data(self, data):

        for key, value in data.items():
            if self.file == "xml":
                if key in BLAST_XML:
                    self[BLAST_XML[key]] = value

            elif self.file == "tsv":
                if key in BLAST_TSV:
                    self[BLAST_TSV[key]] = value
            else:
                self[key] = value


class KMAHit(Hit):

    def __init__(self, software="kma", data=None, empty=False, file=None):
        super().__init__(software=software, data=data, empty=empty, file=file)
        self._init_kmahit()

    def _init_kmahit(self):
        self["conclave_score"] = None
        self["depth"] = None
        self["q_value"] = None
        self["p_value"] = None
        self["fragments"] = None
        self["reads_maped"] = None
        self["fragments_mapped"] = None
        self["mapScoreSum"] = None
        self["template_coveredPos"] = None
        self["template_consesusSum"] = None
        self["bpTotal"] = None  #Coverage?
        self["depth_variance"] = None
        self["nucHigh_depth_variance"] = None
        self["depth_max"] = None
        self["snps"] = None
        self["insertions"] = None
        self["deletions"] = None
        self["matrix"] = None
