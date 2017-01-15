from nanotubes import Nanotubes
from config import file_with_coor
from visualizer import Visualizer


def main():
    nanotubes = Nanotubes(100, file_with_coor)
    view = Visualizer(nanotubes)
    view.show(set_lim=False, nan_limit=1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
