import numpy as np
from .nanotube import Nanotube, NanotubeOverflow


class ReadCoordinatesException(Exception):
    pass


class Nanotubes(object):
    def __init__(self, num, file_name=None):
        """
        :param num: int, number of particles in nanotube
        """
        self.num = num
        self.counter = 0
        self.nanotubes = []
        if file_name:
            self.read_coor_from_file(file_name)

    """ Read Coordinates """

    def read_coor_from_file(self, file_name):
        with open(file_name) as f:
            self.counter += 1
            nan = Nanotube(self.counter, self.num)
            for line in f:
                coor = self.parse_coor(line)
                nan.create_particle(coor)
                if nan.filled:
                    self.nanotubes.append(nan)
                    self.counter += 1
                    nan = Nanotube(self.counter, self.num)
        if not all(map(lambda x: x.filled, self.nanotubes)):
            raise ReadCoordinatesException("Can't create nanotubes")

    @staticmethod
    def parse_coor(line):
        return np.array(list(map(lambda x: 1e-7 * float(x), line.strip().split())))  # hack, 1e-7

    """ Magic Methods"""

    def __iter__(self):
        for nan in self.nanotubes:
            yield nan

    def __getitem__(self, index):
        return self.nanotubes[index]

    def __repr__(self):
        return "<Nanotubes: {0} nanotubes, {1} particles>".format(self.counter, self.counter * self.num)
