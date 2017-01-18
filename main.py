from config import file_with_coor
from nanotubes import Nanotubes
from utils.parser import Parser
from visualizer import Visualizer


def main():
    nanotubes = Nanotubes(100)
    parser = Parser(file_with_coor, norm=1e-7)
    nanotubes.set_coordinates(parser.coordinates)

    view = Visualizer(nanotubes)
    view.show(nodes=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
