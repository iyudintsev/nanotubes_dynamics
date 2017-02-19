from config import file_with_coor, particles_number
from model import Model
from utils.parser import Parser
from utils.visualizer import Visualizer
from utils.time_dec import time_spent_dec


def main():
    parser = Parser(file_with_coor, norm=1e-7)
    model = Model(num=particles_number, coordinates=parser.coordinates)
    calc_func = time_spent_dec(model.calc_old)
    calc_func()

    view = Visualizer(model.nanotubes)
    view.show()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
