'''
This example is a simple 1d plot with two curves and a legend.

The legend background and text are part of a jalapeno color scheme and can be modified easily.

Several plots are made, some with default legends and others with specially colored legends.
'''


import matplotlib.pyplot as plt

import jalapeno.plots.colorscheme as jpc
import jalapeno.plots.plots as jpp
import jalapeno.colors.svgcolors as jcs


# generate the plot
plt.plot([1, 2, 4, 7], 'r', label='curve 1')
plt.plot([1, 2, 3, 4], 'b', label='curve 2')
plt.legend(loc='upper left')

# grab the figure and axes for convenience
fig = plt.gcf()
ax = plt.gca()

# print figures with different legend colors
jpc.FigColors.scheme('white').apply(fig, ax)
jpp.print_fig_to_pdf(fig, 'result-white-default-legend')

jpc.FigColors.scheme('black').apply(fig, ax)
jpp.print_fig_to_pdf(fig, 'result-black-default-legend')

jpc.FigColors.scheme('black', legendbg=jcs.limegreen).apply(fig, ax)
jpp.print_fig_to_pdf(fig, 'result-black-lime-legend')

jpc.FigColors.scheme('white', legendbg=jcs.chocolate, legendtext='w').apply(fig, ax)
jpp.print_fig_to_pdf(fig, 'result-white-brown-legend')
