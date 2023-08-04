import ternary

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# list of angle files
N_angles = np.array([4, 16, 32, 64, 128, 256])
N_angles2 = np.array([64, 96, 128, 256])
#N_angles = N_angles2

#location = 


cmap = mpl.cm.viridis

# find scalaing inforamtion for all subplots
# sharing maxs and mins
all_mins = []
all_maxs = []

for i in range(N_angles.size):
    #open the data files
    with np.load('local_runs/runtimes_{}.npz'.format(N_angles[i])) as runs:
        runtime_ratio = runs['runtime_ratio']
    
    all_mins.append(np.min(runtime_ratio[:,3]))
    all_maxs.append(np.max(runtime_ratio[:,3]))
    
max_rat = np.max(all_maxs)
max_rat = 3.0
min_rat = np.min(all_mins)
#min_rat = 0.99


for i in range(N_angles.size):
    #open the data files
    with np.load('local_runs/runtimes_{}.npz'.format(N_angles[i])) as runs:
        runtime_ratio = runs['runtime_ratio']
        scale = runs['scale']

    figure, tax = ternary.figure(scale=scale)

    #make the data into a dictionary for ternery to understand
    data = dict()
    for p in range(runtime_ratio.shape[0]):
        data[(runtime_ratio[p,0], runtime_ratio[p,1], runtime_ratio[p,2])] = runtime_ratio[p,3]

    # i to 2D indices

    #ax =  #grid[i]
    # calling the ternary wraper
    

    #setting axis names and data
    hm = tax.heatmap(data=data, cmap=cmap, vmax=max_rat, vmin=min_rat, colorbar=False)


    tax.boundary(linewidth=2.0)
    #tax.gridlines(color="black", multiple=1, linewidth=0.25, ls='-')

    # get and set the custom ticks:
    N_ticks = 6
    tax.set_axis_limits({'b': [0.05, 1.0], 'l': [0.0, 0.95], 'r': [0.05, 10.0]})
    tax.get_ticks_from_axis_limits(multiple=N_ticks)
    tick_formats = {'b': "%.2f", 'r': "%.1f", 'l': "%.2f"}
    tax.set_custom_ticks(fontsize=9, offset=0.045, tick_formats=tick_formats, multiple=N_ticks)
    tax._redraw_labels()

    # labels
    #tax.set_title(r"S$_{{{}}}$".format(N_angles[i]), fontsize=18, y=1.13, pad=-14)
    tax.left_axis_label("scattering ratio [$\Sigma_s/\Sigma$]", offset=0.20, fontsize=10)
    tax.right_axis_label("mfp thickness [$\Sigma*\Delta x$]", offset=0.20, fontsize=10)
    tax.bottom_axis_label("time step [$\Delta t$]", offset=0.3, fontsize=10)

    # controling the matplotlib function
    tax.get_axes().axis('off')
    tax.clear_matplotlib_ticks()
    tax._redraw_labels()

    # adding color bar to the bottom
    #cbar = ax.cax.colorbar(hm)
    #cbar = grid.cbar_axes[0].colorbar(hm)

    cbar = figure.colorbar(hm, ax=tax.ravel().tolist())

    #norm = mpl.colors.Normalize(vmin=min_rat, vmax=max_rat)
    #figure.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax.ravel().tolist(), orientation='vertical', label='Speed Up')

    #figure.subplots_adjust(bottom=0.1, top=0.9, left=0.1, right=0.8,
    #                    wspace=0.02, hspace=0.02)
    #cb_ax = figure.add_axes([0.83, 0.1, 0.02, 0.8])
    #cbar = figure.colorbar(hm, cax=cb_ax)

    #plt.tight_layout()

    #plt.show()

    # saving
    plt.savefig('turns_S{}.png'.format(N_angles[i]), dpi=600)












