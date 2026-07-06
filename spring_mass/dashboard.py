"""
Dashboard utilities for the spring-mass system.
"""

import numpy as np

from .dynamics import simulate_system
from .energy import compute_energy
from .bode import bode_response
from .animation import animate_response
from .forcing import sinusoidal_forcing


def dashboard(
    m=1.0,
    k=2.0,
    c=0.1,
    forcing=None,
    t_span=(0.0, 10.0),
    n_points=1000,
):
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
        External forcing function f(t).
    t_span : tuple
        Start and end time.
    n_points : int
        Number of time points.

    Returns
    -------
    dict
        Dictionary containing time, displacement, velocity, and energy.
    """

    if forcing is None:
        def forcing(t):
            return sinusoidal_forcing(t, amplitude=1.0, freq=1.0)

    t, x, v = simulate_system(
        m=m,
        k=k,
        c=c,
        forcing=forcing,
        t_span=t_span,
        n_points=n_points,
    )

    kinetic, potential, total = compute_energy(m, k, x, v)

    freq = np.linspace(0.5, 50.0, 200)
    bode_response(freq=freq, m=m, k=k, c=c)
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
