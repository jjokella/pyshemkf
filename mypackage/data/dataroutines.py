#!/usr/bin/python


import os
import numpy as np
import mypackage.plot.plotfunctions as pltfct
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm



def my_maskedarray(arr, ind_x = None, ind_y = None ):
    """
    Return the array arr with mask for the input indices
    """

    if ind_x != None and ind_y != None:
        masky = np.array([[ix in ind_x and iy in ind_y
                           for ix in range(arr.shape[0])]
                          for iy in range(arr.shape[1])])
        masky = np.logical_not(masky)
        arr = np.ma.array(arr, mask = masky)
            
    return arr

def my_subarray(arr, ind_x = None, ind_y = None):
    """
    Return array consisting only of the indices shown.
    """
    
    if ind_x != None and ind_y != None:
        arr = np.array([[arr[ix][iy] for ix in ind_x] for iy in ind_y])

    return arr





os.chdir('/home/jk125262/PythonDir_Cluster')



