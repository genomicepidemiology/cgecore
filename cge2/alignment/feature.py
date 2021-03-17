# Created by Alfred Ferrer Florensa
"""Contains objects for Features of Hit"""

import os
import sys
import subprocess


class _DictionaryFeaturesBase(dict):

    def __init__(self, results_format, **kwargs):

        self.results_format = results_format

class _BlastFeatures(_DictionaryFeaturesBase):

    def __init__(self, results_format=None, **kwargs):
        blast_features = [

        ]


class DictionarFeatures(_DictionaryFeaturesBase):

    def __init__(self, results_format=None, **kwargs):
        initial_features = [
            _Feature(
                names=["queryID", "Query Sequence ID"],
                description="",
                key_aligners={"blast_tab": "qseqid",
                              "blast_xml": "Iteration_query-def",
                              "kma": "Template"}
            ),
            _Feature(
                names=["queryXMLID", "Query Sequence XML ID"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Iteration_query-ID"}
            ),
            _Feature(
                names=["query_length", "Query Sequence Length"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Iteration_query-len"}
            ),
            _Feature(
                names=["query_GI", "Query GI"],
                description="",
                key_aligners={"blast_tab": "qgi",
                              "blast_xml": None}
            ),
            _Feature(
                names=["query_accession", "Query Accession"],
                description="",
                key_aligners={"blast_tab": "qacc",
                              "blast_xml": None}
            ),
            _Feature(
                names=["templateID", "Template SeqID"],
                description="",
                key_aligners={"blast_tab": "sseqid",
                              "blast_xml": "Hit_id"}
            ),
            _Feature(
                names=["template_def", "Template Definition"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Hit-def"}
            ),
            _Feature(
                names=["all_templateID", "All Template SeqID"],
                description="",
                key_aligners={"blast_tab": "sallseqid",
                              "blast_xml": None}
            ),
            _Feature(
                names=["template_GI", "Template GI"],
                description="",
                key_aligners={"blast_tab": "sgi",
                              "blast_xml": None}
            ),
            _Feature(
                names=["all_template_GI", "All Template GI"],
                description="",
                key_aligners={"blast_tab": "sallgi",
                              "blast_xml": None}
            ),
            _Feature(
                names=["template_accession", "Template Accession"],
                description="",
                key_aligners={"blast_tab": "sacc",
                              "blast_xml": "Hit_accession"}
            ),
            _Feature(
                names=["template_length", "Template Length"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Hit_len",
                              "kma": "Template_length"}
            ),
            _Feature(
                names=["all_template_accession", "All Template Accession"],
                description="",
                key_aligners={"blast_tab": "sallacc",
                              "blast_xml": None}
            ),
            _Feature(
                names=["query_saln", "Query Start Align"],
                description="",
                key_aligners={"blast_tab": "qstart",
                              "blast_xml": "Hsp_query-from"}
            ),
            _Feature(
                names=["query_ealn", "Query End Align"],
                description="",
                key_aligners={"blast_tab": "qend",
                              "blast_xml": "Hsp_query-to"}
            ),
            _Feature(
                names=["template_saln", "Template Start Align"],
                description="",
                key_aligners={"blast_tab": "sstart",
                              "blast_xml": "Hsp_hit-from"}
            ),
            _Feature(
                names=["template_ealn", "Template End Align"],
                description="",
                key_aligners={"blast_tab": "send",
                              "blast_xml": "Hsp_hit-to"}
            ),
            _Feature(
                names=["query_aln", "Query Align Seq"],
                description="",
                key_aligners={"blast_tab": "qseq",
                              "blast_xml": "Hsp_qseq"}
            ),
            _Feature(
                names=["template_aln", "Template Align Seq"],
                description="",
                key_aligners={"blast_tab": "sseq",
                              "blast_xml": "Hsp_hseq"}
            ),
            _Feature(
                names=["evalue", "Evalue"],
                description="",
                key_aligners={"blast_tab": "evalue",
                              "blast_xml": "Hsp_evalue"}
            ),
            _Feature(
                names=["bitscore", "Bitscore"],
                description="",
                key_aligners={"blast_tab": "bitscore",
                              "blast_xml": "Hsp_bit-score"}
            ),
            _Feature(
                names=["raw_score", "Raw Score"],
                description="",
                key_aligners={"blast_tab": "score",
                              "blast_xml": "Hsp_score"}
            ),
            _Feature(
                names=["conclave_score", "Conclave Score"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": None,
                              "kma": "Score"}
            ),
            _Feature(
                names=["expected_score", "Expected Score"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": None,
                              "kma": "Expected"}
            ),
            _Feature(
                names=["aln_length", "Alignment Length"],
                description="",
                key_aligners={"blast_tab": "length",
                              "blast_xml": "Aln_len"}
            ),
            _Feature(
                names=["identity", "Identity Percentage"],
                description="",
                key_aligners={"blast_tab": "pident",
                              "blast_xml": None,
                              }
            ),
            _Feature(
                names=["n_identity", "Identity Number"],
                description="",
                key_aligners={"blast_tab": "nident",
                              "blast_xml": "Hsp_identity"}
            ),
            _Feature(
                names=["mismatches", "Mismatches Number"],
                description="",
                key_aligners={"blast_tab": "mismatch",
                              "blast_xml": None}
            ),
            _Feature(
                names=["n_pos_matches", "Positive Matches Number"],
                description="",
                key_aligners={"blast_tab": "positive",
                              "blast_xml": "Hsp_positive"}
            ),
            _Feature(
                names=["pos_matches", "Positive Matches Percentage"],
                description="",
                key_aligners={"blast_tab": "ppos",
                              "blast_xml": None}
            ),
            _Feature(
                names=["gapopen", "Gap Openings"],
                description="",
                key_aligners={"blast_tab": "gapopen",
                              "blast_xml": None}
            ),
            _Feature(
                names=["gaps", "Gaps"],
                description="",
                key_aligners={"blast_tab": "gaps",
                              "blast_xml": "Hsp_gaps"}
            ),
            _Feature(
                names=["frames", "Frames"],
                description="",
                key_aligners={"blast_tab": "frames",
                              "blast_xml": None}
            ),
            _Feature(
                names=["query_frames", "Query Frames"],
                description="",
                key_aligners={"blast_tab": "qframe",
                              "blast_xml": "Hsp_query-frame"}
            ),
            _Feature(
                names=["template_frames", "Template Frames"],
                description="",
                key_aligners={"blast_tab": "sframe",
                              "blast_xml": "Hsp_hit-frame"}
            ),
            _Feature(
                names=["btop", "BTOP"],
                description="",
                key_aligners={"blast_tab": "btop",
                              "blast_xml": None}
            ),
            _Feature(
                names=["template_taxids", "Template TaxIDs"],
                description="",
                key_aligners={"blast_tab": "staxids",
                              "blast_xml": None}
            ),
            _Feature(
                names=["template_scie_name", "Template ScieName"],
                description="",
                key_aligners={"blast_tab": "sccinames",
                              "blast_xml": None}
            ),
            _Feature(
                names=["template_common_name", "Template Common Name"],
                description="",
                key_aligners={"blast_tab": "scomnames",
                              "blast_xml": None}
            ),
            _Feature(
                names=["template_blast_name", "Template Blast Name"],
                description="",
                key_aligners={"blast_tab": "sblastnames",
                              "blast_xml": None}
            ),
            _Feature(
                names=["template_superkingdom", "Template SuperKingdom"],
                description="",
                key_aligners={"blast_tab": "sskingdoms",
                              "blast_xml": None}
            ),
            _Feature(
                names=["template_title", "Template Title"],
                description="",
                key_aligners={"blast_tab": "stitle",
                              "blast_xml": None}
            ),
            _Feature(
                names=["all_template_title", "All Template Titles"],
                description="",
                key_aligners={"blast_tab": "salltitles",
                              "blast_xml": None}
            ),
            _Feature(
                names=["template_strand", "Template Strand"],
                description="",
                key_aligners={"blast_tab": "sstrand",
                              "blast_xml": None}
            ),
            _Feature(
                names=["query_coverage", "Query Coverage"],
                description="Query Coverage per Template",
                key_aligners={"blast_tab": "qcovs",
                              "blast_xml": None}
            ),
            _Feature(
                names=["query_coverage_hsp", "Query Coverage HSP"],
                description="Query Coverage per HSP",
                key_aligners={"blast_tab": "qcovhsp",
                              "blast_xml": None}
            ),
            _Feature(
                names=["query_coverage_once", "Query Coverage Once"],
                description="Query Coverage per template once",
                key_aligners={"blast_tab": "qcovus",
                              "blast_xml": None}
            ),
            _Feature(
                names=["query_coverage_once", "Query Coverage Once"],
                description="Query Coverage per template once",
                key_aligners={"blast_tab": "qcovus",
                              "blast_xml": None}
            ),
            _Feature(
                names=["db_number", "DB Number"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Statistics_db-num"}
            ),
            _Feature(
                names=["db_length", "DB Length"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Statistics_db-len"}
            ),
            _Feature(
                names=["hsp_length", "HSP Length"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Statistics_hsp-len"}
            ),
            _Feature(
                names=["effective_space", "Effective Space"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Statistics_eff-space"}
            ),
            _Feature(
                names=["kappa", "Kappa"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Statistics_kappa"}
            ),
            _Feature(
                names=["lambda", "Lambda"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Statistics_lambda"}
            ),
            _Feature(
                names=["entropy", "Entropy"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Statistics_entropy"}
            ),
            _Feature(
                names=["match_symbols", "Match Symbols"],
                description="",
                key_aligners={"blast_tab": None,
                              "blast_xml": "Hsp_midline"}
            ),
        ]


class KMAFeatures(_DictionaryFeaturesBase):

    def __init__(self):
        res_features = [
            _Feature(
                names=["template_identity", "Template Identity"],
                description="",
                key_aligners={"kma": "Template_Identity"}
            ),
            _Feature(
                names=["template_coverage", "Template Coverage"],
                description="",
                key_aligners={"kma": "Template_Coverage"}
            ),
            _Feature(
                names=["query_identity", "Query Identity"],
                description="",
                key_aligners={"kma": "Query_Identity"}
            ),
            _Feature(
                names=["query_coverage", "Query Coverage"],
                description="",
                key_aligners={"kma": "Query_Coverge"}
            ),
            _Feature(
                names=["depth", "Depth"],
                description="",
                key_aligners={"kma": "Depth"}
            ),
            _Feature(
                names=["q_value", "Q Value"],
                description="",
                key_aligners={"kma": "Q_value"}
            ),
            _Feature(
                names=["p_value", "P Value"],
                description="",
                key_aligners={"kma": "P_value"}
            ),
        ]

        frag_features = [
            _Feature(
                names=["fragments", "Fragment Information"],
                description="",
                key_aligners={"kma": "fragment"}
            )
        ]
        mapstat_features = [
            _Feature(
                names=["template", "Template Sequence"],
                description="",
                key_aligners={"kma": "refSequence"}
            ),
            _Feature(
                names=["reads_mapped", "Reads Mapped"],
                description="",
                key_aligners={"kma": "readCount"}
            ),
            _Feature(
                names=["fragments_mapped", "Fragments Mapped"],
                description="",
                key_aligners={"kma": "fragmentCount"}
            ),
            _Feature(
                names=["mapScoreSum", "Fragments Mapped"],
                description="",
                key_aligners={"kma": "fragmentCount"}
            ),
            _Feature(
                names=["mapScoreSum", "Fragments Mapped"],
                description="",
                key_aligners={"kma": "fragmentCount"}
            ),
        ]


class _Feature:

    def __init__(self, names, description, key_aligners=None):

        if not isinstance(names, list):
            raise TypeError("Names has to be a list")
        if not isinstance(key_aligners):
            raise TypeError("Key_aligners has to be a dictionary")
        self.names = names
        self.description = description
        self.key_aligners = key_aligners
        self.value = None
