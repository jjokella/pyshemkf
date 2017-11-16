# Read routine for monitor arrays

import numpy as np
from mypackage.plot import specs as sc

from mypackage.plot import plotfunctions as pf
from mypackage.run import runmodule as rm
from mypackage.run import pythonmodule as pm
from mypackage.monitor import arrays as ma

import exceptions

def read(model_name,dat,let,
         fdir = None,
         fname = None,
         varname = 'uindex',
         num_mon = 1,
):
    """
    Reading monitor arrays from SHEMAT-Suite.

    Parameters
    ----------
    model_name : string
        String of model name.

    dat : string
        String with date of model run.

    let : string
        String of letter of model run.

    varname : string
        Variable name for array to be read.
        Possibilities: 'uindex' 'head','temp','kz', 'v'

    Returns
    -------
    numpy_array : array
        Array containing the monitor variable array

    numpy_array_name : string
        Containing proposed saving location for Array.
    """

    # Dirs
    if fdir == None:
        fdir = rm.make_output_dirs(model_name,dat,let)[1] # samples_output_dir
    if fname == None:
        fname = rm.make_file_dir_names(model_name)[16] # monitor_file

    # Read from monitor file ##################################################
    numpy_array = np.genfromtxt(fdir+'/'+fname,
                                dtype='f8',
                                comments='%',
                                usecols=(ma.varpos[varname]),
                                )
    # Reshape #################################################################
    num_mons = sc.num_mons(model_name,dat,let)
    if np.remainder(len(numpy_array),num_mons):
        raise exceptions.RuntimeError('Problem with num_mons')
    numpy_array = numpy_array.reshape(len(numpy_array)/num_mons, num_mons)
    numpy_array = numpy_array[:,num_mon-1]
    
    # Numpy Array Name ########################################################
    numpy_array_name = pm.py_output_filename(ma.tag,varname,sc.specl(model_name,dat,let)+'_'+str(num_mon),"npy")
    
    return numpy_array, numpy_array_name


