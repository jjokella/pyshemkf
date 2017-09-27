# Sort routine for errorplot arrays

import os
import numpy as np
from mypackage.plot import specs as sc

from mypackage.plot import plotfunctions as pf
from mypackage.plot import plotarrays as pa
from mypackage.run import runmodule as rm
from mypackage.run import pythonmodule as pm
from mypackage.errorplot import arrays as ea

import exceptions

def sort(which_methods,
         indsort = None,
         is_1000 = True,
         is_wavebc = True,
         which_res = 'endres',
         stat_method = 'mean',
         template_which_methods = [0,1,2,3,4,5,6],
         template_which_res = 'endres',
         template_stat_method = 'mean',
         template_is_1000 = True,
         template_is_wavebc = True,
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

    is_1000 : boolean
        True - Jobs/Ensemble Sizes for which 1000 runs exist
               typically, 50, 70, 100, 250
        False - Jobs/Ensemble Sizezs for which 100 runs exist
               typically, 500, 1000, 2000

    is_wavebc : boolean
        True - Model wavebc
        False - Model wave

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

    template_which_methods : array int
        Array of integers containing the method specifiers
        from module plotarrays for the template array.

    template_is_1000 : boolean
        Specified of the template array.
        True - Jobs/Ensemble Sizes for which 1000 runs exist
               typically, 50, 70, 100, 250
        False - Jobs/Ensemble Sizezs for which 100 runs exist
               typically, 500, 1000, 2000

    template_is_wavebc : boolean
        Specified of the template array.
        True - Model wavebc
        False - Model wave

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
        template_str_1000 = '1000' if template_is_1000 else ''
        template_str_wavebc = 'wavebc' if template_is_wavebc else ''
        template_array_name = pm.py_output_filename(ea.tag,template_which_res,template_stat_method+template_str_1000+'_'+template_str_wavebc+'_'+'_'.join([str(i) for i in template_which_methods]),'npy')
        template_array = np.load(template_array_name)[:,template_enssize]
        # Indices for sorting order
        indsort = np.argsort(template_array)

    # Load to be sorted array
    str_1000 = '1000' if is_1000 else ''
    str_wavebc = 'wavebc' if is_wavebc else ''
    stat_array = np.load(pm.py_output_filename(ea.tag,which_res,stat_method+str_1000+'_'+str_wavebc+'_'+'_'.join([str(i) for i in which_methods]),'npy'))

    # Sort array
    for i in range(stat_array.shape[1]):
        stat_array[:,i] = np.array(stat_array)[:,i][indsort]

    # Save name for sorted array
    stat_array_name = pm.py_output_filename(ea.tag,which_res,stat_method+str_1000+'_'+str_wavebc+'_'+'_'.join([str(i) for i in indsort]),'npy')

    return stat_array, stat_array_name, indsort
