import numpy as np
from .nanotube import Nanotube, NanotubeOverflow


class ReadCoordinatesException(Exception):
    pass


class Nanotubes(object):
    def __init__(self, num):
        """
        :param num: int, number of particles in nanotube
        """
        self.num = num
        self.counter = 0
        self.nanotubes = []

    """ Read Coordinates """

    def read_coor_from_file(self, file_name, norm=1):
        with open(file_name) as f:
            self.counter += 1
            nan = Nanotube(self.counter, self.num)
            for line in f:
                coor = self.parse_coor(line, norm)
                nan.create_particle(coor)
                if nan.filled:
                    self.nanotubes.append(nan)
                    self.counter += 1
                    nan = Nanotube(self.counter, self.num)
        if not all(map(lambda x: x.filled, self.nanotubes)):
            raise ReadCoordinatesException("Can't create nanotubes")

    @staticmethod
    def parse_coor(line, norm):
        return np.array(list(map(lambda x: norm * float(x), line.strip().split())))

    """ Magic Methods"""

    def __iter__(self):
        for nan in self.nanotubes:
            yield nan

    def __getitem__(self, index):
        return self.nanotubes[index]

    def __repr__(self):
        return "<Nanotubes: {0} nanotubes, {1} particles>".format(self.counter, self.counter * self.num)
