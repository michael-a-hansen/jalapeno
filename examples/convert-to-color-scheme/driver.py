'''
This example shows how to convert the color scheme of an existing figure.

The key here is that a figure and axis can be created without jalapeno functions, and still modified by them.

Three figures are produced, each with a different color scheme, two lines each!
'''


import matplotlib.pyplot as plt

import jalapeno.plots.colorscheme as jpc
import jalapeno.plots.plots as jpp


# generate the plot
plt.plot([1,2,4,7])
plt.xlabel('abscissa')
plt.ylabel('ordinate')
plt.title('example!')

# size the figure
jpp.SquareFigure(width=4, fontsize=12).set_size(plt.gcf())

# produce the figures with different color schemes
jpc.FigColorScheme.scheme('black').apply(plt.gcf(), plt.gca())
jpp.print_fig_to_pdf(plt.gcf(), 'fig-black')

jpc.FigColorScheme.scheme('white').apply(plt.gcf(), plt.gca())
jpp.print_fig_to_pdf(plt.gcf(), 'fig-white')

jpc.FigColorScheme.scheme('crazy').apply(plt.gcf(), plt.gca())
jpp.print_fig_to_pdf(plt.gcf(), 'fig-crazy')