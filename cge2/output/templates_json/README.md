# Templates

## Introduction

Output from CGE tools are written into
[JSON](https://en.wikipedia.org/wiki/JSON) formatted files. The output is in
addition to being JSON formatted further defined in a set of definition files,
which are also JSON formatted.  
The definition files describe how to read the output from the CGE tools. A
python module has also been developed, that can be used to read CGE JSON files
into python objects. But more importantly the module is implemented by the
CGE tools to write output JSON files that adhere to the definitions provided.
In order to change or add the CGE tools output, one just needs to alter the
template that defines the results that needs to be output.

## Definitions

The idea is that several definitions can exist, but at the moment there is only
one, and we hope to keep it this way.

### BeOne

The default definition for all CGE tools. Named BeOne after the collaboration in which it was developed.
**Detailed description**:
[BeOne definition](https://bitbucket.org/genomicepidemiology/cge_core_module/src/2.0/cge2/output/templates_json/beone/)
