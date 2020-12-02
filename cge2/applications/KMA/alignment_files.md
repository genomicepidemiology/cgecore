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
>>> from kma_alignment import KMA_ResultFile, KMA_alignment
>>> res_file = KMA_ResultFile("Result", "/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputwrong", extension=".res", read_method=Read_Alignment.read_resfile)
>>> print(res_file)
Traceback (most recent call last):
...
OSError: File /home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputwrong.res does not exists
>>> res_file = KMA_ResultFile("Result","/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output", extension=".res", read_method=Read_Alignment.read_resfile)
>>> print(res_file)
/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output.res
>>> res_file.read()
{'blaB-2_1_AF189300': {'Template': 'blaB-2_1_AF189300', 'Score': 8196, 'Expected': 0, 'Template_length': 750, 'Template_Identity': 100.0, 'Template_Coverage': 100.0, 'Query_Identity': 100.0, 'Query_Coverage': 100.0, 'Depth': 11.08, 'q_value': 8196.0, 'p_value': 1e-26}}
>>> alignment = KMA_alignment(output_path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output", files=["Result", "Consensus"])
>>> alignment_wrong = KMA_alignment(output_path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputwrong", files=["Result", "Consensus"])
>>> alignment.read()
>>> new_kma = KMA_alignment(output_path="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output", files=["Result", "Mapstat", "Matrix"])
>>> print(new_kma.list_files)
>>> new_kma.read(json_dump="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.json")
