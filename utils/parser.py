import numpy as np


class Parser(object):
    def __init__(self, file_name, norm=1):
        self.file_name = file_name
        self.norm = norm

    def parse(self, line):
        return np.array(list(map(lambda x: self.norm * float(x), line.strip().split())))

    @property
    def coordinates(self):
        with open(self.file_name) as f:
            for line in f:
                yield self.parse(line)
