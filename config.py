""" Configuration File """

""" File with coordinates"""
file_with_coor = "coordinates/1n20p.txt"

""" Model Parameters"""
L = 200e-7
LV = [0, L]  # border
particles_number = 20
h_max = 5e-13  # max step
h_coul = 1e-9  # coul step
time_of_calc = 2e-9
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
