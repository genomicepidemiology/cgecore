import os
import json
import itertools
from cge2.applications.KMA.kma_application import KMACommandline
from cge2.alignment.KMA.kma_alignment import KMA_alignment


class KMA_aligner:

    def __init__(self, datasets, **kwargs):
        assert datasets is not None

        self.datasets = KMA_aligner.is_list_or_strings(datasets)
        self.kma_param = {}
        self.kma_param.update((key, value) for key, value in kwargs.items())
        self.commands = []

        self.make_commands(**kwargs)
        self.results = itertools.chain()

    @staticmethod
    def is_list_or_strings(lst):
        if isinstance(lst, str):
            return [lst]
        elif bool(lst) and isinstance(lst, list) and all(isinstance(elem, str) for elem in lst):
            return lst
        else:
            raise TypeError("The datasets variable have to be a string or a"
                            "list of strings")

    def validate(self):
        if "output" not in self.kma_param:
            raise KeyError("The parameter 'output' is required for running"
                           " KMA")
        #if not os.path.isdir(self.kma_param["template_db"]):
        #    raise AttributeError("The parameter 'template_db' has to be a "
        #                         "folder, where the different datasets are.")

    def make_commands(self, **kwargs):
        self.validate()

        for dataset in self.datasets:
            template_db = None
#            if os.path.isfile(dataset):
            template_db = dataset
            dataset_name = os.path.basename(dataset)
            output_path = self.kma_param["output"] + dataset_name
#            elif os.path.isfile(self.kma_param["template_db"] + "/" + dataset):
#                template_db = self.kma_param["template_db"] + "/" + dataset
#            else:
#                raise OSError("Neither %s or %s template files exists" % (dataset, self.kma_param["template_db"] + "/" + dataset))
            command = KMACommandline(**kwargs)
            command.output = output_path
            command.template_db = template_db
            self.commands.append(command)

    def alignment_files(self, command, read_files):
        output_path = command.output
        if command.sparse is True:
            read_files = ["Sparse"]
        else:
            if command.non_consensus is True and "Consensus" in read_files:
                read_files = read_files.remove("Consensus")
            if command.no_aln is True and "Alignment" in read_files:
                read_files = read_files.remove("Alignment")
            if command.no_frag is True and "Fragments" in read_files:
                read_files = read_files.remove("Fragments")
        db_hits, meta_data = KMA_alignment(output_path=output_path,
                                           files=read_files).read()
        return db_hits

    def __call__(self,  read_files=["Result", "Consensus", "Mapstat"],
                 json_path=False):
        if not isinstance(read_files, list):
            raise TypeError("The variable 'read_files' needs to be a list")

        for run_command in self.commands:
            stdout, stderr = run_command()
            data = self.alignment_files(run_command, read_files)
            for hit in data:
                self.results = itertools.chain(self.results, hit)
            #self.results.update(data)
        if json_path:
            KMA_alignment.dump_json(json_path, self.results)
        return self.results
