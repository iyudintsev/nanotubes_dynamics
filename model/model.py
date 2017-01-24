from nanotubes import Nanotubes
from vanderwaals import calc_vanderwaals_energy, calc_vanderwaals_forces


class Model(object):
    def __init__(self, num):
        """
        Constructor
        :param num: int, number of particles in one nanotube
        """
        self.nanotubes = Nanotubes(num)

        """ Energy """
        self.total_energy = 0
        self.bonding_energy = 0
        self.vanderwaals_energy = 0
        self.coul_energy = 0

    def set_coordinates(self, coordinates):
        self.nanotubes.set_coordinates(coordinates)

    """ Energy Calculation """

    def calc_bonding_energy(self):
        self.bonding_energy = 0
        for nanotube in self.nanotubes:
            self.bonding_energy += nanotube.calc_bonding_energy()

    def calc_vanderwaals_energy(self):
        self.vanderwaals_energy = 0
        for nanotube_i in self.nanotubes:
            for p_i in nanotube_i:
                for nanotube_j in self.nanotubes:
                    for p_j in nanotube_j:
                        self.vanderwaals_energy += calc_vanderwaals_energy(p_i, p_j)  # TODO fix duplication problem
        self.vanderwaals_energy *= .5

    """ Forces Calculation"""
    
    def calc_bonding_forces(self):
        for nanotube in self.nanotubes:
            nanotube.calc_bonding_forces()

    def calc_vanderwaals_forces(self):
        for nanotube_i in self.nanotubes:
            for p_i in nanotube_i:
                for nanotube_j in self.nanotubes:
                    for p_j in nanotube_j:
                        calc_vanderwaals_forces(p_i, p_j)  # TODO fix duplication problem

    """ Magic Methods"""

    def __repr__(self):
        counter = self.nanotubes.counter
        num = self.nanotubes.num
        return "<Model: {0} nanotubes, {1} particles>".format(counter, counter * num)
