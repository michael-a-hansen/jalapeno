"""@package jalapeno.plots.colorscheme

Details forthcoming...
"""


class FigColorScheme:
    def __init__(self,
                 figbg='w',
                 axisbg='w',
                 axistext='k',
                 gridlines='k'):
        self.figbg = figbg
        self.axisbg = axisbg
        self.axistext = axistext
        self.gridlines = gridlines

    @classmethod
    def scheme(cls, colorscheme='white'):
        figbg = 'w'
        axisbg = 'w'
        axistext = 'k'
        gridlines = 'k'

        if colorscheme == 'black':
            figbg = 'k'
            axisbg = 'k'
            axistext = 'w'
            gridlines = 'w'
        elif colorscheme == 'crazy':
            figbg = 'r'
            axisbg = 'c'
            axistext = 'k'
            gridlines = 'b'

        return cls(figbg,axisbg,axistext,gridlines)

    def apply(self, fig, ax):
        fig.patch.set_facecolor(self.figbg)
        ax.patch.set_facecolor(self.axisbg)
        ax.spines['bottom'].set_color(self.axisbg)
        ax.spines['right'].set_color(self.axisbg)
        ax.spines['left'].set_color(self.axisbg)
        ax.spines['top'].set_color(self.axisbg)
        ax.xaxis.label.set_color(self.axistext)
        ax.yaxis.label.set_color(self.axistext)
        ax.title.set_color(self.axistext)
        ax.tick_params(colors=self.axistext)
        ax.xaxis.grid(color=self.gridlines)
        ax.yaxis.grid(color=self.gridlines)
        return fig, ax