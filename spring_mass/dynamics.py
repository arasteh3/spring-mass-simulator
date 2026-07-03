import numpy as np
from scipy.integrate import solve_ivp


def mass_spring_damper_ode(t, y, m, c, k, forcing_func):
    x, v = y
    F = forcing_func(t)
    dxdt = v
    dvdt = (F - c * v - k * x) / m
    return [dxdt, dvdt]


def simulate_system(
    m=1.0,
    c=0.5,
    k=2.0,
    forcing_func=lambda t: 0.0,
    t_max=20.0,
    x0=1.0,
    v0=0.0,
    num_points=2000,
):
    t_eval = np.linspace(0.0, t_max, num_points)
    sol = solve_ivp(
        mass_spring_damper_ode,
        (0.0, t_max),
        [x0, v0],
        args=(m, c, k, forcing_func),
        t_eval=t_eval,
        dense_output=False,
    )
    return t_eval, sol.y[0], sol.y[1]
