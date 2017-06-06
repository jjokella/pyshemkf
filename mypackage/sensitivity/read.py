import os
import numpy as np
import exceptions
import mypackage.sensitivity.arrays as sa
from mypackage.plot import specs as sc
from mypackage.run import runmodule as rm
from mypackage.run import pythonmodule as pm

###############################################################################
#                        Read data for sensitivity analysis                   #
###############################################################################

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
    monitor_file = rm.make_file_dir_names(model_name)[16]

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

###############################################################################
#                              Sensitivity arrays                             #
###############################################################################

def mix(
        model_name,
        dat,
        let,
        length = 10,
        logspacing = False,
        is_diff = False
        ):
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
    num_mons = sc.num_mons(model_name,dat,let)
    nt = sc.nt(model_name,dat,let)

    # Sensitivy Letters
    slets = senselets(model_name,dat,let,length=length,logspacing=logspacing)

    # Empty sensitivity arrays
    if not is_diff:
        sense = np.zeros([nt,num_mons,length])
    else:
        sense = np.zeros([nt,num_mons/2,length])

    # Loop for letters/parameter values
    for il,slet in enumerate(slets):

        # Load temperature array
        temp = np.load(pm.py_output_filename(sa.tag,"truetemp",sc.specl(model_name,dat,slet),"npy"))

        if not is_diff:
            # Fill sense with temperature data
            sense[:,:,il] = temp[:,:]
        else:
            # Fill sense with temperature difference data
            for j in range(num_mons/2):
                sense[:,j,il] = temp[:,j] - temp[:,j+4]


    # Name
    if not is_diff:
        sense_name = pm.py_output_filename(sa.tag,"sense",sc.specl(model_name,dat,let),"npy")
    else:
        sense_name = pm.py_output_filename(sa.tag,"sensedt",sc.specl(model_name,dat,let),"npy")

    return sense, sense_name

###############################################################################
#                              Sensitivity curves                             #
###############################################################################

def nmix(
        model_name,
        dat,
        let,
        imons = 9
):

    # Specifier
    spec = sc.specl(model_name,dat,let)

    # Load array
    sense = np.load(pm.py_output_filename(sa.tag,
                                          "sense",
                                          spec,
                                          "npy"))

    # Calculation
    numsense = sense[:,imons,-1] - sense[:,imons,0]
    numsense_label = sa.sensitivity_varnames[spec] \
      + ", Unit:"+ str(sa.unit_numbers[spec])

    numsense_name = pm.py_output_filename(sa.tag,"numsense_"+str(imons).zfill(2),spec,"npy")
    numsense_label_name = pm.py_output_filename(sa.tag,"numsense_label_"+str(imons).zfill(2),spec,"npy")

    return numsense, numsense_name, numsense_label, numsense_label_name


###############################################################################
#                              Sensitivity Letters                            #
###############################################################################

def senselets(
        model_name,
        dat,
        let,
        length = 10,
        logspacing = False,
        ):

    # Full variable range
    frange = sa.varranges[sc.specl(model_name,dat,let)]

    # Sensitivity range
    vrange = sa.varranges_sense[sc.specl(model_name,dat,let)]

    # Find indices inside letters
    first=rm.get_num_let(let)
    beg = np.searchsorted(frange,vrange[0])
    end = np.searchsorted(frange,vrange[1])-1

    # Index array with stepsize
    if not logspacing:
        irange = np.linspace(beg,end,length,dtype=int)
    else:
        irange = np.logspace(np.log10(beg),np.log10(end),length,dtype=int)

    # Letter array
    senselets = [rm.get_let_num(first+i) for i in irange]

    return senselets
