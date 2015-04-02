#!/usr/bin/python

#Paths
python_dir = '/home/jk125262/PythonDir_Cluster'
output_files_dir    = '/home/jk125262/shematOutputDir_Cluster/'

# Modules
import sys                      # System variables (PYTHONPATH as list sys.path)
import os			# Operating system (os.chdir, os.path)
import exceptions  		# Raising exception (raise exceptions.RuntimeError)
from matplotlib import pyplot as plt
import vtk	  		# Adapt vtk to NumPy (vtk.util.numpy_support.vtk_to_numpy)
import string     		# Load alphabet (string.alphabet())

sys.path[0] = python_dir
from mypackage.run import runmodule as rm
from mypackage.plot import plotfunctions as pltfct
from mypackage.plot import myplots


# #Reload changed modules
# rm = reload(rm)                 

plt.close('all')

def pc(
model_name = myplots.mymodel_name,
date = myplots.mydate,
is_save_fig = 1,
is_show_fig = 1,
# 
suffix_start=rm.get_num_let(myplots.myletter),
n_l=1,
step_l = 1,
output = 'res',                  # 'res' 'std'
# 
save_letter = 'b', #letters[0]
# 
figure_size_x = 20.0,
figure_size_y = 11.8,
# 
title_text = None,
# 
n_rows = 2,
n_cols = 2,
# 
x_min = 0,
x_max = 10,
y_min = 0.30,
y_max = 0.66,
# 
bbox_loc = 'upper right',
bbox_anchor = (1.0,1.0),
# 
colored = None,
# 
marker_colors = None,
line_colors = None,
#
png_file_name = 'plot_compare'
):
    
    #############################################################################
    #Immediate variables
    suffix_end = suffix_start + (n_l)*step_l
    model_name_big = model_name.upper()
    alphabet=string.lowercase
    letters = [(alphabet[i/26-1]+alphabet[i%26] if i>25 else alphabet[i]) 
               for i in range(suffix_start,suffix_end,step_l)]
    
    letters_iterative = [(alphabet[i/26-1]+alphabet[i%26] if i>25 else alphabet[i]) 
                         for i in range(rm.get_num_let('el'),rm.get_num_let('fe')+1,1)]
    
    png_file_name= png_file_name + '_' + letters[0] + '_' + str(n_l) + '.png'
    save_fig_dir = output_files_dir + model_name +"_output/" + date + "/" \
        + date + "_" + save_letter + "/pics"
    

    getting_darker = [(float(i)/float(n_l),float(i)/float(n_l),float(i)/float(n_l)) for i in range(n_l)]
    getting_darker.reverse()
    
    changing_black_white = [(0,0,0) if i%2 else (0.5,0.5,0.5) for i in range(n_l)]


    if colored is None:
        colored = [i/2 for i in range(n_l)]
    if marker_colors is None:
        marker_colors = getting_darker
    if line_colors is None:
        line_colors = [myplots.color_arr[i/2] for i in range(n_l)]
    
    if output == 'res':
        if title_text is None:
            title_text = 'Residual ' + date
        var_name = 'rms_kz_aft'
        input_file_name = 'residual_E1.vtk'
    elif output  == 'std':
        if title_text is None:
            title_text = 'Stddevs ' + date
        var_name = 'std_kz_aft'
        input_file_name = 'stddev_E1.vtk'
    else:
        raise exceptions.RuntimeError, 'Wrong input_file_name.  ' + input_file_name



    residuals_dirs = [output_files_dir 
                      + model_name +"_output/" 
                      + date + "/" 
                      + date + "_" + letter + "/" 
                      + 'enkf_output' for letter in letters]

    #############################################################################
    #############################################################################
    #############################################################################
    #Checks
    for residuals_dir in residuals_dirs:
        if not pltfct.is_scalar_var_in_file(var_name, input_file_name, residuals_dir):
            raise exceptions.RuntimeError, 'var_name ' + var_name \
                + 'not in input_file_name ' + input_file_name \
                + 'in residuals_dir' + residuals_dir


    ############################################################################
    #Generate the figure
    fig = plt.figure(1, figsize=(figure_size_x,figure_size_y))
    fig.set_facecolor((0.50, 0.50, 0.50))
    #Generate the axis
    ax = fig.add_subplot(1,1,1)
    #ax.set_position([0.55,0.55,
    #                          0.35,0.35])
    ax.set_title(title_text,
                 fontsize = 25)
    ax.set_xlabel('obstime')
    ax.set_ylabel('Residuals')





    cell_numpy_x=[]
    cell_numpy_y=[]
    plot_letter=[]
    plot_label=[]

    for i,letter in enumerate(letters):
        os.chdir(residuals_dirs[i])
        reader=vtk.vtkRectilinearGridReader()
    #reader.ReadFromInputStringOn()
    #reader.SetInputString(in_str)
        reader.SetFileName(input_file_name)
        if letter in letters_iterative:
            reader.SetFileName('residual_E2.vtk')
        reader.SetScalarsName('obstime')
        reader.Update()
        cell_vtk_x = reader.GetOutput().GetCellData().GetArray(0)
        reader.SetScalarsName(var_name)

        reader.Update()
        cell_vtk_y = reader.GetOutput().GetCellData().GetArray(0)
    #num_cells = reader.GetOutput().GetNumberOfCells()
    #whole_extent = reader.GetOutput().GetExtent()
    #grid_bounds = reader.GetOutput().GetBounds()
    #grid_dims = reader.GetOutput().GetDimensions()
        cell_numpy_x.append(vtk.util.numpy_support.vtk_to_numpy(cell_vtk_x))
        cell_numpy_y.append(vtk.util.numpy_support.vtk_to_numpy(cell_vtk_y))
        len_arrays = len(cell_numpy_x[i])
        num_arrays = 20


    #Generate the plot
        plot_letter.append(ax.plot(cell_numpy_x[i],
                                   cell_numpy_y[i],
                                   color=line_colors[i] if colored[i] else 'grey', 
                                   linestyle='-',
                                   linewidth=2.5,
                                   marker='o',
                                   markerfacecolor=marker_colors[i], #if colored[i] else 'grey',
                                   markeredgecolor=marker_colors[i], #if colored[i] else 'grey',
                                   markersize=6))
                               #label='Mean')
        plot_label.append('Residuals ' + letter)
    #    for i_arr in range(num_arrays):
    #        reader.SetScalarsName('rm_kz_aft_' + str(i_arr+1))
    #        reader.Update()
    #        cell_vtk_y = reader.GetOutput().GetCellData().GetArray(0)
    #        cell_numpy_y= vtk.util.numpy_support.vtk_to_numpy(cell_vtk_y)
    #        plot_ens=plot_function = ax.plot(cell_numpy_x[i-1],
    #                                                  cell_numpy_y[i-1],
    #                                                  color='grey',
    #                                                  linestyle='-',
    #                                                  marker='',
    #                                                  markerfacecolor='grey',
    #                                                  markeredgecolor='grey',
    #                                                  markersize=6)
    #                                              #label='Ensemble')



    bbox_loc = 'upper right'
    bbox_anchor = (1.0,1.0)
    refined_legend=plt.legend(plot_letter,
                              plot_label,
                              title = 'Legend',
                              loc=bbox_loc,
                              bbox_to_anchor=bbox_anchor,
                              handlelength=2,
                              numpoints=2,
                              handletextpad=0.5,
                              ncol=6,
                              prop={'size':16})


    plt.axis([x_min,x_max,y_min,y_max])



    #Showing the figure with matplotlib
    if is_show_fig:
        plt.show()


    #Save the figure as png
    if is_save_fig:
        myplots.saving_fig(save_fig_dir,
                           [png_file_name],
                           [fig])

    os.chdir(python_dir)
    print('')
    print('Done with plot_compare')

