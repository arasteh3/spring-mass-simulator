import numpy as np
from scipy.integrate import solve_ivp


def simulate_system(m=1.0, k=10.0, c=0.2, F=None, t_max=10.0):
    """
    Simulate a damped spring-mass system.
    m: mass
    k: spring constant
    c: damping coefficient
    F: forcing function F(t)
    """

    def ode(t, y):
        x, v = y
        force = F(t) if F else 0.0
        dxdt = v
        dvdt = (force - c * v - k * x) / m
        return [dxdt, dvdt]

    t_eval = np.linspace(0, t_max, 2000)
    sol = solve_ivp(ode, [0, t_max], [0, 0], t_eval=t_eval)

    return sol.t, sol.y[0], sol.y[1]
