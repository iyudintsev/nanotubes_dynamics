from nanotubes import Nanotubes


class Model(object):
    def __init__(self, num):
        """
        Constructor
        :param num: int, number of particles in one nanotube
        """
        self.nanotubes = Nanotubes(num)

    def set_coordinates(self, coordinates):
        self.nanotubes.set_coordinates(coordinates)
