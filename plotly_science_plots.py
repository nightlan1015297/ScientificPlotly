import plotly.graph_objects as go
import numpy as np

def apply_science_style(fig, style_name, palette='science', grid=False, legend_pos='top_right', xaxis_title=None, yaxis_title=None):
    """
    Applies a science plot style to a Plotly figure.

    Args:
        fig (go.Figure): The Plotly figure to style.
        style_name (str): The name of the style to apply ('science', 'ieee', 'nature').
        palette (str): The color palette to use ('science', 'bright', 'vibrant', 'muted').
        grid (bool): If True, displays a grid.
        legend_pos (str): The position of the legend.
        xaxis_title (str): The title for the x-axis.
        yaxis_title (str): The title for the y-axis.
    """

    # --- Legend Position Mapping ---
    legend_positions = {
        'top_right':     dict(x=0.99, y=0.99, xanchor='right', yanchor='top'),
        'top_center':    dict(x=0.5,  y=0.99, xanchor='center',yanchor='top'),
        'top_left':      dict(x=0.01, y=0.99, xanchor='left',  yanchor='top'),
        'middle_right':  dict(x=0.99, y=0.5,  xanchor='right', yanchor='middle'),
        'middle_center': dict(x=0.5,  y=0.5,  xanchor='center',yanchor='middle'),
        'middle_left':   dict(x=0.01, y=0.5,  xanchor='left',  yanchor='middle'),
        'bottom_right':  dict(x=0.99, y=0.01, xanchor='right', yanchor='bottom'),
        'bottom_center': dict(x=0.5,  y=0.01, xanchor='center',yanchor='bottom'),
        'bottom_left':   dict(x=0.01, y=0.01, xanchor='left',  yanchor='bottom'),
    }

    legend_opts = legend_positions.get(legend_pos, legend_positions['top_right'])

    # --- Color Palettes ---
    palettes = {
        'science': ['#0C5DA5', '#00B945', '#FF9500', '#FF2C00', '#845B97', '#474747', '#9e9e9e'],
        'bright': ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE', '#AA3377', '#BBBBBB'],
        'vibrant': ['#EE7733', '#0077BB', '#33BBEE', '#EE3377', '#CC3311', '#009988', '#BBBBBB'],
        'muted': ['#CC6677', '#332288', '#DDCC77', '#117733', '#88CCEE', '#882255', '#44AA99', '#999933', '#AA4499']
    }
    color_palette = palettes.get(palette, palettes['science'])

    if style_name == 'science':
        # General layout updates
        fig.update_layout(
            font=dict(family="Times New Roman", size=10),
            colorway=color_palette,
            plot_bgcolor='white',
            legend=dict(
                title_text='Legend',
                font=dict(size=16),
                **legend_opts,
                bgcolor='white',
                bordercolor='black',
                borderwidth=1
            ),
            margin=dict(l=40, r=20, t=20, b=40)
        )

        # Update trace properties
        for trace in fig.data:
            if 'line' in trace:
                trace.line.width = 2.5

        # Axis updates
        fig.update_xaxes(
            title=xaxis_title,
            mirror='ticks',
            ticks='inside',
            showline=True,
            linecolor='black',
            linewidth=2.0,
            minor=dict(ticks="inside", ticklen=4),
            tickfont=dict(size=22),
            title_font=dict(size=22, color='black'),
            ticklen=8,
            tickwidth=2.0,
            showgrid=grid,
            gridwidth=1,
            gridcolor='grey',
            griddash='dash',
            zeroline=True,
            zerolinewidth=1,
            zerolinecolor='grey'
        )
        fig.update_yaxes(
            title=yaxis_title,
            mirror='ticks',
            ticks='inside',
            showline=True,
            linecolor='black',
            linewidth=2.0,
            minor=dict(ticks="inside", ticklen=4),
            tickfont=dict(size=22),
            title_font=dict(size=22, color='black'),
            ticklen=8,
            tickwidth=2.0,
            showgrid=grid,
            gridwidth=1,
            gridcolor='grey',
            griddash='dash',
            zeroline=True,
            zerolinewidth=1,
            zerolinecolor='grey'
        )
    elif style_name == 'ieee':
        # Apply the base 'science' style first
        apply_science_style(fig, 'science', palette=palette, grid=grid, legend_pos=legend_pos, xaxis_title=xaxis_title, yaxis_title=yaxis_title)

        # IEEE specific overrides
        line_styles = ['solid', 'dash', 'dot', 'dashdot']
        colors = ['black', 'red', 'blue', 'green']

        for i, trace in enumerate(fig.data):
            trace.line.dash = line_styles[i % len(line_styles)]
            trace.line.color = colors[i % len(colors)]

    elif style_name == 'nature':
        # Apply the base 'science' style first
        apply_science_style(fig, 'science', palette=palette, grid=grid, legend_pos=legend_pos, xaxis_title=xaxis_title, yaxis_title=yaxis_title)

        # Nature specific overrides
        fig.update_layout(font=dict(family="Arial"))


if __name__ == '__main__':
    # Create a dummy figure
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) + 0.5
    y4 = np.cos(x) - 0.5

    # --- Science Plot ---
    fig_science = go.Figure()
    fig_science.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='$\sin(x)$'))
    fig_science.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='$\cos(x)$'))
    apply_science_style(fig_science, 'science', palette='bright', grid=True, legend_pos='bottom_right', xaxis_title="X-axis Title (units)", yaxis_title="Y-axis Title ($\int_0^x \sin(t) dt$)")
    fig_science.write_image("science.png")

    # --- IEEE Plot ---
    fig_ieee = go.Figure()
    fig_ieee.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Trace 1'))
    fig_ieee.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Trace 2'))
    fig_ieee.add_trace(go.Scatter(x=x, y=y3, mode='lines', name='Trace 3'))
    fig_ieee.add_trace(go.Scatter(x=x, y=y4, mode='lines', name='Trace 4'))
    apply_science_style(fig_ieee, 'ieee', legend_pos='top_left', xaxis_title="Frequency (Hz)", yaxis_title="Power Spectral Density ($\mu V^2/Hz$)")
    fig_ieee.write_image("ieee.png")

    # --- Nature Plot ---
    fig_nature = go.Figure()
    fig_nature.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='sin(x)'))
    fig_nature.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='cos(x)'))
    apply_science_style(fig_nature, 'nature', legend_pos='bottom_center', xaxis_title="Time (s)", yaxis_title="Amplitude ($\\mathring{A}$)")
    fig_nature.write_image("nature.png")
