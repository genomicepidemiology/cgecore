###Testing of CommandLineBase
```python3
>>> from read_files import KMA_ResultFile, KMA_alignment, Iterator_KMA, Parse_ResFile, Parse_MatrixFile, Parse_AlignmentFile, Parse_VCFFile, Parse_SPAFile, Parse_MapstatFile, Parse_FragFile
>>> a = KMA_alignment(output_path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2", files=["Result"])
>>> print(a)
>>> b = Parse_ResFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.res")
>>> print(iter(b[0]))
>>> print(type(iter(b[0])))
>>> print(next(iter(b)))
>>> for n in b: print(n)
>>> c = Parse_MatrixFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.mat.gz")
>>> #for n in c: print(n)
>>> d = Parse_AlignmentFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.aln")
>>> #for n in d: print(n)
>>> el = Parse_VCFFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.vcf.gz")
>>> el.get_info()
>>> #for n in el: print(n)
>>> spa = Parse_SPAFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/results.spa")
>>> for n in spa: print(n)
>>> mapstat = Parse_MapstatFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.mapstat")
>>> mapstat.get_info()
>>> for n in mapstat: print(n)
>>> frag = Parse_FragFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.frag.gz")
>>> for n in frag: print(n)

```
