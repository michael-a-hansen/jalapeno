'''
This example provides three examples of a simple plot of 1-D data.

1. a publication-ready single column figure, which is printed to png (600 dpi), pdf, and svg
2. a presentation-ready figure on a black background

Four steps are involved in each figure:
- load/generate the data
- construct a 1d plot (figure, axis, line series) for the spectrum
- size the figure and font
- print the figure to a pdf
'''


import jalapeno.colors.svgcolors as jc
import jalapeno.plots.plots as jpp
import jalapeno.plots.colorscheme as jpc

import numpy as np


# generate the data
x = np.linspace(0, 2*np.pi, 600)
y = np.abs(np.cos(2*x))

# make a 1d plot
fig, ax, line = jpp.make_1d_plot(linecolor=jc.darkorange,
                                 maxx=max(x/np.pi),
                                 maxy=1.01,
                                 xname='x/pi',
                                 yname='cos(2x)')

# plot the data on our 1d plot
line.set_data(x/np.pi,y)

# size the figure and print it to pdf
jpp.SquareFigure().set_size(fig)
jpp.print_fig(fig, 'xy-for-publication', ['pdf', 'png', 'svg'], dpi=600)

# make another 1d plot
fig, ax, line = jpp.make_1d_plot(colorscheme=jpc.FigColors.scheme('black'),
                                 linecolor=jc.coral,
                                 linewidth=4,
                                 showgrid='off',
                                 maxx=max(x/np.pi),
                                 maxy=1.01,
                                 xname='x/pi',
                                 yname='cos(2x)')

# plot the data on our 1d plot
line.set_data(x/np.pi, y)

# size the figure and print it to pdf
jpp.SquareFigure(width=4, fontsize=12).set_size(fig)
jpp.print_fig(fig, 'xy-for-presentation', exts=['pdf'])  # way 1, use print_fig and provide exts=['pdf']
jpp.print_fig_to_pdf(fig, 'xy-for-presentation')         # way 2, use print_fig_to_pdf