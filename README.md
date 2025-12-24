# Plotly Science Plots

This package provides a simple way to apply formatting styles from the popular Matplotlib library `SciencePlots` to your Plotly figures. The goal is to automate the creation of publication-quality, interactive plots that adhere to strict journal formatting guidelines (e.g., IEEE, Nature).

## Why Use This Package?

While Matplotlib is excellent for static plots, Plotly offers the significant advantage of interactivity, which is invaluable for data exploration and scientific analysis. This package bridges the gap, allowing you to create visually appealing, journal-compliant plots that are also fully interactive.

## Installation

To use this package, you need to have Plotly and NumPy installed. You can install them using pip:

```bash
pip install plotly numpy
```

Then, download the `plotly_science_plots.py` file and place it in your project directory.

## Usage

The core of this package is the `apply_science_style` function. You can import it and apply it to your Plotly figures as shown below.

```python
import plotly.graph_objects as go
import numpy as np
from plotly_science_plots import apply_science_style

# Create a dummy figure
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='$\sin(x)$'))
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='$\cos(x)$'))

# Apply a style
apply_science_style(fig, 'science')

fig.show()
```

### Styles

You can choose from the following journal styles:

*   `'science'` (default)
*   `'ieee'`
*   `'nature'`

### Color Palettes

The package includes several color-blind-safe palettes:

*   `'science'` (default)
*   `'bright'`
*   `'vibrant'`
*   `'muted'`

You can apply a different color palette using the `palette` argument:

```python
apply_science_style(fig, 'science', palette='bright')
```

### Grid

You can enable a grid on your plot using the `grid` argument:

```python
apply_science_style(fig, 'science', grid=True)
```
