import numpy as np
from numpy import linalg as la
from .particle import Particle, Node, Neighbor
from .bonding import force, energy
from config import mass

coeff1_3 = 1. / 3


class Nanotube(object):
    nanotube_id = 0

    def __init__(self):
        self.id = Nanotube.nanotube_id
        self.n = 0
        self.particles = []
        self.nodes = []
        self.energy = 0
        self._m = 1. / mass
        Nanotube.nanotube_id += 1

    def create_particle(self, r):
        p = Particle(r, self.n)
        self.particles.append(p)
        self.n += 1

    def create_one_node(self, i):
        r1 = self.particles[i].r
        r2 = self.particles[i + 1].r
        dr = r2 - r1
        a, b, c = dr
        x0, y0, z0 = r1

        if c < 1e-16:
            c = 1e-15 if c > 0 else -1e15
        z = z0 - (a * (1 - x0) + b * (1 - y0)) / c

        rx = np.array([1., 1., z])
        rx *= 1e-7 / la.norm(rx)

        ry = np.cross(dr, rx)
        ry *= 1e-7 / la.norm(ry)

        sign = -1 if i % 2 else 1
        node = Node([r1 + sign * (np.sqrt(3) / 3) * rx,
                     r1 + sign * ((-np.sqrt(3) / 6) * rx + .5 * ry),
                     r1 + sign * ((-np.sqrt(3) / 6) * rx - .5 * ry), ])
        self.nodes.append(node)

    @staticmethod
    def get_index(i):
        if i == 0:
            return 1, 2
        if i == 1:
            return 2, 0
        if i == 2:
            return 0, 1

    def add_neighbors(self, current_node, nodes):
        for j in xrange(3):
            p = current_node[j]
            for node in nodes:
                for index in self.get_index(j):
                    neighbor = Neighbor(node_id=node.id, index=index)
                    p.neighbors.append(neighbor)
                    p.distances.append(la.norm(node[index].r - p.r))

    def determine_neighbors(self):
        for i in xrange(self.n):
            current_node = self.nodes[i]
            nodes = None
            if i == 0:
                nodes = (current_node, self.nodes[i + 1])
            if 0 < i < self.n - 1:
                nodes = (current_node, self.nodes[i - 1], self.nodes[i + 1])
            if i == self.n - 1:
                nodes = (current_node, self.nodes[i - 1])
            self.add_neighbors(current_node, nodes)

    def create_all_nodes(self):
        for i in xrange(self.n - 1):
            self.create_one_node(i)
        r_before_last = self.particles[self.n - 3].r
        r_last = self.particles[self.n - 1].r

        before_last_node = self.nodes[self.n - 3]
        last_node = Node([r_last + (before_last_node[0].r - r_before_last),
                          r_last + (before_last_node[1].r - r_before_last),
                          r_last + (before_last_node[2].r - r_before_last), ])
        self.nodes.append(last_node)
        self.determine_neighbors()

    """ Bonding """

    def bonding_forces(self, p):
        for i in xrange(len(p.neighbors)):
            neighbor = p.neighbors[i]
            r = self.nodes[neighbor.node_id][neighbor.index].r
            x = p.distances[i]
            p.f_bond += force(p.r, r, x)

    def calc_bonding_forces(self):
        for node in self.nodes:
            for p in node:
                p.f_bond = np.zeros(shape=3)
                self.bonding_forces(p)

    def bonding_energy(self, p):
        e = 0
        for i in xrange(len(p.neighbors)):
            neighbor = p.neighbors[i]
            r = self.nodes[neighbor.node_id][neighbor.index].r
            x = p.distances[i]
            e += .5 * energy(p.r, r, x)
        return e

    def calc_bonding_energy(self):
        self.energy = 0
        for node in self.nodes:
            for p in node:
                self.energy += self.bonding_energy(p)
        return self.energy

    """ MD Step """

    def update_external_forces(self):
        for num, p in enumerate(self.particles):
            f_ex = coeff1_3 * p.f
            for node_particle in self.nodes[num]:
                node_particle.f = f_ex + node_particle.f_bond

    @staticmethod
    def get_coor_from_node(node):
        return coeff1_3 * sum([p.r for p in node])

    def update_coordinates(self):
        for num, node in enumerate(self.nodes):
            self.particles[num].r = self.get_coor_from_node(node)

    def step(self, h, total_max_step):
        self.update_external_forces()
        max_step = 0
        for node in self.nodes:
            dr = np.array([0., 0., 0.])
            for p in node:
                dr += h * p.v + .5 * h * h * self._m * p.f
                dr2 = dr.dot(dr)
                if dr2 > max_step:
                    max_step = dr2
                    p.r += dr
                    p.v += h * self._m * p.f
        max_step = np.sqrt(max_step)
        self.update_coordinates()
        return max_step if max_step > total_max_step else total_max_step

    """ Tests """

    def comp_bonding_dir(self):
        dx = 1e-13
        print '-' * 100
        nodes = self.nodes
        for node in nodes:
            for p in node:
                f = np.zeros(shape=3)
                for i in xrange(3):
                    e0 = self.calc_bonding_energy()
                    p.r[i] += dx
                    e1 = self.calc_bonding_energy()
                    p.r[i] -= dx
                    f[i] = (e0 - e1) / dx
                print f
                print p.f_bond
                print ''
        print '-' * 100

    """ Magic Methods """

    def __iter__(self):
        for p in self.particles:
            yield p

    def __getitem__(self, index):
        return self.particles[index]

    def __repr__(self):
        return "<Nanotube {0}>".format(self.id)
