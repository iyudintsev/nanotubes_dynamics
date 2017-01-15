from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from config import L


class Visualizer(object):
    def __init__(self, nanotubes):
        self.nanotubes = nanotubes
        fig = plt.figure()
        self.ax = fig.add_subplot(111, projection='3d')

    def coordinates(self, nan_limit=None):
        coordinates = []
        nan_slice = self.nanotubes if nan_limit is None else self.nanotubes[:nan_limit]
        for nan in nan_slice:
            for p in nan:
                coordinates.append(p.r)
        return coordinates

    def show(self, nan_limit=None, set_lim=True):
        coor = list(zip(*self.coordinates(nan_limit)))
        xs, ys, zs = coor
        self.ax.scatter(xs, ys, zs)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_zlabel("z")
        if set_lim:
            self.ax.set_xlim(L)
            self.ax.set_ylim(L)
            self.ax.set_zlim(L)
        plt.show()
