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

import arrays as ma

###############################################################################
#               Plot Nonuniform Image of Variable array                       #
###############################################################################

def plot(ax,
         model_name,
         dat,
         let,
         num_mon = 1,
         is_grid = True,
         is_labels= True,
         is_ownticks = True,
         varname = 'temp',                        #'head','v','temp','kz', 'uindex'
         position = [0.1,0.1,0.8,0.8],
         xlims = [0.0,26000.0],
         ylims = [15.0,22.0],
         # marker = 'o',
         # markersize=50,
         # markercolor='red',
         # markeralpha = 1.0,
         xlabelfontsize=40,
         ylabelfontsize=40,
         xownticks = [0.1+i*0.1 for i in range(9)],
         yownticks = [0.1+i*0.1 for i in range(9)],
         pic_format = 'pdf',                        # 'png','eps','pdf'
):
    """
    A plotting function for variable arrays in a NonUniformGrid.

    Parameters
    ----------
    ax : Axes
        The axes to draw to.

    model_name : string
        String of model name.

    dat : string
        String with date of model run.

    let : string
        String of letter of model run.

    Returns
    -------
    ax : Axes
        Axes containing image of variable array.

    pic_name : string
        Containing proposed saving location for Figure.
    """

    # Load variable array
    time = np.load(pm.py_output_filename(ma.tag,'time',sc.specl(model_name,dat,let)+'_'+str(num_mon),"npy"))
    var = np.load(pm.py_output_filename(ma.tag,varname,sc.specl(model_name,dat,let)+'_'+str(num_mon),"npy"))

    ax.plot(time,var)

    # Axis position
    ax.set_position(position)

    # Ticks
    if is_ownticks:
        ax.xaxis.set_ticks(xownticks)
        ax.yaxis.set_ticks(yownticks)

    # Grid
    if is_grid:
        ax.grid()

    # Title
    # ax.set_title('Temperature field')

    # Labels
    ax.set_xlabel('[m]',fontsize=xlabelfontsize, visible=is_labels)
    ax.set_ylabel('[m]',fontsize=ylabelfontsize, visible=is_labels)
    ax.tick_params(length = 20 if is_labels else 0)
    # ax.set_yticklabels(ax.get_yticklabels(),visible=is_labels)
    # ax.set_xticklabels(ax.get_xticklabels(),visible=is_labels)

    # Axis Limits
    ax.set_xlim(xlims[0],xlims[1])
    ax.set_ylim(ylims[0],ylims[1])

    # Figure name
    pic_name = pm.py_output_filename(ma.tag,varname,sc.specl(model_name,dat,let)+'_'+str(num_mon),pic_format)

    return ax, pic_name


