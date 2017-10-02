# Read routine for gaussianity arrays

import os
import numpy as np

from mypackage.plot import plotarrays as pa
from mypackage.run import pythonmodule as pm
from mypackage.gaussianity import arrays as ga

import exceptions

def read(which_method,
         n_syn = 10,
         n_comparisons = 1000,
         n_runs = 1000,
         model = 'wavebc',
         which_res = 'endres',
         enssize = 50,
):
    """
    Reads residual arrays at beginning (begres) or
    end (endres) of the EnKF run and calculates
    an array of means from random subsets of given
    size.

    Parameters
    ----------
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

    Returns
    -------
    gauss_array : array
        Array containing the means.

    gauss_array_name : string
        Containing proposed saving location for array.
    """

    # Checks
    if not n_runs in [100,1000]:
        raise exceptions.RuntimeError('n_runs wrong')
    if not model in ['wavebc','wave']:
        raise exceptions.RuntimeError('model wrong')

    if n_runs==1000:
        if not enssize in [50,70,100,250]:
            raise exceptions.RuntimeError('enssize wrong')
        if n_syn>1000:
            raise exceptions.RuntimeError('n_syn wrong')
    else:
        if not enssize in [500,1000,2000]:
            raise exceptions.RuntimeError('enssize wrong')
        if n_syn>100:
            raise exceptions.RuntimeError('n_syn wrong')


    # Load final residuals for all methods and the ensemblesize
    dats = pa.dats_dic[model][n_runs]
    lets = pa.lets_dic[model][n_runs]
    nums = pa.nums_dic[model][n_runs]

    res = np.load(pm.py_output_filename('dists',which_res,dats[which_method][enssize]+'_'+lets[which_method][enssize],'npy'))

    # Calculate mean array
    gauss_array = [np.mean(res[np.random.permutation(np.arange(nums[which_method][enssize]))[0:n_syn]]) for i in range(n_comparisons)]

    gauss_array_name = pm.py_output_filename(ga.tag,'meanarray_'+which_res,model+'_'+str(n_runs)+'_'+str(enssize)+'_'+str(n_syn)+'_'+str(n_comparisons)+'_'+str(which_method),'npy')

    return gauss_array, gauss_array_name

    
