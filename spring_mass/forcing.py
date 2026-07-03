import numpy as np

def sinusoidal_forcing(F0=1.0, omega=1.0):
    def F(t):
        return F0 * np.sin(omega * t)
    return F

def zero_forcing():
    return lambda t: 0.0
