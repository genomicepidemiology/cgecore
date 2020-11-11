import os
import warnings


def warning_on_one_line(message, category, filename, lineno, file=None,
                        line=None):
    return ' %s: %s:\t%s\n' % (filename, category.__name__, message)


class Dataset:

    # The list of start/stop codons.
    # TODO: Should be updated.
    # TODO: Should it be here?

    codons = {
            "Standard": {"Start": [b"ATG"], "Stop": [b"TAG", b"TAA", b"TGA"]},
            "Mithocondrial": {"Start": [b"ATA", b"ATT"],
                              "Stop": [b"AGA", b"AGG"]},
            "Prokaryotes": {"Start": [b"GTG", b"TTG"], "Stop": []},
            "E.coli": {"Start": [b"AUG", b"GUG", b"UUG"], "Stop": []},
             }

    def __init__(self, location, coding=False, name=None):
        """This should build an object of the database. Should not store the
        sequences because that could take too much memory. However, maybe it
        should store the name, the location, the fasta files, the config files
        (TODO), the phenotypes files (TODO), etc."""

        location = os.path.abspath(location)
        if not os.path.isdir(location):
            raise IOError("Location %s of the dataset is not a folder.")
        self.location = location
        if name is None:
            name = os.path.basename(location)
        self.name = name

        if coding is False:
            self.coding_scheme = False
        else:
            self.coding_scheme = self.determine_coding(coding)
        self.get_fasta_files(location)
        warnings.formatwarning = warning_on_one_line

    def get_fasta_files(self, location):
        """Function to get all fasta files in the directory. Notice that it
        does not matter if it is in the directory or in the subdirectories."""

        fasta_extensions = [".fsa", ".fa", ".fna", ".fasta"]
        self.fasta_files = []
        for root, dirs, files in os.walk(location):
            for file in files:
                if os.path.splitext(file)[1] in fasta_extensions:
                    self.fasta_files.append(root+"/"+file)

    def determine_coding(self, coding):
        """Determine the coding scheme for the fasta files of the database"""

        coding_scheme = {"Start": [], "Stop": []}
        if isinstance(coding, list):
            for code_string in coding:
                if isinstance(code_string, str):
                    if code_string not in Dataset.codons:
                        raise KeyError("The code scheme %s is not in the "
                                       "standard codon schemes" % code_string)
                    else:
                        coding_scheme["Start"].extend(
                                        Dataset.codons[code_string]["Start"])
                        coding_scheme["Stop"].extend(
                                        Dataset.codons[code_string]["Stop"])
                elif isinstance(code_string, dict):
                    coding_scheme["Start"].extend(code_string["Start"])
                    coding_scheme["Stop"].extend(code_string["Stop"])
                else:
                    raise TypeError("The format of the coding dict is not "
                                    "valid")
        elif isinstance(coding, dict):
            coding_scheme["Start"].extend(coding["Start"])
            coding_scheme["Stop"].extend(coding["Stop"])
        else:
            raise TypeError("The coding variable has to be a list of strings"
                            " or dict")
        return coding_scheme
