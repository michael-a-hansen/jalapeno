import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import os


import jalapeno.colors as jc
import jalapeno.spectrum as js










class FigureSize:
    def __init__(self,width=3.5,height=3.5,fontsize=7):
        self.figureWidth=width
        self.figureHeight=height
        self.mainFontSize=fontsize

    def set_size(self,figure):
        font = {'size':self.mainFontSize,
                }
        matplotlib.rc('font', **font)
        figure.set_size_inches(self.figureWidth, self.figureHeight)

class SquareFigure(FigureSize):
    def __init__(self,width=3.5,fontsize=7):
        self.figureWidth=width
        self.figureHeight=self.figureWidth
        self.mainFontSize=fontsize

    @classmethod
    def forjournal(cls,
                   columns=1,
                   standard='elsevier',
                   fontsize=7):
        width=3.5
        if( standard == 'elsevier'):
            if columns==1:
                width=3.54
            elif columns==1.5:
                width=5.51
            elif columns==2:
                width=7.48
        if( standard == 'nature'):
            if columns==1:
                width=3.51
            elif columns==2:
                width=7.20
        if( standard == 'IEEE'):
            if columns==1:
                width=3.5
            elif columns==2:
                width=7.16
        return cls(width=width,fontsize=fontsize)



class PlaneSize:
    def __init__( self,
                  planesizelhp, spacinglhp, startticklhp,
                  planesizerhp, spacingrhp, starttickrhp,
                  planesizeimg, spacingimg, starttickimg ):
        self.planesizelhp = planesizelhp
        self.spacinglhp   = spacinglhp
        self.startticklhp = startticklhp
        self.planesizerhp = planesizerhp
        self.spacingrhp   = spacingrhp
        self.starttickrhp = starttickrhp
        self.planesizeimg = planesizeimg
        self.spacingimg   = spacingimg
        self.starttickimg = starttickimg


def square_plane( planesize = 18, spacing = 4, starttick = 4 ):
    return PlaneSize( planesize, spacing, starttick,
                      planesize, spacing, starttick,
                      planesize, spacing, starttick )

class PlotColorScheme:
    def __init__( self,
                  figurebackground = jc.white,
                  axisbackground = jc.white,
                  originlines = jc.black,
                  gridlines = jc.black,
                  axistext = jc.black ):
        self.figurebackground=figurebackground
        self.axisbackground=axisbackground
        self.originlines=originlines
        self.gridlines=gridlines
        self.axistext=axistext

    def __init__( self,
                  colorscheme = 'white'):
        if( colorscheme == 'white' ):
            figurebackground = jc.white
            axisbackground = jc.white
            originlines = jc.black
            gridlines = jc.black
            axistext = jc.black
        elif( colorscheme == 'black' ):
            figurebackground = jc.black
            axisbackground = jc.black
            originlines = jc.white
            gridlines = jc.white
            axistext = jc.white
        else:
            print( 'Error! Colorscheme: ' + colorscheme + ' not found! Using default white color scheme.' )
            figurebackground = jc.white
            axisbackground = jc.white
            originlines = jc.black
            gridlines = jc.black
            axistext = jc.black

        self.figurebackground = figurebackground
        self.axisbackground   = axisbackground
        self.originlines      = originlines
        self.gridlines        = gridlines
        self.axistext         = axistext








def make_complex_plane( planesize = square_plane(),
                        colorscheme = PlotColorScheme(),
                        markercolor = jc.blueviolet_mah,
                        markerform = 'o',
                        markersize = 8,
                        showticks = True,
                        showgrid = True ):

    # make the figure and put an axis on it
    fig = plt.figure()
    ax = fig.add_subplot( 111 )
    fig.patch.set_facecolor( colorscheme.figurebackground )
    ax.patch.set_facecolor( colorscheme.axisbackground )

    # symmetric log scaling
    ax.set_xscale( 'symlog' )
    ax.set_yscale( 'symlog' )

    # axis limits
    ax.set_xlim( [-10**planesize.planesizelhp, +10**planesize.planesizerhp] )
    ax.set_ylim( [-10**planesize.planesizeimg, +10**planesize.planesizeimg] )

    # plot origin lines
    ax.plot( [ -10**planesize.planesizelhp, +10**planesize.planesizerhp ], [ 0, 0 ], color=colorscheme.originlines )
    ax.plot( [ 0, 0 ], [ -10**planesize.planesizeimg, +10**planesize.planesizeimg ], color=colorscheme.originlines )

    # ticks, gridlines
    lefthalf   = -10**( np.arange( planesize.startticklhp, planesize.planesizelhp, planesize.spacinglhp ) )
    righthalf  = +10**( np.arange( planesize.starttickrhp, planesize.planesizerhp, planesize.spacingrhp ) )
    tophalf    = -10**( np.arange( planesize.starttickimg, planesize.planesizeimg, planesize.spacingimg ) )
    bottomhalf = +10**( np.arange( planesize.starttickimg, planesize.planesizeimg, planesize.spacingimg ) )
    xticks = np.hstack( [lefthalf, np.hstack( [0, righthalf] ) ] )
    yticks = np.hstack( [bottomhalf, np.hstack( [0, tophalf] ) ] )
    ax.spines['bottom'].set_color( colorscheme.axisbackground )
    ax.spines['right'] .set_color( colorscheme.axisbackground )
    ax.spines['left']  .set_color( colorscheme.axisbackground )
    ax.spines['top']   .set_color( colorscheme.axisbackground )
    ax.tick_params( axis=u'both', which=u'both', length=0 )

    ax.xaxis.label.set_color( colorscheme.axistext )
    ax.yaxis.label.set_color( colorscheme.axistext )
    ax.tick_params( colors=colorscheme.axistext )

    if( ( not showticks ) and showgrid ):
        print( 'error! you are not allowed to ask for a grid without labels.')
        print( 'exiting!!!' )
        exit()

    if( showticks ):
        ax.xaxis.set_ticks( xticks )
        ax.yaxis.set_ticks( yticks )
    else:
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])

    if showgrid:
        ax.grid( showgrid, color=colorscheme.gridlines )

    # axis labels
    ax.set_xlabel( 'real' )
    ax.set_ylabel( 'imaginary' )

    # add base for line series to modify with spectrum
    l, = ax.plot( [], [],
                  linestyle='none',
                  markeredgecolor='none',
                  marker=markerform,
                  markersize=markersize,
                  color=markercolor )

    return fig, ax, l



def make_1d_plot(maxx = 1e16,
                 minx = 0,
                 maxy = 1e16,
                 miny = 0,
                 absAxisScale = 'linear',
                 ordAxisScale = 'linear',
                 xname = 'abscissa',
                 yname = 'ordinate',
                 colorscheme = PlotColorScheme(),
                 linecolor = jc.blueviolet_mah,
                 linewidth = 1,
                 showticks = True,
                 showgrid = True):

    # make the figure and put an axis on it
    fig = plt.figure()
    ax = fig.add_subplot( 111 )
    fig.patch.set_facecolor( colorscheme.figurebackground )
    ax.patch.set_facecolor( colorscheme.axisbackground )

    # axis scaling
    ax.set_xscale( absAxisScale )
    ax.set_yscale( ordAxisScale )

    # axis limits
    ax.set_xlim( [minx, maxx] )
    ax.set_ylim( [miny, maxy] )

    # ticks, gridlines
    # lefthalf   = -10**( np.arange( planesize.startticklhp, planesize.planesizelhp, planesize.spacinglhp ) )
    # righthalf  = +10**( np.arange( planesize.starttickrhp, planesize.planesizerhp, planesize.spacingrhp ) )
    # tophalf    = -10**( np.arange( planesize.starttickimg, planesize.planesizeimg, planesize.spacingimg ) )
    # bottomhalf = +10**( np.arange( planesize.starttickimg, planesize.planesizeimg, planesize.spacingimg ) )
    # xticks = np.hstack( [lefthalf, np.hstack( [0, righthalf] ) ] )
    # yticks = np.hstack( [bottomhalf, np.hstack( [0, tophalf] ) ] )
    ax.spines['bottom'].set_color( colorscheme.gridlines )
    ax.spines['right'] .set_color( colorscheme.axisbackground )
    ax.spines['left']  .set_color( colorscheme.gridlines )
    ax.spines['top']   .set_color( colorscheme.axisbackground )
    ax.tick_params( axis=u'both', which=u'both', length=0 )

    ax.xaxis.label.set_color( colorscheme.axistext )
    ax.yaxis.label.set_color( colorscheme.axistext )
    ax.tick_params( colors=colorscheme.axistext )

    # if( ( not showticks ) and showgrid ):
    #     print( 'error! you are not allowed to ask for a grid without labels.')
    #     print( 'exiting!!!' )
    #     exit()

    # if( showticks ):
    #     ax.xaxis.set_ticks( xticks )
    #     ax.yaxis.set_ticks( yticks )
    # else:
    #     ax.xaxis.set_ticklabels([])
    #     ax.yaxis.set_ticklabels([])

    if showgrid:
        ax.grid( showgrid, color=colorscheme.gridlines )

    # axis labels
    ax.set_xlabel( xname )
    ax.set_ylabel( yname )

    # add base for line series to modify with spectrum
    l, = ax.plot( [], [],
                  linestyle='-',
                  linewidth=linewidth,
                  color=linecolor )

    return fig, ax, l


def make_zeroD_time_plot_one_var( maxTime = 1e16,
                                  minTime = 0,
                                  maxOrdinateValue = 1e16,
                                  minOrdinateValue = 0,
                                  absAxisScale = 'linear',
                                  ordAxisScale = 'linear',
                                  abscissaName = 'time',
                                  ordinateName = 'ordinate',
                                  colorscheme = PlotColorScheme(),
                                  linecolor = jc.blueviolet_mah,
                                  linethickness = 1,
                                  showticks = True,
                                  showgrid = True ):

    # make the figure and put an axis on it
    fig = plt.figure()
    ax = fig.add_subplot( 111 )
    fig.patch.set_facecolor( colorscheme.figurebackground )
    ax.patch.set_facecolor( colorscheme.axisbackground )

    # axis scaling
    ax.set_xscale( absAxisScale )
    ax.set_yscale( ordAxisScale )

    # axis limits
    ax.set_xlim( [minTime, maxTime] )
    ax.set_ylim( [minOrdinateValue, maxOrdinateValue] )

    # ticks, gridlines
    # lefthalf   = -10**( np.arange( planesize.startticklhp, planesize.planesizelhp, planesize.spacinglhp ) )
    # righthalf  = +10**( np.arange( planesize.starttickrhp, planesize.planesizerhp, planesize.spacingrhp ) )
    # tophalf    = -10**( np.arange( planesize.starttickimg, planesize.planesizeimg, planesize.spacingimg ) )
    # bottomhalf = +10**( np.arange( planesize.starttickimg, planesize.planesizeimg, planesize.spacingimg ) )
    # xticks = np.hstack( [lefthalf, np.hstack( [0, righthalf] ) ] )
    # yticks = np.hstack( [bottomhalf, np.hstack( [0, tophalf] ) ] )
    ax.spines['bottom'].set_color( colorscheme.gridlines )
    ax.spines['right'] .set_color( colorscheme.axisbackground )
    ax.spines['left']  .set_color( colorscheme.gridlines )
    ax.spines['top']   .set_color( colorscheme.axisbackground )
    ax.tick_params( axis=u'both', which=u'both', length=0 )

    ax.xaxis.label.set_color( colorscheme.axistext )
    ax.yaxis.label.set_color( colorscheme.axistext )
    ax.tick_params( colors=colorscheme.axistext )

    # if( ( not showticks ) and showgrid ):
    #     print( 'error! you are not allowed to ask for a grid without labels.')
    #     print( 'exiting!!!' )
    #     exit()

    # if( showticks ):
    #     ax.xaxis.set_ticks( xticks )
    #     ax.yaxis.set_ticks( yticks )
    # else:
    #     ax.xaxis.set_ticklabels([])
    #     ax.yaxis.set_ticklabels([])

    if showgrid:
        ax.grid( showgrid, color=colorscheme.gridlines )

    # axis labels
    ax.set_xlabel( abscissaName )
    ax.set_ylabel( ordinateName )

    # add base for line series to modify with spectrum
    l, = ax.plot( [], [],
                  linestyle='-',
                  linewidth=linethickness,
                  color=linecolor )

    return fig, ax, l






def print_fig(fig, specpath, ext = 'pdf', dpi=1200):
    fig.savefig(specpath + '.' + ext, facecolor=fig.get_facecolor(), edgecolor='none', dpi=dpi, bbox_inches='tight' )

# prints pdf, svg, png, and tiff
def print_all4(fig, specpath, dpi=1200):
    print_fig(fig, specpath, 'pdf', dpi=dpi)
    print_fig(fig, specpath, 'svg', dpi=dpi)
    print_fig(fig, specpath, 'png', dpi=dpi)
    print_fig(fig, specpath, 'tiff', dpi=dpi)








def print_single_spectrum( fig,
                           line,
                           filepath,
                           outputpath = None,
                           ext = 'pdf' ):
    if( outputpath == None ):
        outputpath = filepath + '.' + ext
    realpart, imagpart = js.load_spectrum( filepath )
    line.set_data( realpart, imagpart )
    print_fig( fig, outputpath, ext )








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
        print_fig( fig, pngfolderpath + '/plot-' + str( i+1 ).zfill( 6 ), 'png', dpi=dpi )
        print( '- frame ' + str( i ) + ' of ' + str( nf ) + ' written' )
