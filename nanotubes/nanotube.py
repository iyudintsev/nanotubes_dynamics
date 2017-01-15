import numpy as np
from numpy import linalg as la
from math import sqrt
from particle import Particle, NodeParticle, Node


SQRT3_6 = sqrt(3) / 6
SQRT3_3 = SQRT3_6 * 2


class NanotubeOverflow(Exception):
    pass


class NanotubeUnfilled(Exception):
    pass


class Nanotube(object):
    def __init__(self, nan_id, total_num):
        self.nan_id = nan_id
        self.total_num = total_num
        self.num = 0
        self.particles = []
        self.nodes = []
        self.filled = False

    """ Create Particle """

    def create_particle(self, r):
        if self.num >= self.total_num:
            raise NanotubeOverflow("Nanotube {0}: total number = {1}".format(self.nan_id, self.total_num))
        self.particles.append(Particle(r))
        self.num += 1
        if self.num == self.total_num:
            self.create_nodes()
            self.filled = True

    """ Create Nodes """

    def create_node(self, index):
        r1 = self.particles[index].r
        r2 = self.particles[index+1].r
        dr = r2 - r1
        a, b, c = dr
        x0, y0, z0 = r1
        if c < 1e-16:
            c = 1e-15 if c > 0 else -1e-15
        z = z0 - (a * (1 - x0) + b * (1 - y0)) / c
        rx = np.array([1, 1, z])
        rx *= 1e-7 / la.norm(rx)
        ry = np.cross(dr, rx)
        ry *= 1e-7 / la.norm(ry)
        sign = -1 if index % 2 else 1
        node = Node(NodeParticle(r1 + sign * SQRT3_3 * rx),
                    NodeParticle(r1 + sign * (-SQRT3_6 * rx + .5 * ry)),
                    NodeParticle(r1 + sign * (-SQRT3_6 * rx - .5 * ry)), )
        self.nodes.append(node)

    def create_nodes(self):
        if not self.num == self.total_num:
            stat = self.total_num - self.num
            raise NanotubeUnfilled("Nanotube {0}: need to add {1} particles".format(self.nan_id, stat))
        for index in xrange(self.num - 1):
            self.create_node(index)
        penult_r = self.particles[self.num - 3].r
        last_r = self.particles[self.num - 1].r
        penult_node = self.nodes[self.num - 3]
        last_node = Node(*[NodeParticle(last_r + (penult_node[num].r - penult_r)) for num in xrange(3)])
        self.nodes.append(last_node)

    def __iter__(self):
        for p in self.particles:
            yield p

    def __repr__(self):
        return "<Nanotube {0}>".format(self.nan_id)
