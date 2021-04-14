

class Translate_Hits:

    BLAST_TSV = {
        "qseqid": "queryID",
        "sseqid": "templateID",
        "pident": "query_identity",
        "sstart": "template_start_aln",
        "send": "template_end_aln",
        "qseq": "query_aln",
        "sseq": "template_aln",
        "evalue": "evalue",
        "length": "aln_length",
        "qcov": "query_coverage",
        "qstart": "query_start_aln",
        "qend": "query_end_aln",
        "bitscore": "bitscore",
        }

    BLAST_XML_HSP = {
        "query": "query_aln",
        "sbjct": "template_aln",
        "pident": "query_identity",
        "sbjct_start": "template_start_aln",
        "sbjct_end": "template_end_aln",
        "expect": "evalue",
        "align_length": "aln_length",
        "qcov": "query_coverage",
        "query_start": "query_start_aln",
        "query_end": "query_end_aln",
        "bits": "bitscore",
        "score": "score",
        "num_alignments": "N_alignments",
        "match": "match_symbols"
    }

    KMA_RES = {
        "Template": "templateID",
        "Score": "conclave_score",
        "Expected": "evalue",
        "Template_length": "template_length",
        "Template_Identity": "template_identity",
        "Template_Coverage": "template_coverage",
        "Query_Identity": "query_identity",
        "Query_Coverage": "query_coverage",
        "Depth": "depth",
        "Q_value": "q_value",
        "P_value": "p_value"
    }

    KMA_MAPSTAT = {
        "refSequence": "templateID",
        "readCount": "reads_mapped",
        "fragmentCount": "fragments_mapped",
        "mapScoreSum": "mapScoreSum",
        "refCoveredPositions": "template_coveredPos",
        "refConsensusSum": "template_consesusSum",
        "bpTotal": "bpTotal",
        "depthVariance": "depth_variance",
        "nucHighDepthVariance": "nucHigh_depth_variance",
        "depthMax": "depth_max",
        "snpSum": "snps",
        "insertSum": "insertions",
        "deletionSum": "deletions"
    }

    KMA_SPA = {
        "#Template": "templateID",
        "Num": "Num",
        "Score": "score",
        "Expected": "evalue",
        "Template_length": "template_length",
        "Query_Coverge": "query_coverage",
        "Template_Coverage": "template_coverage",
        "Depth": "depth",
        "tot_query_Coverage": "tot_query_coverage",
        "tot_template_Coverage": "tot_template_coverage",
        "tot_depth": "tot_depth",
        "q_value": "q_value",
        "p_value": "p_value"
    }

    @staticmethod
    def translate_keys(key, dict, strict=False):
        if key in dict:
            return dict[key]
        else:
            if strict:
                raise KeyError("Key %s is not included in the dictionary" % key)
            else:
                return key
