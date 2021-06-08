# BeOne template

BeOne example output from ResFinder: [example.json](https://bitbucket.org/genomicepidemiology/cge_core_module/src/2.0/cge2/output/templates_json/beone/example.json)

## Classes

- **software_result**
- **database**
- **seq_region**
- **seq_variation**
- **phenotype**

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
    "seq_regions": "dict seq_region:class",
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

**seq_regions**: See "gene" description.

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

### seq_region

```json

"gene": {
    "type": "seq_region",
    "key": "string*",
    "name": "string*",
    "gene": "bool_or_unknown",
    "identity": "percentage",
    "alignment_length": "integer",
    "ref_seq_lenght": "integer",
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
    "ref_database": "database.key*",
    "note": "string"
  }

```

**key**: Unique identifier for seq_region hit. Several hits to the same seq_region can occur. Unlike the ref_id, this key must be unique between these hits.  
*Example*: aph(6)-Id;;1;;M28829;;d5sm

**name**: Gene name / Region name.  
*Example*: aph(6)-Id

**gene**: True if the seq_region is a gene, if not, False or unknown.

**identity**: Percent identical bps between query data (input) and reference
seq_region (database).

**alignment_length**: Number of bps in the alignment between query and
reference.

**ref_seq_lenght**: Length in bps of the reference seq_region.

**coverage**: Percentage of the reference seq_region covered by the query data.

**depth**: Average number of times the reference seq_region has been covered by the
query data.

**ref_id**: Unique identifier for seq_region in database, but doesn't have to be
unique in the results. See also "key".  
*Example*: aph(6)-Id_1_M28829

**ref_acc**: If the reference seq_region is extracted from a public database, the
accession number identifying the sequence is stored here.  
*Example*: M28829

**ref_start_pos**: Position in reference seq_region where the alignment starts.

**ref_end_pos**: Position in reference seq_region where the alignment ends.

**query_id**: Unique identifier for the input sequence. For example a contig or
read header.  
*Example*: NODE_47_length_14097_cov_7.40173_ID_3656

**query_start_pos**: Position in query seq_region where the alignment starts.

**query_end_pos**: Position in query seq_region where the alignment starts.

**phenotypes**: List of phenotypes associated to the seq_region.

**ref_database**: Uniquely identifying the database where the reference seq_region can
be found.  
*Example*: PointFinder-d48a0fe

**note**: Free text field for additional information.

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
    "ref_database": "database.key*",
    "seq_regions": "array seq_region.key",
    "phenotypes": "array phenotype.key"
  }

```

**key**: Unique identifier for sequence variation. Format is:
<seq_region>;;<ref_start_pos>;;<var_codon>(;;<random_string>), where pos is the
position of the first nucleotide in the codon. The codon can be a single
nucleotide if found in a non-coding region. If the first part is not unique then
a small random string of small letters will be attached.
*Example*: 23S;;357;;t

**ref_id**: String to identify the mutation in the reference database. Format
is: <seq_region>;;<ref_start_pos>;;<var_codon>. Similar to key but not
guarenteed to be unique.
*Example*: folP;;28;;tta

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

**seq_regions**: List of seq_regions associated to the sequence variation.

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
    "seq_regions": "array seq_region.key",
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

**seq_regions**: List of seq_regions causing the phenotype, found in the output in question. Not a comprehensive list of seq_regions causing the phenotype in question.

**seq_variations**: List of sequence variations causing the phenotype, found in the output in question. Not a comprehensive list of sequence variations causing the phenotype in question.

**ref_database**: Uniquely identifying the database where the variation is annotated.  
*Example*: ResFinder-d48a0fe


## ISSUES

**genes and seq_variation notes**
Should add a free text notes field for seq_variation entries.

**seq_variation key and ref_id**  
Are they always identical. If so, can there be two identical keys?

**Missing value parser**
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
