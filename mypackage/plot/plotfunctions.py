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

# Paths
python_dir = os.environ['HOME']+'/PythonDir'

alphabet = string.lowercase


def my_vtk_to_numpy(fdir,fname,varname):
    """
    Read array of variable varname from vtk-file fname 
    in directory fdir and output as  numpy array.
    """
    # Prepare vtk-Reader 
    os.chdir(fdir)                        #Directory
    reader=vtk.vtkRectilinearGridReader() #Reader
    reader.SetFileName(fname)             #Filename
    reader.SetScalarsName(varname)        #Variable name
    reader.Update()                       #Refresh

    # Grid properties
    grid_dims      = reader.GetOutput().GetDimensions() # Grid Dimensions
    grid_bounds    = reader.GetOutput().GetBounds() # Grid Bounds

    # Check if scalar variable is in vtk-file
    is_var_in_file(fdir,fname,varname)
    #Reshape array to grid geometry
    if grid_bounds[0] == 0.0:   # CELLS
        vtk_array = reader.GetOutput().GetCellData().GetArray(0) # 0: Scalar 
        # vtk_to_numpy and reshape
        numpy_array=vtk_to_numpy(vtk_array).reshape(grid_dims[0]-1,
                                                    1 if grid_dims[1]== 1 else grid_dims[1]-1)
    else:                       # POINTS
        vtk_array = reader.GetOutput().GetPointData().GetArray(0) # 0: Scalar
        # vtk_to_numpy and reshape
        numpy_array = vtk_to_numpy(vtk_array).reshape(grid_dims[0],grid_dims[1])

    return numpy_array


def vtk_grid_props(fdir,fname,varname):
    #Go to directory
    os.chdir(fdir)
    #Open vtk-Reader
    reader=vtk.vtkRectilinearGridReader()
    reader.SetFileName(fname)
    #Read NumPy array form vtk-file
    reader.SetScalarsName(varname)
    reader.Update()

    #Read attributes of the vtk-Array
    num_cells = reader.GetOutput().GetNumberOfCells()
    num_points = reader.GetOutput().GetNumberOfPoints()
    whole_extent = reader.GetOutput().GetExtent()
    grid_bounds = reader.GetOutput().GetBounds()
    grid_dims = reader.GetOutput().GetDimensions()

    #Grid information
    step_x = (grid_bounds[1]-grid_bounds[0])/(grid_dims[0]-1)
    step_y = (grid_bounds[3]-grid_bounds[2])/(grid_dims[1]-1)
    if grid_bounds[0] == 0.0:     # CELLS
        npts_x = grid_dims[0]-1
        npts_y = grid_dims[1]-1
        low_m_x = grid_bounds[0] + 0.5*step_x   # Middle of cells: first x cell
        high_m_x = grid_bounds[1] - 0.5*step_x  # Middle of cells: last x cell
        low_m_y = grid_bounds[2] + 0.5*step_y   # Middle of cells: first y cell
        high_m_y = grid_bounds[3] - 0.5*step_y  # Middle of cells: last y cell
        low_x = grid_bounds[0]       # Edge of cells: first x cell
        high_x = grid_bounds[1]      # Edge of cells: last x cell
        low_y = grid_bounds[2]       # Edge of cells: first y cell
        high_y = grid_bounds[3]      # Edge of cells: last y cell
    else:                       # POINTS
        npts_x = grid_dims[0]
        npts_y = grid_dims[1]
        low_m_x = grid_bounds[0]   # Middle of cells: first x cell
        high_m_x = grid_bounds[1]  # Middle of cells: last x cell
        low_m_y = grid_bounds[2]   # Middle of cells: first y cell
        high_m_y = grid_bounds[3]  # Middle of cells: last y cell
        low_x = grid_bounds[0] - 0.5*step_x  # Edge of cells: first x cell
        high_x = grid_bounds[1] + 0.5*step_x # Edge of cells: last x cell
        low_y = grid_bounds[2] - 0.5*step_y  # Edge of cells: first y cell
        high_y = grid_bounds[3] + 0.5*step_y # Edge of cells: last y cell

    # x = np.linspace(low_x, high_x, npts_x)
    # y = np.linspace(low_x, high_x, npts_y)
    # X, Y = np.meshgrid(x, y)

    return step_x, step_y, npts_x, npts_y, low_m_x, high_m_x, low_m_y, high_m_y, low_x, high_x, low_y, high_y


def make_arrows(ax,n_arrays,befaft,nrobs_int,arr_xvars,arr_yvars,color_arr):
    for n in range(n_arrays):
        if(n+1 in range(n_arrays)
           and befaft[n] == 'bef' 
           and befaft[n+1] == 'aft'):
            for i in range(nrobs_int):
                ax.annotate("",
                            xy=(arr_xvars[i],
                                arr_yvars[n+1][i]), #End point
                            xycoords = 'data',
                            xytext=(arr_xvars[i],
                                    arr_yvars[n][i]), # Start point
                            textcoords = 'data',
                            arrowprops = dict(arrowstyle='-|>',
                                              connectionstyle='arc3',
                                              linewidth=1.0,
                                              linestyle='solid',
                                              color = color_arr[0],
                                              mutation_scale=10.0
                                              ))
            for i in range(nrobs_int-1):
                ax.annotate("",
                            xy=(arr_xvars[i+1],
                                arr_yvars[n][i+1]), #End point
                            xycoords = 'data',
                            xytext=(arr_xvars[i],
                                    arr_yvars[n+1][i]), # Start point
                            textcoords = 'data',
                            arrowprops = dict(arrowstyle='-|>',
                                              connectionstyle='arc3',
                                              linewidth=1.0,
                                              linestyle='solid',
                                              color = color_arr[0],
                                              mutation_scale=10.0
                                              ))
    return ax


def make_quiver(fdir,fname,varname,ax):
    """
    Insert a field of arrows from vtk-file.
    """
    #Quiver
    os.chdir(fdir)# Go to directory
    reader=vtk.vtkRectilinearGridReader() # Open vtk-Reader
    reader.SetFileName(fname) # Give filename 
    reader.SetVectorsName(varname) # Give name of Vector quantity
    reader.Update() # Update the reader (might have been used before)

    num_points = reader.GetOutput().GetNumberOfPoints() # Get Number of Points
    grid_bounds = reader.GetOutput().GetBounds()        # Get Bounds (middle of cell (points))
    grid_dims = reader.GetOutput().GetDimensions()      # Get Dims (of middle of cells)
    v_vtk = reader.GetOutput().GetPointData().GetArray(1) # 1:Get Vector quantitiy

    step_x = (grid_bounds[1]-grid_bounds[0])/(grid_dims[0]-1)
    step_y = (grid_bounds[3]-grid_bounds[2])/(grid_dims[1]-1)
    npts_x = grid_dims[0]
    npts_y = grid_dims[1]
    npts_z = grid_dims[2]
    low_m_x = grid_bounds[0]   # Middle of cells: first x cell
    high_m_x = grid_bounds[1]  # Middle of cells: last x cell
    low_m_y = grid_bounds[2]   # Middle of cells: first y cell
    high_m_y = grid_bounds[3]  # Middle of cells: last y cell
    low_x = grid_bounds[0] - 0.5*step_x  # Edge of cells: first x cell
    high_x = grid_bounds[1] + 0.5*step_x # Edge of cells: last x cell
    low_y = grid_bounds[2] - 0.5*step_x  # Edge of cells: first y cell
    high_y = grid_bounds[3] + 0.5*step_x # Edge of cells: last y cell

    v = vtk_to_numpy(v_vtk) # vtk file to NumPy array
    vx = v[:,0].reshape(npts_x,npts_y) # Vector components resahped to grid
    vy = v[:,1].reshape(npts_x,npts_y)
    vz = v[:,2].reshape(npts_x,npts_y)
    x = np.arange(low_m_x,high_m_x+1,step_x) # Take middle of cells, incl the last cell
    y = np.arange(low_m_y,high_m_y+1,step_y)
    X, Y = np.meshgrid(x, y)
    ax.quiver(X,Y,vx,vy,scale=None)
    
    return ax

def get_nrobs_int(fname,path):
    """
    Deprecated: See specs.py
    """
    #Number of observations
    os.chdir(path)
    f = open(fname)
    n = 0
    for i in range(20):
        line = f.readline()
        if(line[0:11] == '# nrobs_int'):
            n = int(f.readline())
            break
    if(n == 0):
        raise exceptions.RuntimeError('# nrobs_int not found in first 20 lines of: \n'\
            + model_name_big + '.enkf')
    f.close()
    return n

def get_num_mons(fname,path):
    """
    Get the number of monitoring points
    from observations_MODEL.dat

    Deprecated: See specs.py
    """
    #Number of monitoring points
    os.chdir(path)
    f = open(fname)
    f.readline()
    line = f.readline()
    n = int(line.split()[2])
    f.close()
    return n
    
def get_mons_inds(fname, path, num_mons):
    os.chdir(path)
    arr = np.genfromtxt(fname,
                        dtype='f8',
                        comments='%',
                        usecols=(5,6,7)) # uindex
    return arr[0:num_mons]


def get_start_obs(fname, path):
    """
    Get the time step of the first observation
    from observations_MODEL.dat
    """
    os.chdir(path)
    try:
        f = open(fname, 'r')
    except:
        print('\n' + path + '\n')
        raise
        
    
    f.readline()
    line=f.readline()
    n = int(line.split()[0])
    f.close()
    return n
    
def get_diff_obs(fname, path, num_mons, start_obs):
    """
    Get the time step difference of the first two observations
    from observations_MODEL.dat
    """
    os.chdir(path)
    try:
        f = open(fname, 'r')
    except IOError:
        print('\n' + path + '\n')
        raise
    
    f.readline()
    f.readline()
    for i in range(num_mons):
        f.readline()

    line=f.readline()
    n = int(line.split()[0])-start_obs
    f.close()
    return n


def get_num_timesteps(fname, path, num_mons):
    """
    Get the number of timesteps from monitor file.
    """
    os.chdir(path)
    try:
        f = open(fname, 'r')
    except IOError:
        print('\n' + path + '\n')
        raise
    
    arr = np.genfromtxt(fname,
                        dtype='f8',
                        comments='%',
                        usecols=(0))
    
    f.close()
    n = len(arr)/num_mons -1
    return n

def is_var_in_file(path,fname,var, raise_io_error = 1, raise_var_error = 1,
                              only_scalar = 0, only_vector = 0):
    """
    Checks the existence of the file and whether var is a variable
    inside the file. Output: 1 if it is inside, 0 if it is not.
    By default, exceptions are raised if the variable is not inside
    the file.
    """
    # Check existence of file.
    try:
        f = open(path+'/'+fname,'r')
    except IOError:
        if raise_io_error:
            print('\n' + path + '\n')
            raise
        else:
            return 0
        
    # Check if variable is SCALAR and in file.
    if not only_vector:
        for line in f:
            if line.find('SCALARS ' + var) > -1:
                f.close()
                return 1
            elif line.find('SCALARS  ' + var) > -1:
                f.close()
                return 1
            elif line.find('SCALARS   ' + var) > -1:
                f.close()
                return 1
            elif line.find('SCALARS    ' + var) > -1:
                f.close()
                return 1
    f.seek(0)
    # Check if variable is VECTOR and in file.
    if not only_scalar:
        for line in f:
            if line.find('VECTORS ' + var) > -1:
                f.close()
                return 1
            elif line.find('VECTORS  ' + var) > -1:
                f.close()
                return 1
            elif line.find('VECTORS   ' + var) > -1:
                f.close()
                return 1
            elif line.find('VECTORS    ' + var) > -1:
                f.close()
                return 1
    if raise_var_error:
        raise exceptions.RuntimeError(var + ' not in ' + fname \
            + '\n Dir: ' + path)
    else:
        return 0


def get_cbar_high(var,m_kz_std_high,m_cbar_kz_high,m_cbar_kz_res_high,m_cbar_cor_high,m_cbar_lz_high):
    """
    Returns high and low values for certain variables.
    """
    if var == 'kz_mean' or var == 'kz':
        high = m_cbar_kz_high
    elif var == 'head_mean' or var == 'head':
        high = 30
    elif var == 'kz_std':
        high = m_kz_std_high
    elif var == 'kz_res':
        high = m_cbar_kz_res_high
    elif var in ['correlations000' + str(i) for i in range(1,7)]:
        high = m_cbar_cor_high
    elif var == 'lz_mean':
        high = m_cbar_lz_high
    else:
        raise exceptions.RuntimeError('Wrong variable ' + var \
            + ' use kz_mean or correlations000i')
    return high

def get_cbar_low(var,m_kz_std_low,m_cbar_kz_low,m_cbar_kz_res_low,m_cbar_cor_low,m_cbar_lz_low):
    """
    Returns high and low values for certain variables.
    """
    if var == 'kz_mean' or var == 'kz':
        low = m_cbar_kz_low
    elif var == 'head_mean' or var == 'head':
        low = 10
    elif var == 'kz_std':
        low = m_kz_std_low
    elif var == 'kz_res':
        low = m_cbar_kz_res_low
    elif var in ['correlations000' + str(i) for i in range(1,7)]:
        low = m_cbar_cor_low
    elif var == 'lz_mean':
        low = m_cbar_lz_low
    else:
        raise exceptions.RuntimeError('Wrong variable ' + var \
            + ' use kz_mean or correlations000i')
    
    return low

def m_input_check(nfiles,
                  input_file_name_stems,
                  assim_variables_dir,
                  samples_out_dir,
                  varnames, m_first, m_n_rows, m_n_cols,
                  m_diff, nrobs_int):
    #Check scalar variable in file
    return_value = [0 for i in range(nfiles)]
    for i in range(nfiles):
        if not (is_var_in_file(assim_variables_dir,
                                      input_file_name_stems[i] + str(m_first).zfill(4) + '.vtk',
                                      varnames[i],
                                      raise_io_error = 0)
                or
                is_var_in_file(samples_out_dir,
                                      input_file_name_stems[i] + str(m_first) + '.vtk',
                                      varnames[i],
                                      raise_io_error = 0)):
            if not is_var_in_file(assim_variables_dir,
                                         input_file_name_stems[i] + 'param_' + str(m_first).zfill(4) + '.vtk',
                                         varnames[i],):
                raise exceptions.RuntimeError('Variable  ' \
                    + varnames[i] + '  not in:\n' \
                    + assim_variables_dir + '/' \
                    + input_file_name_stems[i] + str(1).zfill(4) + '.vtk')
            else:
                return_value[i] = 1

    # Check npics
    npics = m_first + ((m_n_rows*m_n_cols-1)/nfiles)*m_diff
    if( npics > nrobs_int ):
        raise exceptions.RuntimeError('Too high number of observations called. Check '\
            + 'm_first, m_diff')
    

    return return_value



##########################################################################################
def ts_from_av(path,fname,befaft,var,cell,nrobs_int):
    """
    Output: Array containing values of var at
    cell for the nrobs_int observation times.

    Input:
       path:        string containing enkf_output path
       fname:       Function name until before 'bef' or 'aft'
       befaft:      'bef' or 'aft'
       var:         Variable name
       cell:        [i,j] cell indices
       nrobs_int:   Number of observation times.


    i0 = ... -1, because the reader 
                 counts points, not cells
    l  = ... -1, because the Python
                 array starts at 0"""

    os.chdir(path)
    #Open vtk-Reader
    reader=vtk.vtkRectilinearGridReader()
    arr = []
    for iobs in range(nrobs_int):
        #Set vtk-Reader
        reader.SetFileName(fname + befaft + '_' + str(iobs+1).zfill(4) + '.vtk')
        reader.SetScalarsName(var)
        reader.Update()
        #Read
        i0 = reader.GetOutput().GetDimensions()[0]-1
        vtk_arr = reader.GetOutput().GetCellData().GetArray(0)
        #Convert
        numpy_arr = vtk_to_numpy(vtk_arr)
        if iobs==0:
            #Linear index
            i = cell[0]
            j = cell[1]
            lin = (j-1)*(i0) + i - 1
        arr.append(numpy_arr[lin])
    return arr

def ts_from_cor(path,fname,refcell,refvar,befaft,var,cell,nrobs_int):
    """
    correlation_0022_0016_0001_0003_bef_0001.vtk

    Output: Array containing values of var at
    cell for the nrobs_int observation times.

    Input:
       path:        string containing enkf_output path
       fname:       Function name until before 'bef' or 'aft'
       refcell:     indices of reference cell (used in filename)
       refvar:      number of reference variable (used in filename)
       befaft:      'bef' or 'aft'
       var:         Variable name
       cell:        [i,j] cell indices
       nrobs_int:   Number of observation times.


    i0 = ... -1, because the reader 
                 counts points, not cells
    l  = ... -1, because the Python
                 array starts at 0"""

    os.chdir(path)
    #Open vtk-Reader
    reader=vtk.vtkRectilinearGridReader()
    fname = fname + str(refcell[0]).zfill(4) + '_' \
        + str(refcell[1]).zfill(4) + '_' \
        + str(refcell[2]).zfill(4) + '_' \
        + str(refvar).zfill(4) + '_'
    arr = []
    for iobs in range(nrobs_int):
        #Set vtk-Reader
        reader.SetFileName(fname + befaft + '_' + str(iobs+1).zfill(4) + '.vtk')
        reader.SetScalarsName(var)
        reader.Update()
        #Read
        i0 = reader.GetOutput().GetDimensions()[0]-1
        vtk_arr = reader.GetOutput().GetCellData().GetArray(0)
        #Convert
        numpy_arr = vtk_to_numpy(vtk_arr)
        if iobs==0:
            #Linear index
            i = cell[0]
            j = cell[1]
            lin = (j-1)*(i0) + i - 1
        arr.append(numpy_arr[lin])
    return arr

def ts_from_mon(path,fname,in_vars):
    """
    Output: Time series from monitoring file
            using np.genfromtxt
    
    Input:
          var: "time", "x", "y", "z","uindex", "i", "j", "k", 
               "head", "temp", "pres", "satn", "epot", "conc0001", 
               "vx", "vy", "vz", "bhpr" "kz"
               """
    os.chdir(path)
    arr = []
    for var in in_vars:
        n=-1
        str_vs = ["time", "x", "y", "z","uindex", "i", "j", "k", 
                  "head", "temp", "pres", "satn", "epot", "conc0001", 
                  "vx", "vy", "vz", "bhpr" "kz"]
        dtypes = ['f8','f8','f8','f8','i8','i8','i8','i8',
                  'f8','f8','f8','f8','f8','f8',
                  'f8','f8','f8','f8','f8']
        for i,str_v in enumerate(str_vs):
            if(str_v == var):
                n=i
        if(var == 'conc' or var == 'conc_mean'):
            n=13
        elif(var == 'kz' or var == 'kz_mean'):
            n=18
        if(n==-1):
            raise exceptions.RuntimeError('Variable not found.')


        arr.append( np.genfromtxt(fname,
                                  dtype=dtypes[n],
                                  comments='%',
                                  usecols=(n)))
    
    for i in range(len(arr)):
        if in_vars[i] == 'kz' or in_vars[i] == 'kz_mean':
            arr[i] = map(math.log10,arr[i])

    return np.array(arr)



def ts_from_as(path,fname,nrobs_int,var,mon_num):
    """
    Input:
        var: "meanS", "innov","obs_pert"
        """
    os.chdir(path)
    arr = []
    if(var == 'meanS' or var == 'innov'):
        for i in range(nrobs_int):
            f = open(fname[:-1] + str(i+101))
            arr_tmp = []
            for i in range(100):
                line = f.readline()
                if(var == 'meanS' and line[0:6] == ' meanS'):
                    line = f.readline()
                    arr_tmp=line.split()
                    arr_tmp=map(float,arr_tmp)
                    break
                elif(var == 'innov' and line[0:20] == '  Compute innovation'):
                    line = f.readline()
                    arr_tmp=line.split()
                    arr_tmp=map(float,arr_tmp)
                    break
            if(arr_tmp == []):
                raise exceptions.RuntimeError(var + 'not found in \n' + fname)
            arr.append(arr_tmp)
        arr = np.array(arr)
        arr = arr[:,mon_num]
        f.close()
    elif(var == 'obs_pert'):
        meanS = ts_from_as(path,fname,nrobs_int,'meanS',mon_num)
        innov = ts_from_as(path,fname,nrobs_int,'innov',mon_num)
        arr = meanS + innov
    else:
        raise exceptions.RuntimeError('Wrong variable specification: ' + var )
    return arr




def ts_from_sc(path,point_1,vbl_1,befaft_1,point_2,vbl_2,befaft_2,nrobs_int):

    os.chdir(path)
    corr = []
    fnames = ['','']
    for i in range(nrobs_int):
        fnames[0] = 'single_cell_E1_' + str(point_1[0]).zfill(4)\
            + '_' + str(point_1[1]).zfill(4)\
            + '_' + str(point_1[2]).zfill(4)\
            + '_' + str(vbl_1).zfill(4)\
            + '_' + befaft_1\
            + '_' + str(i+1).zfill(4)\
            + '.plt'
        fnames[1] = 'single_cell_E1_' + str(point_2[0]).zfill(4)\
            + '_' + str(point_2[1]).zfill(4)\
            + '_' + str(point_2[2]).zfill(4)\
            + '_' + str(vbl_2).zfill(4)\
            + '_' + befaft_2\
            + '_' + str(i+1).zfill(4)\
            + '.plt'
        data = []
        for fname in fnames:
            data.append(np.loadtxt(fname,skiprows = 5))
        
        len_1 = len(data[0])
        len_2 = len(data[1])
        if len_1 != len_2:
            raise exceptions.RuntimeError('Non compatible single cell arrays.')
        
        mean_1 = 0.0
        for k in range(len_1):
            mean_1 = mean_1 + data[0][k]
        mean_1 = mean_1/len_1
        
        mean_2 = 0.0
        for k in range(len_2):
            mean_2 = mean_2 + data[1][k]
        mean_2 = mean_2/len_2

        var_1 = 0.0
        for k in range(len_1):
            var_1 = var_1 + (data[0][k]-mean_1)*(data[0][k]-mean_1)
        var_1 = var_1/(len_1-1)

        var_2 = 0.0
        for k in range(len_2):
            var_2 = var_2 + (data[1][k]-mean_2)*(data[1][k]-mean_2)
        var_2 = var_2/(len_2-1)

        cov = 0.0
        for k in range(len_1):
            cov = cov +  (data[0][k]-mean_1)*(data[1][k]-mean_2)
        cov = cov/(len_1-1)
        
        corr.append(cov/(math.sqrt(var_1)*math.sqrt(var_2)))

    return corr


def f2_plot_input_checks(f2_num_arrays,f2_i_want,f2_j_want,f2_befaft,f2_y_variables,
                         f2_show_mons,f2_num_show_mons,f2_y_variables_mon,
                         f2_num_variables_mon,num_mons,f2_show_assimstp,f2_num_show_assimstp,
                         f2_mon_num_assimstp,f2_corr_letters,f2_corr_num_arrays,
                         f2_corr_i_want,f2_corr_j_want,f2_corr_befaft,f2_corr_y_variables):
    """
    Checks input of f2_plot for inconsistencies
    """

    if len(filter(lambda x: len(x)<f2_num_arrays,
                  [f2_i_want,f2_j_want,f2_befaft,f2_y_variables])):
        raise exceptions.RuntimeError('The arrays f2_i_want, f2_j_want, f2_befaft and'\
            + 'f2_y_variables are too short (at least one of them)')
        
    if len(filter(lambda x: not x in ['bef','aft'], f2_befaft)):
        raise exceptions.RuntimeError('Wrong f2_befaft (use bef,aft!)')

    # if len(filter(lambda x: not x in ['conc_mean','kz_mean'], f2_y_variables)):
    #     raise exceptions.RuntimeError, 'Wrong f2_y_variables (use conc_mean,kz_mean!)'

    if any([len(f2_show_mons)<f2_num_show_mons,
            len(f2_y_variables_mon)<f2_num_variables_mon]):
        raise exceptions.RuntimeError('f2_num_show_mons/f2_num_variables_mon is too short')

    if len(filter(lambda x: x>=num_mons or x<0,f2_show_mons[0:f2_num_show_mons])):
        raise exceptions.RuntimeError('Wrong monitoring point specification. Has to be'\
            + ' (including boundaries) between 0 and ' + str(num_mons-1) )

    if len(filter(lambda x: not x in ['kz_mean','conc_mean'], 
                  f2_y_variables_mon[0:f2_num_variables_mon])):
        raise exceptions.RuntimeError('Wrong f2_show_assimstp (choose from 1,2,3!)')
        
    if len(filter(lambda x: not x in [1,2,3], f2_show_assimstp[0:f2_num_show_assimstp])):
        raise exceptions.RuntimeError('Wrong f2_show_assimstp (choose from 1,2,3!)')

    if (len(f2_show_assimstp)<f2_num_show_assimstp 
        or len(f2_mon_num_assimstp)<f2_num_show_assimstp):
        raise exceptions.RuntimeError('f2_show_assimstp and f2_mon_num_assimstp should'\
            + ' be longer than f2_num_show_assimstp')
    if any([len(f2_corr_letters)<f2_corr_num_arrays,
            len(f2_corr_i_want)<f2_corr_num_arrays,
            len(f2_corr_j_want)<f2_corr_num_arrays,
            len(f2_corr_befaft)<f2_corr_num_arrays,
            len(f2_corr_y_variables)<f2_corr_num_arrays]):
        raise exceptions.RuntimeError('One corr array is shorter than f2_corr_num_arrays')

    
