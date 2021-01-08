###Testing of CommandLineBase
```python3
>>> from run_kma import KMA_aligner
>>> a = KMA_aligner(path_exec="/home/alfred/bio_tools/kma/",input=["/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/Ecoli4_S9_L001_R1_001.fastq","/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/Ecoli4_S9_L001_R2_001.fastq"], output = "/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output3", matrix=True, vcf=True, extra_files=True, datasets=["/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/beta-lactam", "/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/glycopeptide", "/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/aminoglycoside", "/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/colistin", "/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/fosfomycin", "/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/macrolide"])
>>> a()
>>> #a(json_path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output3.json")
