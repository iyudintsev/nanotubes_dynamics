from nanotube import Nanotube
from copy import copy


class Nanotubes(object):
    def __init__(self, num):
        """
        Constructor
        :param num: int, number of particles in one nanotube
        """
        self.num = num
        self.counter = 0
        self.nanotubes = []
        self.particle_num = None

    def get_node_particles(self):
        for nan in self.nanotubes:
            for node in nan.nodes:
                for p in node:
                    yield p

    """ Set Coordinates """

    def set_coordinates(self, coordinates):
        c = 0
        nanotube = Nanotube()
        for r in coordinates:
            nanotube.create_particle(r)
            c += 1
            if c == self.num:
                nanotube.create_all_nodes()
                self.nanotubes.append(copy(nanotube))
                nanotube = Nanotube()
                self.counter += 1
                c = 0
        self.particle_num = self.counter * self.num

    """ Magic Methods"""

    def __iter__(self):
        for nan in self.nanotubes:
            yield nan

    def __getitem__(self, index):
        return self.nanotubes[index]

    def __repr__(self):
        return "<Nanotubes: {0} items, {1} particles>".format(self.counter, self.counter * self.num)


class SetCoorException(Exception):
    pass
