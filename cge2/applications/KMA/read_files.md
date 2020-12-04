###Testing of CommandLineBase
```python3
>>> from read_files import KMA_ResultFile, KMA_alignment, Iterator_KMA, Parse_ResFile, Parse_MatrixFile
>>> a = KMA_alignment(output_path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2", files=["Result"])
>>> print(a)
>>> b = Parse_ResFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.res")
>>> print(iter(b[0]))
>>> print(type(iter(b[0])))
>>> print(next(iter(b)))
>>> for n in b: print(n)
>>> c = Parse_MatrixFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.mat.gz")
>>> for n in c: print(n)


```
