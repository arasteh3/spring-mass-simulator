"""
Spring-mass-damper simulator package.
"""

from .dynamics import simulate_system
from .energy import compute_energy
from .bode import bode_response
from .animation import animate_response
from .forcing import sinusoidal_forcing
from .dashboard import dashboard

__all__ = [
    "simulate_system",
    "compute_energy",
    "bode_response",
    "animate_response",
    "sinusoidal_forcing",
    "dashboard",
]
