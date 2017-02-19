from numpy import linalg as la
from config import k_bond


def energy(r1, r2, x0):
    dr = r1 - r2
    dr_norm = la.norm(dr)
    dx = (dr_norm - x0)
    return .5 * k_bond * dx * dx


def force(r1, r2, x0):
    dr = r1 - r2
    dr_norm = la.norm(dr)
    return - k_bond * (dr_norm - x0) / dr_norm * dr
