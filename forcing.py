import numpy as np


def sinusoidal_force(A=1.0, w=1.0):
    return lambda t: A * np.sin(w * t)
