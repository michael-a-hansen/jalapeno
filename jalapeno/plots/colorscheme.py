"""@package jalapeno.plots.colorscheme

Use to control the colors of a figure, axis, legend, etc.

Details on implementation (the 'scheme' classmethod especially) forthcoming...
"""


class FigColorScheme:
    def __init__(self,
                 figbg='w',
                 axisbg='w',
                 legendbg='w',
                 axistext='k',
                 legendtext='k',
                 gridlines='k',
                 legendedge='k'):
        self.figbg = figbg
        self.axisbg = axisbg
        self.legendbg = legendbg
        self.axistext = axistext
        self.legendtext = legendtext
        self.gridlines = gridlines
        self.legendedge = legendedge

    @classmethod
    def scheme(cls, colorscheme='white', **kwargs):
        # if no colorscheme is given, default to white
        figbg = 'w'
        axisbg = 'w'
        legendbg = 'w'
        axistext = 'k'
        legendtext = 'k'
        gridlines = 'k'
        legendedge = 'k'

        if colorscheme == 'black':
            figbg = 'k'
            axisbg = 'k'
            legendbg = 'k'
            axistext = 'w'
            legendtext = 'w'
            gridlines = 'w'
            legendedge = 'w'
        elif colorscheme == 'crazy':
            figbg = 'r'
            axisbg = 'c'
            legendbg = 'm'
            axistext = 'k'
            legendtext = 'w'
            gridlines = 'b'
            legendedge = 'r'

        # allows overriding any colors, so one can say 'black' but also red legend text, for instance
        figbg = kwargs.get('figbg', figbg)
        axisbg = kwargs.get('axisbg', axisbg)
        legendbg = kwargs.get('legendbg', legendbg)
        axistext = kwargs.get('axistext', axistext)
        legendtext = kwargs.get('legendtext', legendtext)
        gridlines = kwargs.get('gridlines', gridlines)
        legendedge = kwargs.get('legendedge', legendedge)

        return cls(figbg, axisbg, legendbg, axistext, legendtext, gridlines, legendedge)

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

        legend = ax.get_legend()
        if legend is not None:
            legend.get_frame().set_facecolor(self.legendbg)
            legend.get_title().set_color(self.legendtext)
            legend.legendPatch.set_edgecolor(self.legendedge)
            labels = legend.get_texts()
            for label in labels:
                label.set_color(self.legendtext)
