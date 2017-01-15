import numpy as np


class Particle(object):
    def __init__(self, r):
        self.r = r
        self.v = np.array([0., 0., 0.])
        self.f_coul = np.array([0., 0., 0.])
        self.f_coul_corr = np.array([0., 0., 0.])
        self.f_lg = np.array([0., 0., 0.])

    def __repr__(self):
        return "<Particle {0}>".format(self.r)


class NodeParticle(object):
    def __init__(self, r):
        """
        :param r: numpy array
        :param order: int,
            0: first particle
            1: simple particle
            2: last particle
        """
        self.r = r
        self.f_bond = np.array([0, 0, 0])
        self.current_dist = np.array([0, 0])
        self.next_dist = np.array([0, 0])

    def __repr__(self):
        return "<NodeParticle {0}>".format(self.r)


class Node(object):
    def __init__(self, p0, p1, p2):
        self.particles = {0: p0, 1: p1, 2: p2}

    def __iter__(self):
        for key, p in self.particles.iteritems():
            yield p

    def __getitem__(self, index):
        return self.particles[index]
