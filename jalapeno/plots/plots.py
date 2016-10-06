"""@package jalapeno.plots

Details forthcoming...
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import jalapeno.plots.colorscheme as jpc


class FigureSize:
    """@class FigureSize

    Transparent container for figure sizes, namely width, height, and axis fonts.
    """

    def __init__(self, width=3.5, height=3.5, fontsize=7):
        self.figureWidth = width
        self.figureHeight = height
        self.mainFontSize = fontsize

    def set_size(self, figure):
        matplotlib.rc('font', **{'size': self.mainFontSize})
        figure.set_size_inches(self.figureWidth, self.figureHeight)


class SquareFigure(FigureSize):
    """@class Square Figure

    Transparent container for square figures - width and
    """

    def __init__(self, width=3.5, fontsize=7):
        super(SquareFigure,self).__init__(width, width, fontsize)

    @classmethod
    def forjournal(cls,
                   columns=1,
                   standard='elsevier',
                   fontsize=7):
        width = 3.5
        if standard == 'elsevier':
            if columns == 1:
                width = 3.54
            elif columns == 1.5:
                width = 5.51
            elif columns == 2:
                width = 7.48
        if standard == 'nature':
            if columns == 1:
                width = 3.51
            elif columns == 2:
                width = 7.20
        if standard == 'IEEE':
            if columns == 1:
                width = 3.5
            elif columns == 2:
                width = 7.16
        return cls(width=width, fontsize=fontsize)


def print_fig(fig, file, exts=['pdf'], dpi=1200):
    for ext in exts:
        fig.savefig(file + '.' + ext, facecolor=fig.get_facecolor(), edgecolor='none', dpi=dpi, bbox_inches='tight')


def print_fig_to_pdf(fig, file):
    print_fig(fig, file, ['pdf'])


def print_fig_to_svg(fig, file):
    print_fig(fig, file, ['svg'])


# This class, the square_plane function, and make_complex_plane should be moved.
# They belong in a special plots module for eigenspectra.
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
                       colorscheme=jpc.FigColorScheme(),
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


def make_1d_plot(maxx=1e16,
                 minx=0,
                 maxy=1e16,
                 miny=0,
                 xscale='linear',
                 yscale='linear',
                 xname='abscissa',
                 yname='ordinate',
                 colorscheme=jpc.FigColorScheme(),
                 linecolor='b',
                 linewidth=1,
                 showgrid=True):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xscale(xscale)
    ax.set_yscale(yscale)

    ax.set_xlim([minx, maxx])
    ax.set_ylim([miny, maxy])

    ax.tick_params(axis=u'both', which=u'both', length=0)

    # We must apply the color scheme before the grid in case the grid is to be turned off.
    colorscheme.apply(fig, ax)

    ax.grid(showgrid)

    ax.set_xlabel(xname)
    ax.set_ylabel(yname)

    # Add base for line series to emplace for faster plotting and animations.
    l, = ax.plot([], [],
                 linestyle='-',
                 linewidth=linewidth,
                 color=linecolor)

    return fig, ax, l



# I should move this to spectrum or a special plotter.
# def print_single_spectrum( fig,
#                            line,
#                            filepath,
#                            outputpath = None,
#                            ext = 'pdf' ):
#     if( outputpath == None ):
#         outputpath = filepath + '.' + ext
#     realpart, imagpart = js.load_spectrum( filepath )
#     line.set_data( realpart, imagpart )
#     print_fig( fig, outputpath, ext )

# This is commented out for now, likely needs to be moved to fit into the jalapeno packaging, etc.
# def get_movie_writer( fps=15 ):
#     FFMpegWriter = animation.writers['ffmpeg']
#     return FFMpegWriter( fps )
#
# def flock_on_plane_movie( writer, fig, spectrumplot, nf, Freal, Fimag, moviepath, dpi=600 ):
#     with writer.saving( fig, moviepath, dpi ):
#         for i in np.arange(0,nf):
#             realpart = Freal[:,i]
#             imagpart = Fimag[:,i]
#             spectrumplot.set_data( realpart, imagpart )
#             writer.grab_frame()
#             print( '- frame ' + str( i ) + ' of ' + str( nf ) + ' written' )
#
# def flock_on_plane_pngs( fig, spectrumplot, nf, Freal, Fimag, pngfolderpath, dpi=600 ):
#     if not os.path.exists(pngfolderpath):
#         os.makedirs(pngfolderpath)
#     for i in np.arange(0,nf):
#         realpart = Freal[:,i]
#         imagpart = Fimag[:,i]
#         spectrumplot.set_data( realpart, imagpart )
#         print_fig( fig, pngfolderpath + '/plot-' + str( i+1 ).zfill( 6 ), 'png', dpi=dpi )
#         print( '- frame ' + str( i ) + ' of ' + str( nf ) + ' written' )
