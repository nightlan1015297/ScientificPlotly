import plotly.graph_objects as go
import numpy as np
from cycler import cycler

def apply_science_style(fig, style_name):
    """
    Applies a science plot style to a Plotly figure.
    """
    if style_name == 'science':
        # Color Palette
        color_palette = ['#0C5DA5', '#00B945', '#FF9500', '#FF2C00', '#845B97', '#474747', '#9e9e9e']

        # General layout updates
        fig.update_layout(
            font=dict(family="Times New Roman", size=10),
            colorway=color_palette,
            plot_bgcolor='white',
            legend=dict(
                bgcolor='rgba(0,0,0,0)',
                bordercolor='rgba(0,0,0,0)'
            )
        )

        # Axis updates
        fig.update_xaxes(
            mirror=True,
            ticks='inside',
            showline=True,
            linecolor='black',
            linewidth=0.5,
            minor=dict(ticks="inside")
        )
        fig.update_yaxes(
            mirror=True,
            ticks='inside',
            showline=True,
            linecolor='black',
            linewidth=0.5,
            minor=dict(ticks="inside")
        )
    elif style_name == 'ieee':
        # Apply the base 'science' style first
        apply_science_style(fig, 'science')

        # IEEE specific overrides
        line_styles = ['solid', 'dash', 'dot', 'dashdot']
        colors = ['black', 'red', 'blue', 'green']

        fig.update_layout(
            font=dict(family="Times New Roman", size=8)
        )

        for i, trace in enumerate(fig.data):
            trace.line.dash = line_styles[i % len(line_styles)]
            trace.line.color = colors[i % len(colors)]

    elif style_name == 'nature':
        # Apply the base 'science' style first
        apply_science_style(fig, 'science')

        # Nature specific overrides
        fig.update_layout(
            font=dict(family="Arial", size=7)
        )
        fig.update_xaxes(tickfont=dict(size=7), title_font=dict(size=7))
        fig.update_yaxes(tickfont=dict(size=7), title_font=dict(size=7))
        fig.update_layout(legend=dict(font=dict(size=7)))


if __name__ == '__main__':
    # Create a dummy figure
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) + 0.5
    y4 = np.cos(x) - 0.5

    # --- Science Plot ---
    fig_science = go.Figure()
    fig_science.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='sin(x)'))
    fig_science.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='cos(x)'))
    apply_science_style(fig_science, 'science')
    fig_science.write_image("science.png")

    # --- IEEE Plot ---
    fig_ieee = go.Figure()
    fig_ieee.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Trace 1'))
    fig_ieee.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Trace 2'))
    fig_ieee.add_trace(go.Scatter(x=x, y=y3, mode='lines', name='Trace 3'))
    fig_ieee.add_trace(go.Scatter(x=x, y=y4, mode='lines', name='Trace 4'))
    apply_science_style(fig_ieee, 'ieee')
    fig_ieee.write_image("ieee.png")

    # --- Nature Plot ---
    fig_nature = go.Figure()
    fig_nature.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='sin(x)'))
    fig_nature.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='cos(x)'))
    apply_science_style(fig_nature, 'nature')
    fig_nature.write_image("nature.png")
