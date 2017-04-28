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
         cb_ax,
         model_name,
         dat,
         let,
         is_grid = True,
         is_cb = True,
         is_mask = False,
         is_labels= True,
         is_ownticks = True,
         varname = 'uindex',                        #'head','v','temp','kz', 'uindex'
         v_component = 1,                           #0,1,2
         varlabels = {'temp':'Temperature [deg]',
                      'head':'Hydraulic Head [m] - 10m',
                      'uindex':'Unit Index'},
         xlims = [0.0,0.8032],
         ylims = [0.0,0.8032],
         maskvalue = 7,
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

    model_name : String
        String of model name.

    dat : String
        String with date of model run.

    let : String
        String of letter of model run.
    """
    # Read measurement locations
    locs = sc.locs(model_name,dat,let)

    # Read grid arrays from mypackage/plot/grids.py
    x = grids.x(model_name,dat,let)
    y = grids.y(model_name,dat,let)
    xticks = grids.xticks(model_name,dat,let)
    yticks = grids.yticks(model_name,dat,let)

    # Load variable array
    var = np.load(pm.py_output_filename(fa.tag,varname,spec,"npy"))

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
    ax.set_position([0.1,0.1,0.6,0.8])

    # Create image
    im = mpl.image.NonUniformImage(ax,interpolation='nearest',
                                       cmap=mycolors.cmap_discretize(cm.viridis,num_cbar),
                                       norm = colors.Normalize(vmin=low_cbar,
                                                                   vmax=high_cbar,
                                                                   clip=False))
    im.set_data(x,y,var)
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
    for i in range(len(locs)):
        ax.scatter(x[locs[i][0]-1],
                   y[locs[i][1]-1],
                   marker='o',
                   c='black',
                   s=50)

    # Title
    # ax.set_title('Temperature field')

    # Labels
    if is_labels:
        ax.set_xlabel('[m]',fontsize=40)
        ax.set_ylabel('[m]',fontsize=40)
        ax.tick_params(labelsize = 20)
    else:
        ax.set_yticklabels('')
        ax.set_xticklabels('')

    # Axis Limits
    ax.set_xlim(xlims[0],xlims[1])
    ax.set_ylim(ylims[0],ylims[1])

    # colorbar
    if is_cb:
        cb_ax.set_position([0.8,0.1,0.03,0.8])
        cb_ax.tick_params(labelsize = 20)
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


    # Figure name
    if varname == 'v':
        varname = varname+'_'+str(v_component)
    if is_mask:
        varname = varname+'_'+str(maskvalue).zfill(2)

    pic_name = pm.py_output_filename(fa.tag,varname,sc.specl(model_name,dat,let),pic_format)
    
    return ax, pic_name