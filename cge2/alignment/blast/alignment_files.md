Alignment results class test
=================



###Testing results
```python3
>>> from alignment_files import Iterator_BlastSepFile, Iterator_XMLFile
>>> iter_res = Iterator_BlastSepFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino6.tab", separator="tab", comment_lines=False)
>>> print(next(iter_res))
>>> print(next(iter_res))
>>> print(next(iter_res))
>>> print(next(iter_res))
>>> print(next(iter_res))
>>> iter_res = Iterator_BlastSepFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino10.tab", separator="comma")
>>> print(next(iter_res))
>>> print(next(iter_res))
>>> iter_res = Iterator_BlastSepFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino7.tab", separator="tab", comment_lines=True)
>>> print(next(iter_res))
>>> print(next(iter_res))
>>> print(next(iter_res))
>>> print(next(iter_res))
>>> iter_res = Iterator_XMLFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino5.xml")
>>> print(next(iter_res))
>>> print(next(iter_res))
>>> iter_res = Iterator_XMLFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino5.xml")
>>> for i in iter_res: print(i)
