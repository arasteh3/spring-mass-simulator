import numpy as np

def bode_response(m=1.0, c=0.5, k=2.0, omega_min=0.1, omega_max=10.0, num_points=500):
    omega = np.linspace(omega_min, omega_max, num_points)
    denom = k - m * omega**2 + 1j * c * omega
    H = 1.0 / denom
    mag = np.abs(H)
    phase = np.angle(H)
    return omega, mag, phase
