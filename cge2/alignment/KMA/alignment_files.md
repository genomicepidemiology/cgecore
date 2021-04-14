Alignment results class test
=================



###Testing results
```python3
>>> from alignment_files import Iterator_ResFile, Iterator_MapstatFile, Iterator_MatrixFile, Iterator_AlignmentFile, Iterator_ConsensusFile, Iterator_VCFFile, Iterator_SPAFile, Iterator_FragmentFile
>>> iter_res = Iterator_ResFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.res")
>>> print(iter_res.extension)
>>> print(next(iter_res))
>>> print(next(iter_res))
>>> iter_map = Iterator_MapstatFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.mapstat")
>>> print(next(iter_map))
>>> print(next(iter_map))
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
>>> c = Iterator_MatrixFile(path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.mat.gz")
>>> print(next(c))
>>> print(next(c))
