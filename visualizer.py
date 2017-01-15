from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from config import L


class Visualizer(object):
    def __init__(self, nanotubes):
        self.coor = list(zip(*self.coordinates(nanotubes)))
        fig = plt.figure()
        self.ax = fig.add_subplot(111, projection='3d')
        self.show()

    @staticmethod
    def coordinates(nanotubes):
        coordinates = []
        for nan in nanotubes:
            for p in nan:
                coordinates.append(p.r)
        return coordinates

    def show(self):
        xs, ys, zs = self.coor
        self.ax.scatter(xs, ys, zs)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_zlabel("z")
        self.ax.set_xlim([0, L])
        self.ax.set_ylim([0, L])
        self.ax.set_zlim([0, L])
        plt.show()
