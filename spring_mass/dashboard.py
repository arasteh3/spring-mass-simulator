"""
Dashboard utilities for the spring-mass system.
"""

from .dynamics import simulate_system
from .energy import compute_energy
from .bode import bode_response
from .animation import animate_response


def dashboard(m=1.0, k=2.0, c=0.1, forcing=None):
    """
    Run the full dashboard: simulate, compute energy, plot bode, animate.

    Parameters
    ----------
    m : float
        Mass.
    k : float
        Spring constant.
    c : float
        Damping coefficient.
    forcing : callable or None
        External forcing function.

    Returns
    -------
    dict
        Dictionary containing time, displacement, velocity, and energy.
    """

    t, x, v = simulate_system(m=m, k=k, c=c, forcing=forcing)
    kinetic, potential, total = compute_energy(m, k, x, v)

    bode_response(freq=range(1, 50), m=m, k=k, c=c)
    animate_response(t, x, m=m, k=k)

    return {
        "time": t,
        "displacement": x,
        "velocity": v,
        "energy": {
            "kinetic": kinetic,
            "potential": potential,
            "total": total,
        },
    }
