###Testing of CommandLineBase
```python3
>>> from read_files import KMA_ResultFile, KMA_alignment, Iterate_KMAFiles, Iterator_KMAAlignment
>>> a = KMA_ResultFile(name="Result", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.res")
>>> print(a)
>>> a = KMA_alignment(output_path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2", files=["Result"])
>>> print(a)
>>> b = Iterate_KMAFiles(output_path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2", files=["Result"])
>>> print(next(b))
>>> b = Iterate_KMAFiles(output_path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2", files=["Result","Matrix"])
>>> print(next(b))
>>> print(next(b))
>>> #x = Iterator_KMAAlignment(output_path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/", template_files=["Result", "Mapstat"], output_files=["output3macrolide", "output3fosfomycin", "output3colistin", "output3aminoglycoside", "output3glycopeptide", "output3beta-lactam"])
>>> x = Iterator_KMAAlignment(output_path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/", template_files=["Result", "Matrix"], output_files=["output3macrolide", "output3fosfomycin", "output3colistin", "output3aminoglycoside", "output3glycopeptide", "output3beta-lactam"])
>>> print(next(x))
>>> print(next(x))
>>> print(next(x))
>>> print(next(x))
>>> print(next(x))
>>> print(next(x))
>>> print(next(x))
>>> print(next(x))
>>> print(next(x))
>>> print(next(x))
>>> print(next(x))
>>> print(next(x))

```
