""" Configuration File """

""" File with coordinates"""
file_with_coor = "coordinates.txt"

""" Model Parameters"""
L = [1e-7 * x for x in [0, 200]]  # border
h_max = 5e-13  # max step
h_coul = 1e-9  # coul step
time_of_calc = 1e-7
time_of_repr = 1e-9


""" Nanotube Parameters """
k_bond = 5e3  # coefficient for bonding force and energy
mass = 20 * 12 * 1.661e-24  # node particle mass
