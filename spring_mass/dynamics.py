"""
Dynamics of the spring-mass-damper system.
"""

import numpy as np
from scipy.integrate import solve_ivp


def _equations(t, y, m, k, c, forcing):
    x, v = y
    f_ext = forcing(t) if forcing is not None else 0.0
    a = (f_ext - c * v - k * x) / m
    return [v, a]


def simulate_system(
    m=1.0,
    k=2.0,
    c=0.1,
    forcing=None,
    t_span=(0.0, 10.0),
    n_points=1000,
    x0=1.0,
    v0=0.0,
):
    """
    Simulate the spring-mass-damper system.

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
    x0 : float
        Initial displacement.
    v0 : float
        Initial velocity.

    Returns
    -------
    t : ndarray
        Time array.
    x : ndarray
        Displacement array.
    v : ndarray
        Velocity array.
    """

    t_eval = np.linspace(t_span[0], t_span[1], n_points)
    sol = solve_ivp(
        _equations,
        t_span,
        [x0, v0],
        args=(m, k, c, forcing),
        t_eval=t_eval,
        dense_output=False,
    )

    x = sol.y[0]
    v = sol.y[1]
    return t_eval, x, v
