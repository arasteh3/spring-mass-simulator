"""
Spring-mass-damper simulator package.
"""

# Remove all unused imports here

def dashboard():
    """Public entry point for the spring-mass dashboard."""
    from .dynamics import simulate_system
    from .energy import compute_energy
    from .bode import bode_response
    from .animation import animate_response
