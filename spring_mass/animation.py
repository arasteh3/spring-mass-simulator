import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate_response(t, x, m=1.0, k=2.0):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_xlabel("Position")
    ax.set_yticks([])
    ax.set_title("Mass–spring animation")

    ax.plot([-1.5, -1.0], [0.0, 0.0], "k", lw=2)
    wall = plt.Rectangle((-1.0, -0.25), 0.05, 0.5, color="gray")
    ax.add_patch(wall)

    mass_width = 0.3
    mass_height = 0.2
    mass_patch = plt.Rectangle((0.0, -mass_height / 2), mass_width, mass_height, color="tab:blue")
    ax.add_patch(mass_patch)

    spring_line, = ax.plot([], [], "k", lw=2)

    def init():
        spring_line.set_data([], [])
        return mass_patch, spring_line

    def update(frame):
        x_pos = x[frame]
        mass_patch.set_x(x_pos - mass_width / 2)

        spring_x = np.linspace(-1.0, x_pos - mass_width / 2, 20)
        spring_y = 0.05 * np.sin(10 * (spring_x + 1.0))
        spring_line.set_data(spring_x, spring_y)

        return mass_patch, spring_line

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(t),
        init_func=init,
        interval=1000 * (t[-1] - t[0]) / len(t),
        blit=True,
    )

    plt.tight_layout()
    plt.show()
    return ani
