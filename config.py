""" Configuration File """

""" File with coordinates"""
file_with_coor = "coordinates/coordinates.txt"

""" Model Parameters"""
L = 200e-7
LV = [75e-7, 105e-7]  # border
particles_number = 100
h_max = 5e-13  # max step
h_coul = 1e-9  # coul step
time_of_calc = 1e-7
dump_file = "result.txt"  # coordinates during calculation

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
