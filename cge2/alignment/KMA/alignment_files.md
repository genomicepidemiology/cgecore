Alignment results class test
=================



###Testing results
```python3
>>> from alignment_files import Read_Alignment
>>> resfile = Read_Alignment.read_resfile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output.res")
>>> fragfile = Read_Alignment.read_alnfile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output.aln")
>>> consfile = Read_Alignment.read_matrixfile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output.mat.gz")
>>> alnfile = Read_Alignment.read_mapstatfile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output.mapstat")
>>> matrixfile = Read_Alignment.read_fragfile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output.frag.gz")
>>> mapstatfile = Read_Alignment.read_rawfragfile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output.frag_raw.gz")
>>> rawfragfile = Read_Alignment.read_consfile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output.fsa")
>>> from alignment_files import Iterator_ResFile, Iterator_MapstatFile, Iterator_MatrixFile, Iterator_AlignmentFile, Iterator_ConsensusFile, Iterator_VCFFile, Iterator_SPAFile, Iterator_FragmentFile
>>> iter_res = Iterator_ResFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.res")
>>> print(next(iter_res))
>>> print(next(iter_res))
>>> iter_map = Iterator_MapstatFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.mapstat")
>>> print(next(iter_map))
>>> print(next(iter_map))
>>> c = Iterator_MatrixFile(path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.mat.gz")
>>> print(next(c))
>>> print(next(c))
>>> c = Iterator_AlignmentFile(path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.aln")
>>> print(next(c))
>>> print(next(c))
>>> c = Iterator_ConsensusFile(path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.fsa")
>>> print(next(c))
>>> print(next(c))
>>> c = Iterator_VCFFile(path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.vcf.gz")
>>> print(next(c))
>>> print(next(c))
>>> c = Iterator_SPAFile(path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/results.spa")
>>> print(next(c))
>>> print(next(c))
>>> c = Iterator_FragmentFile(path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.frag.gz")
>>> print(next(c))
>>> print(next(c))
