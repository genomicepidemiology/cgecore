Datasets class test
===============


###Testing of Datasets
```python3
>>> from cge2.datasets.dataset_test import Check_Dataset
>>> from cge2.datasets import Dataset
>>> dataset_instance = Dataset("/home/alfred/Projects/cge_core_module2/cge2/tests/datasets/data/db_resfinder", coding=["Standard"])
>>> Check_Dataset.check_dataset(dataset_instance.fasta_files,                        coding=dataset_instance.coding_scheme)
