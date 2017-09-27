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

    # Load sort array
    if not indsort:
        template_str_1000 = '1000' if template_is_1000 else ''
        template_str_wavebc = 'wavebc' if template_is_wavebc else ''
        sort_array_name = pm.py_output_filename(ea.tag,template_which_res,template_stat_method+template_str_1000+'_'+template_str_wavebc+'_'+'_'.join([str(i) for i in template_which_methods]),'npy')
        sort_array = np.load(sort_array_name)[:,template_enssize]
        indsort = np.argsort(sort_array)

    # Load to be sorted array
    str_1000 = '1000' if is_1000 else ''
    str_wavebc = 'wavebc' if is_wavebc else ''
    stat_array = np.load(pm.py_output_filename(ea.tag,which_res,stat_method+str_1000+'_'+str_wavebc+'_'+'_'.join([str(i) for i in which_methods]),'npy'))
    
    # Sort array
    for i in range(stat_array.shape[1]):
        stat_array[:,i] = np.array(stat_array)[:,i][indsort]

    # Save name
    stat_array_name = pm.py_output_filename(ea.tag,which_res,stat_method+str_1000+'_'+str_wavebc+'_'+'_'.join([str(i) for i in indsort]),'npy')
    
    return stat_array, stat_array_name, indsort
