#!/usr/bin/python

# Paths
python_dir = '/home/jk125262/PythonDir_Cluster' 

# Modules
import os                            # Operating system (os.chdir, os.path)
import sys                      # System variables (PYTHONPATH as list sys.path)
import exceptions                    # Raising exception (raise exceptions.RuntimeError)
import numpy as np                   # Numerical Python (np.genfromtxt())
import matplotlib as mpl             # Matplotlib
from matplotlib import pyplot as plt # Plot commands (plt.show(), plt.close())
from matplotlib import cm            # Colormap commands (cm.get_cmap())
from matplotlib import colors        # Normalize colors (colors.Normalize())
import vtk                           # Adapt vtk to np (vtk.util.numpy_support.vtk_to_numpy)
from datetime import date            # Getting todays date
import time         # Timing the execution (time.time(), time.clock())

sys.path[0] = python_dir        # Set path to read mypackage
from mypackage.plot import plotfunctions as pltfct
from mypackage.plot import myplots
from mypackage.plot import mycolors

today = str(date.today().timetuple()[0]) + '_' + str(date.today().timetuple()[1]).zfill(2) \
    + '_' + str(date.today().timetuple()[2]).zfill(2) 


def pt(
model_name = myplots.mymodel_name,
date = myplots.mydate,
letter_true = myplots.myletter_true,
output_dir = 'samples_output',
input_file_name = None,
variable_name = 'tracer1',
is_show = 1,
is_save = 1,
low_cbar = 0.006,
high_cbar = 0.008,
cmap_cbar = cm.viridis,
num_cbar = 15,
low_cbar_single = -11.0,
high_cbar_single = -9.0,
num_cbar_single = 15,
obsnum_start = 2,               # This is just the index of the observation
obsnum_diff = 4,
obstimes_model = range(1,20), # Put in time output times from MODEL input file
save_png_fname = None,
save_png_dir = None,
figure_backgroundcolor = (0.5,0.5,0.5),
figure_size_x = 20.0,
figure_size_y = 11.8,
grid_loc = 'p',
n_rows = 2,
n_cols = 2,
grid_factor = 1.3,
left_space = 0.04,
upper_space = 0.10,
ax_main_titlefont = 30,
ax_main_ticksize = 30,
ax_main_labelsize = 30,
ax_main_labelpad = 30,
ax_main_legendtitle = r'Concentration [$\frac{mol}{L}$]',
ax_single_title = 'True Permeability Field',
ax_single_varname = 'kz',
ax_single_legendtitle = r'Permeability [$\log(\frac{1}{m^{2}})$]',
ax_single_titlefont=30,
ax_single_labelsize = 30,
ax_single_labelpad = 30,
ax_single_ticksize = 20,
ax_func_titlefont = 30,
ax_func_labelfont = 25,
ax_func_labelpad = 10,
ax_func_ticksize = 20,
ax_single_position = [0.550,0.100,0.400,0.350], # left, bottom, width, height
ax_function_position = [0.575,0.550,0.400,0.350], # left, bottom, width , height
ax_single_cbar_position = [0.550+0.32,0.100,0.010,0.350],
ax_single_scattersize = 200,
is_show_text = 0,
is_main = 1,
is_func = 1,
is_true = 1
):

    """
    -----------------------------------------------
    Description
    ----------------------------------------------
    Plots a number of figures describing the true model.

    
    -----------------------------------------------
    Input Variables
    ----------------------------------------------
    model_name                  # Name of the model
    date                        # Date of the output directory
    letter_true                 # Letter of the true for that date
    output_dir                  # Directory of output ('samples_output' for True)
    input_file_name             # Input file name with last number left out
    variable_name               # Variable to be sketched
    is_show                     # Show the plot (default 1)
    is_save                     # Save the plot (default 1)
    low_cbar                    # Minimum of colorbar range
    high_cbar                   # Maximum of colorbar range
    num_cbar                    # Number of colorbar steps
    low_cbar_single             # Minimum of colorbar range for single plot
    high_cbar_single            # Maximum of colorbar range for single plot
    num_cbar_single             # Number of colorbar steps for single plot
    obsnum_start                # First observation time plotted
    obsnum_diff                 # Difference between two observations plotted
    save_png_fname              # Name for the png file of the plot
    save_png_dir                # Directory of png file of plot
    figure_size_x               # x size of the figure
    figure_size_y               # y size of the figure
    grid_loc                    # 'p' for POINTS of 'c' for CELLS in vtk file
    n_rows                      # number of rows of figures
    n_cols                      # number of columns of figures
    grid_factor                 # Scale factor for single plot in grid of plots
    left_space                  # Space left of grid of plots
    upper_space                 # Space above the grid of plots
    ax_single_position          # Position of axis of single plot
    ax_function_position        # Position of axis of function plot
    is_show_text                # Possibly show text
    """

    plt.close('all')

    # Variable definitions
    model_name_big = model_name.upper() # Upper case model name

    if input_file_name is None:
        input_file_name = model_name_big + '_TRUE_E0_time_out_'    


    if save_png_fname is None:
        save_png_fname = input_file_name + 'pic.png' # Default function name for png

    if save_png_dir is None:
        save_png_dir = "/home/jk125262/shematOutputDir_Cluster/"\
            + model_name +"_output/"\
            + date + "/" \
            + "pics"            # Default saving directory

    image_width=0.24*grid_factor # image size according to factor
    image_height=0.24*grid_factor
    image_pad_hori=0.01*grid_factor
    image_pad_vert=0.04*grid_factor

    ######################################################################################
    ######################################################################################

    num_mons = pltfct.get_num_mons('observations_' + model_name_big + '.dat',
                                "/home/jk125262/shematOutputDir_Cluster/"
                                + model_name +"_output/" + date + "/" 
                                + date + "_" + letter_true) # Number of monitoring points
    
    cell_numpy_ind = pltfct.get_mons_inds(model_name_big + '_TRUE_E0_monitor_1.dat',
                                       "/home/jk125262/shematOutputDir_Cluster/"
                                       + model_name +"_output/" + date + "/"
                                       + date + "_" + letter_true + "/" + output_dir,
                                       num_mons) # Monitoring point indices

    color_arr = ['black',       # Standard color array
                 'darkred',(0,1,0),(0,0,1),
                 (1,1,0),(1,0,1),(0,1,1),
                 (0.5,0,0),(0,0.5,0),(0,0,0.5),
                 (0.5,0.5,0),(0.5,0,0.5),(0,0.5,0.5),
                 (1.0,0.5,0),(1.0,0,0.5),(0,1.0,0.5),
                 (0.5,1.0,0),(0.5,0,1.0),(0,0.5,1.0)]

    #Vertical space check
    if(n_rows*image_height+(n_rows-1)*image_pad_vert+upper_space > 1.0-upper_space):
        print(n_rows*image_height+(n_rows-1)*image_pad_vert+upper_space)
        print('>')
        print(1.0-upper_space)
        raise exceptions.RuntimeError('Too much vertical space used.')

    #Generate the figure
    fig = plt.figure(1, figsize=(figure_size_x,figure_size_y))
    fig.set_facecolor(figure_backgroundcolor)
    # plt.suptitle(input_file_name + ' ' + letter_true, y = 0.97, fontsize=20)

    ######################################################################################
    ############################# MAIN PLOT ##############################################
    ######################################################################################

    #Go to the general output directory
    os.chdir("/home/jk125262/shematOutputDir_Cluster/" + model_name +"_output/" + date + "/" \
             + date + "_" + letter_true + "/")
    #Create pics directory if not already existing
    if(not(os.path.exists('pics'))):
        os.mkdir('pics')
    #Go to the specific output directory
    os.chdir("./" + output_dir)
    #print(os.getcwd())

    #Open vtk-Reader
    reader = vtk.vtkRectilinearGridReader()
    reader.SetFileName(input_file_name + str(1).zfill(4) + '.vtk')
    #Read NumPy array from vtk-file
    reader.SetScalarsName(variable_name)
    reader.Update()

    if grid_loc == 'c':
        #Read cell data and data propertires
        cell_vtk_array = reader.GetOutput().GetCellData().GetArray(0)
        num_cells = reader.GetOutput().GetNumberOfCells()
        whole_extent = reader.GetOutput().GetExtent()
        grid_bounds = reader.GetOutput().GetBounds()
        grid_dims = reader.GetOutput().GetDimensions()
        #Convert to NumPy array
        cell_numpy_array = vtk.util.numpy_support.vtk_to_numpy(cell_vtk_array)
        #Array is given grid dimensions
        cell_numpy_array = cell_numpy_array.reshape(grid_dims[0]-1,grid_dims[1]-1)
    elif grid_loc == 'p':
        #Read point data and data properties
        cell_vtk_array = reader.GetOutput().GetPointData().GetArray(0)
        num_cells = reader.GetOutput().GetNumberOfCells()
        whole_extent = reader.GetOutput().GetExtent()
        grid_bounds = reader.GetOutput().GetBounds()
        grid_dims = reader.GetOutput().GetDimensions()
        #vtk-array converted to NumPy
        cell_numpy_array = vtk.util.numpy_support.vtk_to_numpy(cell_vtk_array)
        #Array given grid dimensions
        cell_numpy_array = cell_numpy_array.reshape(grid_dims[0],grid_dims[1])

    else:
        raise exceptions.RuntimeError('Wrong variable: grid_loc (c or p allowed)')

    #Properties of the grid
    step_x = (grid_bounds[1]-grid_bounds[0])/(grid_dims[0]-1)
    step_y = (grid_bounds[3]-grid_bounds[2])/(grid_dims[1]-1)
    if grid_loc == 'c':
        npts_x = grid_dims[0]-1
        npts_y = grid_dims[1]-1
    elif grid_loc =='p':
        npts_x = grid_dims[0]
        npts_y = grid_dims[1]
        # low_x = grid_bounds[0] + 0.5*step_x  #Middle of cells
        # high_x = grid_bounds[1] - 0.5*step_x  #Middle of cells
        # low_y = grid_bounds[2] + 0.5*step_y  #Middle of cells
        # high_y = grid_bounds[3] - 0.5*step_y  #Middle of cells
        low_x = grid_bounds[0] #Middle of cells
        high_x = grid_bounds[1] #Middle of cells
        low_y = grid_bounds[2]  #Middle of cells
        high_y = grid_bounds[3]  #Middle of cells
    # Grid array coordinates
    x = np.linspace(low_x, high_x, npts_x)
    y = np.linspace(low_x, high_x, npts_y)
    #Coordinate matrices from coordinate vectors
    X, Y = np.meshgrid(x, y)

    if is_main:

        # Text for figure
        step_x_string = '%10.1f' %step_x
        step_y_string = '%10.1f' %step_y
        npts_x_string = '%10.1f' %npts_x
        npts_y_string = '%10.1f' %npts_y
        low_x_string = '%10.1f' %low_x
        high_x_string = '%10.1f' %high_x
        low_y_string = '%10.1f' %low_y
        high_y_string = '%10.1f' %high_y
        #y_factor_string = '%10.1f' % y_factor
        #corr_string = '%10.1f' %corr_mat[0,1]
        #    text_string = 'Correlation: ' + str(corr_mat[0,1])[0:8]
        text_string = 'Step_x:  ' + step_x_string \
            + '\nStep_y: ' + step_y_string \
            + '\nNpts_x: ' + npts_x_string \
            + '\nNpts_y: ' + npts_y_string \
            + '\nLow_x:  ' + low_x_string \
            + '\nHigh_x: ' + high_x_string \
            + '\nLow_y:  ' + low_y_string \
            + '\nHigh_y: ' + high_y_string #\
        #    + '\nCorr_xy: ' + corr_string
        if is_show_text:
            text = fig.text(0.0,0.5,text_string,fontsize=16)
            text.set_bbox(dict(facecolor=(0.8,0.8,0.8), alpha=0.5))

        #Generate axes
        ax_grid = [fig.add_subplot(n_rows,n_cols,i) for i in range(1,n_rows*n_cols+1)]
        for i in range(n_rows):
            for j in range(n_cols):
                ax_grid[i*n_cols+j].set_position([left_space+j*(image_width+image_pad_hori), 
                                                  1.0-upper_space-image_height-i*(image_height+image_pad_vert),
                                                  image_width,
                                                  image_height])
                ax_grid[i*n_cols+j].tick_params(labelsize=ax_main_ticksize)
                x_axis = ax_grid[i*n_cols+j].xaxis
                y_axis = ax_grid[i*n_cols+j].yaxis
                if(i==n_rows-1):
                    x_axis.set_ticks([100.0, 200.0, 300.0, 400.0, 500.0])
                    ax_grid[i*n_cols+j].set_xlabel('x[$m$]',fontsize=ax_main_labelsize,labelpad=ax_main_labelpad)
                else:
                    x_axis.set_ticks([])
                if(j==0):
                    y_axis.set_ticks([100.0, 200.0, 300.0, 400.0, 500.0])
                    ax_grid[i*n_cols+j].set_ylabel('y[$m$]',fontsize=ax_main_labelsize,labelpad=ax_main_labelpad)
                else:
                    y_axis.set_ticks([])


        for i_subplt in range(n_rows*n_cols):

            os.chdir("/home/jk125262/shematOutputDir_Cluster/" \
                         + model_name +"_output/" \
                         + date + "/" \
                         + date + "_" + letter_true + "/" \
                         + output_dir)

            j_start = obsnum_start
            j_diff = obsnum_diff
            j_subplt = j_start + i_subplt*j_diff
            #Open vtk-Reader
            reader.SetFileName(input_file_name + str(j_subplt).zfill(4) + '.vtk')
            reader.SetScalarsName(variable_name)
            reader.Update()

            if grid_loc == 'c':
                # Read Cell data and convert to grid dimensions
                cell_vtk_array = reader.GetOutput().GetCellData().GetArray(0)
                cell_numpy_array = vtk.util.numpy_support.vtk_to_numpy(cell_vtk_array)
                cell_numpy_array = cell_numpy_array.reshape(npts_x,npts_y)
            elif grid_loc == 'p':
                # Read Point data and convert to grid dimensions
                cell_vtk_array = reader.GetOutput().GetPointData().GetArray(0)
                cell_numpy_array = vtk.util.numpy_support.vtk_to_numpy(cell_vtk_array)
                cell_numpy_array = cell_numpy_array.reshape(npts_x,npts_y)


            #Generate Image
            im = ax_grid[i_subplt].imshow(cell_numpy_array,
                                          interpolation='nearest',
                                          cmap = mycolors.cmap_discretize(cmap_cbar,num_cbar),
                                          # 'gray', 'rgb', 'rainbow', 'jet'
                                          norm = colors.Normalize(vmin=low_cbar,
                                                                  vmax=high_cbar,
                                                                  clip=False),
                                          origin='lower',
                                          extent=grid_bounds[0:4])

            #Title for image
            ax_grid[i_subplt].set_title(#'Time step # ' + str(j_subplt) + '\n'+
                                        't = '
                                        + str(obstimes_model[j_subplt-1]).zfill(1)
                                        + ' days',fontsize=ax_main_titlefont)
            ax_grid[i_subplt].set_xlim(grid_bounds[0],grid_bounds[1])
            ax_grid[i_subplt].set_ylim(grid_bounds[2],grid_bounds[3])


        # Add Colorbar
        colorbar_pad = 0.01
        cb_ax = fig.add_subplot(1,5,1)
        cb_ax.set_position([left_space+n_cols*image_width+(n_cols-1)*image_pad_hori + colorbar_pad,
                            1.0-upper_space-n_rows*image_height-(n_rows-1)*image_pad_vert,
                            0.03,
                            n_rows*image_height + (n_rows-1.0)*image_pad_vert])
        # cb_ax.set_position([0.03,0.1,
        #                     0.5,0.05])
        mpl.colorbar.Colorbar(cb_ax,
                              im,
                              orientation='vertical')
        cb_ax.set_ylabel(ax_main_legendtitle,
                           fontsize=ax_main_labelsize,
                           labelpad=ax_main_labelpad)
        cb_ax.tick_params(labelsize=ax_main_ticksize)

        cb_ax.yaxis.set_ticks([0,0.25,0.5,0.75,1.0])
        formatter = mpl.ticker.FixedFormatter(["6","6.5","7","7.5","8  $10^{-3}$"])
        cb_ax.yaxis.set_major_formatter(formatter)

        # locator = mpl.ticker.MultipleLocator(base = 0.2)
        # cb_ax.yaxis.set_major_locator(locator)


        #Scatter plot with observation locations
        ind_x = [cell_numpy_ind[i,0]*step_x-0.5*step_x for i in range(num_mons)]
        ind_y = [cell_numpy_ind[i,1]*step_y-0.5*step_y for i in range(num_mons)]

        for i_subplt in range(n_rows*n_cols):
            ax_grid[i_subplt].scatter(ind_x,
                                      ind_y,
                                      marker='o',
                                      c=['black','darkred'],
                                      s=200,
                                      linewidths=2)
        #Delete arrays, variables
        del cb_ax, cell_vtk_array, cell_numpy_array, ind_x, ind_y


    ############################################################################################
    ############################# MONITOR PLOT #################################################
    ############################################################################################


    if is_func:
        os.chdir("/home/jk125262/shematOutputDir_Cluster/" + model_name +"_output/" + date + "/" \
                             + date + "_" + letter_true + "/" + output_dir)

        cell_numpy_x = np.genfromtxt(model_name_big + '_TRUE_E0_monitor_1.dat',
                                     dtype='f8',
                                     comments='%',
                                     usecols=(0)) # obstime
        cell_numpy_y = np.genfromtxt(model_name_big + '_TRUE_E0_monitor_1.dat',
                                     dtype='f8',
                                     comments='%',
                                     usecols=(13)) # concentration
        cell_numpy_x = cell_numpy_x.reshape(len(cell_numpy_x)/num_mons, num_mons)
        cell_numpy_y = cell_numpy_y.reshape(len(cell_numpy_y)/num_mons, num_mons)
        num_arrays = 20

        #Generate axis
        ax_function = fig.add_subplot(1,3,2)
        ax_function.set_position(ax_function_position)
        # ax_function.set_title(model_name_big + '_TRUE_E0_monitor_1.vtk')
        ax_function.set_title('Tracer at observation points', fontsize=ax_func_titlefont, y=1.02)
        ax_function.set_xlabel('Time [$d$]', fontsize=ax_func_labelfont, labelpad = ax_func_labelpad)
        ax_function.set_ylabel('Concentration [$mol/L$]', fontsize=ax_func_labelfont, labelpad = ax_func_labelpad)



        #Array containing plots
        plot_arr=[ax_function.plot(cell_numpy_x[:,i],
                                             cell_numpy_y[:,i],
                                             color=color_arr[i],
                                             linestyle='-',
                                             marker='o',
                                             markerfacecolor=color_arr[i],
                                             markeredgecolor=color_arr[i],
                                             markersize=3)
                  for i in range(min(num_mons,19))]

        formatter = mpl.ticker.ScalarFormatter()
        formatter.set_powerlimits((-2,2))
        locator = mpl.ticker.MultipleLocator(base = 0.0005)
        ax_function.yaxis.set_major_formatter(formatter)
        ax_function.yaxis.set_major_locator(locator)

        ax_function.tick_params(labelsize=ax_func_ticksize)

        #Ranges of the plot
        plt.axis([np.amin(cell_numpy_x)-0.5,
                  np.amax(cell_numpy_x)+0.5,
                  np.amin(cell_numpy_y)-0.00005,
                  np.amax(cell_numpy_y)+0.00005])

        #Legend lables
        # label_arr = ['Conc ' + str(int(cell_numpy_ind[i][0]))
        #                  + ' ' + str(int(cell_numpy_ind[i][1]))
        #                  + ' ' + str(int(cell_numpy_ind[i][2]))
        #                  for i in range(min(num_mons,19))]
        label_arr = ['Right','Left']
        #Legend
        plt.legend(# plot_arr,
                   label_arr,
                   loc = 'upper left',
                   bbox_to_anchor=([0.0,1.0]),
                   handlelength=2,
                   numpoints=40,
                   handletextpad=0.5,
                   ncol=1,
                   prop={'size':12})

        del plot_arr, label_arr, ax_function, num_arrays, cell_numpy_x, cell_numpy_y

    ############################################################################################
    ############################ TRUE PLOT #####################################################
    ############################################################################################

    
    if is_true:

        #Generate axis
        ax_single = fig.add_subplot(1,3,3)
        ax_single.set_position(ax_single_position) 
        ax_single.set_title(ax_single_title,fontsize = ax_single_titlefont)
        ax_single.set_xlabel('x [$m$]',fontsize = ax_single_labelsize, labelpad=ax_single_labelpad)
        ax_single.set_ylabel('y [$m$]',fontsize = ax_single_labelsize, labelpad=ax_single_labelpad)
        ax_single.tick_params(labelsize=ax_single_ticksize)
        
        #Open vtk-Reader
        reader = vtk.vtkRectilinearGridReader()
        reader.SetFileName(model_name_big + '_TRUE_E0_init_1.vtk')
        #Read NumPy array from vtk-file
        reader.SetScalarsName(ax_single_varname)       
        reader.Update()

        if grid_loc == 'c':
            cell_vtk_array = reader.GetOutput().GetCellData().GetArray(0)
            num_cells = reader.GetOutput().GetNumberOfCells()
            whole_extent = reader.GetOutput().GetExtent()
            grid_bounds = reader.GetOutput().GetBounds()
            grid_dims = reader.GetOutput().GetDimensions()

            cell_numpy_array = vtk.util.numpy_support.vtk_to_numpy(cell_vtk_array)
            cell_numpy_array = cell_numpy_array.reshape(grid_dims[0]-1,grid_dims[1]-1)
        elif grid_loc == 'p':
            cell_vtk_array = reader.GetOutput().GetPointData().GetArray(0)
            num_cells = reader.GetOutput().GetNumberOfCells()
            whole_extent = reader.GetOutput().GetExtent()
            grid_bounds = reader.GetOutput().GetBounds()
            grid_dims = reader.GetOutput().GetDimensions()

            cell_numpy_array = vtk.util.numpy_support.vtk_to_numpy(cell_vtk_array)
            cell_numpy_array = cell_numpy_array.reshape(grid_dims[0],grid_dims[1])
        else:
            raise exceptions.RuntimeError('Wrong variable: grid_loc (c or p allowed)')


        #Generate image
        im = ax_single.imshow(cell_numpy_array,
                              interpolation='nearest',
                              cmap = mycolors.cmap_discretize(cmap_cbar,num_cbar),
                              # 'gray', 'rgb', 'rainbow', 'jet'
                              norm = colors.Normalize(vmin=low_cbar_single,
                                                      vmax=high_cbar_single,
                                                      clip=False),
                              origin='lower',
                              extent=grid_bounds[0:4])

        ax_single = pltfct.make_quiver("/home/jk125262/shematOutputDir_Cluster/" + model_name +"_output/" + date + "/" + date + "_" + letter_true + "/" + output_dir,
                                    model_name_big + '_TRUE_E0_1.vtk',
                                    'v',
                                    ax_single) # quiver

        ax_single.set_xlim(grid_bounds[0],grid_bounds[1])
        ax_single.set_ylim(grid_bounds[2],grid_bounds[3])

        #Add Colorbar                      
        ax_cbar = fig.add_subplot(1,2,2)
        ax_cbar.set_position(ax_single_cbar_position)
        mpl.colorbar.Colorbar(ax_cbar,im)
        ax_cbar.set_ylabel(ax_single_legendtitle,
                           fontsize=ax_single_labelsize,
                           labelpad=ax_single_labelpad)
        ax_cbar.tick_params(labelsize=ax_single_ticksize)

        #Scatter plot with observation locations    
        ind_x = [cell_numpy_ind[i,0]*step_x-0.5*step_x for i in range(num_mons)]
        ind_y = [cell_numpy_ind[i,1]*step_y-0.5*step_y for i in range(num_mons)]

        # ax_grid[i_subplt].scatter(ind_x,
        #                           ind_y,
        #                           marker='o',
        #                           c=['black','darkred'],
        #                           s=200,
        #                           linewidths=2)
        ax_single.scatter(ind_x,
                          ind_y,
                          marker='o',
                          c=['black','darkred'],
                          s=ax_single_scattersize,
                          linewidths=2)

        del ind_x, ind_y, ax_cbar, im, ax_single, reader, cell_vtk_array, num_cells
        del whole_extent, grid_bounds, grid_dims, cell_numpy_array

    ############################################################################################
    ############################################################################################
    ############################################################################################

    #Showing the figure with matplotlib
    if is_show:
        plt.show()

    # Save the figure as png
    if is_save:
        print(save_png_dir)
        myplots.saving_fig(save_png_dir,[save_png_fname],[fig])

    os.chdir(python_dir)
    print('\nDone with plot_true.py')
    print(time.asctime( time.localtime( time.time())))
