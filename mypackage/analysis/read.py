# Read routine for analysis pictures

import numpy as np
from mypackage.plot import specs as sc

from mypackage.plot import plotfunctions as pf
from mypackage.run import runmodule as rm
from mypackage.run import pythonmodule as pm
from mypackage.analysis import variables as av

def read(model_name,dat,let,
         varname = 'kz_mean',
         befaft = 'aft',
         fdir = None,
         fname = None,
         nt = 10,
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
        Possibilities: 'kz_mean' 'kz_std','head_mean','lz_mean', 'temp_mean'

    nt : integer
        Number inside file name.

    fdir : string
        Full directory of vtk file.

    fname : string
        Full name of vtk file.
        
    Returns
    -------
    numpy_array : array
        Array containing the variable array

    numpy_array_name : string
        Containing proposed saving location for Array.
    """

    # Automatic file name generation
    if (not fdir and not fname):
        fdir = rm.make_output_dirs(model_name,dat,let)[2] # enkf_output_dir
        if befaft == 'aft':
            fname = rm.make_file_dir_names(model_name,nt)[19] # assim_out_file_aft
        elif befaft == 'bef':
            fname = rm.make_file_dir_names(model_name,nt)[18] # assim_out_file_bef

    # Get vtk_reader ##########################################################
    vtk_reader = pf.my_vtk(fdir,fname,varname)
    
    # Debug ###################################################################
    print(varname, vtk_reader.GetOutput().GetCellData().GetArray(0).GetValueRange())

    # Numpy Array  ############################################################
    numpy_array = pf.my_vtk_to_numpy(vtk_reader)

    # Numpy Array Name ########################################################
    numpy_array_name = pm.py_output_filename(av.tag,varname+'_'+str(nt).zfill(4),sc.specl(model_name,dat,let),"npy")
    
    return numpy_array, numpy_array_name
    
    
