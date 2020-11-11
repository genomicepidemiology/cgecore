import os
import warnings


class Check_Dataset:

    @staticmethod
    def check_dataset(folder, coding=False):
        """Function to iterate over a list of fasta files and check that they
        follow the standard format"""

        for file in folder:
            Check_Dataset.check_file(file, coding=coding)

    @staticmethod
    def check_file(file, coding):
        """Check that the fasta file follows the standard format. The Standard
        format follows:
            -> Header of sequences: no empty spaces.
            -> End of lines: '\n'
            -> Length of sequence lines: 60
        It raises warnings if:
            -> The start/stop codon of the sequence are not the ones required
        """

        outfile = os.path.splitext(file)[0]+"_tmp"+os.path.splitext(file)[1]
        if not os.path.isfile(file):
            raise IOError("The file %s is not a valid file" % file)
        if os.path.splitext(file)[1] not in [".fsa", ".fa", ".fna",
                                             ".fasta"]:
            raise TypeError("The FASTA file %s has a not valid extension. It "
                            "should be .fsa, .fa, .fna or .fasta")
        with open(file, 'rb') as infile:
            with open(outfile, 'wb') as out:
                gene_seq = []
                header = b""
                for line in infile:
                    line = Check_Dataset.check_whitespace(line)
                    line = Check_Dataset.check_crlf(line)
                    if line.startswith(b">"):
                        if gene_seq:
                            gene_str = b"".join(gene_seq)
                            if coding is not False:
                                Check_Dataset.startend_codon(header, gene_str,
                                                             coding)
                            lines = Check_Dataset.split_lines(gene_str)
                            out.write(lines)
                        header = line
                        out.write(header)
                        gene_seq = []
                    else:
                        if gene_seq and coding is not False:
                            Check_Dataset.startend_codon(header, gene_seq[0],
                                                         coding)
                        gene_seq.append(line.rstrip())
                if not gene_seq and coding is not False:
                    Check_Dataset.startend_codon(header, gene_seq[0], coding)
                gene_str = b"".join(gene_seq)
                lines = Check_Dataset.split_lines(gene_str)
                out.write(lines)
        os.rename(outfile, file)

    @staticmethod
    def startend_codon(header, gene_seq, coding):
        """Check if the start/stop codon is not the one that is required"""

        if (len(coding["Start"]) > 0
                and gene_seq[:3].upper() not in coding["Start"]):
            list_coding_start = b", ".join(coding["Start"])
            warnings.warn("The gene %s start with %s, instead of a valud "
                          "start codon (%s)" % (header[1:].rstrip(),
                                                gene_seq[:3],
                                                str(list_coding_start)))
        if (len(coding["Stop"]) > 0
                and gene_seq.rstrip(b"\n")[-3:].upper() not in coding["Stop"]):
            warnings.warn("The gene %s ends with %s, instead of a valud ends "
                          "codon (%s)" % (header[1:].rstrip(),
                                          gene_seq.rstrip(b"\n")[-3:],
                                          b", ".join(coding["Stop"])))

    @staticmethod
    def check_crlf(line):
        """Check that the end of the line follows always the UNIX newline
        ('\n')"""

        UNIX_NEWLINE = b"\n"
        WINDOWS_NEWLINE = b"\r\n"
        MAC_NEWLINE = b"\r"
        if WINDOWS_NEWLINE in line:
            line = line.replace(WINDOWS_NEWLINE, UNIX_NEWLINE)
        elif MAC_NEWLINE in line:
            line = line.replace(MAC_NEWLINE, UNIX_NEWLINE)
        return line

    @staticmethod
    def split_lines(line, every=60):
        """Split lines every n characters"""

        line = line.replace(b'\r', b'').replace(b'\n', b'')
        lines = []
        for i in range(0, len(line), every):
            lines.append(line[i:i+every])
        string_lines = b'\n'.join(lines)
        return string_lines+b'\n'

    @staticmethod
    def check_whitespace(line):
        """Check that there is no whitespace in the sequences"""

        if b' ' in line:
            line = line.replace(b" ", b"")
        return line

    @staticmethod
    def check_header(header, repair=False):
        """Check that there is no whitespace in the header (substitute by '-')
        """
        if b' ' in header:
            header = header.replace(b" ", b"-")
        return header
