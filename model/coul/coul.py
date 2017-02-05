import numpy as np
from math import sqrt, pi, erfc, exp, log
from numpy import linalg as la
from config import L
from model.coul.error import EwaldConditionError

EVAL = np.array([1000., 0., 0.])  # Field
ALPHA = .5e5
ALPHA2 = ALPHA * ALPHA
ALPHA_SQRT_PI = ALPHA / sqrt(pi)
A_LG = (7.1 / 2) * 1e-8
ALPHA_CUTOFF = 1e7


def check_coul_condition():
    e = 1e-4
    coefficient = int((ALPHA * L / pi) * sqrt(-log(e)))
    if coefficient > 0:
        print coefficient
        raise EwaldConditionError()


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


class ChargeCalc(object):
    def __init__(self, nanotubes):

        self.nanotubes = nanotubes
        self.n = nanotubes.particle_num
        self.pm = None
        self.am = None
        self.ev = None

    def calc_potential(self):
        self.pm = np.zeros(shape=(self.n, self.n))
        for nanotube_i in self.nanotubes:
            for p_i in nanotube_i:
                for nanotube_j in self.nanotubes:
                    for p_j in nanotube_j:
                        if p_i.id == p_j.id:
                            self.pm[p_i.id][p_i.id] = -2. * ALPHA_SQRT_PI + 2. / A_LG
                        vdr = p_i.r - p_j.r
                        dr = la.norm(vdr)
                        if dr > 0:
                            self.pm[p_i.id][p_j.id] = (erfc(ALPHA * dr) / dr) * (1. - exp(-ALPHA_CUTOFF * dr))

    def calc_diff_matrix(self):
        self.ev = np.array([0. for _ in xrange(self.n)])
        for nanotube_i in self.nanotubes:
            p_last = nanotube_i[-1]
            for p_i in nanotube_i[:-1]:
                self.ev[p_i.id] = np.dot(EVAL, p_i.r - p_last.r)

        self.am = np.zeros(shape=(self.n, self.n))
        for nanotube_i in self.nanotubes:
            n_last = nanotube_i[-1].id
            for i in xrange(nanotube_i[0].id, n_last):
                for j in xrange(self.n):
                    self.am[i][j] = self.pm[i][j] - self.pm[i][n_last]
                self.am[i][n_last] = 1e6

    def run(self):
        self.calc_potential()
        self.calc_diff_matrix()
        _am = la.inv(self.am)
        qv = _am.dot(self.ev)
        for nanotube_i in self.nanotubes:
            for p_i in nanotube_i:
                p_i.q = qv[p_i.id]
