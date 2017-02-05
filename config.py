""" Configuration File """

""" File with coordinates"""
file_with_coor = "coordinates.txt"

""" Model Parameters"""
L_VAL = 200e-7
L = [x for x in [0, L_VAL]]  # border
h_max = 5e-13  # max step
h_coul = 1e-9  # coul step
time_of_calc = 1e-7
time_of_repr = 1e-9

""" FIRE Parameters"""
fire_n_min = 5
fire_alpha0 = 0.1
fire_f_inc = 1.1
fire_f_dec = 0.5
fire_f_alpha = 0.99
max_step_lim = 3e-10

""" Nanotube Parameters """
k_bond = 5e3  # coefficient for bonding force and energy
mass = 20 * 12 * 1.661e-24  # node particle mass
