from nanotube import Nanotube


class Nanotubes(object):
    def __init__(self, num):
        """
        Constructor
        :param num: int, number of particles in one nanotube
        """
        self.num = num
        self.counter = 0
        self.nanotubes = []

    """ Set Coordinates """

    def set_coordinates(self, coordinates):
        self.counter += 1
        nan = Nanotube(self.counter, self.num)
        for coor in coordinates:
            nan.create_particle(coor)
            if nan.filled:
                self.nanotubes.append(nan)
                self.counter += 1
                nan = Nanotube(self.counter, self.num)
        if not all(map(lambda x: x.filled, self.nanotubes)):
            raise SetCoorException("Can't create model")

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
