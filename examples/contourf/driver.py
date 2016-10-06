import numpy as np
import matplotlib.pyplot as plt

import jalapeno.plots.colorscheme as jpc
import jalapeno.plots.plots as jpp


# grab the figure and axes for convenience
fig = plt.figure()
ax = plt.Axes(fig, [0., 0., 1., 1.])
fig.add_axes(ax)

ax.set_axis_off()

# make the figure
delta = 0.025
x = y = np.arange(-10, 10, delta)
X, Y = np.meshgrid(x, y)
Z2 = np.cos(X)*np.sin(Y)*np.exp(-5e-3*(x+y)**2)-1e-2*(x**2+y**2)

CS = ax.contourf(X, Y, Z2, 8,
                 cmap=plt.cm.inferno)

# size the figure
jpp.SquareFigure(width=4, fontsize=12).set_size(fig)

# produce the figures with different color schemes
jpc.FigColors.scheme('black').apply(fig, ax)
jpp.print_fig_to_pdf(fig, 'figure')
