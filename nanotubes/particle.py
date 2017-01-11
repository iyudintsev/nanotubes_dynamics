from vanderwaals.lg_modified import force


class Particle(object):
    def __init__(self, r):
        self.r = r
        self.v = None
        self.f_bond = None
        self.f_coul = None
        self.f_coul_corr = None
        self.f_lg = None

    def __repr__(self):
        return "<Particle {0}>".format(self.r)
