from nanotubes import Nanotubes
from vanderwaals import calc_vanderwaals_energy, calc_vanderwaals_forces
from coul import ChargeCalc, calc_coul_energy, calc_coul_forces, check_coul_condition
from config import h_max, h_coul, time_of_calc, time_of_repr


class Model(object):
    def __init__(self, num):
        """
        Constructor
        :param num: int, number of particles in one nanotube
        """
        self.nanotubes = Nanotubes(num)
        check_coul_condition()
        self.charge_calc = ChargeCalc(self.nanotubes)
        self.h = h_max  # current step
        self.t = 0  # current time
        self.t_coul = h_coul  # control process charge calc
        self.t_repr = time_of_repr  # control of repr
        self.repr_now = False

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

    def calc_coul_energy(self):
        self.coul_energy = calc_coul_energy(self.nanotubes)

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

    def calc_coul_forces(self):
        calc_coul_forces(self.nanotubes)

    """ Process of Calculation """

    def calc(self):
        while self.t < time_of_calc:
            if self.t_coul >= h_coul:
                self.t_coul -= h_coul
                self.charge_calc.run()
                self.calc_coul_forces()
            self.t_coul += self.h

            self.calc_vanderwaals_forces()
            max_step = 0
            for nan in self.nanotubes:
                max_step = nan.step(self.h, max_step)
            # FIRE
            
    """ Magic Methods"""

    def __repr__(self):
        counter = self.nanotubes.counter
        num = self.nanotubes.num
        return "<Model: {0} nanotubes, {1} particles>".format(counter, counter * num)
