import numpy as np


def bode_response(m=1.0, k=10.0, c=0.2, w_range=None):
    if w_range is None:
        w_range = np.linspace(0.1, 10, 500)

    mag = []
    phase = []

    for w in w_range:
        H = 1 / (k - m * w**2 + 1j * c * w)
        mag.append(abs(H))
        phase.append(np.angle(H))

    return w_range, np.array(mag), np.array(phase)
