###Testing of BLASTNCommandLineBase
```python3
>>> from blast.blast_application import BlastNCommandline
>>> blastnline = BlastNCommandline(task="megablast")
>>> blastnline = BlastNCommandline(subject="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/glycopeptide.fsa", query="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/44571.fna", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/outputblast", outfmt=5, perc_identity=0.9, max_target_seqs=50000, dust="no")
>>> blastnline
>>> str(blastnline)
>>> std_output, err_output = blastnline()
>>> print(std_output)
>>> print(err_output)
