###############################################################################
#                        Read data for sensitivity analysis                   #
###############################################################################

import os
import numpy as np
import exceptions
import mypackage.sensitivity.arrays as sa
from mypackage.plot import specs as sc
from mypackage.run import runmodule as rm
from mypackage.run import pythonmodule as pm


def read(model_name,dat,let,varname="temp"):

    # Name of monitoring file
    monitor_file = rm.make_file_dir_names(sc.model_name)[16]

    # Read number monitoring points
    num_mons = sc.num_mons(model_name,dat,let)

    # Col 0 in obs_file: obstime
    # Col 9 in obs_file: Temperature
    if varname ==  "t":
        colnum = 0
    elif varname == "temp":
        colnum = 9
    else:
        raise exceptions.RuntimeError("varname must be t or temp")

    # Read variable
    var = np.genfromtxt(rm.make_output_dirs(model_name,dat,let)[1]+'/'+monitor_file,
                        dtype='f8', comments='%', usecols=(colnum))

    # Reshape arrays
    if varname == "t":
        var = var.reshape(len(var)/num_mons, num_mons)[:,0]
    elif varname == "temp":
        var = var.reshape(len(var)/num_mons, num_mons)

    # Array name
    array_name = pm.py_output_filename(sa.tag,"truet",sc.specl(model_name,dat,let),"npy")

    return var, array_name

