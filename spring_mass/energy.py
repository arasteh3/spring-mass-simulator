"""
Energy calculations for the spring-mass system.
"""


def compute_energy(m, k, x, v):
    """
    Compute kinetic, potential, and total energy.

    Parameters
    ----------
    m : float
        Mass.
    k : float
        Spring constant.
    x : array-like
        Displacement.
    v : array-like
        Velocity.

    Returns
    -------
    kinetic : array-like
        Kinetic energy.
    potential : array-like
        Potential energy.
    total : array-like
        Total energy.
    """

    kinetic = 0.5 * m * v**2
    potential = 0.5 * k * x**2
    total = kinetic + potential
    return kinetic, potential, total
