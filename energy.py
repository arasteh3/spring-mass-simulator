def compute_energy(x, v, m=1.0, k=10.0):
    kinetic = 0.5 * m * v**2
    potential = 0.5 * k * x**2
    total = kinetic + potential
    return kinetic, potential, total
