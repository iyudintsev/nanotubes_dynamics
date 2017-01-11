from particle import Particle


class NanotubeOverflow(Exception):
    pass


class Nanotube(object):
    def __init__(self, nan_id, total_num):
        self.nan_id = nan_id
        self.total_num = total_num
        self.num = 0
        self.particles = []

    def add_particle(self, r):
        if self.num >= self.total_num:
            raise NanotubeOverflow("Nanotube {0}: total number = {1}".format(self.nan_id, self.total_num))
        self.particles.append(Particle(r))

    def __repr__(self):
        return "<Nanotube {0}>".format(self.nan_id)
