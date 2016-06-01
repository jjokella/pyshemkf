#!/usr/bin/python

# Paths
output_files_dir    = '/home/jk125262/shematOutputDir/'
python_dir = '/home/jk125262/PythonDir'

# Modules
import sys                      # System variables (PYTHONPATH as list sys.path)
import os			# Operating system (os.chdir, os.path)
import numpy as np     		# Numerical Python 
from numpy import random as rnd # Numerical Pythons random number generator
import scipy as sp		# Scientific Python (sp.mean(), sp.cov())
from matplotlib import pyplot as plt	# Plot commands (plt.show(), plt.close())
from matplotlib import colors	        # Normalize colors (colors.Normalize())
from matplotlib import cm		# Colormap commands (cm.get_cmap())

import mpl_toolkits			#  axes (mpl_toolkits.axes_grid.make_axes_locatable)
import pylab				# Axes (pylab.axis())
import vtk	  		# Adapt vtk to NumPy (vtk.util.numpy_support.vtk_to_numpy)
import exceptions  		# Raising exception (raise exceptions.RuntimeError)
import time         # Timing the execution (time.time(), time.clock())

from mypackage.plot import myplots
from mypackage.plot import plotfunctions as pltfct

def psc(
model_name = myplots.mymodel_name,
date = myplots.mydate,
letter = myplots.myletter,
# 
file_type = ['sc', 'sc'],       # log not has to be thought about
sc_cell_vars = [[22,16,1],[22,16,1]],
befaft = ['aft','aft'],
obstimes = [range(9,50,3),range(9,50,3)],

num_figs = 1,
fig_titles = None,
#input_file_names = ['assim_variables_E1_aft_0001.vtk',
#                    'logk_onedir.dat']
variable_names = [4,3],         #3 for kz, 4 for conc, other for kz_res
num_input_data = 500,
# 
fig_size_x = 12.0,
fig_size_y = 11.0,
n_rows = 1,
n_cols = 1,
#
num_bins = 30,
width_factors = [1,1,1,1],      # [x_left, x_right, y_down, y_up] bigger means more space
#
scatter_colors = ['black'],     # [[(i/31)/40.0,(i/31)/40.0,(i/31)/40.0] for i in range(31*31)]
scatter_linewidths = [0.01],
scatter_size = [10],
scatter_x_ticks = np.arange(-15,15,0.2),         # [-11.5,-11,-10.5,-10,-9.5,-9], 
scatter_normed_y_ticks = np.arange(-10,10,0.2),
# 
cmap_cbar = cm.viridis,
#
save_pics_dir = None,
save_pics_name = 'plot_single_cell.png',
#
is_text = 1,
is_show = 1,
is_save = 1,
):
###########################################################################################
###########################################################################################
###########################################################################################


    plt.close('all')

    if fig_titles == None:
        fig_titles = ['Figure Title' for i in range(num_figs)]
    
    if save_pics_dir is None:
        save_pics_dir = "/home/jk125262/shematOutputDir/"\
            + model_name +"_output/" + date + "/"\
            + date + "_" + letter + "/pics"
    if not os.path.exists(save_pics_dir):
        os.mkdir(save_pics_dir)
        
    if(num_figs > len(obstimes[0])):
        raise exceptions.RuntimeError('Specified number of figures (num_figs) too large.')

    model_name_big = model_name.upper()

    figs = [None for i in range(num_figs)]
    save_pics_names = [None for i in range(num_figs)]
    ###########################################################################################
    ###########################################################################################
    ###########################################################################################
    for i in range(num_figs):

        #####################  INPUT  ###################################################

        # x-axis and y-axis input-files
        input_file_names = ['single_cell_E1_' + str(sc_cell_vars[0][0]).zfill(4) + '_'
                            + str(sc_cell_vars[0][1]).zfill(4) + '_'
                            + str(sc_cell_vars[0][2]).zfill(4) + '_'
                            + str(variable_names[0]).zfill(4) + '_'
                            + befaft[0] + '_'
                            + str(obstimes[0][i]).zfill(4) + '.plt'
                            if file_type[0] == 'sc' else
                            'assim_variables_E1_' + befaft[0] + '_'
                            + str(obstimes[0][i]).zfill(4) + '.vtk',
                            # Above: xaxis, below: yaxis
                            'single_cell_E1_' + str(sc_cell_vars[1][0]).zfill(4) + '_'
                            + str(sc_cell_vars[1][1]).zfill(4) + '_'
                            + str(sc_cell_vars[1][2]).zfill(4) + '_'
                            + str(variable_names[1]).zfill(4) + '_'
                            + befaft[1] + '_'
                            + str(obstimes[1][i]).zfill(4) + '.plt'
                            if file_type[1] == 'sc' else
                            'assim_variables_E1_' + befaft[1] + '_'
                            + str(obstimes[1][i]).zfill(4) + '.vtk',
                            ]

        run_output_dir = output_files_dir + model_name +"_output/" + date + "/" \
            + date + "_" + letter + "/" 

        data = [None,None]
        #Read in the data
        for j,input_file_name in enumerate(input_file_names):
            if(input_file_name == 'logk_' + model_name + '.dat'):
                num_skiprows = 3
                os.chdir(run_output_dir)
                data[j] = np.loadtxt(input_file_name, skiprows=num_skiprows)
            elif(input_file_name[0:5] == 'assim'):
                variable_name = 'kz_mean' if variable_names[j] == 4 else ('conc_mean'
                                                                          if variable_names[j] ==3 else
                                                                          'kz_res')
                data[j] = pltfct.my_vtk_to_numpy(run_output_dir + 'enkf_output',
                                              input_file_name,
                                              variable_name)
            elif(input_file_name[0:11] == 'single_cell'):
                num_skiprows = 5
                os.chdir(run_output_dir + 'single_cell_output')
                data[j] = np.loadtxt(input_file_name, skiprows=num_skiprows)


        ##################### DATA MANIPULATION    ############################################
        # Two distribution data sets are filled into arrays
        if input_file_names[0][0:5] == 'assim':
            data[0] = [value for sublist in data[0] for value in sublist]
        if input_file_names[1][0:5] == 'assim':
            data[1] = [value for sublist in data[1] for value in sublist]

        if num_input_data > len(data[0]) or num_input_data > len(data[1]):
            raise exceptions.RuntimeError('num_input_data too big')
        
        x = data[0][0:num_input_data]
        y = data[1][0:num_input_data] #+ rnd.randn(num_input_data)*1.0
        #y = np.random.randn(1000)
        
        x_mean = sp.mean(x)     # Means
        y_mean = sp.mean(y)
        cov_xy =sp.cov(x,y)     # Covariance Matrix (2 by 2)
        corr_mat = cov_xy/(np.sqrt(cov_xy[0,0]*cov_xy[1,1])) # Correlation matrix

        # now determine nice limits by hand:
        x_diff_max = np.max(np.fabs(x-x_mean)) # Maximal
        y_diff_max = np.max(np.fabs(y-y_mean))
        x_lim = x_diff_max
        y_lim = y_diff_max

        #Rescale y_bin and y to have a square figure...
        y_factor = x_lim/y_lim
        if i==0:
            y_mean_first = y_mean
            y_factor_first = y_factor
        
        y = (y-y_mean_first)*y_factor_first + y_mean_first

        if i==0:
            x_bins = np.linspace(x_mean-width_factors[0]*x_lim,
                                 x_mean+width_factors[1]*x_lim,
                                 num_bins)
            y_bins = np.linspace(y_mean-width_factors[2]*x_lim,
                                 y_mean+width_factors[3]*x_lim,
                                 num_bins)

        ##################### FIGURE    ############################################

        # Generate the figure (Figure 1, size)
        fig = plt.figure(i+1, figsize=(fig_size_x,fig_size_y))
        fig.set_facecolor((0.50, 0.50, 0.50))

        if is_text:
            x_mean_string = '%16.8f' %x_mean
            y_mean_string = '%7.3e' %y_mean
            x_std_string = '%16.8f' %np.sqrt(cov_xy[0,0])
            y_std_string = '%7.3e' %np.sqrt(cov_xy[1,1])
            y_factor_string = '%16.8f' % y_factor
            corr_string = '%16.8f' %corr_mat[0,1]
            text_string = 'Mean_x:  ' + x_mean_string[0:-3] \
                + '\nMean_y:  ' + y_mean_string \
                + '\nStd_x:   ' + x_std_string[0:-3] \
                + '\nStd_y:   ' + y_std_string \
                + '\nCorr_xy: ' + corr_string[0:-3]
                # + '\nScale_y: ' + y_factor_string[0:-7] \
            text = fig.text(0.78,0.75,text_string,fontsize=16)
            text.set_bbox(dict(facecolor=(0.8,0.8,0.8), alpha=0.5))

        # Generate the subplot(n_rows, n_cols, 1 .le. n_fig .le. n_rows,example: 111)
        subplot_input = int(str(n_rows) + str(n_cols) + str(1))
        axScatter = plt.subplot(subplot_input)
        axScatter.set_position([0.1,0.1,0.79,0.79])

        # pylab.axis('equal')
        # pylab.axis([-3,3,-3,3])

        plt.xlabel('kz_mean' if variable_names[0]==4 else
                   ('conc_mean' if variable_names[0]==3 else 'kz_res'))
        plt.ylabel('kz_mean' if variable_names[1]==4 else
                   ('conc_mean' if variable_names[1]==3 else 'kz_res'))
        plt.title('')
        plt.suptitle(fig_titles[i], y = 0.97, fontsize=30)


        divider = mpl_toolkits.axes_grid.make_axes_locatable(axScatter)
        # create a new axes with a height of 1.2 inch above the axScatter
        axHistx = divider.new_vertical(1.5, pad=0.1, sharex = axScatter, ylim = [0,1000])
        fig.add_axes(axHistx)
        axHistx.set_xlabel('')
        axHistx.set_ylabel('')
        axHistx.set_title(input_file_names[0])
        histo_scale_x = 1.0/(x_bins[num_bins-1]-x_bins[0])
        axHistx.yaxis.set_ticks([j*histo_scale_x for j in [1,2,3]])
        axHistx.yaxis.set_ticklabels([str(j*histo_scale_x)[0:5] for j in [1,2,3]])

        # create a new axes with a width of 1.2 inch on the right side of the axScatter
        axHisty = divider.new_horizontal(1.5, pad=0.1, sharey=axScatter)
        fig.add_axes(axHisty)
        axHisty.set_xlabel('')
        axHisty.set_ylabel('')
        axHisty.set_title(input_file_names[1],rotation = 270, ha = 'left', va = 'center', position = [1.1,0.5])
        histo_scale_y = 1.0/abs(y_bins[num_bins-1]-y_bins[0])
        axHisty.xaxis.set_ticks([j*histo_scale_y for j in [1,2,3]]) # x axis is y axis because of rotated plot
        axHisty.xaxis.set_ticklabels([str(y_factor*j*histo_scale_y)[0:6] for j in [1,2,3]], rotation = 270)


        # PLOTS
        axScatter.scatter(x, y, c=scatter_colors, linewidths = scatter_linewidths, s=scatter_size, marker='d')
        axScatter.yaxis.set_ticks(scatter_normed_y_ticks)
        axScatter.yaxis.set_ticklabels([str((j-y_mean_first)/y_factor_first + y_mean_first)[0:7] for j in scatter_normed_y_ticks])
        axScatter.xaxis.set_ticks(scatter_x_ticks)
        axScatter.xaxis.set_ticklabels(map(str,scatter_x_ticks))
        
        hist_vals,hist_bins,hist_patches = axHistx.hist(x,
                                                        bins=x_bins,
                                                        facecolor='darkblue', 
                                                        normed=True,
                                                        histtype='bar')
        hist_cmap = cmap_cbar
        hist_norm = colors.normalize(-11.0 if variable_names[0]==4 else
                                      (0.006 if variable_names[0]==3 else 0.0),
                                   -9.0 if variable_names[0]==4 else
                                      (0.008 if variable_names[0]==3 else 1.0))
        for this_bin, this_patch in zip(hist_bins,hist_patches): 
            this_color = hist_cmap(hist_norm(this_bin)) # Color chosen from cmap
            this_patch.set_facecolor(this_color) # Patch set to corresponding color
        
        
        hist_vals,hist_bins,hist_patches = axHisty.hist(y,
                                                        bins=y_bins,
                                                        facecolor='dimgrey',
                                                        normed=True, 
                                                        histtype='bar',
                                                        orientation='horizontal')
            
        # hist_cmap = cmap_cbar
        # hist_norm = colors.normalize(-11.0 if variable_names[1]==4 else 0.006,
        #                            -9.0 if variable_names[1]==4 else 0.008)
        # for this_bin, this_patch in zip(hist_bins,hist_patches): 
        #     this_color = hist_cmap(hist_norm(this_bin)) # Color chosen from cmap
        #     this_patch.set_facecolor(this_color) # Patch set to corresponding color
        


        plt.setp(axHistx.get_xticklabels(), visible = False)
        plt.setp(axHisty.get_yticklabels(), visible = False)        
        


    #Saving the current figure in variable for later output
        fig = plt.gcf()

    #Possible show the figure inside matplotlib
        plt.draw()

    #Save the figure
        figs[i] = fig
        save_pics_names[i] = save_pics_name[0:-4] + '_' + str(i+1).zfill(2) + '.png'

    # Save the plots af png
    if is_save:
        myplots.saving_fig(save_pics_dir,save_pics_names,figs)

    if is_show:
        plt.show()

    os.chdir(python_dir)

    print('\nDone with plot_single_cell.py')
    print(time.asctime( time.localtime( time.time())))
    
