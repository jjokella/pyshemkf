#!/usr/bin/python

# Paths
python_dir = '/home/jk125262/PythonDir_Cluster'

# Modules
import sys                      # System variables (PYTHONPATH as list sys.path)
import os			# Operating system (os.chdir, os.path)
import exceptions  		# Raising exception (raise exceptions.RuntimeError)
import time       		# Timing the execution (time.time(), time.clock())
import numpy as np     		# Numerical Python 
import matplotlib as mpl           	# Matplotlib
from matplotlib import pyplot as plt	# Plot commands (plt.show(), plt.close())
from matplotlib import cm		# Colormap commands (cm.get_cmap())
from matplotlib import colors	        # Normalize colors (colors.Normalize())
import vtk
import math	  		# Mathematical Functions (math.pi, math.sqrt())
import scipy as sp		# Scientific Python (sp.mean(), sp.cov())

sys.path[0] = python_dir        # Set path to read mypackage
from mypackage.plot import plotfunctions as pltfct
from mypackage.plot import myplt
from mypackage.data import dataroutines as dr

import datetime                 # Date and time functions

# # Reload changed module
# pltfct = reload(pltfct)

mymodel_name = 'wave'

# Current default plotting date
this_day = datetime.date.today()
mydate = str(this_day.year) + '_' + str(this_day.month).zfill(2) + '_' + str(this_day.day).zfill(2)

# Current default letter
myletter = 'b'
myletter_true = 'a'

# Color array containing 61 colors
color_arr = [(0.00,0.00,0.00),
             (1.00,0.00,0.00),(0.00,1.00,0.00),(0.00,0.00,1.00),
             (1.00,1.00,0.00),(1.00,0.00,1.00),(0.00,1.00,1.00),
             (0.50,0.00,0.00),(0.00,0.50,0.00),(0.00,0.00,0.50),
             (0.50,0.50,0.00),(0.50,0.00,0.50),(0.00,0.50,0.50),
             (1.00,0.50,0.00),(1.00,0.00,0.50),(0.00,1.00,0.50),
             (0.50,1.00,0.00),(0.50,0.00,1.00),(0.00,0.50,1.00),
             (0.25,0.00,0.00),(0.00,0.25,0.00),(0.00,0.00,0.25),
             (0.25,0.25,0.00),(0.25,0.00,0.25),(0.00,0.25,0.25),
             (1.00,0.25,0.00),(1.00,0.00,0.25),(0.00,1.00,0.25),
             (0.25,0.50,0.00),(0.25,0.00,0.50),(0.00,0.25,0.50),
             (0.50,0.25,0.00),(0.50,0.00,0.25),(0.00,0.50,0.25),
             (0.25,0.50,0.00),(0.25,0.00,0.50),(0.00,0.25,0.50),
             (0.75,0.00,0.00),(0.00,0.75,0.00),(0.00,0.00,0.75),
             (0.75,0.75,0.00),(0.75,0.00,0.75),(0.00,0.75,0.75),
             (1.00,0.75,0.00),(1.00,0.00,0.75),(0.00,1.00,0.75),
             (0.75,0.50,0.00),(0.75,0.00,0.50),(0.00,0.75,0.50),
             (0.50,0.75,0.00),(0.50,0.00,0.75),(0.00,0.50,0.75),
             (0.75,0.50,0.00),(0.75,0.00,0.50),(0.00,0.75,0.50),
             (0.25,0.75,0.00),(0.25,0.00,0.75),(0.00,0.25,0.75),
             (0.75,0.25,0.00),(0.75,0.00,0.25),(0.00,0.75,0.25)]

# Array of color maps
cmaps = ['jet','Greys','RdBu',  # 'Greys', 'Reds' are monotonous, 'RdBu' is divergent
         'Greens','Reds',
         'Blues','Reds',
         'Greys','YlOrRd',
         'RdBu','hot',
         'binary','Blues','BuGn',
         'jet','gray','YlOrRd',
         'gnuplot','gnuplot2''spring','summer','autumn','winter','rgb','rainbow']

    
###########################################################################################
#                                   Functions                                             #
###########################################################################################


########################################################################################
########################################################################################
########################################################################################
def m_plot(num_timesteps,nrobs_int,letters,mons_inds,m_infiles,start_obs,
           assim_variables_dir,stddev_name,run_output_dirs,m_n_cols,
           varnames,letter_true,assimstp_name,assimstp_dir,mons_file_name,
           m_cbar_space,m_num_cbar,diff_obs,m_cbar_left_pad,m_is_show_mons,mons_file_dir,
           figure_size_y,m_diff,assim_variables_dirs,corr_name,
           assimstp_dirs,m_is_text,m_n_rows,resid_name,figure_size_x,model_name_big,
           im_left,run_output_dir,m_grid_factor,corr_dir,m_mons_size,m_kz_std_low,
           true_output_dir,resid_dir,num_mons,corr_dirs,m_kz_std_high,im_up,
           stddev_dir,assim_variables_name,model_name,m_first,m_cbar_kz_low,m_cbar_kz_high,
           m_cbar_kz_res_low, m_cbar_kz_res_high,m_fig_title,m_fig_title_font,m_cbar_titles,
           m_cor_cell_var,m_befaft,m_cbar_cor_low,m_cbar_cor_high,
           m_single_fig_title,m_cbar_width,
           m_is_masked, m_is_subarray, model_output_dir, date_output_dir,
           resid_dirs, stddev_dirs,
           m_cmaps,fig_m = 0 ):


    # PREPARATION
    
    n_fnames = len(m_infiles) # Number of different variables shown
    if n_fnames > m_n_rows*m_n_cols:
        n_fnames = m_n_rows*m_n_cols

    infile_stems = ['assim_variables_E1_' + m_befaft[i] + '_'
                    if m_infiles[i] == 'av' else
                    ('correlation_'
                     + str(m_cor_cell_var[i][0]).zfill(4) + '_'
                     + str(m_cor_cell_var[i][1]).zfill(4) + '_'
                     + str(m_cor_cell_var[i][2]).zfill(4) + '_'
                     + str(m_cor_cell_var[i][3]).zfill(4) + '_'
                     + m_befaft[i] + '_'
                     if m_infiles[i]=='cor' else
                     (model_name_big + '_E0_init_'
                      if m_infiles[i]=='init' else
                      model_name_big + '_E1_'))
                    for i in range(n_fnames)]
    
    param_inserts =  pltfct.m_input_check(n_fnames, # Input check
                                       infile_stems,
                                       assim_variables_dir,
                                       run_output_dir + 'samples_output',
                                       varnames,
                                       m_first, m_n_rows, m_n_cols, m_diff,
                                       nrobs_int,
                                       im_up)
    infile_stems = [infile_stems[i] + 'param_' 
                        if param_inserts[i]
                        else infile_stems[i]
                        for i in range(n_fnames)]

    os.chdir(run_output_dir)    #Go to the general run output directory
    if(not(os.path.exists('pics'))):    #Create pics directory if not already existing
        os.mkdir('pics')


 
    # DATA

    data = pltfct.my_vtk_to_numpy(assim_variables_dir # Get NumPy Array
                               if m_infiles[0] in ['av','cor'] else
                               run_output_dir + 'samples_output',
                               infile_stems[0] + str(1).zfill(4) + '.vtk'
                               if m_infiles[0] in ['av','cor'] else
                               infile_stems[0] + str(1) + '.vtk',
                               varnames[0])

    step_x, step_y, \
    npts_x, npts_y, \
    low_m_x, high_m_x,\
    low_m_y, high_m_y,\
    low_x, high_x, \
    low_y, high_y = pltfct.vtk_grid_props(assim_variables_dir   # Get Grid Properties
                                       if m_infiles[0] in ['av','cor'] else
                                       run_output_dir + 'samples_output',
                                       infile_stems[0] + str(1).zfill(4) + '.vtk'
                                       if m_infiles[0] in ['av','cor'] else
                                       infile_stems[0] + str(1) + '.vtk',
                                       varnames[0]) 
    
    # PLOT
    if not fig_m:
        fig_m = plt.figure(1, figsize=(figure_size_x,figure_size_y)) #Generate the figure
        fig_m.set_facecolor((0.50, 0.50, 0.50)) # Set figure background color
        plt.suptitle(infile_stems[0]
                     if m_fig_title == None else
                     m_fig_title, y = 0.97, fontsize=m_fig_title_font)    #Insert figure title

    ax_grid = myplt.myaxgrid(fig_m, # List of axes, ordered row before column
                             n_rows = m_n_rows,
                             n_cols = m_n_cols,
                             grid_factor = m_grid_factor,
                             left_pad = im_left,
                             up_pad = im_up,
                             x_ticks = [100.0,200.0,300.0,400.0,500.0],
                             y_ticks = [100.0,200.0,300.0,400.0,500.0],
                             x_ticklabels = [100,200,300,400,500],
                             y_ticklabels = [100,200,300,400,500],)
        
    if m_is_show_mons:    # Plot Monitoring cells
        ind_x = [mons_inds[i,0]*step_x-0.5*step_x for i in range(num_mons)]
        ind_y = [mons_inds[i,1]*step_y-0.5*step_y for i in range(num_mons)]

        for i_subplt in range(m_n_rows*m_n_cols):
            ax_grid[i_subplt].scatter(ind_x,
                                       ind_y,
                                       marker='o',
                                       c='black',
                                       s=m_mons_size)


    m_low_cbars = [pltfct.get_cbar_low(varname,# Calculate appropriate min/max for cbar
                                    m_kz_std_low,m_cbar_kz_low,
                                    m_cbar_kz_res_low,m_cbar_cor_low)
                   for varname in varnames]

    m_high_cbars = [pltfct.get_cbar_high(varname,
                                      m_kz_std_high, m_cbar_kz_high,
                                      m_cbar_kz_res_high, m_cbar_cor_high)
                    for varname in varnames]

    
    for i_subplt in range(m_n_rows*m_n_cols):

        i_obs = m_first + (i_subplt/n_fnames)*m_diff # Observation index
        i_fnames = i_subplt%n_fnames                 # Different variable index

        data=pltfct.my_vtk_to_numpy(assim_variables_dir        # Getting the NumPy Array
                                 if m_infiles[0] in ['av','cor'] else
                                 run_output_dir + 'samples_output',
                                 infile_stems[i_fnames] + str(i_obs).zfill(4)+'.vtk'
                                 if m_infiles[i] in ['av','cor'] else
                                 infile_stems[i_fnames] + str(i_obs) + '.vtk', 
                                 varnames[i_fnames])

        if m_is_subarray:
            data = dr.my_subarray(data, # Subarray selection
                                  ind_x = np.arange(10,22,1),
                                  ind_y = np.arange(10,22,1))
            

        if m_is_masked:
            data = dr.my_maskedarray(data, # Mask the array
                                     ind_x = np.arange(16,32,1),
                                     ind_y = np.arange(16,32,1))
        
        im=ax_grid[i_subplt].imshow(data,        #Generate plot
                                    interpolation='nearest',
                                    cmap=cm.get_cmap(name=m_cmaps[i_fnames], 
                                                     lut=m_num_cbar), 
                                    norm = colors.Normalize(vmin=m_low_cbars[i_fnames],
                                                            vmax=m_high_cbars[i_fnames],
                                                            clip=False),
                                    origin='lower',
                                    extent=[low_x,high_x,low_y,high_y])

        if not m_single_fig_title: # Set default for m_single_fig_title
            m_single_fig_title = 'Observation '
        ax_grid[i_subplt].set_title(m_single_fig_title + str(i_obs).zfill(2)) #Add plot title
        
        if i_subplt in range(n_fnames): # Add Colorbar for every variable
            cb_ax = fig_m.add_subplot(1,25,i_subplt)
            cbar_pad = m_cbar_left_pad + i_subplt*m_cbar_space
            cb_ax.set_position([im_left+m_n_cols*(0.12*m_grid_factor)+(m_n_cols-1)*(0.01*m_grid_factor)+cbar_pad,
                                1.0-im_up-m_n_rows*(0.24*m_grid_factor)-(m_n_rows-1)*(0.04*m_grid_factor),
                                m_cbar_width,
                                m_n_rows*(0.24*m_grid_factor) + (m_n_rows-1.0)*(0.04*m_grid_factor)])
            cb_ax.set_title(m_cbar_titles[i_subplt])
            mpl.colorbar.Colorbar(cb_ax, im)

    return fig_m

########################################################################################
########################################################################################
##########################################################################################
def f_plot(f_ax_legend_bbox,num_timesteps,letters,nrobs_int,start_obs,assim_variables_dir,
           f_plot_x_min,stddev_name,letter_true,f_plot_y_min,f_ax_legend_loc,
           f_line_colors,assimstp_name,assimstp_dir,mons_file_name,f_plot_y_max,
           f_y_vars_mean,diff_obs,f_y_variables_ens,f_res_std,f_ax_y_labels,
           f_ax_legend_handle_length,run_output_dirs,assim_variables_dirs,corr_name,
           assimstp_dirs,model_name_big,resid_name,figure_size_y,f_markersize,
           f_ax_pos,f_x_variable,run_output_dir,f_ax_legend_cols,mons_file_dir,corr_dir,
           stddev_dir,true_output_dir,resid_dir,num_mons,corr_dirs,f_plot_x_max,
           figure_size_x,mons_inds,f_ax_x_label,model_name,f_ax_legend_labels,
           f_force_y_range,f_ens_alpha,
           assim_variables_name,f_fig_title,f_fig_title_font,
           model_output_dir, date_output_dir,resid_dirs, stddev_dirs,
           fig_f = 0):


    if not fig_f:
        # Generate the figure
        fig_f = plt.figure(2, figsize=(figure_size_x,figure_size_y))
        fig_f.set_facecolor((0.50, 0.50, 0.50))
        # Insert figure title
        plt.suptitle(f_fig_title, y = 0.97, fontsize=f_fig_title_font)

    f_dirs = [resid_dir,stddev_dir,resid_dir,resid_dir]
    f_fnames = [resid_name,stddev_name,resid_name,resid_name]
    is_ax_exists = 0
    ax_f = [0 for i in range(4)]

    for i in range(4):
        if f_res_std[i]:

            # Data input
            data_x = pltfct.my_vtk_to_numpy(f_dirs[i],
                                            f_fnames[i],
                                            f_x_variable)
            if i in range(3):
                data_y = pltfct.my_vtk_to_numpy(f_dirs[i],
                                                f_fnames[i],
                                                f_y_vars_mean[i])
            else:
                resids = pltfct.my_vtk_to_numpy(f_dirs[0],
                                                f_fnames[0],
                                                f_y_vars_mean[0])
                stddevs = pltfct.my_vtk_to_numpy(f_dirs[1],
                                                 f_fnames[1],
                                                 f_y_vars_mean[1])
                data_y = np.sqrt(resids**2 + stddevs**2)

            #Properties of read arrays
            len_arrays =len(data_x)
            min_value_x=min(data_x)[0] # 1-element array to float
            max_value_x=max(data_x)[0]
            min_value_y=min(data_y)[0]
            max_value_y=max(data_y)[0]

            #Generate axis
            if is_ax_exists == 1:
                ax_f[i] = ax_f[0].twinx()
            elif is_ax_exists == 2:
                ax_f[i] = ax_f[0].twinx()
                ax_f[i].spines['left'].set_position(('axes',-0.04)) # No label overlap
                ax_f[i].set_frame_on(True)
                ax_f[i].patch.set_visible(False)
                ax_f[i].yaxis.set_label_position('left')
            elif is_ax_exists == 3:
                ax_f[i] = ax_f[0].twinx()
                ax_f[i].spines['left'].set_position(('axes',-0.08)) # No label overlap
                ax_f[i].set_frame_on(True)
                ax_f[i].patch.set_visible(False)
                ax_f[i].yaxis.set_label_position('left')
            else:
                ax_f[0] = fig_f.add_subplot(1,2,i)
            is_ax_exists = is_ax_exists + 1
            ax_f[i].set_position(f_ax_pos)
            ax_f[i].set_title('')
            ax_f[i].set_xlabel(f_ax_x_label)
            ax_f[i].set_ylabel(f_ax_y_labels[i])

            #Generate plot
            ax_f[i].plot(data_x,
                         data_y,
                         color=f_line_colors[i],
                         linestyle='-',
                         linewidth=2.0,
                         marker='o',
                         markerfacecolor='black',
                         markeredgecolor='black',
                         markersize=f_markersize)
                                       #label='Mean')

            ax_f[i].set_xlim(min(f_plot_x_min,min_value_x),
                             max(f_plot_x_max,max_value_x))
            ax_f[i].set_ylim(f_plot_y_min[i] if f_force_y_range else\
                                 min(f_plot_y_min[i],min_value_y),
                             f_plot_y_max[i] if f_force_y_range else\
                                 max(f_plot_y_max[i],max_value_y))
            # Do zero again, because of twin, probably
            ax_f[0].set_ylim(f_plot_y_min[0] if f_force_y_range else\
                                 min(f_plot_y_min[0],min_value_y),
                             f_plot_y_max[0] if f_force_y_range else\
                                 max(f_plot_y_max[0],max_value_y))

            for f_y_var_ens in f_y_variables_ens[i]:
                data_y = pltfct.my_vtk_to_numpy(f_dirs[i],
                                                f_fnames[i],
                                                f_y_var_ens)
                #Generate plot
                ax_f[i].plot(data_x,
                             data_y,
                             color='grey',
                             linestyle='-',
                             linewidth=1.3,
                             marker='',
                             alpha = f_ens_alpha,
                             markerfacecolor='grey',
                             markeredgecolor='grey',
                             markersize=f_markersize)
                                                          #label='Ensemble')
            #Set axis legend
            plt.legend(f_ax_legend_labels[i],
                       loc=f_ax_legend_loc[i],
                       bbox_to_anchor=f_ax_legend_bbox[i],
                       handlelength=f_ax_legend_handle_length[i],
                       numpoints=3,
                       handletextpad=0.5,
                       ncol=f_ax_legend_cols[i],
                       prop={'size':18})

    return fig_f


##########################################################################################
########################################################################################
########################################################################################
def f2_plot(f2_y_variables,
            f2_plot_y_max,
            f2_ax_kz_y_max,
            f2_ax_kz_y_min,
            f2_ax_kz_res_y_max,
            f2_ax_kz_res_y_min,
            f2_ax_kz_res_legend_bbox,
            f2_ax_kz_res_legend_or,
            f2_ax_kz_res_legend_cols,
            f2_ax_kz_std_y_max,
            f2_ax_kz_std_y_min,
            f2_ax_kz_std_legend_bbox,
            f2_ax_kz_std_legend_or,
            f2_ax_kz_std_legend_cols,
            f2_ax_conc_res_y_max,
            f2_ax_conc_res_y_min,
            f2_ax_conc_res_legend_bbox,
            f2_ax_conc_res_legend_or,
            f2_ax_conc_res_legend_cols,
            f2_ax_conc_std_y_max,
            f2_ax_conc_std_y_min,
            f2_ax_conc_std_legend_bbox,
            f2_ax_conc_std_legend_or,
            f2_ax_conc_std_legend_cols,
            f2_ax_offset_kz,
            f2_ax_offset_kz_res,
            f2_ax_offset_kz_std,
            f2_ax_offset_conc_res,
            f2_ax_offset_conc_std,
            f2_ax_offset_corr,
            f2_corr_num_arrays,
            f2_ax_kz_legend_bbox,
            f2_plot_x_min,
            f2_ax_1_y_label,
            f2_plot_x_max,
            f2_corr_j_want,
            f2_is_enforce_axis_input,f2_ax_legend_bbox,f2_num_show_assimstp,f2_ax_corr_y_min,
            f2_ax_corr_legend_cols,f2_ax_corr_y_max,f2_corr_colored,f2_ax_legend_cols,
            f2_ax_corr_legend_or,f2_corr_i_want,f2_ax_corr_legend_bbox,
            f2_assimstp_marker_size,f2_corr_y_variables,f2_array_marker_size,
            f2_corr_ref_cells,f2_assimstp_letters,f2_num_arrays,f2_y_variables_mon,
            f2_befaft,f2_is_show_arrows,f2_num_show_mons,f2_ax_kz_legend_or,
            f2_show_assimstp, f2_kz_marker_size,
            f2_i_want,f2_av_letters,f2_show_mons,f2_x_variable,f2_ax_kz_legend_cols,
            f2_mon_num_assimstp,f2_j_want,f2_num_variables_mon,f2_ax_legend_or,
            f2_corr_letters,f2_corr_ref_var,f2_ax_x_label,f2_plot_y_min,f2_assimstp_var,
            f2_corr_befaft,f2_ax_pos,f2_ax_corr_show_line, f2_ax_corr_show_marker,
            num_mons,mons_inds,nrobs_int,start_obs,diff_obs,num_timesteps,
            resid_dir,mons_file_name,run_output_dirs,corr_dir,f2_assimstp_show_line,
            assim_variables_dirs,corr_name,assimstp_dirs,assimstp_dir,
            stddev_dir,true_output_dir,corr_dirs,stddev_name,resid_name,assimstp_name,
            assim_variables_dir,mons_file_dir,run_output_dir,assim_variables_name,
            letters,model_name_big,letter_true,figure_size_x,figure_size_y,model_name,
            f2_fig_title,f2_fig_title_font,f2_axis_title,f2_color_arr,
            model_output_dir, date_output_dir,resid_dirs, stddev_dirs,
            fig_f2 = 0):


    pltfct.f2_plot_input_checks(f2_num_arrays,f2_i_want,f2_j_want,f2_befaft,f2_y_variables,
                             f2_show_mons,f2_num_show_mons,f2_y_variables_mon,
                             f2_num_variables_mon,num_mons,f2_show_assimstp,
                             f2_num_show_assimstp,
                             f2_mon_num_assimstp,f2_corr_letters,f2_corr_num_arrays,
                             f2_corr_i_want,f2_corr_j_want, f2_corr_befaft,f2_corr_y_variables
                             )
    

    #Initialisation
    f2_num_plots = 0 # Total number of plots
    
    f2_innov_inds = []
    f2_kz_inds = []
    f2_conc_inds = []
    f2_kz_res_inds = []
    f2_kz_std_inds = []
    f2_conc_res_inds = []
    f2_conc_std_inds = []
    f2_corr_inds = []
    f2_show_line = []
    f2_show_marker = []
    arr_yvars=[] 

    #Make small arrays
    del f2_i_want[f2_num_arrays:]
    del f2_j_want[f2_num_arrays:]
    del f2_befaft[f2_num_arrays:]
    del f2_y_variables[f2_num_arrays:]


    ### X-array
    #Read
    arr_xvars = pltfct.ts_from_mon(mons_file_dir,
                                mons_file_name,
                                ['time'])
    #Reshape(ts_from_mon gives array containing one array)
    arr_xvars = arr_xvars[0].reshape(len(arr_xvars[0])/num_mons, num_mons)
    arr_xvars = arr_xvars[start_obs-1:num_timesteps:diff_obs,0]

    ### Y-array
    #Read assim_variables
    arr_yvars.extend([np.array(pltfct.ts_from_av(assim_variables_dirs[f2_av_letters[i]],
                                              assim_variables_name,
                                              f2_befaft[i],
                                              f2_y_variables[i],
                                              [f2_i_want[i],f2_j_want[i]],
                                              nrobs_int))
                      for i in range(f2_num_arrays)])
    #Change related variables/arrays
    f2_num_plots = f2_num_plots + f2_num_arrays
    f2_show_line.extend([0 for i in range(f2_num_arrays)])
    f2_show_marker.extend(['s' for i in range(f2_num_arrays)])
    f2_kz_inds.extend([i for i,e in enumerate(f2_y_variables) if e == 'kz_mean'])    
    f2_conc_inds.extend([i for i,e in enumerate(f2_y_variables) if e == 'conc_mean'])
    f2_kz_res_inds.extend([i for i,e in enumerate(f2_y_variables) if e == 'kz_res'])
    f2_kz_std_inds.extend([i for i,e in enumerate(f2_y_variables) if e == 'kz_std'])
    f2_conc_res_inds.extend([i for i,e in enumerate(f2_y_variables) if e == 'conc_res'])
    f2_conc_std_inds.extend([i for i,e in enumerate(f2_y_variables) if e == 'conc_std'])
    ###############################################################################
    #Read correlation
    arr_yvars.extend([np.array(pltfct.ts_from_cor(corr_dirs[f2_corr_letters[i]],
                                               corr_name,
                                               f2_corr_ref_cells[i],
                                               f2_corr_ref_var,
                                               f2_corr_befaft[i],
                                               f2_corr_y_variables[i],
                                               [f2_corr_i_want[i],f2_corr_j_want[i]],
                                               nrobs_int))
                      for i in range(f2_corr_num_arrays)])
    #Change related variables/arrays
    f2_num_plots = f2_num_plots + f2_corr_num_arrays
    f2_show_line.extend([f2_ax_corr_show_line for i in range(f2_corr_num_arrays)])
    f2_show_marker.extend(['o' if f2_ax_corr_show_marker else '' for i in range(f2_corr_num_arrays)])
    f2_corr_inds.extend([i+f2_num_arrays for i in range(f2_corr_num_arrays)])
    ###############################################################################
    #Read monitor
    temp_y = pltfct.ts_from_mon(mons_file_dir,
                             mons_file_name,
                             f2_y_variables_mon[0:f2_num_variables_mon])
    #Reshape
    temp_y = [np.array(temp_y[i].reshape(len(temp_y[i])/num_mons, num_mons))
               for i in range(f2_num_variables_mon)]
    temp_y = np.array(temp_y)
    arr_yvars.extend([temp_y[j][start_obs-1:num_timesteps:diff_obs,i] 
                      for j in range(f2_num_variables_mon) 
                      for i in f2_show_mons[0:f2_num_show_mons]])
    #Change related variables/arrays
    f2_num_plots = f2_num_plots + f2_num_variables_mon*f2_num_show_mons
    f2_show_line.extend([1 for i in range(f2_num_variables_mon*f2_num_show_mons)])
    f2_show_marker.extend(['o' for i in range(f2_num_variables_mon*f2_num_show_mons)])
    f2_kz_inds.extend([i*f2_num_show_mons+j+f2_num_arrays+f2_corr_num_arrays 
                       for i,e in enumerate(f2_y_variables_mon[0:f2_num_variables_mon]) 
                       for j in range(f2_num_show_mons)
                       if e=='kz_mean'])
    f2_conc_inds.extend([i*f2_num_show_mons+j+f2_num_arrays+f2_corr_num_arrays 
                         for i,e in enumerate(f2_y_variables_mon[0:f2_num_variables_mon]) 
                         for j in range(f2_num_show_mons)
                         if e == 'conc_mean'])


    ##########################################################################
    #Read from assimstp
    for j,i in enumerate(f2_show_assimstp[0:f2_num_show_assimstp]):
        if i == 1:
            arr_yvars.append(pltfct.ts_from_as(assimstp_dirs[f2_assimstp_letters[j]],
                                            assimstp_name,nrobs_int,
                                            'meanS',f2_mon_num_assimstp[j]))
        elif i == 2:
            arr_yvars.append(pltfct.ts_from_as(assimstp_dirs[f2_assimstp_letters[j]],
                                            assimstp_name,nrobs_int,
                                            'innov',f2_mon_num_assimstp[j]))
            f2_innov_inds.append(f2_num_arrays
                                 + f2_corr_num_arrays
                                 + f2_num_show_mons*f2_num_variables_mon+j)
        elif i == 3:
            arr_yvars.append(pltfct.ts_from_as(assimstp_dirs[f2_assimstp_letters[j]],
                                            assimstp_name,nrobs_int,
                                            'obs_pert',f2_mon_num_assimstp[j]))
            
    f2_num_plots = f2_num_plots + f2_num_show_assimstp
    f2_show_line.extend([ f2_assimstp_show_line[i-1]
                          for i in f2_show_assimstp[0:f2_num_show_assimstp]])
    f2_show_marker.extend([('o' if i==2 else 'o') 
                           for i in f2_show_assimstp[0:f2_num_show_assimstp]])
    f2_kz_inds.extend([i + f2_num_arrays + f2_corr_num_arrays
                       + f2_num_show_mons*f2_num_variables_mon
                       for i in range(f2_num_show_assimstp)
                       if f2_assimstp_var == 'kz_mean'
                       if f2_show_assimstp[i]!=2])
    f2_conc_inds.extend([i + f2_num_arrays + f2_corr_num_arrays
                         + f2_num_show_mons*f2_num_variables_mon
                         for i in range(f2_num_show_assimstp)
                         if f2_assimstp_var == 'conc_mean'
                         if f2_show_assimstp[i]!=2])
    ##########################################################################

    #Properties of read arrays
    min_value_x=min(arr_xvars)
    max_value_x=max(arr_xvars)
    min_value_y=[min(arr_yvars[i]) for i in f2_conc_inds]
    max_value_y=[max(arr_yvars[i]) for i in f2_conc_inds]

    #Prepare axis legend (assim_variables)
    f2_ax_legend_labels=[letters[f2_av_letters[i]] + ': '
                         + str(f2_i_want[i]).zfill(2)+','+str(f2_j_want[i]).zfill(2) 
                         + ' ' + f2_befaft[i] 
                         for i in range(f2_num_arrays)]
    #Prepare axis legend (correlations)
    f2_ax_legend_labels.extend([letters[f2_corr_letters[i]] + ': '
                                + 'corr of ' + str(f2_corr_i_want[i]).zfill(2) + ',' 
                                + str(f2_corr_j_want[i]).zfill(2) + ' var '
                                + str(f2_corr_y_variables[i][-2:]) + ' , '
                                + ' with ' + str(f2_corr_ref_cells[i][0]).zfill(2) + ','
                                + str(f2_corr_ref_cells[i][1]).zfill(2) + ','
                                + str(f2_corr_ref_cells[i][2]).zfill(2) + ',var '
                                + str(f2_corr_ref_var) 
                                for i in range(f2_corr_num_arrays)])

    #Prepare axis legend (Trues)
    f2_ax_legend_labels.extend(['True' + str(int(mons_inds[i][0])).zfill(2)
                                + ',' + str(int(mons_inds[i][1])).zfill(2)
                                + ',' + j
                                for j in f2_y_variables_mon[0:f2_num_variables_mon] 
                                for i in f2_show_mons[0:f2_num_show_mons]])

    #Prepare axis legend (Assimstp)
    f2_ax_legend_labels.extend([(letters[f2_assimstp_letters[j]] + ': ' + 'meanS' 
                                 if i == 1 else 
                                 (letters[f2_assimstp_letters[j]] + ': ' + 'innov' 
                                  if i == 2 else 
                                  (letters[f2_assimstp_letters[j]] + ': ' + 'obs_pert'))) 
                                for j,i in enumerate(f2_show_assimstp[0:f2_num_show_assimstp])])


    ################################################################################

    if not fig_f2:
        # Generate the figure
        fig_f2 = plt.figure(3, figsize=(figure_size_x,figure_size_y)) 
        fig_f2.set_facecolor((0.50, 0.50, 0.50))
        # Insert figure title
        plt.suptitle(f2_fig_title, y = 0.97, fontsize=f2_fig_title_font)

    #Generate axis
    ax_f_1 = fig_f2.add_subplot(1,11,1)
    ax_f_1.set_position(f2_ax_pos)
    ax_f_1.set_title(f2_axis_title)
    ax_f_1.set_xlabel(f2_ax_x_label)
    ax_f_1.set_ylabel(f2_ax_1_y_label)
    #Linestyle
    f2_linestyle_array = [('-' if show else '') for show in f2_show_line]
    #Markerstyle
    f2_markerstyle_array = f2_show_marker
    f2_markersize_array = [(f2_array_marker_size 
                            if i<f2_num_arrays 
                            else f2_assimstp_marker_size) 
                           for i in range(f2_num_plots)]
    if len(f2_conc_inds):
        #Generate plot
        plot_main=[ax_f_1.plot(arr_xvars,
                               arr_yvars[i],
                               color=f2_color_arr[i],
                               linestyle=f2_linestyle_array[i],
                               marker=f2_markerstyle_array[i],
                               markerfacecolor=f2_color_arr[i],
                               markeredgecolor=f2_color_arr[i],
                               markersize=f2_markersize_array[i])
                   for i in f2_conc_inds]
                                   #label='Mean')
        #Print arrows
        if f2_is_show_arrows:
            ax_f_1 = pltfct.make_arrows(ax_f_1,f2_num_arrays,f2_befaft,nrobs_int,arr_xvars,arr_yvars,f2_color_arr)

        #Set axis ranges
        plt.axis([min(f2_plot_x_min,min_value_x),
                  max(f2_plot_x_max,max_value_x),
                  min(f2_plot_y_min,min(min_value_y)),
                  max(f2_plot_y_max,max(max_value_y))])

        #Conc legend
        conc_legend_labels = [f2_ax_legend_labels[i] for i in f2_conc_inds]

        #Set axis legend
        plt.legend(conc_legend_labels,
                   title = 'conc',
                   loc=f2_ax_legend_or,
                   bbox_to_anchor=f2_ax_legend_bbox,
                   handlelength=2,
                   numpoints=3,
                   handletextpad=0.5,
                   ncol=f2_ax_legend_cols,
                   prop={'size':14})
    else:
        ax_f_1.yaxis.set_visible(False)
    #############################################################################
    #Correlation axis
    if f2_corr_num_arrays:
        #Twinx-Axis (second y-axis on the right)
        ax_f_5 = ax_f_1.twinx()
        ax_f_5.spines['left'].set_position(('axes',f2_ax_offset_corr))
        ax_f_5.set_frame_on(True)
        ax_f_5.patch.set_visible(False)
        ax_f_5.set_ylabel('Correlation')
        ax_f_5.yaxis.set_label_position('left')
        for j,i in enumerate(f2_corr_inds):
            ax_f_5.plot(arr_xvars,
                        arr_yvars[i],
                        color=f2_color_arr[i],
                        linestyle=f2_linestyle_array[i],
                        linewidth=2,
                        marker=f2_markerstyle_array[i],
                        markerfacecolor=f2_color_arr[i] if j in f2_corr_colored else 'grey',
                        markeredgecolor=f2_color_arr[i] if j in f2_corr_colored else 'grey',
                        markersize=f2_markersize_array[i])
        #Set y-axis ranges for twinx-axis
        plt.ylim([f2_ax_corr_y_min,
                  f2_ax_corr_y_max])
        #Add a horizontal line at zero
        plt.axhline(y=0,
                    xmin=f2_plot_x_min,
                    xmax=f2_plot_x_max,
                    color='black')
        #Set axis legend
        corr_legend_labels = [f2_ax_legend_labels[i] for i in f2_corr_inds]
        plt.legend(corr_legend_labels,
                   loc=f2_ax_corr_legend_or,
                   bbox_to_anchor=f2_ax_corr_legend_bbox,
                   handlelength=2,
                   numpoints=3,
                   handletextpad=0.5,
                   ncol=f2_ax_corr_legend_cols,
                   prop={'size':14})
    #############################################################################
    #Innovation axis
    if(len(f2_innov_inds) > 0):
        #Twinx-Axis (second y-axis on the right)
        ax_f_2 = ax_f_1.twinx()
        for i in f2_innov_inds:
            ax_f_2.plot(arr_xvars,
                        arr_yvars[i],
                        color=f2_color_arr[i],
                        linestyle=f2_linestyle_array[i],
                        linewidth=2,
                        marker=f2_markerstyle_array[i],
                        markerfacecolor=f2_color_arr[i],
                        markeredgecolor=f2_color_arr[i],
                        markersize=f2_markersize_array[i])
            ax_f_2.set_ylabel('Innovation')
        #Set y-axis ranges for twinx-axis
        plt.ylim([-0.003,
               0.003])
        #Add a horizontal line at zero
        plt.axhline(y=0,
                    xmin=f2_plot_x_min,
                    xmax=f2_plot_x_max,
                    color='black')
        #Set axis legend
        innov_legend_labels = ['innov'+ 
                               str(int(mons_inds[f2_mon_num_assimstp[i]][0])).zfill(2)
                                + ',' +
                               str(int(mons_inds[f2_mon_num_assimstp[i]][1])).zfill(2) 
                               for i in range(len(f2_innov_inds))]
        plt.legend(innov_legend_labels,
                   loc='upper right',
                   bbox_to_anchor=[1.0,1.0],
                   handlelength=2,
                   numpoints=3,
                   handletextpad=0.5,
                   ncol=f2_ax_legend_cols,
                   prop={'size':20})
    ##############################################################################
    # Permeability axis
    if len(f2_kz_inds):
        ax_f_4 = ax_f_1.twinx()
        ax_f_4.spines['left'].set_position(('axes',f2_ax_offset_kz))
        ax_f_4.set_frame_on(True)
        ax_f_4.patch.set_visible(False)
        ax_f_4.set_ylabel('Permeability')
        ax_f_4.yaxis.set_label_position('left')
        for i in f2_kz_inds:
            ax_f_4.plot(arr_xvars,
                        arr_yvars[i],
                        color=f2_color_arr[i],
                        linestyle=f2_linestyle_array[i],
                        marker=f2_markerstyle_array[i],
                        markerfacecolor=f2_color_arr[i],
                        markeredgecolor=f2_color_arr[i],
                        markersize=f2_kz_marker_size)
        #kz legend
        kz_legend_labels = [f2_ax_legend_labels[i] for i in f2_kz_inds]
        #Set y-axis ranges for twinx-axis
        plt.ylim([f2_ax_kz_y_min,f2_ax_kz_y_max])
        #Set axis legend
        plt.legend(kz_legend_labels,
                   title = 'kz',
                   loc=f2_ax_kz_legend_or,
                   bbox_to_anchor=f2_ax_kz_legend_bbox,
                   handlelength=2,
                   numpoints=3,
                   handletextpad=0.5,
                   ncol=f2_ax_kz_legend_cols,
                   prop={'size':14})
        #Include Arrows
        if f2_is_show_arrows:
            ax_f_4 = pltfct.make_arrows(ax_f_4,f2_num_arrays,f2_befaft,nrobs_int,
                                     arr_xvars,arr_yvars,f2_color_arr)

    if len(f2_kz_res_inds):
        ax_f_6 = ax_f_1.twinx()
        ax_f_6.spines['left'].set_position(('axes',f2_ax_offset_kz_res))
        ax_f_6.set_frame_on(True)
        ax_f_6.patch.set_visible(False)
        ax_f_6.set_ylabel('kz Residuals')
        ax_f_6.yaxis.set_label_position('left')
        for i in f2_kz_res_inds:
            ax_f_6.plot(arr_xvars,
                        arr_yvars[i],
                        color=f2_color_arr[i],
                        linestyle=f2_linestyle_array[i],
                        marker=f2_markerstyle_array[i],
                        markerfacecolor=f2_color_arr[i],
                        markeredgecolor=f2_color_arr[i],
                        markersize=9)
        kz_res_legend_labels = [f2_ax_legend_labels[i] for i in f2_kz_res_inds]
        plt.ylim([f2_ax_kz_res_y_min,f2_ax_kz_res_y_max])
        plt.legend(kz_res_legend_labels,
                   title = 'kz_res',
                   loc=f2_ax_kz_res_legend_or,
                   bbox_to_anchor=f2_ax_kz_res_legend_bbox,
                   handlelength=2,
                   numpoints=3,
                   handletextpad=0.5,
                   ncol=f2_ax_kz_res_legend_cols,
                   prop={'size':14})
        #Include Arrows
        if f2_is_show_arrows:
            ax_f_6 = pltfct.make_arrows(ax_f_6,f2_num_arrays,f2_befaft,nrobs_int,
                                     arr_xvars,arr_yvars,f2_color_arr)

    if len(f2_kz_std_inds):
        ax_f_7 = ax_f_1.twinx()
        ax_f_7.spines['left'].set_position(('axes',f2_ax_offset_kz_std))
        ax_f_7.set_frame_on(True)
        ax_f_7.patch.set_visible(False)
        ax_f_7.set_ylabel('kz Standard Deviation')
        ax_f_7.yaxis.set_label_position('left')
        for i in f2_kz_std_inds:
            ax_f_7.plot(arr_xvars,
                        arr_yvars[i],
                        color=f2_color_arr[i],
                        linestyle=f2_linestyle_array[i],
                        marker=f2_markerstyle_array[i],
                        markerfacecolor=f2_color_arr[i],
                        markeredgecolor=f2_color_arr[i],
                        markersize=9)
        kz_std_legend_labels = [f2_ax_legend_labels[i] for i in f2_kz_std_inds]
        plt.ylim([f2_ax_kz_std_y_min,f2_ax_kz_std_y_max])
        plt.legend(kz_std_legend_labels,
                   title = 'kz_std',
                   loc=f2_ax_kz_std_legend_or,
                   bbox_to_anchor=f2_ax_kz_std_legend_bbox,
                   handlelength=2,
                   numpoints=3,
                   handletextpad=0.5,
                   ncol=f2_ax_kz_std_legend_cols,
                   prop={'size':14})
        #Include Arrows
        if f2_is_show_arrows:
            ax_f_7 = pltfct.make_arrows(ax_f_7,f2_num_arrays,f2_befaft,nrobs_int,
                                     arr_xvars,arr_yvars,f2_color_arr)

    if len(f2_conc_res_inds):
        ax_f_8 = ax_f_1.twinx()
        ax_f_8.spines['left'].set_position(('axes',f2_ax_offset_conc_res))
        ax_f_8.set_frame_on(True)
        ax_f_8.patch.set_visible(False)
        ax_f_8.set_ylabel('conc Residuals')
        ax_f_8.yaxis.set_label_position('left')
        for i in f2_conc_res_inds:
            ax_f_8.plot(arr_xvars,
                        arr_yvars[i],
                        color=f2_color_arr[i],
                        linestyle=f2_linestyle_array[i],
                        marker=f2_markerstyle_array[i],
                        markerfacecolor=f2_color_arr[i],
                        markeredgecolor=f2_color_arr[i],
                        markersize=9)
        conc_res_legend_labels = [f2_ax_legend_labels[i] for i in f2_conc_res_inds]
        plt.ylim([f2_ax_conc_res_y_min,f2_ax_conc_res_y_max])
        plt.legend(conc_res_legend_labels,
                   title = 'conc_res',
                   loc=f2_ax_conc_res_legend_or,
                   bbox_to_anchor=f2_ax_conc_res_legend_bbox,
                   handlelength=2,
                   numpoints=3,
                   handletextpad=0.5,
                   ncol=f2_ax_conc_res_legend_cols,
                   prop={'size':14})
        #Include Arrows
        if f2_is_show_arrows:
            ax_f_8 = pltfct.make_arrows(ax_f_8,f2_num_arrays,f2_befaft,nrobs_int,
                                     arr_xvars,arr_yvars,f2_color_arr)

    if len(f2_conc_std_inds):
        ax_f_9 = ax_f_1.twinx()
        ax_f_9.spines['left'].set_position(('axes',f2_ax_offset_conc_std))
        ax_f_9.set_frame_on(True)
        ax_f_9.patch.set_visible(False)
        ax_f_9.set_ylabel('conc Standard Deviation')
        ax_f_9.yaxis.set_label_position('left')
        for i in f2_conc_std_inds:
            ax_f_9.plot(arr_xvars,
                        arr_yvars[i],
                        color=f2_color_arr[i],
                        linestyle=f2_linestyle_array[i],
                        marker=f2_markerstyle_array[i],
                        markerfacecolor=f2_color_arr[i],
                        markeredgecolor=f2_color_arr[i],
                        markersize=9)
        conc_std_legend_labels = [f2_ax_legend_labels[i] for i in f2_conc_std_inds]
        plt.ylim([f2_ax_conc_std_y_min,f2_ax_conc_std_y_max])
        plt.legend(conc_std_legend_labels,
                   title = 'conc_std',
                   loc=f2_ax_conc_std_legend_or,
                   bbox_to_anchor=f2_ax_conc_std_legend_bbox,
                   handlelength=2,
                   numpoints=3,
                   handletextpad=0.5,
                   ncol=f2_ax_conc_std_legend_cols,
                   prop={'size':14})
        #Include Arrows
        if f2_is_show_arrows:
            ax_f_9 = pltfct.make_arrows(ax_f_9,f2_num_arrays,f2_befaft,nrobs_int,
                                     arr_xvars,arr_yvars,f2_color_arr)

    if f2_is_enforce_axis_input: # X axis
        plt.xlim([f2_plot_x_min,f2_plot_x_max])
        
    return fig_f2

########################################################################################
########################################################################################
##########################################################################################
def f3_plot(num_timesteps,nrobs_int,f3_num_arrays,mons_inds,f3_ax_legend_bbox,
            start_obs,f3_plot_x_max,f3_y_variable_mean,stddev_name,
            letter_true,figure_size_y,letters,assimstp_name,corr_dirs,mons_file_name,
            f3_i_want,assim_variables_dirs,diff_obs,assimstp_dir,f3_ax_y_label,
            f3_source_file_name,f3_plot_y_max,f3_plot_y_min,f3_ax_pos,f3_ax_legend_cols,
            f3_j_want,run_output_dirs,f3_ax_legend_labels,corr_name,assimstp_dirs,
            f3_x_variable,resid_name,f3_is_enforce_axis_input,model_name_big,f3_befaft,
            assim_variables_dir,run_output_dir,mons_file_dir,corr_dir,f3_ax_x_label,
            stddev_dir,true_output_dir,resid_dir,num_mons,f3_markersize,figure_size_x,
            model_output_dir, date_output_dir,resid_dirs, stddev_dirs,
            f3_plot_x_min,model_name,assim_variables_name,fig_f3 = 0):


    if not fig_f3:
        # Generate the figure
        fig_f3 = plt.figure(4, figsize=(figure_size_x,figure_size_y))
        fig_f3.set_facecolor((0.50, 0.50, 0.50))
        # Insert figure title
        plt.suptitle('Update tracking 2', y = 0.97, fontsize=20)
        

    #Go to directory
    os.chdir(assim_variables_dir)
    #Open vtk-Reader
    reader=vtk.vtkRectilinearGridReader()

    cell_numpy_y=[] 
    for i_arr in range(f3_num_arrays):
        wanted_nums=[]
        for i in range(nrobs_int):
            reader.SetFileName(f3_source_file_name + f3_befaft[i_arr] +'_' + str(i+1).zfill(4) + '.vtk')
            reader.SetScalarsName(f3_y_variable_mean)
            reader.Update()
            grid_dims = reader.GetOutput().GetDimensions()
            cell_vtk_y = reader.GetOutput().GetCellData().GetArray(0)
            cell_numpy_temp_y = vtk.util.numpy_support.vtk_to_numpy(cell_vtk_y)
            wanted_nums.append(cell_numpy_temp_y[(f3_j_want[i_arr]-1)*grid_dims[0] + f3_i_want[i_arr]])

        cell_numpy_y.append(wanted_nums)


    os.chdir(mons_file_dir)

    f3_num_show_mons = num_mons
    f3_start_obs = 2
    f3_diff_obs = 2
    f3_num_timesteps = 100
    f3_linestyle_array = ['' for i in range(f3_num_arrays + f3_num_show_mons)]
    f3_linestyle_array[f3_num_arrays:f3_num_arrays+f3_num_show_mons] = ['-' for i in range(f3_num_show_mons)]
    f3_markersize_array = [9 for i in range(f3_num_arrays + f3_num_show_mons)]
    f3_markersize_array[f3_num_arrays:f3_num_arrays+f3_num_show_mons] = [5 for i in range(f3_num_show_mons)]

    cell_numpy_x = np.genfromtxt(mons_file_name,
                                 dtype='f8',
                                 comments='%',
                                 usecols=(0)) # obstime
    if  f3_y_variable_mean == 'conc_mean':
        f3_variable_num = 13
    elif f3_y_variable_mean =='kz_mean':
        f3_variable_num = 18
    else:
        raise exceptions.RuntimeError, 'No supported variable name for true from mon_file'
    cell_numpy_temp_y = np.genfromtxt(mons_file_name,
                                      dtype='f8',
                                      comments='%',
                                      usecols=(f3_variable_num))
    if f3_y_variable_mean == 'kz_mean':
        cell_numpy_temp_y = map(math.log10,cell_numpy_temp_y)
        cell_numpy_temp_y = np.array(cell_numpy_temp_y)
#    mons_indsices = get_mons_inds(mons_file_name,
#                                       "/home/jk125262/shematOutputDir_Cluster/" \
#                                           + model_name +"_output/" + date + "/" \
#                                           + date + "_" + letter_true\
#                                           + "/samples_output",
#                                       num_mons)
    cell_numpy_x = cell_numpy_x.reshape(len(cell_numpy_x)/num_mons, num_mons)
    cell_numpy_x = cell_numpy_x[1:100:2,0]
    cell_numpy_temp_y = cell_numpy_temp_y.reshape(len(cell_numpy_temp_y)/num_mons, num_mons)
    for i in range(f3_num_show_mons):
        cell_numpy_y.append( cell_numpy_temp_y[f3_start_obs-1:f3_num_timesteps:f3_diff_obs,i])


    #Properties of read arrays
    len_arrays = len(cell_numpy_x)
    min_value_x=min(cell_numpy_x)
    max_value_x=max(cell_numpy_x)
    min_value_y=[min(cell_numpy_y[i]) for i in range(f3_num_arrays+f3_num_show_mons)]
    max_value_y=[max(cell_numpy_y[i]) for i in range(f3_num_arrays+f3_num_show_mons)]

    #Generate axis
    ax_f = fig_f3.add_subplot(1,11,2)
    ax_f.set_position(f3_ax_pos)
    ax_f.set_title(f3_source_file_name)
    ax_f.set_xlabel(f3_ax_x_label)
    ax_f.set_ylabel(f3_ax_y_label)
    #Generate plot
    plot_main=[ax_f.plot(cell_numpy_x,
                         cell_numpy_y[i],
                         color=color_arr[i],
                         linestyle=f3_linestyle_array[i],
                         marker='o',
                         markerfacecolor=color_arr[i],
                         markeredgecolor=color_arr[i],
                         markersize=f3_markersize_array[i])
               for i in range(f3_num_arrays+f3_num_show_mons)]
                               #label='Mean')

    #Set axis ranges
    if f3_is_enforce_axis_input:
        plt.axis([f3_plot_x_min,
                  f3_plot_x_max,
                  f3_plot_y_min,
                  f3_plot_y_max])

    else:
        plt.axis([min(f3_plot_x_min,min_value_x),
                  max(f3_plot_x_max,max_value_x),
                  min(f3_plot_y_min,min(min_value_y)),
                  max(f3_plot_y_max,max(max_value_y))])


    for i in range(f3_num_show_mons):
        f3_ax_legend_labels.append('True' 
                                   + str(int(mons_inds[i][0])).zfill(2)
                                   + ','
                                   + str(int(mons_inds[i][1])).zfill(2))
        

    #Set axis legend
    plt.legend(f3_ax_legend_labels,
               loc='upper left',
               bbox_to_anchor=f3_ax_legend_bbox,
               handlelength=2,
               numpoints=3,
               handletextpad=0.5,
               ncol=f3_ax_legend_cols,
               prop={'size':12})

    return fig_f3

########################################################################################
########################################################################################
##########################################################################################
def t_plot(num_timesteps,nrobs_int,t_ax_pos,t_variable_name,t_ax_high_cbar,mons_inds,
           start_obs,stddev_name,letter_true,t_ax_ylabel,t_ax_low_cbar,
           true_output_dir,assimstp_name,corr_dirs,mons_file_name,run_output_dir,
           t_is_show_mons,diff_obs,assimstp_dir,run_output_dirs,
           assim_variables_dirs,corr_name,assimstp_dirs,t_source_file_name,model_name_big,
           resid_name,t_ax_title,figure_size_y,assim_variables_dir,t_ax_num_cbar,
           mons_file_dir,t_mons_size,t_ax_xlabel,corr_dir,stddev_dir,t_ax_cbar_pos,
           model_output_dir, date_output_dir,resid_dirs, stddev_dirs,
           resid_dir,num_mons,letters,figure_size_x,model_name,assim_variables_name,
           t_is_scatter_inds,t_scatter_inds_x,t_scatter_inds_y,fig_t = None):


    if not fig_t:
        # Generate the figure
        fig_t = plt.figure(5, figsize=(figure_size_x,figure_size_y))
        fig_t.set_facecolor((0.50, 0.50, 0.50))
        # Insert figure title
        plt.suptitle('True plot', y = 0.97, fontsize=20)
        

    # Vtk readout functions
    data = pltfct.my_vtk_to_numpy(mons_file_dir, t_source_file_name,t_variable_name)
    step_x, step_y, npts_x, npts_y, low_m_x, high_m_x, low_m_y, high_m_y,\
        low_x, high_x, low_y, high_y = pltfct.vtk_grid_props(mons_file_dir, t_source_file_name,t_variable_name)


    #Generate axis
    ax_true = fig_t.add_subplot(1,3,3)
    ax_true.set_position(t_ax_pos)
    ax_true.set_title(t_ax_title)
    ax_true.set_xlabel(t_ax_xlabel)
    ax_true.set_ylabel(t_ax_ylabel)

    if t_is_show_mons:
        # Grid indices of observation locations
        ind_x = [mons_inds[i,0]*step_x-0.5*step_x for i in range(num_mons)]
        ind_y = [mons_inds[i,1]*step_y-0.5*step_y for i in range(num_mons)]

        #Scatterplot of observation locations
        ax_true.scatter(ind_x,
                        ind_y,
                        marker='o',
                        c='black',
                        s=t_mons_size)
    elif t_is_scatter_inds:
        # Own indices
        ind_x=[t_scatter_inds_x[i]*step_x-0.5*step_x for i in range(len(t_scatter_inds_x))]
        ind_y=[t_scatter_inds_y[i]*step_y-0.5*step_y for i in range(len(t_scatter_inds_y))]
        
        #Scatterplot of selfdefined indices
        ax_true.scatter(ind_x,
                        ind_y,
                        marker='o',
                        c=color_arr,
                        s=t_mons_size)
        


    ax_true = pltfct.make_quiver(mons_file_dir,t_source_file_name,'v',ax_true) # quiver
    

    #Generate image
    im = ax_true.imshow(data,
                        interpolation='nearest',
                        cmap=cm.get_cmap(name='jet',
                                         lut=t_ax_num_cbar),# 'gray', 'rgb', 'rainbow'
                        norm = colors.Normalize(vmin=t_ax_low_cbar,
                                                vmax=t_ax_high_cbar,
                                                clip=False),
                        origin='lower',
                        extent=[low_x,high_x,low_y,high_y])

    #Generate Colorbar
    ax_cbar = fig_t.add_subplot(1,4,4)
    ax_cbar.set_position(t_ax_cbar_pos)
    mpl.colorbar.Colorbar(ax_cbar,im)

    return fig_t

##########################################################################################
########################################################################################
########################################################################################
def h_plot(num_timesteps,nrobs_int,mons_inds,
           start_obs,stddev_name,letter_true,
           true_output_dir,assimstp_name,corr_dirs,mons_file_name,run_output_dir,
           diff_obs,assimstp_dir,run_output_dirs,
           assim_variables_dirs,corr_name,assimstp_dirs,model_name_big,
           resid_name,assim_variables_dir,
           mons_file_dir,corr_dir,stddev_dir,
           resid_dir,num_mons,letters,model_name,assim_variables_name,
           model_output_dir, date_output_dir,resid_dirs, stddev_dirs,
           h_ax_pos,h_ax_title,h_ax_xlabel,h_ax_ylabel,
           h_file_type, h_sc_cell_vars, h_befaft,
           h_obstimes, h_variable_name,
           h_width_factors, h_num_bins,
           h_hist_color, h_hist_normed, h_hist_type,
           h_cmap, h_cmap_kz, h_cmap_conc,
           h_n_cols,h_n_rows,
           h_data_bins,h_y_max,
           h_im_left,h_im_up, h_grid_factor,
           figure_size_x, figure_size_y, fig_h = None):

    if not fig_h:
        # Generate the figure
        fig_h = plt.figure(5, figsize=(figure_size_x,figure_size_y))
        fig_h.set_facecolor((0.50, 0.50, 0.50))
        # Insert figure title
        plt.suptitle('Histograms assim variables'
                     if h_file_type == 'av' else
                     'Histograms single cell ' + str(h_sc_cell_vars), y = 0.97, fontsize=20)


    
        
    # Axis Grid
    ax_h_grid = [fig_h.add_subplot(h_n_rows,h_n_cols,i)
                 for i in range(h_n_rows*h_n_cols)] 
    h_im_width=0.20*h_grid_factor
    h_im_height=0.15*h_grid_factor
    h_im_pad_hori=0.02*h_grid_factor
    h_im_pad_vert=0.05*h_grid_factor
    for i in range(h_n_rows):                       # Positions of Axis Grid
        for j in range(h_n_cols):
            ax_h_grid[i*h_n_cols+j].set_position([h_im_left+j*(h_im_width+h_im_pad_hori), 
                                                  1.0-h_im_up-h_im_height-i*(h_im_height+h_im_pad_vert),
                                                  h_im_width,
                                                  h_im_height])

    for i_subplt in range(h_n_rows*h_n_cols):
        # Get data
        h_source_file_name = ('single_cell_E1_'
                              + str(h_sc_cell_vars[0]).zfill(4) + '_'
                              + str(h_sc_cell_vars[1]).zfill(4) + '_'
                              + str(h_sc_cell_vars[2]).zfill(4) + '_'
                              + str(h_sc_cell_vars[3]).zfill(4) + '_'
                              + h_befaft + '_'
                              + str(h_obstimes[i_subplt]).zfill(4)
                              + '.plt'
                              if h_file_type == 'sc' else
                              'assim_variables_E1_'
                              + h_befaft + '_'
                              + str(h_obstimes[i_subplt]).zfill(4)
                              + '.vtk')
        if(h_source_file_name == 'logk_' + model_name + '.dat'):
            num_skiprows = 3
            os.chdir(run_output_dir)
            data = np.loadtxt(h_source_file_name, skiprows=num_skiprows)
        elif(h_source_file_name[0:5] == 'assim'):
            data = pltfct.my_vtk_to_numpy(run_output_dir + 'enkf_output',
                                          h_source_file_name,
                                          h_variable_name)
            data = [value for sublist in data for value in sublist]
        elif(h_source_file_name[0:11] == 'single_cell'):
            num_skiprows = 5
            os.chdir(run_output_dir + 'single_cell_output')
            data = np.loadtxt(h_source_file_name, skiprows=num_skiprows)

        # Data manipulation
        if i_subplt == 0:
            data_mean = sp.mean(data)
            data_var = sp.cov(data)
            
            data_dist = np.max(np.fabs(data-data_mean))

            if len(h_data_bins): # Data bins by hand
                data_bins = np.linspace(h_data_bins[0],
                                        h_data_bins[1],
                                        h_num_bins)
            else:               # Data bins from data mean
                data_bins = np.linspace(data_mean-h_width_factors[0]*data_dist,
                                        data_mean+h_width_factors[1]*data_dist,
                                        h_num_bins)

        ax_h_grid[i_subplt].set_title(h_ax_title + ' ' + str(h_obstimes[i_subplt]))
        hist_vals,hist_bins,hist_patches = ax_h_grid[i_subplt].hist(data, # Histogram
                                                                    bins = data_bins,
                                                                    normed = h_hist_normed,
                                                                    histtype = h_hist_type,
                                                                    rwidth = 0.95)

        # Constrain y-values
        if h_y_max:
            ax_h_grid[i_subplt].axis([data_bins[0],
                                      data_bins[-1],
                                      0,
                                      h_y_max])
        
        hist_cmap = cm.get_cmap(h_cmap) # Load cmap instance (name is input)
        h_norm = colors.normalize(h_cmap_kz[0]
                                  if h_variable_name[0:2]=='kz' else
                                  h_cmap_conc[0],
                                  h_cmap_kz[1]
                                  if h_variable_name[0:2]=='kz' else
                                  h_cmap_conc[1])
    
        for this_bin, this_patch in zip(hist_bins,hist_patches): 
            this_color = hist_cmap(h_norm(this_bin)) # Color chosen from cmap via bin
            this_patch.set_facecolor(this_color) # Patch set to corresponding color

        
    return fig_h

##########################################################################################
########################################################################################
########################################################################################
def s_plot(num_timesteps,nrobs_int,mons_inds,
           start_obs,stddev_name,letter_true,
           true_output_dir,assimstp_name,corr_dirs,mons_file_name,run_output_dir,
           diff_obs,assimstp_dir,run_output_dirs,
           assim_variables_dirs,corr_name,assimstp_dirs,model_name_big,
           resid_name,assim_variables_dir,
           mons_file_dir,corr_dir,stddev_dir,
           resid_dir,num_mons,letters,model_name,assim_variables_name,
           model_output_dir, date_output_dir,resid_dirs, stddev_dirs,
           s_ax_pos,s_ax_title,s_ax_xlabel,s_ax_ylabel,
           s_variable_names, s_num_input_data,
           s_width_factors,s_is_text,s_num_bins,
           s_ax_enforce, s_ax_minmax, s_file_types, s_sc_cell_vars,
           s_befaft,s_obstime,
           s_colors, s_linewidths, s_size,
           s_y_ticks, s_y_ticklabels, s_x_ticks, s_x_ticklabels,
           figure_size_x, figure_size_y, fig_s = None):

    if not fig_s:
        # Generate the figure
        fig_s = plt.figure(5, figsize=(figure_size_x,figure_size_y))
        fig_s.set_facecolor((0.50, 0.50, 0.50))
        # Insert figure title
        plt.suptitle('Scatter plot', y = 0.97, fontsize=20)

    #Generate axis
    ax_s = fig_s.add_subplot(1,21,21)
    ax_s.set_position(s_ax_pos)
    ax_s.set_title(s_ax_title)
    ax_s.set_xlabel(s_ax_xlabel)
    ax_s.set_ylabel(s_ax_ylabel)

    # Source file names
    s_source_file_names = ['single_cell_E1_'
                           + str(s_sc_cell_vars[0][0]).zfill(4) + '_'
                           + str(s_sc_cell_vars[0][1]).zfill(4) + '_'
                           + str(s_sc_cell_vars[0][2]).zfill(4) + '_'
                           + str(s_sc_cell_vars[0][3]).zfill(4) + '_'
                           + s_befaft[0] + '_'
                           + str(s_obstime[0]).zfill(4) + '.plt'
                           if s_file_types[0] == 'sc' else
                           'assim_variables_E1_'
                           + s_befaft[0] + '_'
                           + str(s_obstime[0]).zfill(4)
                           + '.vtk'
                           ,
                           'single_cell_E1_'
                           + str(s_sc_cell_vars[1][0]).zfill(4) + '_'
                           + str(s_sc_cell_vars[1][1]).zfill(4) + '_'
                           + str(s_sc_cell_vars[1][2]).zfill(4) + '_'
                           + str(s_sc_cell_vars[1][3]).zfill(4) + '_'
                           + s_befaft[1] + '_'
                           + str(s_obstime[1]).zfill(4) + '.plt'
                           if s_file_types[1] == 'sc' else
                           'assim_variables_E1_'
                           + s_befaft[1] + '_'
                           + str(s_obstime[1]).zfill(4)
                           + '.vtk',
                           ]

    # Get data
    data = [None,None]
    for i,source_file_name in enumerate(s_source_file_names):
        if(source_file_name == 'logk_' + model_name + '.dat'):
            num_skiprows = 3
            os.chdir(run_output_dir)
            data[i] = np.loadtxt(source_file_name, skiprows=num_skiprows)
        elif(source_file_name[0:5] == 'assim'):
            variable_name = s_variable_names[i]
            data[i] = pltfct.my_vtk_to_numpy(run_output_dir + 'enkf_output',
                                       source_file_name,
                                       variable_name)
            data[i] = [value for sublist in data[i] for value in sublist]
        elif(source_file_name[0:11] == 'single_cell'):
            num_skiprows = 5
            os.chdir(run_output_dir + 'single_cell_output')
            data[i] = np.loadtxt(source_file_name, skiprows=num_skiprows)


    # Data manipulation
    x = data[0][0:s_num_input_data]
    y = data[1][0:s_num_input_data] #+ rnd.randn(num_input_data)*1.0
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

    x_bins = np.linspace(x_mean-s_width_factors[0]*x_lim,
                         x_mean+s_width_factors[1]*x_lim,
                         s_num_bins)
    y_bins = np.linspace(y_mean-s_width_factors[2]*x_lim,
                         y_mean+s_width_factors[3]*x_lim,
                         s_num_bins)
    
    if s_is_text:
        x_mean_string = '%16.8f' %x_mean
        y_mean_string = '%7.3e' %y_mean
        x_std_string = '%16.8f' %np.sqrt(cov_xy[0,0])
        y_std_string = '%7.3e' %np.sqrt(cov_xy[1,1])
        corr_string = '%16.8f' %corr_mat[0,1]
        text_string = 'Mean_x:  ' + x_mean_string[0:-3] \
            + '\nMean_y:  ' + y_mean_string \
            + '\nStd_x:   ' + x_std_string[0:-3] \
            + '\nStd_y:   ' + y_std_string \
            + '\nCorr_xy: ' + corr_string[0:-3]
        text = fig.text(0.78,0.75,text_string,fontsize=16)
        text.set_bbox(dict(facecolor=(0.8,0.8,0.8), alpha=0.5))
    
    # Make scatter plot
    ax_s.scatter(x,
                 y,
                 c=s_colors,
                 linewidths = s_linewidths,
                 s=s_size,
                 marker='d')

    # ax_s.yaxis.set_ticks(s_y_ticks)
    # ax_s.yaxis.set_ticklabels(s_y_ticklabels)
    # ax_s.xaxis.set_ticks(s_x_ticks)
    # ax_s.xaxis.set_ticklabels(s_x_ticklabels)

    if s_ax_enforce:
        ax_s.set_xlim(s_ax_minmax[0],s_ax_minmax[1])
        ax_s.set_ylim(s_ax_minmax[2],s_ax_minmax[3])
    
    return fig_s

##########################################################################################
########################################################################################
########################################################################################
def pc_plot(num_timesteps,nrobs_int,mons_inds,
            start_obs,stddev_name,letter_true,
            true_output_dir,assimstp_name,corr_dirs,mons_file_name,run_output_dir,
            diff_obs,assimstp_dir,run_output_dirs,
            assim_variables_dirs,corr_name,assimstp_dirs,model_name_big,
            resid_name,assim_variables_dir,
            mons_file_dir,corr_dir,stddev_dir,
            resid_dir,num_mons,letters,model_name,assim_variables_name,
            model_output_dir, date_output_dir,resid_dirs, stddev_dirs,
            nl,date,
            pc_output,pc_is_show_ens,pc_num_ens,pc_title_text,pc_x_min,pc_x_max,
            pc_nl,pc_dates,pc_letters,
            pc_y_min,pc_y_max,pc_legend_loc,pc_legend_bbox_anchor,pc_colored,
            pc_n_per_color,pc_marker_colors,pc_line_colors,
            figure_size_x, figure_size_y, fig_pc = None):

    
    if not fig_pc:
        # Generate the figure
        fig_pc = plt.figure(5, figsize=(figure_size_x,figure_size_y))
        fig_pc.set_facecolor((0.50, 0.50, 0.50))
        # Insert figure title
        plt.suptitle('Compare plot', y = 0.97, fontsize=20)

    if pc_nl:
        nl = pc_nl
    if pc_dates and pc_letters:
        if len(pc_dates) == len(pc_letters) and len(pc_dates) == pc_nl:
            resid_dirs = [model_output_dir + pc_dates[i] + "/"
                          + pc_dates[i] + "_" + pc_letters[i] + "/"
                          + "enkf_output" for i in range(len(pc_dates))]
            letters = pc_letters
        else:
            os.chdir(python_dir)
            raise exceptions.RuntimeError, "pc_dates, pc_letters or pc_nl not as wanted"
        

    nl_f = float(nl)            # Color themes
    getting_darker = [(float(i)/nl_f , float(i)/nl_f , float(i)/nl_f)  for i in range(nl)]
    getting_darker.reverse()
    
    changing_black_white = [(0,0,0) if i%2 else (0.5,0.5,0.5) for i in range(nl)]
    
    if pc_colored is None:
        pc_colored = [1 for i in range(nl)] # False: Grey instead of color, Default: all true
    if pc_marker_colors is None:
        pc_marker_colors = getting_darker # Marker colors
    if pc_line_colors is None:
        pc_line_colors = [color_arr[i/pc_n_per_color] if pc_colored[i] else 'grey'
                       for i in range(nl)] # Line colors


    if pc_output == 'res':         # Title, filename, variable depending on 'res'/'std'
        if pc_title_text is None:
            pc_title_text = 'Residual ' + date
        var_name = 'rms_kz_aft'
        input_file_name = 'residual_E1.vtk'
    elif pc_output  == 'std':
        if pc_title_text is None:
            pc_title_text = 'Stddevs ' + date
        var_name = 'std_kz_aft'
        input_file_name = 'stddev_E1.vtk'
    else:
        raise exceptions.RuntimeError, 'Wrong input_file_name.  ' + input_file_name

    #############################################################################
    #Checks
    for resid_dir in resid_dirs: # Does file exist? Is variables in file?
        if not pltfct.is_scalar_var_in_file(var_name, input_file_name, resid_dir):
            raise exceptions.RuntimeError, 'var_name ' + var_name \
                + 'not in input_file_name ' + input_file_name \
                + 'in resid_dir' + resid_dir


    ############################################################################

    ax = fig_pc.add_subplot(1,1,1) # Axis
    # ax.set_position([0.55,0.55,
    #                  0.35,0.35])
    ax.set_title(pc_title_text,
                 fontsize = 25)
    ax.set_xlabel('obstime')
    ax.set_ylabel('Residuals')


    data_x=[]         
    data_y=[]
    plots=[]
    plot_labels=[]

    for i,letter in enumerate(letters): # Loop over letters
        
        data_x = pltfct.my_vtk_to_numpy(resid_dirs[i], # x-data
                                               input_file_name,
                                               'obstime')
        data_y = pltfct.my_vtk_to_numpy(resid_dirs[i], # y-data
                                               input_file_name,
                                               var_name)
        

        plots.append(ax.plot(data_x, # Main plot
                             data_y,
                             color=pc_line_colors[i],
                             linestyle='-',
                             linewidth=2.5,
                             marker='o',
                             markerfacecolor=pc_marker_colors[i],
                             markeredgecolor=pc_marker_colors[i],
                             markersize=6))
                               #label='Mean')
        plot_labels.append('Residuals ' + letter
                           if not pc_nl else
                           'Res ' + pc_dates[i] + '_' + letter )


        if pc_is_show_ens:         # Ensemble of residuals
            for i_arr in range(pc_num_ens): 
                data_ens = pltfct.my_vtk_to_numpy(resid_dirs[i],
                                                  input_file_name,
                                                  'rm_kz_aft_' + str(i_arr+1))
                plot_ens = ax.plot(data_x,
                                   data_ens,
                                   color=pc_line_colors[i],
                                   linestyle='-',
                                   marker='',
                                   markerfacecolor='grey',
                                   markeredgecolor='grey',
                                   markersize=6)


    refined_legend=plt.legend(plots, # Legend
                              plot_labels,
                              title = 'Legend',
                              loc=pc_legend_loc,
                              bbox_to_anchor=pc_legend_bbox_anchor,
                              handlelength=2,
                              numpoints=2,
                              handletextpad=0.5,
                              ncol=3,
                              prop={'size':16})


    plt.axis([pc_x_min,pc_x_max,pc_y_min,pc_y_max]) # R
        

    return fig_pc


########################################################################################
########################################################################################
########################################################################################## 
def set_paths(output_files_dir, model_name, model_name_big, date, letters, letter_true, nl):

    # Output path for the model
    model_output_dir = output_files_dir + model_name + "_output/"

    # Output path for model and date
    date_output_dir = model_output_dir + date + "/"

    # Output path for mode, date and run (specified by letter)
    run_output_dir = date_output_dir + date + "_" + letters[0] + "/"
    run_output_dirs = [date_output_dir 
                       + date + "_" + letters[i] + "/"
                       for i in range(nl)]

    # Output path for model, date and true run (specified be letter for true)
    true_output_dir = date_output_dir + date + "_" + letter_true + "/"
    
    #Assim variables file/path
    assim_variables_dir= run_output_dir + 'enkf_output'
    assim_variables_dirs= [run_output_dirs[i] + 'enkf_output' for i in range(nl)]
    assim_variables_name='assim_variables_E1_' #'residual' 'stddev'

    #Assim variables file/path
    corr_dir= run_output_dir + 'enkf_output'
    corr_dirs= [run_output_dirs[i] + 'enkf_output' for i in range(nl)]
    corr_name='correlation_' #'residual' 'stddev'

    #Residuals file/path
    resid_dir= run_output_dir + 'enkf_output'
    resid_dirs = [run_output_dirs[i] + 'enkf_output' for i in range(nl)]
    resid_name='residual_E1.vtk'

    #Stddev file/path
    stddev_dir= run_output_dir + 'enkf_output'
    stddev_dirs = [run_output_dirs[i] + 'enkf_output' for i in range(nl)]
    stddev_name='stddev_E1.vtk'

    #Monitor file/path
    mons_file_dir= true_output_dir + "samples_output"
    mons_file_name= model_name_big + '_TRUE_E0_monitor_1.dat'

    #Assimstp file/path
    assimstp_dir = run_output_dir + 'enkf_output'
    assimstp_dirs = [run_output_dirs[i] + 'enkf_output' for i in range(nl)]
    assimstp_name = 'assimstp_E1_1'

    dir_in={'model_output_dir':model_output_dir,
            'date_output_dir': date_output_dir,
            'run_output_dir':run_output_dir,
            'run_output_dirs':run_output_dirs,
            'true_output_dir':true_output_dir,
            'assim_variables_dir':assim_variables_dir,
            'assim_variables_dirs':assim_variables_dirs,
            'assim_variables_name':assim_variables_name,
            'corr_dir':corr_dir,
            'corr_dirs':corr_dirs,
            'corr_name':corr_name,
            'resid_dir':resid_dir,
            'resid_dirs':resid_dirs,
            'resid_name':resid_name,
            'stddev_dir':stddev_dir,
            'stddev_dirs':stddev_dirs,
            'stddev_name':stddev_name,
            'mons_file_dir':mons_file_dir,
            'mons_file_name':mons_file_name,
            'assimstp_dir':assimstp_dir,
            'assimstp_dirs':assimstp_dirs,
            'assimstp_name':assimstp_name,
            }
    return dir_in
########################################################################################
########################################################################################
#####################################################################################
def set_immediate_vars(model_name_big, run_output_dir, mons_file_name, mons_file_dir):

    #Number of monitoring points
    num_mons = pltfct.get_num_mons('observations_'+ model_name_big + '.dat',run_output_dir)
    #Indices of monitoring points
    mons_inds = pltfct.get_mons_inds(mons_file_name, mons_file_dir, num_mons)

    #Number of observation intervals
    nrobs_int = pltfct.get_nrobs_int(model_name_big + '.enkf', run_output_dir)

    #Time step of first observation
    start_obs = pltfct.get_start_obs('observations_'+ model_name_big + '.dat',run_output_dir)

    #Time step difference for first two observations
    diff_obs = pltfct.get_diff_obs('observations_'+ model_name_big + '.dat',run_output_dir,
                               num_mons, start_obs)
    #Number of timesteps
    num_timesteps = pltfct.get_num_timesteps(mons_file_name, mons_file_dir, num_mons)


    fun_in = {'num_mons':num_mons,'mons_inds':mons_inds,'nrobs_int':nrobs_int,'start_obs':start_obs,'diff_obs':diff_obs,'num_timesteps':num_timesteps}

    return fun_in

########################################################################################
########################################################################################
#####################################################################################
def saving_fig(save_pics_dir,save_pics_names,figs):
    if not os.path.exists(save_pics_dir):
        os.mkdir(save_pics_dir)
    os.chdir(save_pics_dir)
    if len(save_pics_names) == len(figs):
        for i in range(len(save_pics_names)):
            figs[i].savefig(save_pics_names[i],
                        facecolor=figs[i].get_facecolor(), # Keep background color in png
                        edgecolor='none')
            print('\nSaved ' + save_pics_names[i] + ' in ' + save_pics_dir)
    else:
        raise exceptions.RuntimeError, 'save_pics_names and figs must be of equal length.'

print('\n Done with module : myplots.py.')
print(time.asctime( time.localtime( time.time())))
