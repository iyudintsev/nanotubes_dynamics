import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


path = "../result.txt"


class StopPlotData(Exception):
    pass


class ShutDownError(Exception):
    pass


class MDViewer(object):
    def __init__(self, N=100, L=None, freq=None, pause=None):
        try:
            self.f = open(path)
        except IOError:
            print "There is no file 'data.dat'"
            raise ShutDownError
        self.N = N - 1  # the Number of particles
        self.L = L or [0, 200]  # the length of the counting area
        self.freq = freq if freq is not None else 1
        self.ax = axes3d.Axes3D(plt.figure())
        self.pause = pause if pause is not None else 1

    def pre_receive_data_for_plot(self):
        data = []
        for number, line in enumerate(self.f):
            data.append(map(float, line.split()))
            if number == self.N:
                break
        if not data:
            raise StopPlotData
        coor = lambda ind: [elem[ind] for elem in data]
        return map(coor, xrange(3))

    def receive_data_for_plot(self):
        data = None
        for _ in range(self.freq):
            data = self.pre_receive_data_for_plot()
        return data

    def plot_data(self):
         plt.cla()
         x, y, z = self.receive_data_for_plot()
         self.ax.scatter(x, y, z, c='m', marker='o')
         self.ax.set_xlim(*self.L)
         self.ax.set_ylim(*self.L)
         self.ax.set_zlim(*self.L)
         self.ax.set_xlabel('x')
         self.ax.set_ylabel('y')
         self.ax.set_zlabel('z')
         self.ax.set_title('MD viewer')
         plt.pause(self.pause)

    def run(self):
        while True:
            try:
                self.plot_data()
            except StopPlotData:
                self.f.close()
                return

if __name__ == "__main__":
    pause, freq = None, None
    for arg in sys.argv:
        if arg.startswith("-f") and freq is None:
            _, freq = arg.split('=')
            freq = int(freq)
        if arg.startswith("-p") and pause is None:
            _, pause = arg.split('=')
            pause = float(pause)
    try:        
        L = map(lambda x: 1e-7*x, [75, 105])
        viewer = MDViewer(N=300, L=L, freq=freq, pause=pause)
    except ShutDownError:
        pass
    else:
        viewer.run()
