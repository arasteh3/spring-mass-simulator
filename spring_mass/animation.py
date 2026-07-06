"""
Animation utilities for the spring-mass system.
"""

import matplotlib.pyplot as plt
from matplotlib import animation


def animate_response(t, x, m=1.0, k=2.0):
    """
    Animate the mass displacement over time.

    Parameters
    ----------
    t : array-like
        Time values.
    x : array-like
        Displacement values.
    m : float
        Mass value.
    k : float
        Spring constant.

    Returns
    -------
    animation.FuncAnimation
        The generated animation object.
    """

    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.set_xlim(t[0], t[-1])
    ax.set_ylim(min(x), max(x))
    ax.set_xlabel("Time")
    ax.set_ylabel("Displacement")
    ax.set_title("Spring-Mass-Damper Response")

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        line.set_data(t[:frame], x[:frame])
        return line,

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(t),
        init_func=init,
        interval=1000.0 * (t[-1] - t[0]) / len(t),
        blit=True,
    )

    plt.tight_layout()
    plt.show()
    return ani
