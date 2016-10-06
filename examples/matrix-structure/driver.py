'''
This example shows how to load in a matrix from file and plot the structure (sparsity/spy)
'''

import matplotlib.pyplot as plt

import jalapeno.plots.colorscheme as jpc
import jalapeno.plots.plots as jpp
import jalapeno.colors.svgcolors as jcs
import jalapeno.data.matrix as jdm


# set up a figure with subplots
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax1.set(xlabel='c7 reduced')
ax2.set(xlabel='c7 detailed')
ax3.set(xlabel='c8')
ax4.set(xlabel='c7/c8 ref. fuel')

# load in the matrices
print('-- loading matrices...')
m1 = jdm.read_matrix_market('heptane-small.matrix')
m2 = jdm.read_matrix_market('heptane-big.matrix')
m3 = jdm.read_matrix_market('octane.matrix')
m4 = jdm.read_matrix_market('prf.matrix')
print('-- done loading matrices.')

# spy the matrix structures
print('-- plotting matrices...')
ax1.spy(m1, markersize=2, markeredgewidth=0, markerfacecolor=jcs.coral)
ax2.spy(m2, markersize=2, markeredgewidth=0, markerfacecolor=jcs.orangered)
ax3.spy(m3, markersize=2, markeredgewidth=0, markerfacecolor=jcs.aquamarine)
ax4.spy(m4, markersize=2, markeredgewidth=0, markerfacecolor=jcs.limegreen)
print('-- done plotting matrices.')

# color the figure
colorscheme = 'white'
jpc.FigColors.scheme(colorscheme).apply(fig)
for ax in [ax1, ax2, ax3, ax4]:
    jpc.FigColors.scheme(colorscheme).apply(ax=ax)

# size the figure
jpp.SquareFigure.forjournal(columns=2, standard='nature').set_size(fig)

# produce the figures with different color schemes
print('-- writing figure to file...')
jpp.print_fig_to_pdf(fig, 'spy')
print('-- done writing figure to file.')
