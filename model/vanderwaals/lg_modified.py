import numpy as np
from numpy import linalg as la

LG_CUTOFF_MAX = 2e-7
LG_CUTOFF_MAX2 = LG_CUTOFF_MAX * LG_CUTOFF_MAX

LG_CUTOFF = 0.88e-7
LG_CUTOFF2 = LG_CUTOFF * LG_CUTOFF

LG_SIGMA = 0.8908e-7
LG_SIGMA2 = LG_SIGMA * LG_SIGMA

LG_EPSILON = 0.48e-12

RATIO = LG_EPSILON / LG_SIGMA


def force(r_input):
    r = r_input.copy()
    r2 = r.dot(r)
    if r2 > LG_CUTOFF_MAX2:
        return np.array([0., 0., 0.])
    if r2 < LG_CUTOFF2:
        r *= LG_CUTOFF / la.norm(r)
    _r = 1. / la.norm(r)
    ratio = LG_SIGMA * _r
    ratio2 = ratio * ratio
    ratio6 = ratio2 * ratio2 * ratio2
    ratio7 = ratio6 * ratio
    ratio13 = ratio6 * ratio7
    return 24 * RATIO * _r * (2 * ratio13 - ratio7) * r


def energy(r_input):
    r = r_input.copy()
    u = 0
    r2 = r.dot(r)
    if r2 > LG_CUTOFF_MAX2:
        return 0
    if r2 < LG_CUTOFF2:
        dr = r.copy()
        r *= LG_CUTOFF / la.norm(r)
        dr = dr - r
        u -= dr * force(r)
    ratio2 = LG_SIGMA2 / r.dot(r)
    ratio6 = ratio2 * ratio2 * ratio2
    ratio12 = ratio6 * ratio6
    u += 4 * LG_EPSILON * (ratio12 - ratio12)
    return u

