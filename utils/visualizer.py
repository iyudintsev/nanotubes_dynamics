from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from config import LV


class Visualizer(object):
    def __init__(self, nanotubes):
        self.nanotubes = nanotubes
        fig = plt.figure()
        self.ax = fig.add_subplot(111, projection='3d')

    def get_coor(self, nan_limit=None, nodes=False):
        coordinates = []
        nan_slice = self.nanotubes if nan_limit is None else self.nanotubes[:nan_limit]
        for nan in nan_slice:
            self.simple_iter(nan, coordinates) if not nodes else self.nodes_iter(nan, coordinates)
        return coordinates

    @staticmethod
    def simple_iter(nan, coordinates):
        for p in nan:
            coordinates.append(p.r)

    @staticmethod
    def nodes_iter(nan, coordinates):
        for node in nan.nodes:
            for p in node:
                coordinates.append(p.r)

    def show(self, nan_limit=None, set_lim=True, nodes=False):
        coor = list(zip(*self.get_coor(nan_limit, nodes)))
        xs, ys, zs = coor
        self.ax.scatter(xs, ys, zs)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_zlabel("z")
        if set_lim:
            self.ax.set_xlim(LV)
            self.ax.set_ylim(LV)
            self.ax.set_zlim(LV)
        plt.show()
