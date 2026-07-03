"""
Spring–mass–damper simulator package.
"""

from .dynamics import simulate_system
from .energy import compute_energy
from .forcing import sinusoidal_forcing
from .bode import bode_response
from .animation import animate_response
from .dashboard import dashboard
