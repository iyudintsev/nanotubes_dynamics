from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from config import L


class Visualizer(object):
    def __init__(self, nanotubes, nan_limit=None):
        self.coor = list(zip(*self.coordinates(nanotubes, nan_limit)))
        fig = plt.figure()
        self.ax = fig.add_subplot(111, projection='3d')
        self.show()

    @staticmethod
    def coordinates(nanotubes, nan_limit=None):
        coordinates = []
        nan_slice = nanotubes if nan_limit is None else nanotubes[:nan_limit]
        for nan in nan_slice:
            for p in nan:
                coordinates.append(p.r)
        return coordinates

    def show(self, set_lim=True):
        xs, ys, zs = self.coor
        self.ax.scatter(xs, ys, zs)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_zlabel("z")
        if set_lim:
            self.ax.set_xlim(L)
            self.ax.set_ylim(L)
            self.ax.set_zlim(L)
        plt.show()
