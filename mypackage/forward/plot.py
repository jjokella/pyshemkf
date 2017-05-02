#!/usr/bin/python

# Plot routine for forward pics

import matplotlib as mpl
from matplotlib import cm            # Colormap commands (cm.get_cmap())
from matplotlib import colors
from matplotlib import pyplot as plt # ?
import numpy as np
import exceptions               # ?

from mypackage.run import pythonmodule as pm
from mypackage.plot import mycolors
from mypackage.plot import grids
from mypackage.plot import specs as sc

import arrays as fa

def plot(ax,
         model_name,
         dat,
         let,
         is_grid = True,
         is_mask = False,
         is_labels= True,
         is_ownticks = True,
         varname = 'uindex',                        #'head','v','temp','kz', 'uindex'
         v_component = 1,                           #0,1,2
         position = [0.1,0.1,0.6,0.8],
         xlims = [0.0,0.8032],
         ylims = [0.0,0.8032],
         alpha = 1.0,
         maskvalue = 7,
         loc_inds = range(16),
         markersize=50,
         markercolor='red',
         xlabelfontsize=40,
         ylabelfontsize=40,
         xownticks = [0.1+i*0.1 for i in range(9)],
         yownticks = [0.1+i*0.1 for i in range(9)],
         num_cbar = 7,
         low_cbar =  10.0285,
         high_cbar = 10.0304,
         auto_cbar = True,
         pic_format = 'pdf',                        # 'png','eps','pdf'
):
    """
    A plotting function for variable arrays in a NonUniformGrid.

    Parameters
    ----------
    ax : Axes
        The axes to draw to.

    cb_ax : Axes
        The axes for the colorbar.

    model_name : string
        String of model name.

    dat : string
        String with date of model run.

    let : string
        String of letter of model run.
    """
    # Read grid arrays from mypackage/plot/grids.py
    x = grids.x(model_name,dat,let)
    y = grids.y(model_name,dat,let)
    xticks = grids.xticks(model_name,dat,let)
    yticks = grids.yticks(model_name,dat,let)

    # Load variable array
    var = np.load(pm.py_output_filename(fa.tag,varname,sc.specl(model_name,dat,let),"npy"))

    if varname == 'v':
        var = var[:,:,v_component]
    if varname == 'head':
        var = var-10.0

    if auto_cbar:
        low_cbar = var.min()
        high_cbar = var.max()

    # # Possible Mask
    if is_mask:
        var = np.ma.array(var,mask = np.logical_or(var<maskvalue-0.5,var>maskvalue+0.5))

    # Axis position
    ax.set_position(position)

    # Create image
    im = mpl.image.NonUniformImage(ax,interpolation='nearest',
                                       cmap=mycolors.cmap_discretize(cm.viridis,num_cbar),
                                       norm = colors.Normalize(vmin=low_cbar,
                                                                   vmax=high_cbar,
                                                                   clip=False))
    im.set_data(x,y,var)
    im.set_alpha(alpha)
    ax.images.append(im)

    # Ticks
    if is_ownticks:
        ax.xaxis.set_ticks(xownticks)
        ax.yaxis.set_ticks(yownticks)
    else:
        ax.xaxis.set_ticks(xticks[1::10])
        ax.yaxis.set_ticks(yticks[1::10])

    # Grid
    if is_grid:
        ax.grid()

    # Monitoring Points

    # Read
    locs = sc.locs(model_name,dat,let)

    # Scatterplot
    for i in range(len(np.array(locs)[loc_inds])):
        ax.scatter(x[locs[loc_inds[i]][0]-1],
                   y[locs[loc_inds[i]][1]-1],
                   marker='o',
                   c=markercolor,
                   edgecolors=markercolor,
                   s=markersize)

    # Title
    # ax.set_title('Temperature field')

    # Labels
    ax.set_xlabel('[m]',fontsize=xlabelfontsize, visible=is_labels)
    ax.set_ylabel('[m]',fontsize=ylabelfontsize, visible=is_labels)
    ax.tick_params(length = 20 if is_labels else 0)
    ax.set_yticklabels(ax.get_yticklabels(),visible=is_labels)
    ax.set_xticklabels(ax.get_xticklabels(),visible=is_labels)

    # Axis Limits
    ax.set_xlim(xlims[0],xlims[1])
    ax.set_ylim(ylims[0],ylims[1])

    # Figure name
    if varname == 'v':
        varname = varname+'_'+str(v_component)
    if is_mask:
        varname = varname+'_'+str(maskvalue).zfill(2)

    pic_name = pm.py_output_filename(fa.tag,varname,sc.specl(model_name,dat,let),pic_format)
    
    return ax, pic_name


def cb(cb_ax,
       ax,
       varname = "uindex",
       varlabels = {'temp':'Temperature [deg]',
                    'head':'Hydraulic Head [m] - 10m',
                    'uindex':'Unit Index'},
       cb_ax_position = [0.8,0.1,0.03,0.8],
       labelsize = 20,
):

    im = ax.images[0]

    # colorbar
    cb_ax.set_position(cb_ax_position)
    cb_ax.tick_params(labelsize = labelsize)
    cb_ax.set_title(varlabels[varname], y =1.02, fontsize=40)
    mpl.colorbar.Colorbar(cb_ax, im)
    if varname == 'uindex':
        cb_ax.yaxis.set_ticklabels(["1: sand",
                                    "2: sand",
                                    "3: water",
                                    "4: water",
                                    "5: water",
                                    "6: water",
                                    "7: cement"])
        cb_ax.set_position([0.72,0.1,0.03,0.8])

    return cb_ax
