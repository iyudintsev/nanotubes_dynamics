from math import sqrt, pi, erfc, exp
from numpy import linalg as la

ALPHA = 5e5
ALPHA2 = ALPHA * ALPHA
ALPHA_SQRT_PI = ALPHA / sqrt(pi)
A_LG = (7.1 / 2) * 1e-8
ALPHA_CUTOFF = 1e7


def calc_coul_energy(nanotubes):
    e_self, e_real = 0, 0, 0
    for nanotube_i in nanotubes:
        for p_i in nanotube_i:
            e_self -= (ALPHA_SQRT_PI - 1. / A_LG) * p_i.q * p_i.q
            for nanotube_j in nanotubes:
                for p_j in nanotube_j:
                    dr = la.norm(p_i.r - p_j.r)
                    if dr > 0:
                        e_real += .5 * p_i.q * p_j.q * (erfc(ALPHA * dr) / dr) * (1. - exp(-ALPHA_CUTOFF * dr))
    return e_self + e_real

