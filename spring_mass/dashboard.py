import matplotlib.pyplot as plt

from .dynamics import simulate_system
from .energy import compute_energy
from .forcing import sinusoidal_forcing
from .bode import bode_response
from .animation import animate_response


def dashboard(
    m=1.0,
    c=0.5,
    k=2.0,
    F0=1.0,
    omega=1.0,
    t_max=20.0,
    x0=1.0,
    v0=0.0,
):
    forcing_func = sinusoidal_forcing(F0=F0, omega=omega)
    t, x, v = simulate_system(m=m, c=c, k=k, forcing_func=forcing_func, t_max=t_max, x0=x0, v0=v0)
    ke, pe, E = compute_energy(m, k, x, v)
    w, mag, phase = bode_response(m=m, c=c, k=k)

    fig = plt.figure(figsize=(12, 8))

    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(t, x, label="Displacement x(t)")
    ax1.set_xlabel("Time [s]")
    ax1.set_ylabel("Displacement")
    ax1.set_title("Time-domain response")
    ax1.grid(True)

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(x, v)
    ax2.set_xlabel("Displacement x")
    ax2.set_ylabel("Velocity v")
    ax2.set_title("Phase portrait")
    ax2.grid(True)

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(t, ke, label="Kinetic")
    ax3.plot(t, pe, label="Potential")
    ax3.plot(t, E, label="Total")
    ax3.set_xlabel("Time [s]")
    ax3.set_ylabel("Energy")
    ax3.set_title("Energy vs time")
    ax3.legend()
    ax3.grid(True)

    ax4 = fig.add_subplot(2, 2, 4)
    ax4.semilogx(w, mag)
    ax4.set_xlabel("Frequency ω [rad/s]")
    ax4.set_ylabel("|H(jω)|")
    ax4.set_title("Bode magnitude (displacement/force)")
    ax4.grid(True, which="both")

    plt.tight_layout()
    plt.show()

    animate_response(t, x, m=m, k=k)

    return fig
