'''

This example provides two examples of a 'stationary' (single frame) plot of a matrix spectrum on the complex plane.

1. a publication-ready single column figure
2. a presentation-ready figure on a black background

Four steps are involved in each figure:
- load the spectrum
- construct a complex plane (figure, axis, line series) for the spectrum
- size the figure and font
- print the figure to a pdf
'''


import jalapeno.colors.svgcolors as jcs
import jalapeno.plots.plots as jpp
import jalapeno.plots.complex_plane as jpcp
import jalapeno.plots.colorscheme as jpc
import jalapeno.data.spectrum as jds


# load the spectrum for both purposes
realpart, imagpart = jds.load_spectrum('a.spectrum')


# First we'll make a publication-ready figure with a white background

# make a complex plane for the spectrum
fig, ax, spectrumplot = jpcp.make_complex_plane(colorscheme=jpc.FigColors.scheme('white'),
                                                markercolor=jcs.darkblue,
                                                markersize=4)

# plot the spectrum on the plane we made
spectrumplot.set_data(realpart, imagpart)

# size the figure and print it to pdf
jpp.SquareFigure.forjournal(standard='nature').set_size(fig)
jpp.print_fig(fig, 'a-for-publication', ['pdf'])

# And now we'll make a presentation-ready figure with a black background

# make a complex plane for the spectrum
fig, ax, spectrumplot = jpcp.make_complex_plane(colorscheme=jpc.FigColors.scheme('black'),
                                                markercolor=jcs.springgreen,
                                                markersize=6,
                                                planesize=jpcp.square_plane(18, 6, 6),
                                                showgrid=False)

# plot the spectrum on the new plane
spectrumplot.set_data(realpart, imagpart)

# size the figure and print it to pdf
jpp.SquareFigure(width=4, fontsize=12).set_size(fig)
jpp.print_fig(fig, 'a-for-presentation', ['pdf'])
