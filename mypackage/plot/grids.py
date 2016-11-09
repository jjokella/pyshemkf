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

import pylab
import vtk
from vtk.util.numpy_support import vtk_to_numpy

import re
import string

def x(model_name):
    """
    Read model name and return the corresponding
    array of x-coordinates of cell centers.
    """
    delxarr = delx(model_name)
    arr = np.array([np.sum(delxarr[:i])+0.5*delxarr[i] for i in range(delxarr.size)])
    return arr


def y(model_name):
    """
    Read model name and return the corresponding
    array of y-coordinates of cell centers.
    """
    delyarr = dely(model_name)
    arr = np.array([np.sum(delyarr[:i])+0.5*delyarr[i] for i in range(delyarr.size)])
    return arr

def xticks(model_name):
    """
    Read model name and return the corresponding
    array of x-coordinates of left side of cells.
    """
    delxarr = delx(model_name)
    arr = np.array([np.sum(delxarr[:i]) for i in range(delxarr.size+1)])
    return arr

def yticks(model_name):
    """
    Read model name and return the corresponding
    array of y-coordinates of front side of cells.
    """
    delyarr = dely(model_name)
    arr = np.array([np.sum(delyarr[:i]) for i in range(delyarr.size+1)])
    return arr

def delx(model_name):
    """
    Read model name and return the corresponding
    array of cell lengths in x-direction.
    """
    if model_name == 'headbctest' or model_name == 'alexdiff' or model_name == 'alexdiffbig':
        vec = [[1.0 for i in range(4)],
                   [0.5 for i in range(4)],
                   [0.2 for i in range(5)],
                   [0.1 for i in range(10)],
                   [0.01 for i in range(51)],
                   [0.0032 for i in range(100)],
                   [0.01 for i in range(50)],
                   [0.1 for i in range(10)],
                   [0.2 for i in range(5)],
                   [0.5 for i in range(4)],
                   [1.0 for i in range(4)]]
    elif model_name == 'prescribedhead':
        vec = [[1.0 for i in range(31)]]
    elif model_name == 'cube':
        vec = [[0.01 for i in range(24)],
                   [0.0032 for i in range(101)],
                   [0.01 for i in range(24)]]
    elif model_name == 'cubey':
        vec = [[0.08 for i in range(3)],
                   [0.0096 for i in range(8)],
                   [0.0032 for i in range(53)],
                   [0.0096 for i in range(8)],
                   [0.08 for i in range(3)]]
    else:
        raise exceptions.RuntimeError('Model name not valid: '+model_name) 

    arr = np.array([num for elem in vec for num in elem])
    return arr

def dely(model_name):
    """
    Read model name and return the corresponding
    array of cell lengths in y-direction.
    """
    if model_name == 'headbctest' or model_name == 'alexdiff' or model_name == 'alexdiffbig':
        vec = [[1.0 for i in range(4)],
                   [0.5 for i in range(4)],
                   [0.2 for i in range(5)],
                   [0.1 for i in range(10)],
                   [0.01 for i in range(51)],
                   [0.0032 for i in range(100)],
                   [0.01 for i in range(50)],
                   [0.1 for i in range(10)],
                   [0.2 for i in range(5)],
                   [0.5 for i in range(4)],
                   [1.0 for i in range(4)]]
    elif model_name == 'prescribedhead':
        vec = [[1.0 for i in range(31)]]
    elif model_name == 'cube':
        vec = [[0.01 for i in range(24)],
                   [0.0032 for i in range(101)],
                   [0.01 for i in range(24)]]
    elif model_name == 'cubey':
        vec = [[0.08 for i in range(3)],
                   [0.0096 for i in range(8)],
                   [0.0032 for i in range(53)],
                   [0.0096 for i in range(8)],
                   [0.08 for i in range(3)]]
    else:
        raise exceptions.RuntimeError('Model name not valid: '+model_name) 

    arr = np.array([num for elem in vec for num in elem])
    return arr

