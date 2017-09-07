# Read routine for forward pictures

import numpy as np
from mypackage.plot import specs as sc

from mypackage.plot import plotfunctions as pf
from mypackage.run import runmodule as rm
from mypackage.run import pythonmodule as pm
from mypackage.forward import arrays as fa

def read(model_name,dat,let,
         varname = 'uindex',
):
    """
    Reading variable arrays from SHEMAT-Suite.

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
        Array containing the variable array

    numpy_array_name : string
        Containing proposed saving location for Array.
    """

    # Dirs
    fdir = rm.make_output_dirs(model_name,dat,let)[1] # samples_output_dir
    fname = rm.make_file_dir_names(model_name,1)[17] # time_out_file

    # Get vtk_reader ##########################################################
    vtk_reader = pf.my_vtk(fdir,fname,varname)
    
    # Debug ###################################################################
    if varname == 'v':
        print(varname, vtk_reader.GetOutput().GetPointData().GetArray(0).GetValueRange(0))
        print(varname, vtk_reader.GetOutput().GetPointData().GetArray(0).GetValueRange(1))
        print(varname, vtk_reader.GetOutput().GetPointData().GetArray(0).GetValueRange(2))
    else:
        print(varname, vtk_reader.GetOutput().GetPointData().GetArray(0).GetValueRange())

    # Numpy Array  ############################################################
    numpy_array = pf.my_vtk_to_numpy(vtk_reader)

    # Numpy Array Name ########################################################
    numpy_array_name = pm.py_output_filename(fa.tag,varname,sc.specl(model_name,dat,let),"npy")
    
    return numpy_array, numpy_array_name
    
    
