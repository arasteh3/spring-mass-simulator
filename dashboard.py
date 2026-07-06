import dash
from dash import dcc, html
import plotly.graph_objects as go

from .dynamics import simulate_system
from .forcing import sinusoidal_force


def create_dashboard():
    app = dash.Dash(__name__)

    t, x, v = simulate_system(F=sinusoidal_force())

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=x, mode="lines", name="Displacement"))

    app.layout = html.Div([
        html.H1("Spring-Mass Simulator"),
        dcc.Graph(figure=fig)
    ])

    return app
