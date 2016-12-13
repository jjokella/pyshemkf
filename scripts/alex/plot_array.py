import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy as sp
import numpy as np
# from mypackage.plot import plotfunctions as pf
# from mypackage.plot import plotarrays as pa
# from mypackage.run import runmodule as rm
import pandas as pd

from mypackage.plot import plotfunctions as pf
from mypackage.plot import mycolors
from mypackage.alex import gridfunctions as gf

# Input grid
delx_shem = '4*1.0 4*0.5 5*0.2 10*0.1 51*0.01 100*0.0032 50*0.01 10*0.1 5*0.2 4*0.5 4*1.0'
dely_shem = '4*1.0 4*0.5 5*0.2 10*0.1 50*0.01 100*0.0032 51*0.01 10*0.1 5*0.2 4*0.5 4*1.0'
# Change to lengths array
delxa = gf.s2n_array(delx_shem)
delya = gf.s2n_array(dely_shem)
# Change to coordinate array
delx = np.cumsum(delxa)
dely = np.cumsum(delya)
# Change to grid matrices
delxg,delyg = np.meshgrid(delx,dely)

# Variable array (typically temperature)
var_array = pf.my_vtk_to_numpy(os.environ['HOME']+'/shematModelsDir/alexplain_model/samples_output',
                               'ALEXPLAIN_final.vtk',
                               'kz')
os.chdir(os.environ['HOME']+'/PythonDir')
var_array = var_array.T

# Regular grid for imshow
xg,yg = np.mgrid[min(delx):max(delx):500j,min(dely):max(dely):500j]

resampled = mpl.mlab.griddata(delxg.flatten(),delyg.flatten(),var_array.flatten(),xg,yg, interp='linear')

plt.imshow(resampled,cmap=mycolors.cmap_discretize(cm.viridis,30))
plt.show()


# PROBLEM: varname = 'head' reads in q for some reason. May be problem of
# vtk-read-routine
