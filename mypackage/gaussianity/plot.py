#!/usr/bin/python

# Plot routine for forward pics

import matplotlib as mpl
from matplotlib import cm            # Colormap commands (cm.get_cmap())
from matplotlib import colors
from matplotlib import pyplot as plt # ?
import numpy as np
import exceptions               # ?

from mypackage.run import pythonmodule as pm
from mypackage.plot import plotarrays as pa
from mypackage.plot import mycolors
from mypackage.plot import grids
from mypackage.plot import specs as sc

import arrays as ga



def hist(ax,
         n_syn = 10,
         n_comparisons = 1000,
         which_method = 0,
         n_runs = 1000,
         model = 'wavebc',
         which_res = 'endres',
         enssize = 50,
         is_std = 0,                         # Show std?
         n_bins = 100,
         # std_method = 'std',
         pic_format = 'pdf',      #'png' or 'eps' or 'svg' or 'pdf'
         # figpos = [0.15,0.3,0.8,0.6],               #xbeg, ybeg, xrange, yrange
         # ylims = [0.28,0.82],
         # yticks = [0.3,0.4,0.5,0.6,0.7,0.8],
         # num_pack = 4,                     # Number of methods in pack
         # formatsos = ['o','v','s','p','o','v','s','p'],
         # coleros = [(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),
         #                (1.0,1.0,1.0),(1.0,1.0,1.0),(1.0,1.0,1.0),(1.0,1.0,1.0)],
         # markersize = 10,
         # markeredgesize = 1.5,
         # fontleg = 30,                              #18
         # fonttit = 40,
         # fontlab = 40,
         # fonttic = 30,
             ):
    """
    A histogramming function for means of random subsets
    of given size.

    Parameters
    ----------
    ax : Axes
        The axes to draw to.

    which_method : int
        Integer containing the method specifier
        from module plotarrays.

    n_syn : integer
        Number of synthetic studies in mean calculation.

    n_comparisons : integer
        Number of means calculated.

    n_runs : integer
        1000 - typically exist for ensemble sizes 50, 70, 100, 250
        100 - typically exist for ensemble sizes 500, 1000, 2000

    model : string
        'wavebc' - Model wavebc
        'wave' - Model wave

    which_res : string
        'endres' - use residuals after EnKF run
        'begres' - use residuals before EnKF run

    n_bins : integer
        Number of bins of histogram

    Returns
    -------
    ax : Axes
        Axes containing histogram.

    pic_name : string
        Containing proposed saving location for Figure.
    """

    # Load means
    arr = np.load(pm.py_output_filename(ga.tag,'meanarray_'+which_res,model+'_'+str(n_runs)+'_'+str(enssize)+'_'+str(n_syn)+'_'+str(n_comparisons)+'_'+str(which_method),'npy'))

    # Histogram
    ax.hist(arr,n_bins,color = 'grey')

    # Saving location
    pic_name = pm.py_output_filename(ga.tag,'meanarray_'+which_res,model+'_'+str(n_runs)+'_'+str(enssize)+'_'+str(n_syn)+'_'+str(n_comparisons)+'_'+str(which_method),pic_format)

    return ax, pic_name
    
