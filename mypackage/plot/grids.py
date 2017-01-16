#!/usr/bin/python

# Operating system commands
import os
from os import path
import exceptions
import sys
import time
import atexit

import math
import numpy as np
import numpy.random as rnd
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.colors as colors
from mpl_toolkits.axes_grid import make_axes_locatable

from mypackage.run import runmodule as rm

import pylab
import vtk
from vtk.util.numpy_support import vtk_to_numpy

import re
import string

def x(model_name,dat,let):
    """
    Read model name and return the corresponding
    array of x-coordinates of cell centers.
    """
    delxarr = delx(model_name,dat,let)
    arr = np.array([np.sum(delxarr[:i])+0.5*delxarr[i] for i in range(delxarr.size)])
    return arr


def y(model_name,dat,let):
    """
    Read model name and return the corresponding
    array of y-coordinates of cell centers.
    """
    delyarr = dely(model_name,dat,let)
    arr = np.array([np.sum(delyarr[:i])+0.5*delyarr[i] for i in range(delyarr.size)])
    return arr

def xticks(model_name,dat,let):
    """
    Read model name and return the corresponding
    array of x-coordinates of left side of cells.
    """
    delxarr = delx(model_name,dat,let)
    arr = np.array([np.sum(delxarr[:i]) for i in range(delxarr.size+1)])
    return arr

def yticks(model_name,dat,let):
    """
    Read model name and return the corresponding
    array of y-coordinates of front side of cells.
    """
    delyarr = dely(model_name,dat,let)
    arr = np.array([np.sum(delyarr[:i]) for i in range(delyarr.size+1)])
    return arr

def delx(model_name,dat,let):
    """
    Read model name, output date and letter and
    return the corresponding array of cell lengths
    in x-direction.
    """
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'

    try:
        input_file = rm.make_file_dir_names(model_name)[2]
        line = rm.read_hashtag_input(output_path+input_file,'# delx',1)
    except:
        input_file = rm.make_file_dir_names(model_name)[4]
        line = rm.read_hashtag_input(output_path+input_file,'# delx',1)

    num_entries = len(str.split(line))
    nums = [int(  str.split(str.split(line)[i],"*")[0]) for i in range(num_entries)]
    lens = [float(str.split(str.split(line)[i],"*")[1]) for i in range(num_entries)]

    vec = [[lens[i] for j in range(nums[i]) ] for i in range(num_entries)]
    
    arr = np.array([num for elem in vec for num in elem])
    return arr

def dely(model_name,dat,let):
    """
    Read model name, output date and letter and
    return the corresponding array of cell lengths
    in y-direction.
    """
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'
    input_file = rm.make_file_dir_names(model_name)[2]

    try:
        input_file = rm.make_file_dir_names(model_name)[2]
        line = rm.read_hashtag_input(output_path+input_file,'# dely',1)
    except:
        input_file = rm.make_file_dir_names(model_name)[4]
        line = rm.read_hashtag_input(output_path+input_file,'# dely',1)

    num_entries = len(str.split(line))
    nums = [int(  str.split(str.split(line)[i],"*")[0]) for i in range(num_entries)]
    lens = [float(str.split(str.split(line)[i],"*")[1]) for i in range(num_entries)]

    vec = [[lens[i] for j in range(nums[i]) ] for i in range(num_entries)]
    
    arr = np.array([num for elem in vec for num in elem])
    return arr

