from cge2.applications.command import _OptionArgument, CommandLineBase
from cge2.applications.command import _SwitchArgument, _SwitchValueArgument
from cge2.applications.KMA import _KmaBaseCommandline


class KMACommandline(_KmaBaseCommandline):
    """Base Commandline object for the wrapper of the KMA aligner.
    This is provided for subclassing, it deals with shared options
    common to all the BLAST tools (blastn, rpsblast, rpsblast, etc).
    """

    def __init__(self, cmd="kma", **kwargs):
        assert cmd is not None
        self.parameters = [
            # Input query options:
            # THIS IS wrong. Need allowing double files
            _OptionArgument(
                ["-query", None, "query"],
                "The sequence to search with.",
                filename=True,
                equate=False,
            ),  # Should this be required?
            _OptionArgument(
                ["-o", None, "output"],
                "Output file",
                filename=True,
                is_required=True,
                equate=False,
            ),
            _OptionArgument(
                ["-t_db", None, "TemplateDatabase"],
                "Template DB",
                filename=True,
                equate=False,
                is_required=True,
            ),
            _OptionArgument(
                ["-k", None, "Kmersize"],
                "Kmersize (default by db)",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-ml", None, "MinLen"],
                "Minimum alignment length",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-p", None, "p-value"],
                "p-value",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-ConClave", None, "ConClaveV"],
                "ConClave version",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-mem_mode", None, "MemMode"],
                "Use kmers to choose best template, and save memory",
            ),
            _SwitchValueArgument(
                ["-proxi", None, "ProximityScore"],
                "Use proximity scoring under template mapping",
                filename=False,
                equate=False,
                is_required=False,
                default=1.0,
            ),
            _SwitchArgument(
                ["-ex_mode", None, "ExhaustiveSearch"],
                "Searh kmers exhaustively",
            ),
            _SwitchArgument(
                ["-ef", None, "ExtraFiles"],
                "Output extra files",
            ),
            _SwitchValueArgument(
                ["-vcf", None, "VCF"],
                "Make vcf file, 2 to apply FT",
                filename=False,
                equate=False,
                is_required=False,
                default=0,
            ),
            _SwitchValueArgument(
                ["-sam", None, "SAM"],
                "Output sam to stdout, 4 to output mapped reads,"
                "2096 for aligned",
                filename=False,
                equate=False,
                is_required=False,
                default=0,
            ),
            _SwitchArgument(
                ["-nc", None, "NonConsensus"],
                "No consensus file",
            ),
            _SwitchArgument(
                ["-na", None, "NoAlign"],
                "No aln file",
            ),
            _SwitchArgument(
                ["-nf", None, "NoFrag"],
                "No frag file",
            ),
            _SwitchArgument(
                ["-deCon", None, "deCon"],
                "Remove contamination",
            ),
            _SwitchArgument(
                ["-dense", None, "dense"],
                "Do not allow insertions in assembly",
            ),
            _SwitchArgument(
                ["-sasm", None, "sasm"],
                "Skip alignment and assembly",
            ),
            _SwitchValueArgument(
                ["-ref_fsa", None, "refsa"],
                "Consensus sequence will have 'n' instead of gaps",
                filename=False,
                equate=False,
                is_required=False,
                default=0,
            ),
            _SwitchArgument(
                ["-matrix", None, "Matrix"],
                "Outputs assembly matrix",
            ),
            _SwitchArgument(
                ["-a", None, "BestMapps"],
                "Print all best mappings",
            ),
            _OptionArgument(
                ["-mp", None, "MinPhred"],
                "Minimum phred score",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-5p", None, "Cut5p"],
                "Cut a constant number of nucleotides from the 5 prime",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-3p", None, "Cut3p"],
                "Cut a constant number of nucleotides from the 3 prime",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-Sparse", None, "Sparse"],
                "Only count kmers",
            ),
            _SwitchValueArgument(
                ["-Mt1", None, "MapToTemplate"],
                "Map only to 'num' template",
                filename=False,
                equate=False,
                is_required=False,
                default=0,
            ),
            _OptionArgument(
                ["-ID", None, "ID"],
                "Minimum ID",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-ss", None, "Sparsesort"],
                "Sparse sorting (q,c,d)",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-pm", None, "Pairing"],
                "Pairing method (p,u,f)",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-fpm", None, "FinePairing"],
                "Fine Pairing method (p,u,f)",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-apm", None, "FPM/PM"],
                "Sets both pm and fpm (p,u,f)",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-shm", None, "SharedDB"],
                "Use shared DB made by kma_shm",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-mmap", None, "Memorymap"],
                "Memory map *.comp.by",
            ),
            _OptionArgument(
                ["-tmp", None, "TmpFolder"],
                "Set directory for temporary files.",
                filename=True,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-tmp", None, "TmpFolder"],
                "Set directory for temporary files.",
                filename=True,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-1t1", None, "EndMapping"],
                "Force end to end mapping"
            ),
            _SwitchArgument(
                ["-hmm", None, "HMMMapping"],
                "Use a HMM to assign template(s) to query sequences"
            ),
            _SwitchArgument(
                ["-ck", None, "CountK"],
                "Count kmers instead of pseudo alignment"
            ),
            _SwitchArgument(
                ["-ca", None, "CircularAln"],
                "Make circular alignments"
            ),
            _SwitchArgument(
                ["-boot", None, "Bootstrap"],
                "Bootstrap sequence"
            ),
            _SwitchArgument(
                ["-bc", None, "BaseCalls"],
                "Base calls should be significantly overrepresented"
            ),
            _SwitchArgument(
                ["-bc90", None, "BaseCalls90"],
                "Base calls should be both significantly overrepresented, and"
                " have 90% agreement."
            ),
            _SwitchArgument(
                ["-bcNano", None, "BaseCallsNano"],
                "Call bases at suspicious deletions, made for nanopore."
            ),
            _OptionArgument(
                ["-bcd", None, "MinDepth"],
                "Minimum depth at base.",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-bcg", None, "InsignificantGaps"],
                "Maintain insignificant gaps",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-and", None, "MRS&P_Value"],
                "Both mrs and p_value thresholds has to reached to in order "
                "to	report a template hit.",
            ),
            _OptionArgument(
                ["-mq", None, "MinMapQ"],
                "Minimum mapping quality",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-mrs", None, "MinAlnQ"],
                "Minimum alignment score, normalized to alignment length",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-mct", None, "MaxOverlapTemp"],
                "Max overlap between templates",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-reward", None, "Reward"],
                "Score for match",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-penalty", None, "Penalty"],
                "Penalty for mismatch",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-gapopen", None, "GapOpen"],
                "Penalty for gap opening",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-gapextend", None, "GapExtend"],
                "Penalty for gap extension",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-per", None, "RewardPairing"],
                "Reward for pairing end",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-localopen", None, "LocalOpen"],
                "Penalty for openning a local chain",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-Npenalty", None, "Npenalty"],
                "Penalty matching N",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-transition", None, "PenTrans"],
                "Penalty for transition",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-transversion", None, "PenTransv"],
                "Penalty for transversion",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-cge", None, "CGESet"],
                "Set CGE penalties and rewards",
            ),
            _OptionArgument(
                ["-t", None, "Threads"],
                "Number of threads",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-status", None, "Status"],
                "Extra status",
            ),
            _SwitchArgument(
                ["-verbose", None, "Verbose"],
                "Extra verbose",
            ),
            _SwitchArgument(
                ["-c", None, "Citation"],
                "Citation",
            ),
        ]
        _KmaBaseCommandline.__init__(self, cmd, **kwargs)

class KMAIndexCommandline(_KmaBaseCommandline):
    """Base Commandline object for (new) NCBI BLAST+ wrappers (PRIVATE).
    This is provided for subclassing, it deals with shared options
    common to all the BLAST tools (blastn, rpsblast, rpsblast, etc).
    """

    def __init__(self, cmd="kma_index", **kwargs):
        assert cmd is not None
        extra_parameters = [
            _OptionArgument(
                ["-i", None, "Input"],
                "Input/query file name (STDIN: '--')",
                filename=True,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-o", None, "Output"],
                "Output file",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-batch", None, "Batch"],
                "Batch input file",
                filename=True,
                equate=False,
                is_required=False,
            ),
            _SwitchValueArgument(
                ["-deCon", None, "deCon"],
                "File with contamination (STDIN: '--')",
                filename=True,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-batchD", None, "batchD"],
                "Batch decon file",
                filename=True,
                equate=False,
                is_required=False,
            ),
            _SwitchValueArgument(
                ["-t_db", None, "AddDB"],
                "Add to existing DB",
                filename=True,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-k", None, "kmersize"],
                "Kmersize",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-k_t", None, "KmerTemp"],
                "Kmersize for template identification",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-k_i", None, "KmerIndex"],
                "Kmersize for indexing",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-ML", None, "MinLenTemplate"],
                "Minimum length for templates",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-CS", None, "StartChainSize"],
                "Start chain size",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-ME", None, "MegaDB"],
                "Mega DB",
            ),
            _SwitchArgument(
                ["-NI", None, "NoIndex"],
                "Do not dump *.index.b",
            ),
            _SwitchValueArgument(
                ["-Sparse", None, "Sparse"],
                "Make Sparse DB ('-' for no prefix)",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-ht", None, "HomologyTemp"],
                "Homology template",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-hq", None, "HomologyQuery"],
                "Homology query",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-and", None, "BothHomology"],
                "Both homolgy thresholds has to be reached",
            ),
            _SwitchArgument(
                ["-nbp", None, "NoBias"],
                "No bias print",
            ),
        ]
        _KmaBaseCommandline.__init__(self, cmd, **kwargs)


class KMAShmCommandline(_KmaBaseCommandline):
    """Base Commandline object for (new) NCBI BLAST+ wrappers (PRIVATE).
    This is provided for subclassing, it deals with shared options
    common to all the BLAST tools (blastn, rpsblast, rpsblast, etc).
    """

    def __init__(self, cmd="kma_shm", **kwargs):
        assert cmd is not None
        extra_parameters = [
            _OptionArgument(
                ["-t_db", None, "TemplateDB"],
                "Template DB",
                filename=True,
                equate=False,
                is_required=True,
            ),
            _SwitchArgument(
                ["-destroy", None, "DestroyShared"],
                "Destroy shared memory",
            ),
            _OptionArgument(
                ["-shmLvl", None, "LvlSharedMem"],
                "Level of shared memory",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-shm-h", None, "ExplainLvl"],
                "Explain of shared memory",
            ),
        ]


class KMASeq2FastaCommandline(_KmaBaseCommandline):
    """Base Commandline object for (new) NCBI BLAST+ wrappers (PRIVATE).
    This is provided for subclassing, it deals with shared options
    common to all the BLAST tools (blastn, rpsblast, rpsblast, etc).
    """

    def __init__(self, cmd="kma seq2fasta", **kwargs):
        assert cmd is not None
        extra_parameters = [
            _OptionArgument(
                ["-t_db", None, "TemplateDB"],
                "Template DB",
                filename=True,
                equate=False,
                is_required=True,
            ),
            _SwitchArgument(
                ["-seqs", None, "Seqs"],
                "Comma separated list of templates",
            ),
        ]
        _KmaBaseCommandline.__init__(self, cmd, **kwargs)


class KMADistCommandline(_KmaBaseCommandline):
    """Base Commandline object for (new) NCBI BLAST+ wrappers (PRIVATE).
    This is provided for subclassing, it deals with shared options
    common to all the BLAST tools (blastn, rpsblast, rpsblast, etc).
    """

    def __init__(self, cmd="kma dist", **kwargs):
        assert cmd is not None
        extra_parameters = [
            _OptionArgument(
                ["-t_db", None, "TemplateDB"],
                "Template DB",
                filename=True,
                equate=False,
                is_required=True,
            ),
            _OptionArgument(
                ["-o", None, "Output"],
                "Output file",
                filename=True,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-f", None, "OFlags"],
                "Output flags",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-fh", None, "HelpFlags"],
                "Help on option '-f'",
            ),
            _OptionArgument(
                ["-d", None, "DistanceMethod"],
                "DistanceMethod",
                filename=False,
                equate=False,
                is_required=False,
            ),
            _SwitchArgument(
                ["-dh", None, "HelpDistance"],
                "Help on option '-d'",
            ),
            _SwitchArgument(
                ["-m", None, "DiskAllocate"],
                "Allocate matrix on the disk",
            ),
            _OptionArgument(
                ["-tmp", None, "TmpFile"],
                "Set directory for temporary file",
                filename=True,
                equate=False,
                is_required=False,
            ),
            _OptionArgument(
                ["-t", None, "Threads"],
                "Number of threads",
                filename=False,
                equate=False,
                is_required=False,
            ),
        ]
        _KmaBaseCommandline.__init__(self, cmd, **kwargs)


class KMADBCommandline(_KmaBaseCommandline):
    """Base Commandline object for (new) NCBI BLAST+ wrappers (PRIVATE).
    This is provided for subclassing, it deals with shared options
    common to all the BLAST tools (blastn, rpsblast, rpsblast, etc).
    """

    def __init__(self, cmd="kma db", **kwargs):
        assert cmd is not None
        extra_parameters = [
            _OptionArgument(
                ["-t_db", None, "TemplateDB"],
                "Template DB",
                filename=True,
                equate=False,
                is_required=True,
            ),
        ]
        _KmaBaseCommandline.__init__(self, cmd, **kwargs)
