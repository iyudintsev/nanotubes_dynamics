import numpy as np


class Particle(object):
    def __init__(self, r, particle_id):
        self.id = particle_id
        self.r = r
        self.f_coul = np.zeros(shape=3)
        self.f_coul_corr = np.zeros(shape=3)
        self.f_lg = np.zeros(shape=3)

    @property
    def f(self):
        return self.f_coul + self.f_lg

    def __repr__(self):
        return "<Particle {0}>".format(self.r)


class NodeParticle(object):
    def __init__(self, r):
        self.r = r
        self.v = np.zeros(shape=3)
        self.q = 0
        self.f = np.zeros(shape=3)
        self.f_bond = np.zeros(shape=3)
        self.distances = []
        self.neighbors = []

    def __repr__(self):
        return "<NodeParticle {0}>".format(self.r)


class Node(object):
    id = 0

    def __init__(self, coor):
        self.id = Node.id
        self.particles = [NodeParticle(coor[i]) for i in xrange(3)]
        Node.id += 1

    def __iter__(self):
        for index in xrange(3):
            yield self.particles[index]

    def __getitem__(self, index):
        return self.particles[index]


class Neighbor(object):
    def __init__(self, node_id, index):
        self.node_id = node_id
        self.index = index

    def __repr__(self):
        return "<Neighbor: node {0}| index {1}>".format(self.node_id, self.index)

