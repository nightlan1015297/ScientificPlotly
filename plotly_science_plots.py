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
            font=dict(family="Times New Roman", size=16),
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
        axis_style = dict(
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
            gridcolor='darkgrey',
            griddash='dash',
            zeroline=grid,
            zerolinecolor='darkgrey'
        )
        fig.update_xaxes(title=xaxis_title, **axis_style)
        fig.update_yaxes(title=yaxis_title, **axis_style)

    elif style_name == 'ieee':
        # Apply the base 'science' style first
        apply_science_style(fig, 'science', palette=palette, grid=grid, legend_pos=legend_pos, xaxis_title=xaxis_title, yaxis_title=yaxis_title)

        # IEEE specific overrides
        line_styles = ['solid', 'dash', 'dot', 'dashdot']

        for i, trace in enumerate(fig.data):
            trace.line.dash = line_styles[i % len(line_styles)]

    elif style_name == 'nature':
        # Apply the base 'science' style first
        apply_science_style(fig, 'science', palette=palette, grid=grid, legend_pos=legend_pos, xaxis_title=xaxis_title, yaxis_title=yaxis_title)

        # Nature specific overrides
        fig.update_layout(font=dict(family="Arial"))

    elif style_name == 'aps':
        # Apply the base 'science' style first
        apply_science_style(fig, 'science', palette=palette, grid=grid, legend_pos=legend_pos, xaxis_title=xaxis_title, yaxis_title=yaxis_title)

        # APS specific overrides
        fig.update_layout(
            font=dict(family="Times New Roman", color="black"),
            legend=dict(title_text='', bordercolor='lightgrey'),
            margin=dict(l=40, r=20, t=20, b=40)
        )
        # Update grids to match typical APS style (lighter dashed grid)
        fig.update_xaxes(gridcolor='lightgrey', zerolinecolor='lightgrey', title_standoff=5)
        fig.update_yaxes(gridcolor='lightgrey', zerolinecolor='lightgrey', title_standoff=5)


if __name__ == '__main__':
    # Create a dummy figure
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) + 0.5
    y4 = np.cos(x) - 0.5

    # --- Science Plot ---
    fig_science = go.Figure()
    fig_science.add_trace(go.Scatter(x=x, y=y1, mode='lines', name=r'$\sin(x)$'))
    fig_science.add_trace(go.Scatter(x=x, y=y2, mode='lines', name=r'$\cos(x)$'))
    apply_science_style(fig_science, 'science', palette='bright', grid=True, legend_pos='bottom_right', xaxis_title="X-axis Title (units)", yaxis_title=r"Y-axis Title ($\int_0^x \sin(t) dt$)")
    fig_science.write_image("science.png")

    # --- IEEE Plot ---
    fig_ieee = go.Figure()
    fig_ieee.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Trace 1'))
    fig_ieee.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Trace 2'))
    fig_ieee.add_trace(go.Scatter(x=x, y=y3, mode='lines', name='Trace 3'))
    fig_ieee.add_trace(go.Scatter(x=x, y=y4, mode='lines', name='Trace 4'))
    apply_science_style(fig_ieee, 'ieee', palette='bright', grid=True, legend_pos='top_left', xaxis_title="Frequency (Hz)", yaxis_title=r"Power Spectral Density ($\mu V^2/Hz$)")
    fig_ieee.write_image("ieee.png")

    # --- Nature Plot ---
    fig_nature = go.Figure()
    fig_nature.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='sin(x)'))
    fig_nature.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='cos(x)'))
    apply_science_style(fig_nature, 'nature', palette='muted', grid=True, legend_pos='bottom_center', xaxis_title="Time (s)", yaxis_title=r"Amplitude ($\mathring{A}$)")
    fig_nature.write_image("nature.png")

    # --- APS Plot ---
    np.random.seed(42)
    x_data = np.random.normal(0, 1, 10000)
    x_pdf = np.linspace(-4, 4, 100)
    y_pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x_pdf**2)

    fig_aps = go.Figure()

    # Plot histogram
    fig_aps.add_trace(go.Histogram(
        x=x_data,
        histnorm='probability density',
        name='Data',
        showlegend=False,
        marker_color='#7baaf7', # light blue to match image
        marker_line=dict(width=1, color='black'),
        opacity=0.8,
        xbins=dict(start=-4, end=4, size=0.2)
    ))

    # Plot theoretical PDF
    fig_aps.add_trace(go.Scatter(
        x=x_pdf,
        y=y_pdf,
        mode='lines',
        name='Theoretical PDF',
        line=dict(color='darkred', width=3)
    ))

    apply_science_style(
        fig_aps,
        style_name='aps',
        grid=True,
        legend_pos='top_left',
        xaxis_title=r"Position $x$ (units)",
        yaxis_title=r"Probability Density $P(x)$"
    )

    fig_aps.write_image("aps.png")
