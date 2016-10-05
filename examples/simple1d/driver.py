'''

This example provides two examples of a simple plot of 1-D data, x and y

1. a publication-ready single column figure
2. a presentation-ready figure on a black background

Four steps are involved in each figure:
- load/generate the data
- construct a 1d plot (figure, axis, line series) for the spectrum
- size the figure and font
- print the figure to a pdf


Note that if you lack a system-wide installation of the paladin packages

'''

# load the jalapeno modules
import jalapeno.colors as jc
import jalapeno.plots as jp

import numpy as np


# generate the data
x = np.linspace(0,2*np.pi,600)
y = np.abs(np.cos(2*x))


## First we'll make a publication-ready figure with a white background

# make a complex plane for the spectrum
fig, ax, line = jp.make_1d_plot(colorscheme=jp.PlotColorScheme('white'),
                                linecolor=jc.darkorange,
                                maxx=max(x/np.pi),
                                maxy=1.01,
                                xname='x/pi',
                                yname='cos(2x)')

# plot the spectrum on the plane we made
line.set_data(x/np.pi,y)
line.

# size the figure and print it to pdf
jp.SquareFigure.forjournal().set_size(fig)
jp.print_fig( fig, 'xy-for-publication', 'pdf' )



## And now we'll make a presentation-ready figure with a black background

# make a complex plane for the spectrum
fig, ax, line = jp.make_1d_plot(colorscheme=jp.PlotColorScheme('black'),
                                linecolor=jc.coral,
                                linewidth=4,
                                showgrid=False,
                                maxx=max(x/np.pi),
                                maxy=1.01,
                                xname='x/pi',
                                yname='cos(2x)')

# plot the spectrum on the new plane
line.set_data(x/np.pi,y)

# size the figure and print it to pdf
jp.SquareFigure(width=4,fontsize=12).set_size(fig)
jp.print_fig( fig, 'xy-for-presentation', 'pdf' )