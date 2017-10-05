# Sort routine for errorplot arrays

import os
import numpy as np
from mypackage.plot import specs as sc

from mypackage.plot import plotfunctions as pf
from mypackage.run import runmodule as rm
from mypackage.run import pythonmodule as pm
from mypackage.errorplot import arrays as ea

import exceptions

def sort(which_methods,
         indsort = None,
         n_runs = 1000,
         model = 'wavebc',
         which_res = 'endres',
         stat_method = 'mean',
         template_which_methods = [0,1,2,3,4,5,6],
         template_which_res = 'endres',
         template_stat_method = 'mean',
         template_n_runs = 1000,
         template_model = 'wavebc',
         template_enssize = 0,
):
    """
    Reads a template array and sorts the indices. Then it
    sorts the specified stat_array in the same order.

    Parameters
    ----------
    which_methods : array int
        Array of integers containing the method specifiers
        from module plotarrays.

    n_runs : integer
        1000 - typically exist for ensemble sizes 50, 70, 100, 250
        100 - typically exist for ensemble sizes 500, 1000, 2000

    model : string
        'wavebc' - Model wavebc
        'wave' - Model wave

    which_res : string
        'endres' - use residuals after EnKF run
        'begres' - use residuals before EnKF run

    stat_method : string
        'mean' - Calculate means
        'std' - Standard deviation
        'stdm' - Standard deviation of the mean
        'median' - Median or 50 Percentile
        'q25' - 25 Percentile
        'q75' - 75 Percentile

    template_n_runs : integer
        1000 - typically exist for ensemble sizes 50, 70, 100, 250
               template
        100 - typically exist for ensemble sizes 500, 1000, 2000
              template

    template_model : string
        'wavebc' - Model wavebc for template
        'wave' - Model wave for template

    template_which_methods : array int
        Array of integers containing the method specifiers
        from module plotarrays for the template array.

    template_which_res : string
        Specified of the template array.
        'endres' - use residuals after EnKF run
        'begres' - use residuals before EnKF run

    template_stat_method : string
        Specified of the template array.
        'mean' - Calculate means
        'std' - Standard deviation
        'stdm' - Standard deviation of the mean
        'median' - Median or 50 Percentile
        'q25' - 25 Percentile
        'q75' - 75 Percentile

    Returns
    -------
    stat_array : array
        Array containing the statistical measures (sorted).

    stat_array_name : string
        Containing proposed saving location for array (sorted).

    indsort : array of ints
        Array sorted indices.
    """


    if not indsort:
        # Load template array for sorting (only one ensemble size)
        template_array_name = pm.py_output_filename(ea.tag,template_which_res,template_stat_method+'_'+str(template_n_runs)+'_'+template_model+'_'+'_'.join([str(i) for i in template_which_methods]),'npy')
        template_array = np.load(template_array_name)[:,template_enssize]
        # Indices for sorting order
        indsort = np.argsort(template_array)

    # Load to be sorted array
    stat_array = np.load(pm.py_output_filename(ea.tag,which_res,stat_method+'_'+str(n_runs)+'_'+model+'_'+'_'.join([str(i) for i in which_methods]),'npy'))

    # Sort array
    for i in range(stat_array.shape[1]):
        stat_array[:,i] = np.array(stat_array)[:,i][indsort]

    # Save name for sorted array
    stat_array_name = pm.py_output_filename(ea.tag,which_res,stat_method+'_'+str(n_runs)+'_'+model+'_'+'_'.join([str(i) for i in indsort]),'npy')

    return stat_array, stat_array_name, indsort
