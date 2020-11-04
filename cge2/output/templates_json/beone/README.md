# BeOne template

BeOne example output from ResFinder: [example.json](https://bitbucket.org/genomicepidemiology/cge_core_module/src/2.0/cge2/output/templates_json/beone/example.json)

## Classes

- **software_result**
- **database**
- **gene**
- **seq_variation**
- **phenotype**
- **seq_region**

### software_result

```json

"software_result": {
    "type": "software_result",
    "key": "string*",
    "software_name": "string*",
    "software_version": "string*",
    "software_branch": "string",
    "software_commit": "string",
    "software_log": "string",
    "run_id": "string",
    "run_date": "date",
    "databases": "dict database:class",
    "genes": "dict gene:class",
    "seq_variations": "dict seq_variation:class",
    "phenotypes": "dict phenotype:class"
  }

```

**key**: For CGE tools the key will be <software_name>-<software_version>
*Example*: ResFinder-4.1.0

**software_name**: Name of the application creating the output.
*Example*: "software_name": "ResFinder"

**software_version**: [Semantic Versioning](https://semver.org/). Given a version number MAJOR.MINOR.PATCH. If no version number can be provided,
the first seven digits of the Git commit checksum is expected here.
*Example*: 4.1.0
*Example*: d48a0fe

**software_branch**: Name of the git branch.
*Example*: develop

**software_commit**: Git commit checksum.
*Example*: d48a0fe7afa763a50777c89a3289d1fd3b13cee5

**software_log**: Ouput written to stdout and/or stderr by the software.

**run_id**: The id should uniquely define how the software was run. Two
identical run_ids should indicate two identical runs. This could be a checksum.

**run_date**: Date and time for when the software was started. UTC timezone.

**databases**: See "database" description.

**genes**: See "gene" description.

**seq_variations**: See "seq_variation".

**phenotypes**: See "phenotypes".

### database

```json

"database": {
    "type": "database",
    "key": "string*",
    "database_name": "string*",
    "database_version": "string",
    "database_branch": "string",
    "database_commit": "string",
    "checksum_sha256": "char64"
  }

```

**key**: For CGE tools the key will be <database_name>-<database_version>.
*Example*: PointFinder-d48a0fe

**database_name**: Name of a database used when running the software.
*Example*: PointFinder

**database_version**: [Semantic Versioning](https://semver.org/). Given a version number MAJOR.MINOR.PATCH. If no version number can be provided,
the first seven digits of the Git commit checksum is expected here.
*Example*: 4.1.0
*Example*: d48a0fe

**database_branch**: Name of the git branch.
*Example*: develop

**database_commit**: Git commit checksum.
*Example*: d48a0fe7afa763a50777c89a3289d1fd3b13cee5

**checksum_sha256**: SHA256 checksum of entire database.
*Example*: 08304e062528ae12ecb07abe139e26512fb5991e36df93e30e0d92d885479709

### gene

```json

"gene": {
    "type": "gene",
    "key": "string*",
    "name": "string*",
    "identity": "percentage",
    "alignment_length": "integer",
    "ref_gene_lenght": "integer",
    "coverage": "percentage",
    "depth": "float",
    "ref_id": "string*",
    "ref_acc": "string",
    "ref_start_pos": "integer",
    "ref_end_pos": "integer",
    "query_id": "string",
    "query_start_pos": "integer",
    "query_end_pos": "integer",
    "phenotypes": "array phenotype.key",
    "ref_database": "database.key"
  }

```

**key**: Unique identifier for gene hit. Several hits to the same gene can
occur. Unlike the ref_id, this key must be unique between these hits.
*Example*: aph(6)-Id;;1;;M28829;;d5sm

**name**: Gene name.
*Example*: aph(6)-Id

**identity**: Percent identical bps between query data (input) and reference
gene (database).

**alignment_length**: Number of bps in the alignment between query and
reference.

**ref_gene_lenght**: Length in bps of the reference gene.

**coverage**: Percentage of the reference gene covered by the query data.

**depth**: Average number of times the reference gene has been covered by the
query data.

**ref_id**: Unique identifier for gene in database, but doesn't have to be
unique in the results. See also "key".  
*Example*: aph(6)-Id_1_M28829

**ref_acc**: If the reference gene is extracted from a public database, the
accession number identifying the sequence is stored here.  
*Example*: M28829

**ref_start_pos**: Position in reference gene where the alignment starts.

**ref_end_pos**: Position in reference gene where the alignment ends.

**query_id**: Unique identifier for the input sequence. For example a contig or
read header.
*Example*: NODE_47_length_14097_cov_7.40173_ID_3656

**query_start_pos**: Position in query gene where the alignment starts.

**query_end_pos**: Position in query gene where the alignment starts.

**phenotypes**: List of phenotypes associated to the gene.

**ref_database**: Uniquely identifying the database where the reference gene can
be found.  
*Example*: PointFinder-d48a0fe

### seq_variation

```json

"seq_variation": {
    "type": "seq_variation",
    "key": "string*",
    "ref_id": "string*",
    "seq_var": "seq_var_string",
    "codon_change": "codon_change_string",
    "ref_codon": "nucleotides",
    "var_codon": "nucleotides",
    "ref_aa": "aminoacid_1_char",
    "var_aa": "aminoacid_1_char",
    "ref_start_pos": "integer",
    "ref_end_pos": "integer",
    "substitution": "bool",
    "insertion": "bool",
    "deletion": "bool",
    "ref_database": "database.key",
    "genes": "array gene.key",
    "phenotypes": "array phenotype.key"
  }

```

**key**: Unique identifier for sequence variation. Format is:
<name>\_<pos>\_<alternative_codon>, where name is seq_region name, alternative_nt is the codon in the input data, not the reference, and pos is the posiotion of the first nucleotide in the codon. The codon can be a single nucleotide if found in a non-coding region.  
*Example*: 23S_357_t

**ref_id**: Same as key. See ISSUES section.  
*Example*: folP_38_tta

**seq_var**: String describing the nucleotide variation according [HGVS Sequence Variant Nomenclature](http://varnomen.hgvs.org/)  
*Example*: p.I38L

**codon_change**: String describing codon change. Is not used in non-coding variations. The format is <ref codon>><alt_codon>  
*Example*: ata>tta

**ref_codon**: Reference codon.  Is not used in non-coding variations.  
*Example*: ata

**var_codon**: Codon found in the input data. Is not used in non-coding variations.  
*Example*: tta

**ref_aa**: Reference amino acid. 1-character-coding.
*Example*: i

**var_aa**: Amino acid found in input data. 1-character-coding.
*Example*: l

**ref_start_pos**: Position of variation start. If in coding region this is the amino acid position, if in a non-coding region this is the nucleotide acid position. For single amino acid substitution, this will be identical to ref_end_pos.
*Example*: 38

**ref_end_pos**: Position of variation end. If in coding region this is the amino acid position, if in a non-coding region this is the nucleotide acid position. For single amino acid substitution, this will be identical to ref_end_pos.
*Example*: 38

**substitution**: True if the variation is a substitution.

**insertion**: True if the variation is an insertion.

**deletion**: True if the variation is a deletion.

**ref_database**: Uniquely identifying the database where the variation is annotated.  
*Example*:PointFinder-6323b5c

**genes**: List of genes associated to the sequence variation.

**phenotypes**: List of phenotypes associated to the sequence variation.

### phenotype

```json

"phenotype": {
    "type": "phenotype",
    "key": "string*",
    "category": "vocabulary*",
    "amr_classes": "array vocabulary",
    "amr_resistance": "vocabulary",
    "amr_resistant": "bool_or_unknown",
    "genes": "array gene.key",
    "seq_variations": "array seq_variation.key",
    "ref_database": "database.key"
  }

```

**key**: Unique identifier for phenotype.

**category**: phenotype category vocabulary.  
*Example*: amr

**amr_classes**: List of amr classes the phenotype belongs to.

**amr_resistance**: Name of antibiotic to which this phenotype causes resistance.
*Example*: netilmicin

**amr_resistant**: Indicates if the phenotype in question describes amr resistance.

**genes**: List of genes causing the phenotype, found in the output in question. Not a comprehensive list of genes causing the phenotype in question.

**seq_variations**: List of sequence variations causing the phenotype, found in the output in question. Not a comprehensive list of sequence variations causing the phenotype in question.

**ref_database**: Uniquely identifying the database where the variation is annotated.  
*Example*: ResFinder-d48a0fe

### seq_region

**Under construction**
This class will take over from "gene" as it is more appropriate for hits in
promoter regions etc.

```json

"seq_region": {
      "type": "seq_region",
      "key": "string*",
      "name": "string*",
      "gene": "bool_or_unknown",
      "identity": "percentage",
      "alignment_length": "integer",
      "ref_gene_lenght": "integer",
      "coverage": "percentage",
      "depth": "float",
      "ref_id": "string*",
      "ref_acc": "string",
      "ref_start_pos": "integer",
      "ref_end_pos": "integer",
      "query_id": "string",
      "query_start_pos": "integer",
      "query_end_pos": "integer",
      "phenotypes": "array phenotype.key",
      "ref_database": "database.key"
    }

```

## ISSUES

**seq_variation key and ref_id**  
Are they always identical. If so, can there be two identical keys?

**Missing value parser**
- bool_or_unknown
- bool
- seq_var_string
- codon_change_string
- aminoacid_1_char
- vocabulary

**Vocabulary**
*Under construction*
Vocabulary values are only valid if they are found in specific vocabulary templates/definitions. How exactly they should be formatted is still being discussed.  
A vocabulary should be identified either by <key>.vocabulary or <class>.<key>.vocabulary. How to handle different classes using same vocabulary?

**seq_variation.genes**
Should this be a list? Why?

**phenotype**
amr_classes: Is currently being written to the key "classes"  
amr_resistance: Is currently being written to the key "resistance"  
amr_resistant: Not currently used.  
