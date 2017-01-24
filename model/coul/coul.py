import numpy as np
from math import sqrt, pi, erfc, exp
from numpy import linalg as la


EVAL = np.array([0., 1000., 0.])  # Field
ALPHA = 5e5
ALPHA2 = ALPHA * ALPHA
ALPHA_SQRT_PI = ALPHA / sqrt(pi)
A_LG = (7.1 / 2) * 1e-8
ALPHA_CUTOFF = 1e7


def calc_coul_energy(nanotubes):
    e_self, e_real = 0, 0
    e_field = 0
    for nanotube_i in nanotubes:
        for p_i in nanotube_i:
            e_field -= p_i.q * EVAL.dot(p_i.r)
            e_self -= (ALPHA_SQRT_PI - 1. / A_LG) * p_i.q * p_i.q
            for nanotube_j in nanotubes:
                for p_j in nanotube_j:
                    dr = la.norm(p_i.r - p_j.r)
                    if dr > 0:
                        e_real += .5 * p_i.q * p_j.q * (erfc(ALPHA * dr) / dr) * (1. - exp(-ALPHA_CUTOFF * dr))
    return e_self + e_real + e_field


def calc_coul_forces(nanotubes):
    for nanotube_i in nanotubes:
        for p_i in nanotube_i:
            f_real = np.array([0., 0., 0.])
            for nanotube_j in nanotubes:
                for p_j in nanotube_j:
                    vdr = p_i.r - p_j.r
                    dr = la.norm(vdr)
                    _dr = 1. / dr
                    dr2 = dr * dr
                    _dr2 = _dr * _dr
                    if dr > 0:
                        f_real += vdr * p_j.q * _dr2 * \
                                  (erfc(ALPHA * dr) * _dr + 2 * ALPHA_SQRT_PI * exp(-ALPHA2 * dr2)) * \
                                  (1 - exp(-ALPHA_CUTOFF * dr)) + \
                                  vdr * p_j.q * (erfc(ALPHA * dr) * _dr2) * \
                                  (-ALPHA_CUTOFF * exp(-ALPHA_CUTOFF * dr))
            f_real *= p_i.q
            f_field = p_i.q * EVAL
            p_i.f_coul = f_real + + p_i.f_coul_corr + f_field


def calc_potential(nanotubes):
    n = nanotubes.particle_num
    pm = np.zeros(shape=(n, n))
    for nanotube_i in nanotubes:
        for p_i in nanotube_i:
            for nanotube_j in nanotubes:
                for p_j in nanotube_j:
                    if p_i.id == p_j.id:
                        pm[p_i.id][p_i.id] = -2. * ALPHA_SQRT_PI + 2. / A_LG
                    vdr = p_i.r - p_j.r
                    dr = la.norm(vdr)
                    if dr > 0:
                        pm[p_i.id][p_j.id] = (erfc(ALPHA * dr) / dr) * (1. - exp(-ALPHA_CUTOFF * dr))
