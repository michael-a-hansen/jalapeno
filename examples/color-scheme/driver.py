'''
This example shows how to convert the color scheme of an existing figure.

The key here is that a figure and axis can be created without jalapeno functions, and still modified by them.

Three figures are produced, each with a different color scheme, two lines each!
'''


import matplotlib.pyplot as plt

import jalapeno.plots.colorscheme as jpc
import jalapeno.plots.plots as jpp


# generate the plot
plt.plot([1, 2, 4, 7])
plt.xlabel('abscissa')
plt.ylabel('ordinate')
plt.title('example!')

# grab the figure and axes for convenience
fig = plt.gcf()
ax = plt.gca()

# size the figure
jpp.SquareFigure(width=4, fontsize=12).set_size(fig)

# produce the figures with different color schemes
jpc.FigColors.scheme('black').apply(fig, ax)
jpp.print_fig_to_pdf(fig, 'fig-black')

jpc.FigColors.scheme('white').apply(fig, ax)
jpp.print_fig_to_pdf(fig, 'fig-white')

jpc.FigColors.scheme('crazy').apply(fig, ax)
jpp.print_fig_to_pdf(fig, 'fig-crazy')
