"""
Bode response utilities for the spring-mass system.
"""

import matplotlib.pyplot as plt
import numpy as np


def bode_response(freq, m=1.0, k=2.0, c=0.1):
    """
    Plot the Bode magnitude response of the system.

    Parameters
    ----------
    freq : array-like
        Frequency values.
    m : float
        Mass.
    k : float
        Spring constant.
    c : float
        Damping coefficient.
    """

    omega = 2 * np.pi * freq
    numerator = 1
    denominator = np.sqrt((k - m * omega**2)**2 + (c * omega)**2)
    magnitude = numerator / denominator

    plt.figure()
    plt.semilogx(freq, magnitude)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("Bode Magnitude Response")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
