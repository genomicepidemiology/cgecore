###Testing of BLASTNCommandLineBase
```python3
>>> from blast.blast_application import BlastNCommandline
>>> blastnline = BlastNCommandline(subject="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/aminoglycoside.fsa", query="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/44571.fna", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino5.xml", outfmt=5, perc_identity=0.9, max_target_seqs=50000, dust="no")
>>> blastnline.path_exec = "/home/alfred/bio_tools/ncbi-blast-2.8.1+/bin/"
>>> std_output, err_output = blastnline()
>>> blastnline = BlastNCommandline(subject="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/aminoglycoside.fsa", query="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/44571.fna", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino6.tab", outfmt="'6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore'", perc_identity=0.9, max_target_seqs=50000, dust="no")
>>> blastnline.path_exec = "/home/alfred/bio_tools/ncbi-blast-2.8.1+/bin/"
>>> std_output, err_output = blastnline()
>>> blastnline = BlastNCommandline(subject="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/aminoglycoside.fsa", query="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/44571.fna", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino7.tab", outfmt=7, perc_identity=0.9, max_target_seqs=50000, dust="no")
>>> blastnline.path_exec = "/home/alfred/bio_tools/ncbi-blast-2.8.1+/bin/"
>>> std_output, err_output = blastnline()
>>> blastnline = BlastNCommandline(subject="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/aminoglycoside.fsa", query="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/44571.fna", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino10.tab", outfmt=10, perc_identity=0.9, max_target_seqs=50000, dust="no")
>>> blastnline.path_exec = "/home/alfred/bio_tools/ncbi-blast-2.8.1+/bin/"
>>> std_output, err_output = blastnline()
>>> blastnline = BlastNCommandline(subject="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/aminoglycoside.fsa", query="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/44571.fna", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino6_full.tab", outfmt="'6 qseqid qgi qacc sseqid sallseqid sgi sallgi sacc sallacc qstart qend sstart send qseq sseq evalue bitscore score length pident nident mismatch positive gapopen gaps ppos frames qframe sframe btop staxids sscinames scomnames sblastnames sskingdoms stitle salltitles sstrand qcovs qcovhsp qcovus'", perc_identity=0.9, max_target_seqs=50000, dust="no")
>>> blastnline.path_exec = "/home/alfred/bio_tools/ncbi-blast-2.8.1+/bin/"
>>> std_output, err_output = blastnline()
>>> blastnline = BlastNCommandline(subject="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/beta-lactam.fsa", query="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/44571.fna", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino5.xml", outfmt=5, perc_identity=0.9, max_target_seqs=50000, dust="no")
>>> blastnline.path_exec = "/home/alfred/bio_tools/ncbi-blast-2.8.1+/bin/"
>>> std_output, err_output = blastnline()
>>> blastnline = BlastNCommandline(subject="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/beta-lactam.fsa", query="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/44571.fna", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino6.tab", outfmt="'6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore'", perc_identity=0.9, max_target_seqs=50000, dust="no")
>>> blastnline.path_exec = "/home/alfred/bio_tools/ncbi-blast-2.8.1+/bin/"
>>> std_output, err_output = blastnline()
>>> blastnline = BlastNCommandline(subject="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/beta-lactam.fsa", query="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/44571.fna", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino7.tab", outfmt=7, perc_identity=0.9, max_target_seqs=50000, dust="no")
>>> blastnline.path_exec = "/home/alfred/bio_tools/ncbi-blast-2.8.1+/bin/"
>>> std_output, err_output = blastnline()
>>> blastnline = BlastNCommandline(subject="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/beta-lactam.fsa", query="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/44571.fna", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino10.tab", outfmt=10, perc_identity=0.9, max_target_seqs=50000, dust="no")
>>> blastnline.path_exec = "/home/alfred/bio_tools/ncbi-blast-2.8.1+/bin/"
>>> std_output, err_output = blastnline()
>>> blastnline = BlastNCommandline(subject="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/beta-lactam.fsa", query="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/data/data2/44571.fna", output="/home/alfred/Projects/cge_core_module2/cge2/tests/applications/output/outputblastamino6_full.tab", outfmt="'6 qseqid qgi qacc sseqid sallseqid sgi sallgi sacc sallacc qstart qend sstart send qseq sseq evalue bitscore score length pident nident mismatch positive gapopen gaps ppos frames qframe sframe btop staxids sscinames scomnames sblastnames sskingdoms stitle salltitles sstrand qcovs qcovhsp qcovus'", perc_identity=0.9, max_target_seqs=50000, dust="no")
>>> blastnline.path_exec = "/home/alfred/bio_tools/ncbi-blast-2.8.1+/bin/"
>>> std_output, err_output = blastnline()
