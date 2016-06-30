#!/usr/bin/python

# Modules
import sys                      # System variables (PYTHONPATH as list sys.path)
import os			# Operating system (os.chdir, os.path)
import exceptions  		# Raising exception (raise exceptions.RuntimeError)
import time       		# Timing the execution (time.time(), time.clock())
import numpy as np     		# Numerical Python 
import matplotlib as mpl           	# Matplotlib
from matplotlib import pyplot as plt	# Plot commands (plt.show(), plt.close())
from matplotlib import cm		# Colormap commands (cm.get_cmap())
from matplotlib import colors	        # Normalize colors (colors.Normalize())
import vtk
import math	  		# Mathematical Functions (math.pi, math.sqrt())
import scipy as sp		# Scientific Python (sp.mean(), sp.cov())

# Paths
python_dir = os.environ['HOME']+'/PythonDir'

sys.path[0] = python_dir        # Set path to read mypackage
from mypackage.plot import plotfunctions as pltfct


def myaxgrid(fig,
             n_rows = 1,
             n_cols = 1,
             # grid_factor = 1,
             # left_pad = 0.045,
             # up_pad = 0.1,
             # plt_dims = [0.12,0.24], # width, height
             # pads = [0.01,0.04],     # horizontal pad, vertical pad
             x_ticks = None,
             y_ticks = None,
             tickssize = 20,
             # y_tickssize = 20,
             x_ticklabels = None,
             x_ticklabelssize = 30,
             y_ticklabels = None,
             y_ticklabelssize = 30,
             ):

    # width=plt_dims[0]*grid_factor
    # height=plt_dims[1]*grid_factor
    # pad_hori=pads[0]*grid_factor
    # pad_vert=pads[1]*grid_factor

    axgrid = [fig.add_subplot(n_rows,n_cols,i) for i in range(1,n_rows*n_cols+1)]
    
    for i in range(n_rows):
        for j in range(n_cols):

            # axgrid[i*n_cols+j].set_position([left_pad+j*(width+pad_hori), 
            #                                   1.0-up_pad-height-i*(height+pad_vert),
            #                                   width,
            #                                   height])


            if x_ticks:         # Set ticks
                axgrid[i*n_cols+j].xaxis.set_ticks(x_ticks)
            if y_ticks:
                axgrid[i*n_cols+j].yaxis.set_ticks(y_ticks)
            axgrid[i*n_cols+j].tick_params(labelsize = tickssize)

            if x_ticklabels:    # Set ticklabels
                axgrid[i*n_cols+j].xaxis.set_ticklabels(x_ticklabels if i==n_rows-1 else [], fontsize = x_ticklabelssize)
            elif i != n_rows-1:
                axgrid[i*n_cols+j].xaxis.set_ticklabels([],fontsize = x_ticklabelssize)
            if y_ticklabels:
                axgrid[i*n_cols+j].yaxis.set_ticklabels(y_ticklabels if j==0 else [],fontsize = y_ticklabelssize)
            elif j != 0:
                axgrid[i*n_cols+j].yaxis.set_ticklabels([],fontsize = y_ticklabelssize)
    
    return axgrid
