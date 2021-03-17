# Created by Alfred Ferrer Florensa
"""Contains objects to contain the results of an alignment"""

import os
import sys


class Feature_hit:

    def __init__(self, feature, value, description=None, alt_name=None):

        self.feature = feature
        self.value = value
        self.description = description
        self.alt_name = alt_name

    def __str__(self):
        return "%s" % (self.feature)

    def __repr__(self):
        return "%s(value: %s, description: %s, alternative_name: %s)" % (
                self.feature, self.value, self.description, self.alt_name)


class _Hit_Base(dict):

    def __init__(self):

        self["queryID"] = Feature_hit(
                            names=["queryID", "Query Sequence ID"],
                            description="",
                                  )
        self["templateID"] = Feature_hit(
                                names=["templateID", "Template SeqID"],
                                description="",
                                )
        self["identity"] = Feature_hit(
                                names=["identity", "Identity Percentage"],
                                description="",
                                )

class Hit_KMARes(_Hit_Base):

    def __init__(self):
        pass

class Hit_BlastXML(dict):
    """TODO: We need also to extract information about the BlastOutput section"""

    def __init__(self, record_hit):

        self.software = "BLASTN"
        self.format = "XML"
        _Hit_Base.__init__(self)

        if record_hit is not None:
            for key, value in record_hit.items():
                hit_name = Feature_hit.XML_DICT[key]
                self[hit_name] = value

    def __setitem__(self, key, val):
        try:
            new_key = Feature_hit.XML_DICT[key]
        except KeyError:
            new_key = key
        dict.__setitem__(self, new_key, val)


class Hit_KMARes(_Hit_Base):

    def __init__(self):
        pass


class Hit_KMA(_Hit_Base):

    def __init__(self):

        _Hit_Base.__init__()


class Hit_BlastTAB(dict):

    def __init__(self, record_hit):

        self.software = "BLASTN"
        self.format = "TSV/CSV"
        _Hit_Base.__init__(self)

        if record_hit is not None:
            for key, value in record_hit.items():
                hit_name = Feature_hit.BLAST_DICT[key]
                self[hit_name] = value

    def __setitem__(self, key, val):
        try:
            new_key = Feature_hit.BLAST_DICT[key]
        except KeyError:
            new_key = key
        dict.__setitem__(self, new_key, val)


class Hit_Alignment(dict):

    def __init__(self, software=None, data=None, empty=False, file=None):

        self._format_check(software, data, empty, file)
        self.software = software
        if empty:
            self.empty = True
        else:
            self.empty = False
        if software == "blast":
            Hit_BlastXML.__init__(self, data)
        elif software == "kma":
            Hit_KMA.__init__(self, data)
        elif software == "blast":
            Hit_BlastTAB.__init__(self, data)
        elif software == "blank":
            _Hit_Base.__init__(self)
            self.format = "blank"
        else:
            raise ValueError("The hit has to be of the file format: %s" %
                             (", ".join(["blast_xml", "kma", "blast_tab",
                                         "blank"])))

    def _format_check(self, software, data, empty, file):

        if not isinstance(software, str) and format is not None:
            raise TypeError("The variable 'aligner' has to be a string chosen"
                            " between 'blast_xml', 'kma' or 'blast_tab'")

        if not isinstance(data, dict) and data is not None:
            raise TypeError("Data has to be in a dictionary format")

        if not isinstance(empty, bool):
            raise TypeError("Empty variable is not a boolean")

    def __setitem__(self, key, val):
        if self.format == "blank":
            dict.__setitem__(self, key, val)
        elif self.format == "TSV/CSV":
            Hit_BlastTAB.__setitem__(self, key, val)
        elif self.format == "KMA":
            Hit_KMA.__setitem__(self, key, val)
        elif self.format == "XML":
            Hit_BlastXML.__setitem__(self, key, val)
        else:
            raise ValueError("The hit has to be extracted from the files: %s" %
                             (", ".join(["blast_xml", "kma", "blast_tab",
                                         "blank"])))
