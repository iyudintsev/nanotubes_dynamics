from config import file_with_coor
from model import Model
from utils.parser import Parser
from utils.visualizer import Visualizer


def main():
    parser = Parser(file_with_coor, norm=1e-7)
    model = Model(num=100, coordinates=parser.coordinates)
    model.calc()

    view = Visualizer(model.nanotubes)
    view.show(nodes=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
