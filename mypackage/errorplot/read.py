# Read routine for errorplot arrays

import os
import numpy as np
from mypackage.plot import specs as sc

from mypackage.plot import plotfunctions as pf
from mypackage.plot import plotarrays as pa
from mypackage.run import runmodule as rm
from mypackage.run import pythonmodule as pm
from mypackage.errorplot import arrays as ea

import exceptions

def read(which_methods,
         is_1000 = True,
         is_wavebc = True,
         which_res = 'endres',
         stat_method = 'mean',
):
    """
    Reads residual arrays at beginning (begres) or
    end (endres) of the EnKF run and calculates
    an array of given statistical measure.

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

    Returns
    -------
    stat_array : array
        Array containing the statistical measures.

    stat_array_name : string
        Containing proposed saving location for array.
    """

    # Input check
    if not which_res in ['endres','begres']:
        raise exceptions.RuntimeError("which_res has to be 'endres' or 'begres'")
    if not stat_method in ['mean','std','stdm','median','q25','q75']:
        raise exceptsion.RuntimeError("stat_method wrong")

    # Nunber of methods
    num_methods = len(which_methods)
    
    # Number of ensemble sizes
    num_ensemble_sizes = ((4 if is_1000 else 3) if is_wavebc else (4 if is_1000 else 7))

    # Initialize plotarrays arrays
    dats = ((pa.dats1000_wavebc if is_1000 else pa.dats_wavebc)
                if is_wavebc else (pa.dats1000 if is_1000 else pa.dats))
    lets = ((pa.lets1000_wavebc if is_1000 else pa.lets_wavebc)
                if is_wavebc else (pa.lets1000 if is_1000 else pa.lets))
    nums = ((pa.nums1000_wavebc if is_1000 else pa.nums_wavebc)
                if is_wavebc else (pa.nums1000 if is_1000 else pa.nums))

    # Initialize stat_array
    stat_array = np.zeros([num_methods,num_ensemble_sizes])

    # i_kind: counter
    # j_kind: method-index
    for i_kind, j_kind in enumerate(which_methods):
        for j in range(num_ensemble_sizes):

            # Get date and time
            dat = dats[j_kind][j]
            let = lets[j_kind][j]
            num = nums[j_kind][j]
            
            # Read residuals
            res = np.load(pm.py_output_filename('dists',which_res,dat+'_'+let,'npy'))

            # Calculate statistical quantitiy
            if stat_method == 'mean':
                stat_array[i_kind,j] = np.mean(res)
            elif stat_method == 'std':
                stat_array[i_kind,j] = np.std(res)
            elif stat_method == 'stdm':
                stat_array[i_kind,j] = np.std(res)/np.sqrt(num)
            elif stat_method == 'median':
                stat_array[i_kind,j] = np.percentile(res,50)
            elif stat_method == 'q25':
                stat_array[i_kind,j] = np.percentile(res,25)
            elif stat_method == 'q75':
                stat_array[i_kind,j] = np.percentile(res,75)
                

    # Name of the array
    str_1000 = '1000' if is_1000 else ''
    str_wavebc = 'wavebc' if is_wavebc else ''
    stat_array_name = pm.py_output_filename(ea.tag,which_res,stat_method+str_1000+'_'+str_wavebc+'_'+'_'.join([str(i) for i in which_methods]),'npy')


    return stat_array, stat_array_name


