import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate_system(t, x):
    fig, ax = plt.subplots()
    ax.set_xlim(min(x) - 1, max(x) + 1)
    ax.set_ylim(-2, 2)

    point, = ax.plot([], [], "bo", markersize=10)

    def init():
        point.set_data([], [])
        return point,

    def update(i):
        point.set_data(x[i], 0)
        return point,

    animation.FuncAnimation(fig, update, frames=len(t), init_func=init)
    plt.show()
