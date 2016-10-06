import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import os as os

import jalapeno.plots.plots as jpp
import jalapeno.plots.colorscheme as jpc
import jalapeno.data.spectrum as jds


class PlaneSize:
    def __init__(self,
                 planesizelhp, spacinglhp, startticklhp,
                 planesizerhp, spacingrhp, starttickrhp,
                 planesizeimg, spacingimg, starttickimg):
        self.planesizelhp = planesizelhp
        self.spacinglhp = spacinglhp
        self.startticklhp = startticklhp
        self.planesizerhp = planesizerhp
        self.spacingrhp = spacingrhp
        self.starttickrhp = starttickrhp
        self.planesizeimg = planesizeimg
        self.spacingimg = spacingimg
        self.starttickimg = starttickimg


def square_plane(planesize=18, spacing=4, starttick=4):
    return PlaneSize(planesize, spacing, starttick,
                     planesize, spacing, starttick,
                     planesize, spacing, starttick)


def make_complex_plane(planesize=square_plane(),
                       colorscheme=jpc.FigColors(),
                       markercolor='b',
                       markerform='o',
                       markersize=8,
                       showticks=True,
                       showgrid=True):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xscale('symlog')
    ax.set_yscale('symlog')

    ax.set_xlim([-10**planesize.planesizelhp, +10**planesize.planesizerhp])
    ax.set_ylim([-10**planesize.planesizeimg, +10**planesize.planesizeimg])

    # Plot origin lines on the complex plane, a necessity even (especially) if the grid is turned off.
    ax.plot([-10**planesize.planesizelhp, +10**planesize.planesizerhp], [0, 0], color=colorscheme.gridlines)
    ax.plot([0, 0], [-10**planesize.planesizeimg, +10**planesize.planesizeimg], color=colorscheme.gridlines)

    lefthalf = -10**(np.arange(planesize.startticklhp, planesize.planesizelhp, planesize.spacinglhp))
    righthalf = +10**(np.arange(planesize.starttickrhp, planesize.planesizerhp, planesize.spacingrhp))
    tophalf = -10**(np.arange(planesize.starttickimg, planesize.planesizeimg, planesize.spacingimg))
    bottomhalf = +10**(np.arange(planesize.starttickimg, planesize.planesizeimg, planesize.spacingimg))
    xticks = np.hstack([lefthalf, np.hstack([0, righthalf])])
    yticks = np.hstack([bottomhalf, np.hstack([0, tophalf])])
    ax.tick_params(axis=u'both', which=u'both', length=0)

    if not showticks and showgrid:
        print('error! you are not allowed to ask for a grid without labels.')
        print('exiting!!!')
        exit()

    if showticks:
        ax.xaxis.set_ticks(xticks)
        ax.yaxis.set_ticks(yticks)
    else:
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])

    # We must apply the color scheme before the grid in case the grid is to be turned off.
    colorscheme.apply(fig, ax)

    ax.grid(showgrid)

    ax.set_xlabel('real')
    ax.set_ylabel('imaginary')

    # Add base for spectrum to emplace for faster plotting and animations.
    l, = ax.plot([], [],
                 linestyle='none',
                 markeredgecolor='none',
                 marker=markerform,
                 markersize=markersize,
                 color=markercolor)

    return fig, ax, l


def print_single_spectrum( fig,
                           line,
                           filepath,
                           outputpath = None,
                           ext = 'pdf' ):
    if( outputpath == None ):
        outputpath = filepath + '.' + ext
    realpart, imagpart = jds.load_spectrum( filepath )
    line.set_data( realpart, imagpart )
    jpp.print_fig( fig, outputpath, ext )


def get_movie_writer( fps=15 ):
    FFMpegWriter = animation.writers['ffmpeg']
    return FFMpegWriter( fps )


def flock_on_plane_movie( writer, fig, spectrumplot, nf, Freal, Fimag, moviepath, dpi=600 ):
    with writer.saving( fig, moviepath, dpi ):
        for i in np.arange(0,nf):
            realpart = Freal[:,i]
            imagpart = Fimag[:,i]
            spectrumplot.set_data( realpart, imagpart )
            writer.grab_frame()
            print( '- frame ' + str( i ) + ' of ' + str( nf ) + ' written' )


def flock_on_plane_pngs( fig, spectrumplot, nf, Freal, Fimag, pngfolderpath, dpi=600 ):
    if not os.path.exists(pngfolderpath):
        os.makedirs(pngfolderpath)
    for i in np.arange(0,nf):
        realpart = Freal[:,i]
        imagpart = Fimag[:,i]
        spectrumplot.set_data( realpart, imagpart )
        jpp.print_fig( fig, pngfolderpath + '/plot-' + str( i+1 ).zfill( 6 ), 'png', dpi=dpi )
        print( '- frame ' + str( i ) + ' of ' + str( nf ) + ' written' )
