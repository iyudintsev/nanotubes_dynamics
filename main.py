from nanotubes import Nanotubes
from config import file_with_coor


def main():
    nanotubes = Nanotubes(100, file_with_coor)
    print nanotubes


if __name__ == "__main__":
    main()