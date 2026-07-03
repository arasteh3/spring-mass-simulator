import numpy as np

def compute_energy(m, k, x, v):
    kinetic = 0.5 * m * v**2
    potential = 0.5 * k * x**2
    total = kinetic + potential
    return kinetic, potential, total
