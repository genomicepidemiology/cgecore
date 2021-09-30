# Created by Alfred Ferrer Florensa
"""Contains objects for reading """

from cge2.alignment.file import _File, _ResultFile
import cge2.alignment.KMA.alignment_files as alignment_files
from cge2.alignment.Hit import KMAHit


class KMA_alignment:

    def __init__(self, output_path, filename, files):
        self.output_path = output_path

        self.KMA_FILES = {
            "Result":
            _ResultFile("Result", output_path, extension=".res",
                        read_method=alignment_files.Iterator_ResFile),
            "Fragments":
            _ResultFile("Fragments", output_path, extension=".frag.gz",
                        read_method=alignment_files.Iterator_FragmentFile),
            "Consensus":
            _ResultFile("Consensus", output_path, extension=".fsa",
                        read_method=alignment_files.Iterator_ConsensusFile),
            "Alignment":
            _ResultFile("Alignment", output_path, extension=".aln",
                        read_method=alignment_files.Iterator_AlignmentFile),
            "Matrix":
            _ResultFile("Matrix", output_path, extension=".mat.gz",
                        read_method=alignment_files.Iterator_MatrixFile),
            "Mapstat":
            _ResultFile("Mapstat", output_path, extension=".mapstat",
                        read_method=alignment_files.Iterator_MapstatFile),
            "Frag_Raw":
            _ResultFile("Frag_Raw", output_path, extension=".frag_raw.gz",
                        read_method=None),
            "VCF":
            _ResultFile("VCF", output_path, extension=".vcf.gz",
                        read_method=alignment_files.Iterator_VCFFile),
            "Sparse":
            _ResultFile("Sparse", output_path, extension=".spa",
                        read_method=alignment_files.Iterator_SPAFile),
                            }
        if not isinstance(files, list):
            files = [files]
        self.list_files = []
        self._init_files(files)

    def _init_files(self, files):
        len_f = len(files)
        for n_f in range(len_f):
            self.__setitem__(n_f, files[n_f])

    def __len__(self):
        return(len(self.list_files))

    def _check_Sparse(self):
        if "Sparse" in self.list_files and self.__len__() > 1:
            raise IndexError("File 'Sparse' is a unique result file. It "
                             "cannot be read with other files")

    def __setitem__(self, index, value):
        if value in self.KMA_FILES:
            file_result = self.KMA_FILES[value]
        else:
            raise IndexError("Name file '%s' not part of the KMA "
                             "Alignment: %" % (value,
                                               ", ".join(self.KMA_FILES.keys())
                                               ))
        if index == self.__len__():
            self.list_files.append(file_result)
        elif index < self.__len__():
            self.list_files[index] = file_result
        else:
            raise IndexError("list assignment index out of range")
        self._check_Sparse()

    def __getitem__(self, index):
        return(self.list_files[index])

    def __str__(self):
        str_lst = []
        for file in self.list_files:
            str_lst.append(str(file))
        return ", ".join(str_lst)

    def __repr__(self):
        repr_lst = []
        for file in self.list_files:
            repr_lst.append("%s=%s" % (file.name, file.file_path))

        return "KMA_alignment(" + ", ".join(repr_lst) + ")"


class Iterator_KMAFiles:

    def __init__(self, output_path, filename, files):

        KMAfiles = KMA_alignment(output_path, filename, files)
        self.files_kma = files
        self.iter_KMAFiles = {}
        for files in KMAfiles:
            self.iter_KMAFiles[files.name] = files.read()

    def __iter__(self):

        return self

    def __next__(self):
        iter_true = True
        hit = KMAHit()
        while iter_true:
            for kma_file in self.files_kma:
                entry = next(self.iter_KMAFiles[kma_file])
                hit.merge(entry)
            iter_true = False
        return hit


class Iterator_AlignmentKMA:

    def __init__(self, output_path, template_files, output_files):
        self.output_path = output_path
        self.beginnig = True
        self.output_files = output_files
        self.template_files = template_files
        self.aln_pos = 0
        self.iter_dataset = None
        print(self.output_files, self.output_files[self.aln_pos])

    def __iter__(self):

        return self

    def __next__(self):
        hit_template = None
        if self.iter_dataset is None:
            self.iter_dataset = Iterator_KMAFiles(output_path=self.output_path,
                                                  filename=str(self.output_files[self.aln_pos]),
                                                  files=self.template_files)
        while hit_template is None:
            try:
                hit_template = next(self.iter_dataset)
            except StopIteration:
                self.aln_pos += 1
                self.iter_dataset = Iterator_KMAFiles(output_path=self.output_path,
                                                      filename=self.output_files[self.aln_pos],
                                                      files=self.template_files)

        return hit_template
