from lg_modified import force, energy


def calc_vanderwaals_force(p1, p2):
    """
    Force Calculation
    :param p1: Particle
    :param p2: Particle
    """
    f_lg = force(p1.r - p2.r)
    p1.f_lg = f_lg
    p2.f_lg = -f_lg


def calc_vanderwaals_energy(p1, p2):
    """
    Energy calculation
    :param p1: Particle
    :param p2: Particle
    :return: double
    """
    return energy(p1.r - p2.r)
