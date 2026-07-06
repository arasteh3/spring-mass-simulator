"""
Bode response utilities for the spring-mass system.
"""

import numpy as np
import matplotlib.pyplot as plt


def bode_response(freq, m=1.0, k=2.0, c=0.1):
    """
    Plot the Bode magnitude response of the system.

    Parameters
    ----------
    freq : array-like
        Frequency values (Hz).
    m : float
        Mass.
    k : float
        Spring constant.
    c : float
        Damping coefficient.
    """

    omega = 2.0 * np.pi * freq
    numerator = 1.0
    denominator = np.sqrt((k - m * omega**2) ** 2 + (c * omega) ** 2)
    magnitude = numerator / denominator

    plt.figure()
    plt.semilogx(freq, magnitude)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("Bode Magnitude Response")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
