'''

This example provides two examples of a 'stationary' (single frame) plot of a matrix spectrum on the complex plane.

1. a publication-ready single column figure
2. a presentation-ready figure on a black background

Four steps are involved in each figure:
- load the spectrum
- construct a complex plane (figure, axis, line series) for the spectrum
- size the figure and font
- print the figure to a pdf


Note that if you lack a system-wide installation of the paladin packages

'''

# load the jalapeno modules
import jalapeno.colors as jc
import jalapeno.plots as jp
import jalapeno.spectrum as js


# load the spectrum for both purposes
realpart, imagpart = js.load_spectrum('a.spectrum')


## First we'll make a publication-ready figure with a white background

# make a complex plane for the spectrum
fig, ax, spectrumplot = jp.make_complex_plane(colorscheme=jp.PlotColorScheme('white'),
                                              markercolor=jc.darkblue,
                                              markersize=4)

# plot the spectrum on the plane we made
spectrumplot.set_data(realpart,imagpart)

# size the figure and print it to pdf
jp.SquareFigure.forjournal().set_size(fig)
jp.print_fig( fig, 'a-for-publication', 'pdf' )



## And now we'll make a presentation-ready figure with a black background

# make a complex plane for the spectrum
fig, ax, spectrumplot = jp.make_complex_plane(colorscheme=jp.PlotColorScheme('black'),
                                              markercolor=jc.springgreen,
                                              markersize=6,
                                              planesize=jp.square_plane(18,6,6),
                                              showgrid=False)

# plot the spectrum on the new plane
spectrumplot.set_data(realpart,imagpart)

# size the figure and print it to pdf
jp.SquareFigure(width=4,fontsize=12).set_size(fig)
jp.print_fig( fig, 'a-for-presentation', 'pdf' )