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
    """
    Reading time and temperature arrays from output files.

    Parameters
    ----------
    model_name : string
        String of model name.

    dat : string
        String with date of model run.

    let : string
        String of letter of model run.

    varname : string
        String containing the name of the variable to be read in.
        Possibilities:
        - "t"
        - "temp"

    Returns
    -------
    var : array
        Containing variable time series.

    array_name : string
        Containing proposed saving location for var.
    """
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
    array_name = pm.py_output_filename(sa.tag,"true"+varname,sc.specl(model_name,dat,let),"npy")

    return var, array_name



def mix(model_name,dat,lets,is_diff = False):
    """
    Generating sensitivity array holding temperature (difference)
    profiles for varying parameter values.

    Parameters
    ----------
    model_name : string
        String of model name.

    dat : string
        String with date of model run.

    let : string
        String of letter of model run.

    is_diff : logical
        If yes, create an array of temperature differences.

    Returns
    -------
    sense : array
        Temperature profiles for different parameter values.

        sense(it,imons,ilet): Transient Temperature profiles (at locations,
        for different parameter values)

        sensedt(it,imons,ilet): Transient Temperature difference profiles
        (at locations, for different parameter values)

    sense_name : string
        String containing a proposed saving location for sense.
    """

    # Read model parameters
    num_mons = sc.num_mons(model_name,dat,lets[0])
    nt = sc.nt(model_name,dat,lets[0])

    # Empty sensitivity arrays
    if not is_diff:
        sense = np.zeros([nt,num_mons,len(lets)])
    else:
        sense = np.zeros([nt,num_mons/2,len(lets)])


    # Loop for letters/parameter values
    for il,let in enumerate(lets):

        # Load temperature array
        temp = np.load(pm.py_output_filename(sa.tag,"truetemp",sc.specl(model_name,dat,let),"npy"))

        if not is_diff:
            # Fill sense with temperature data
            sense[:,:,il] = temp[:,:]
        else:
            # Fill sense with temperature difference data
            for j in range(num_mons/2):
                sense[:,j,il] = temp[:,j] - temp[:,j+4]


    # Name
    if not is_diff:
        sense_name = pm.py_output_filename(sa.tag,"sense",sc.spec(),"npy")
    else:
        sense_name = pm.py_output_filename(sa.tag,"sensedt",sc.spec(),"npy")

    return sense, sense_name

