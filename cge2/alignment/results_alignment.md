Alignment results class test
=================



###Testing results
```python3
>>> from results_alignment import Hit_Alignment
>>> example = Hit_Alignment(format="kma", empty=True)
>>> print(example)
>>> example["Works"] = True
>>> print(example["Works"])
>>> del example["Works"]
>>> example["software"] = "blastn"
>>> example["software"] = "kma"
>>> example.update(format="kma")
>>> example.update(format="blast_tab", substitute=True)
>>> print(example)
>>> from blast.alignment_files import Iterator_BlastSepFile, Iterator_XMLFile
>>> iter_res = Iterator_BlastSepFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino6.tab", separator="tab", comment_lines=False)
>>> print(next(iter_res))
>>> new_hit = Hit_Alignment(format="blast_tab")
>>> new_hit["qseqid"] = "SUPPPP"
>>> print(new_hit)
>>> iter_res = Iterator_XMLFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino5.xml")
>>> print(next(iter_res))
>>> from KMA.alignment_files import Iterator_ResFile
>>> iter_res = Iterator_ResFile("/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/output2/output2.res")
>>> print(next(iter_res))
>>> print(next(iter_res))
