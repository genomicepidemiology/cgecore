# Alignment sub module documentation

Submodule dedicated to align sequences. It contains the classes for reading the files produced by the two main aligners (BLASTN and KMA). It also has the wrappers that run the aligners and read the files.

## Actual folder

Contains objects shared by KMA and Blast aligners classes

### file.py

Contains objects that encapsulates metadata about any file.

### Hit.py

Contains the objects Hit, BlastHit and KMAHit. They are modified dictionaries that have the information extracted from the alignment files. It is what is returned from the iterators.

### translate_hits.py

Contains the code for translating the information in the alignment files to the Hits objects

##KMA

Contains the iterators to read the KMA alignment files and return KMAHit objects. Also wrappers for running KMA and reading the results

### alignment_files.py

Contains an iterator for each file that can be created by KMA when aligning

### read_files.py

Contains the classes to read the files produced by a KMA alignment. It contains the classes that define the files produced by an alignment (KMA_ResultFile and KMA_alignment), and the iterator that can merge the information from different KMA produced files (Iterate_KMAFiles), and the iterator can join iterators from the aligning to different fasta files (Iterator_KMAAlignment).

### run_kma.py

Contains wrapper to run KMA and return an iterator of Hits.
