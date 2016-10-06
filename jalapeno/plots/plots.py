"""@package jalapeno.plots

Details forthcoming...
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import jalapeno.plots.colorscheme as jpc


def inspect_artist(artist):
    print(artist)
    matplotlib.artist.getp(artist)

def print_fig(fig, file, exts=['pdf'], dpi=1200):
    for ext in exts:
        fig.savefig(file + '.' + ext, facecolor=fig.get_facecolor(), edgecolor='none', dpi=dpi, bbox_inches='tight')


def print_fig_to_pdf(fig, file):
    print_fig(fig, file, ['pdf'])


def print_fig_to_svg(fig, file):
    print_fig(fig, file, ['svg'])


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
        super(SquareFigure, self).__init__(width, width, fontsize)

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


def make_1d_plot(maxx=1e16,
                 minx=0,
                 maxy=1e16,
                 miny=0,
                 xscale='linear',
                 yscale='linear',
                 xname='abscissa',
                 yname='ordinate',
                 colorscheme=jpc.FigColors(),
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