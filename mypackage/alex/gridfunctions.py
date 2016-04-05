# Functions for manipulating grids for alexmodel

import os
import matplotlib as mpl
import scipy as sp
import numpy as np
import numpy.core.defchararray as npstr
# from mypackage.plot import plotfunctions as pf
# from mypackage.plot import plotarrays as pa
# from mypackage.run import runmodule as rm
import pandas as pd


# Shemat to numpy 
def s2n_array(delx_shem):
    """
    Read in shemat_suite input file string and give out
    numpy array containing the same information.
    """
    # Split string
    delx_shem = delx_shem.rsplit()
    delx_split = [delx_shem[i].rsplit("*") for i in range(len(delx_shem))]

    # Read integers and floats
    nums = np.array([np.int(delx_split[i][0]) for i in range(len(delx_split))])
    lens = np.array([np.float(delx_split[i][1]) for i in range(len(delx_split))])

    # Numpy array of dels
    delx_numpy = np.array([])
    for i in range(len(nums)):
        delx_numpy  = np.append(delx_numpy,lens[i]*np.ones(nums[i]))
 
    return delx_numpy

def n2s_array(delx_numpy):
    """
    Read in numpy cumsum array and give out the
    string to be put in the input file.
    """
    delx_shem = np.str(delx_numpy[0])
    delx_shem = npstr.add(delx_shem," ")
    for i in range(1,len(delx_numpy)):
        # delx_shem = npstr.add(delx_shem,np.str(delx_numpy[i]-delx_numpy[i-1]))
        delx_shem = npstr.add(delx_shem,np.str(delx_numpy[i]))
        delx_shem = npstr.add(delx_shem," ")

    return delx_shem
    
              
def n2s_points(xs,ys,vals,dummies):
    """
    Make an inputfile kind of list of points with 
    values behind (and zeros). The goal is to be
    able to do boundary condition input in Python.
    """
    n = xs.size
    pts_shem = np.str("")
    for i in range(n):
        pts_shem = npstr.add(pts_shem,np.str(xs[i]))
        pts_shem = npstr.add(pts_shem," ")
        pts_shem = npstr.add(pts_shem,np.str(ys[i]))
        pts_shem = npstr.add(pts_shem," ")
        pts_shem = npstr.add(pts_shem,np.str(ys[i]))
        pts_shem = npstr.add(pts_shem," ")
        pts_shem = npstr.add(pts_shem,np.str(vals[i]))
        pts_shem = npstr.add(pts_shem," ")
        pts_shem = npstr.add(pts_shem,np.str(dummies[i]))
        pts_shem = npstr.add(pts_shem," \n")

    return pts_shem

def s2n_points(pts_shem):
    """
    Read string with points from shemat input file and
    decompose to xs, ys, zs arrays.
    """
    

    
