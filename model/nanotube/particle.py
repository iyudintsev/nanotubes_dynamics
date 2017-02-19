import numpy as np


class Particle(object):
    def __init__(self, r, particle_id):
        self.id = particle_id
        self.r = r
        self.f_coul = np.array([0., 0., 0.])
        self.f_coul_corr = np.array([0., 0., 0.])
        self.f_lg = np.array([0., 0., 0.])

    @property
    def f(self):
        return self.f_coul + self.f_lg

    def __repr__(self):
        return "<Particle {0}>".format(self.r)


class NodeParticle(object):
    def __init__(self, r):
        """
        :param r: numpy array
        """
        self.r = r
        self.v = np.array([0., 0., 0.])
        self.q = 0
        self.f = np.array([0., 0., 0.])
        self.f_bond = np.array([0., 0., 0.])
        self.current_dist = [0., 0.]
        self.next_dist = [0., 0.]

    def __repr__(self):
        return "<NodeParticle {0}>".format(self.r)


class Node(object):
    def __init__(self, p0, p1, p2):
        self.particles = {0: p0, 1: p1, 2: p2}

    def __iter__(self):
        for index in xrange(3):
            yield self.particles[index]

    def __getitem__(self, index):
        return self.particles[index]
