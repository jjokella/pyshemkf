#!/usr/bin/python

import numpy as np

from mypackage.run import runmodule as rm
from mypackage.run import pythonmodule as pm
from mypackage.plot import specs as sc
import mypackage.sensitivity.arrays as sa

###############################################################################
#               Plot temperature curves for different parameters              #
###############################################################################

def plot(ax,
         model_name,
         dat,
         let,
         imons = 9,
         pic_format = 'pdf',              # png, eps, pdf
         xlims = [10,30*24*3600],
         ylims = [11,20],
     ):

    sense = np.load(pm.py_output_filename(sa.tag,"sense",sc.specl(model_name,dat,let),"npy"))
    t = np.load(pm.py_output_filename(sa.tag,"truet",sc.specl(model_name,dat,let),"npy"))

    pic_name_start = 'sense_'+str(imons).zfill(2)

    # Default behavior
    deflet = rm.get_let_num(rm.get_num_let(let) + np.searchsorted(sa.varranges[sc.specl(model_name,dat,let)],
                                                                         sa.default_values[sc.specl(model_name,dat,let)]))
    deftemp = np.load(pm.py_output_filename(sa.tag,"truetemp",sc.specl(model_name,dat,deflet),"npy"))


    # Title
    ax.set_title('Sensitivity: '+sa.sensitivity_varnames[sc.specl(model_name,dat,let)]
                 +' Unit: '+str(sa.unit_numbers[sc.specl(model_name,dat,let)])
                 +' ('+sa.unit_names[sa.unit_numbers[sc.specl(model_name,dat,let)]]+')',
                 size = 12)

    # Plot 
    for i in range(sense.shape[2]):
        ax.semilogx(t,sense[:,imons,i], 'o',
                    color = [1.0-i/float(sense.shape[2]),
                             1.0-i/float(sense.shape[2]),
                             1.0-i/float(sense.shape[2])], # White to black
                    markersize = 1.6,
                    markeredgewidth = 0.1)
    ax.semilogx(t,deftemp[:,imons], '-',
                color = 'black')

    # Labels
    ax.set_xlabel(r'Time',fontsize = 14, labelpad=0)
    ax.set_ylabel(r'Temperature [$ ^{\circ} C$]',fontsize = 14)
    ax.xaxis.set_ticks([10,60,600,3600,24*3600,10*24*3600])
    ax.xaxis.set_ticklabels(['10s','1min','10min','1h','1d','10d'])
    ax.set_xlim(xlims[0],xlims[1])
    ax.set_ylim(ylims[0],ylims[1])

    # Text
    ax.text(0.95,0.95,
            "White->Black: "+sa.sensitivity_ranges[sc.specl(model_name,dat,let)],
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            transform=ax.transAxes)
    
    ax.text(0.95,0.85,
            "Default: "+sa.default_strings[sc.specl(model_name,dat,let)],
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            transform=ax.transAxes)

    ax.text(0.95,0.75,
            "Measurement: "+sa.obs_longlabels[imons],
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            transform=ax.transAxes)

    # Picture name
    pic_name = pm.py_output_filename(sa.tag,pic_name_start,sc.specl(model_name,dat,let),pic_format)
    
    return ax, pic_name
