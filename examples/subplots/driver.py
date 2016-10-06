'''
This example shows how to do subplots with axes of different color schemes
'''

import matplotlib.pyplot as plt

import jalapeno.plots.colorscheme as jpc
import jalapeno.plots.plots as jpp
import jalapeno.colors.svgcolors as jcs


# generate the plot, labels, a cool line series
fig, axarr = plt.subplots(1, 2)

data0 = [1, 2, 4, 7]
data1 = [2, 4, 8, 3]

l0, = axarr[0].plot(data0)
l10, = axarr[1].plot(data1)
l11, = axarr[1].plot(data1)
l12, = axarr[1].plot(data1)

l0.set(color=jcs.lime)
l10.set(color=jcs.coral, linewidth=40, alpha=0.3)
l11.set(color=jcs.coral, linewidth=20, alpha=0.5)
l12.set(color=jcs.coral, linewidth=10, alpha=1)

axarr[0].set(xlabel='abs 0')
axarr[0].set(ylabel='ord 0')

axarr[1].set(xlabel='abs 1')
axarr[1].set(ylabel='ord 1')

# set the color scheme of the figure and of each axes
jpc.FigColors(figbg=jcs.royalblue).apply(fig=fig)
jpc.FigColors.scheme('black').apply(ax=axarr[0])
jpc.FigColors(axisbg=jcs.bisque).apply(ax=axarr[1])

# size the figure
jpp.SquareFigure.forjournal(columns=2, standard='nature').set_size(fig)

# produce the figures with different color schemes
jpp.print_fig_to_pdf(fig, 'fig-1')
