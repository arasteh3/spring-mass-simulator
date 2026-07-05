"""
Forcing functions for the spring-mass system.
"""

import numpy as np


def sinusoidal_forcing(t, amplitude=1.0, freq=1.0):
    """
    Sinusoidal forcing function.

    Parameters
    ----------
    t : array-like
        Time values.
    amplitude : float
        Amplitude of the forcing.
    freq : float
        Frequency of the forcing.

    Returns
    -------
    array-like
        Forcing values.
    """

    return amplitude * np.sin(2 * np.pi * freq * t)
