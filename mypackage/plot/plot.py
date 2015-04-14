#!/usr/bin/python

#Paths
python_dir = '/home/jk125262/PythonDir_Cluster/'
output_files_dir    = '/home/jk125262/shematOutputDir_Cluster/'

# Operating system commands
import os                            # Operating system (os.chdir, os.path)
import sys                           # System variables (PYTHONPATH as list sys.path)
import time                          # Timing the execution (time.time(), time.clock())
import string                        # Load alphabet (string.alphabet())
from matplotlib import pyplot as plt # Plotting commands (plt.show())

sys.path[0] = python_dir             # Add path to sys.path to load mypackage
from mypackage.plot import myplots
from mypackage.run import runmodule  as rm

# #Reload changed modules
# myplots = reload(myplots)                 

def p(
model_name = myplots.mymodel_name,
date = myplots.mydate,
letter = myplots.myletter,             # Letter inputs
n_l = 1,
step = 1,
letter_true = myplots.myletter_true,
is_m = 0,                 # Grid of Grids
is_f = 0,                 # Plot residuals/stddevs
is_f2 = 0,                # Plot update at point
is_f3 = 0,                # Clone of f2
is_t = 0,                 # True grid
is_h = 0,                 # Histogram grid
is_s = 0,                 # Scatter plot
is_show = 1,
is_save = 1,
figure_size_x = 20.0,
figure_size_y = 11.85,
# 
#
m_infiles = ['av','av','av'],    # 'cor', 'init', 'end'
m_cor_cell_var = [[10,16,1,3],[10,16,1,3],[10,16,1,3]],
m_varnames = ['kz_mean',
              'kz_std',
              'kz_res'],#'correlations0004','kz_res','kz_mean','kz_std'
m_befaft = ['aft','aft','aft'],
m_first =  1,
m_diff =   1, # First timestep, difference between timesteps
#Figure input
m_n_rows = 3,
m_n_cols = 6,               # Number of rows/columns
m_is_subarray = False,
m_is_masked = False,
m_cbar_kz_low = -11,
m_cbar_kz_high = -9,
m_cbar_kz_res_low = -1.0,
m_cbar_kz_res_high = 1.0,
m_cbar_cor_low = -0.3,
m_cbar_cor_high = 0.3,
m_kz_std_low = 0.0,
m_kz_std_high = 1.0,  # Colorbar low/high, var: kz_std
m_grid_factor =1.0,
m_im_left =0.045,
m_im_up =0.10, # Geometry of plots
m_cbar_left_pad = 0.01,
m_cbar_space = 0.06,
m_cbar_titles = ['Mean','Std','Res'],
m_num_cbar = 15, # Geometry of Cbar
m_is_show_mons = 0,
m_mons_size = 10, # Monitoring points in plots/size
m_is_text = 0,   # Show text
m_fig_title = None,             # Stem of the file name if not explicitly set
m_fig_title_font = 30,
m_pic_name = 'plot_m',
m_pic_ending = '.png',
m_cmaps = myplots.cmaps,
# 
# 
f_res_std = [1,1], #Show Residual/show Std
f_x_variable ='obstime',              # x-variable
f_y_vars_mean = ['rms_kz_aft','std_kz_aft'], #Mean variable names
f_y_variables_ens = None, # Ens var names
f_ax_pos =[0.10,0.10,0.80,0.80],  # Axis position [Left,Low,Width,Height]
f_plot_x_min = 0,
f_plot_x_max = 10,
f_plot_y_min = [0.2,0.2],
f_plot_y_max = [1.0,1.0], # Axis Ranges
f_markersize = 8,       # Marker size
f_ax_x_label = 'obstime',
f_ax_y_labels = ['Residuals', 'Standard Deviation'],# Axis labels
f_line_colors = ['black','red'],        # Line colors
f_ax_legend_labels =[['EnsembleMembers' if i else 'Mean' for i in range(1+1)],['Stddev']], # Legend labels
f_ax_legend_cols = [1,1],
f_ax_legend_loc = ['upper right','upper right'],
f_ax_legend_bbox = [(1.0,1.0),(1.0,0.85)],
f_ax_legend_handle_length = [3,5], # Legend geometry
f_fig_title = 'Residuals and Standard Deviation',
f_fig_title_font = 30,
f_pic_name = 'plot_f',
f_pic_ending = '.png',
#
# 
f2_num_arrays = 0,     # Num of arrs from asssim_variables (depends on n_l# )
f2_av_letters = None,  # [0,0,...] len = f2_num_arrays
f2_x_variable = 'obstime',
f2_y_variables = None,          # ['kz_mean','kz_mean',...] len = f2_num_arrays
f2_i = None,               # [10,10,22,22,10,10,22,22,...] len = f2_num_arrays
f2_j = None,               # [16,16,...] len = f2_num_arrays
f2_befaft = None,               # ['bef','aft','bef','aft',...] len = f2_num_arrays
f2_array_marker_size = 9,
f2_color_arr = myplots.color_arr,
#
f2_corr_num_arrays  = 0,
f2_corr_letters = None,         # [0,0,...] len = f2_corr_num_arrays
f2_corr_colored = [0,1,2,3,4,5,6,7,8,9],
f2_corr_y_variables = None,     # ['correlations0004' , ... ] len = f2_corr_num_arrays
f2_corr_i = None,       # [22,22,...] len = f2_corr_num_arrays
f2_corr_j = None,       # [16,16,...] len = f2_corr_num_arrays
f2_corr_befaft = None,          # ['bef','bef',...]    len = f2_corr_num_arrays
f2_corr_ref_cells = None,       # [ [22,16,1] , [22,16,1] , ... ]   len = f2_corr_num_arrays
f2_corr_ref_var = 3,
#
f2_mons_num_mons = 0,
f2_mons_num_variables = 1,
f2_mons_mons_inds = [0,1],
f2_mons_y_variables = ['kz_mean', 'conc_mean'],
#
f2_assimstp_num_show = 0,
f2_assimstp_letters = [0,0,0],
f2_assimstp_show = [1,3,2],     # 1: meanS, 2: innov, 3: obs_pert
f2_assimstp_mon_nums = [0,0,0],
f2_assimstp_var = 'conc_mean',
f2_assimstp_show_line = [0,1,0], # Show lines for meanS,innov,obs_ert respectively
f2_assimstp_marker_size = 9,
#
f2_ax_pos = [0.15,0.10,0.78,0.80], # Axis position [left,low,width,height]
f2_ax_x_label = 'f2_x_variable',
f2_ax_y_label = 'conc_mean',
f2_ax_legend_cols = 3 ,
f2_ax_offset_corr = -0.04,
f2_ax_offset_kz = -0.04,
f2_ax_offset_kz_res = -0.04,
f2_ax_offset_kz_std = -0.04,
f2_ax_offset_conc_res = -0.04,
f2_ax_offset_conc_std = -0.04,
f2_ax_legend_or = 'lower left',
f2_ax_legend_bbox = [0.0,0.0], # Legend geometry
f2_ax_legend_corr_cols = 2,
f2_ax_legend_corr_or = 'upper left',
f2_ax_legend_corr_bbox = [0.0,1.0], # Correlation legend geometry
f2_ax_legend_kz_cols = 3,
f2_ax_legend_kz_or = 'lower right',
f2_ax_legend_kz_bbox = (1.0,0.0), # Perm legend geometry
f2_ax_legend_kz_res_cols = 3,
f2_ax_legend_kz_res_or = 'lower right',
f2_ax_legend_kz_res_bbox = (1.0,0.0), # Perm legend geometry
f2_ax_legend_kz_std_cols = 3,
f2_ax_legend_kz_std_or = 'lower right',
f2_ax_legend_kz_std_bbox = (1.0,0.0), # Perm legend geometry
f2_ax_legend_conc_res_cols = 3,
f2_ax_legend_conc_res_or = 'lower right',
f2_ax_legend_conc_res_bbox = (1.0,0.0), # Perm legend geometry
f2_ax_legend_conc_std_cols = 3,
f2_ax_legend_conc_std_or = 'lower right',
f2_ax_legend_conc_std_bbox = (1.0,0.0), # Perm legend geometry
f2_is_enforce_axis_input = 1,
f2_ax_x_min = 0,
f2_ax_x_max = 10.5, # x-axis Range
f2_ax_y_min = 0.0055,
f2_ax_y_max = 0.0085, # y-axis Range
f2_ax_corr_y_min = -0.8,
f2_ax_corr_y_max = 0.8, # corr y-axis Range
f2_ax_kz_y_min = -14.0,
f2_ax_kz_y_max = -9.0,   # kz y-axis Range
f2_ax_kz_res_y_min = 0.0,
f2_ax_kz_res_y_max = 1.0,   # kz y-axis Range
f2_ax_kz_std_y_min = 0.0,
f2_ax_kz_std_y_max = 1.0,   # kz y-axis Range
f2_ax_conc_res_y_min = 0.0,
f2_ax_conc_res_y_max = 0.001,   # kz y-axis Range
f2_ax_conc_std_y_min = 0.0,
f2_ax_conc_std_y_max = 0.001,   # kz y-axis Range
f2_ax_corr_show_line = 1,        # Show line in correlation
f2_ax_corr_show_marker = 1,        # Show marker in correlation
f2_is_show_arrows = 1, # Show the arrows
f2_fig_title = 'Update Tracking',
f2_fig_title_font = 30,
f2_axis_title = 'Axis Title',
f2_pic_name = 'plot_f2',
f2_pic_ending = '.png',
#
# 
f3_source_file_name = 'assim_variables_E1_', #'residual' 'stddev'
f3_x_variable ='obstime',
f3_y_variable_mean = 'kz_mean',
f3_num_arrays = 4,
f3_i_want = [10,10,22,22,10],
f3_j_want = [16,16,16,16,26],
f3_befaft = ['bef', 'aft', 'bef', 'aft'],
f3_ax_pos = [0.10,0.10,0.80,0.80], # Axis position [left,low,width,height]
f3_ax_x_label = 'obstime',
f3_ax_y_label = 'kz_mean', # Axis labels
f3_ax_legend_labels = [],
f3_ax_legend_cols = 1,
f3_ax_legend_bbox = (0.0,1.0), # Legend
f3_markersize = 4,     # Marker size
f3_is_enforce_axis_input = 0, # Enforce axis range input
f3_plot_x_min = 0,
f3_plot_x_max = 10.5,
f3_plot_y_min = -11,
f3_plot_y_max = -9, # Axis Ranges
f3_pic_name = 'plot_f3',
f3_pic_ending = '.png',
#
# 
t_source_file_name = None,
t_variable_name = 'head',
t_ax_pos = [0.20,0.14,0.25,0.25],
t_ax_title = 'True.vtk',
t_ax_xlabel = 'x',
t_ax_ylabel = 'y',
t_ax_cbar_pos = [ 0.40, 0.14, 0.01, 0.25 ],
t_ax_num_cbar = 15,
t_ax_low_cbar = 0,
t_ax_high_cbar = 20,
t_is_show_mons = 0,     # Show scatterplot of monitoring points
t_mons_size= 50,
t_is_scatter_inds = 1,  # Show scatterplot of selfdefined points(mons must be off)
t_scatter_inds_x = [5,27,10,22,5,27],
t_scatter_inds_y = [5,5,16,16,27,27],
t_pic_name = 'plot_t',
t_pic_ending = '.png',
#
#
# h_source_file_name = 'assim_variables_E1_aft_0009.vtk',
h_file_type = 'av',             # 'av', 'sc'
h_sc_cell_vars = [22,16,1,3],     # Single cell, which cell, which variable
h_befaft = 'aft',               # 'bef', 'aft'
h_obstimes = range(9,50,3),      # observation times
h_variable_name = 'kz_mean',    # only important for 'av'
h_ax_pos = [0.1,0.1,0.8,0.8],
h_ax_title = 'Histogram',
h_ax_xlabel = 'x',
h_ax_ylabel = 'y',
h_pic_name = 'plot_h',
h_pic_ending = '.png',
h_width_factors = [1,1],             # left, right
h_num_bins = 20,
h_hist_color = 'black',
h_hist_normed = True,
h_hist_type = 'bar',
h_cmap_kz = [-10.2,-9.8],
h_cmap_conc = [0.005,0.008],
h_cmap = 'Reds',
h_n_cols = 3,
h_n_rows = 3,
h_grid_factor = 1.4,
h_im_left = 0.045,
h_im_up = 0.13,
#
#
s_source_file_names = ['assim_variables_E1_aft_0009.vtk','assim_variables_E1_aft_0009.vtk'],
s_variable_names = ['kz_mean','kz_mean'],
s_num_input_data = 500,
s_ax_pos = [0.1,0.1,0.8,0.8],
s_ax_title = 'Scatter',
s_ax_xlabel = 'x',
s_ax_ylabel = 'y',
s_pic_name = 'plot_s',
s_pic_ending = '.png',
s_width_factors = [1,1,1,1],     # x_left, x_right, y_down, y_up
s_num_bins = 30,
s_is_text = 0,
s_colors = ['black'], # [[(i/31)/40.0,(i/31)/40.0,(i/31)/40.0] for i in range(31*31)]
# [[(i%31)/40.0,(i%31)/40.0,(i%31)/40.0] for i in range(31*31)]
s_linewidths = [0.01],
s_size = 20,
s_y_ticks = None,
s_y_ticklabels = None,
s_x_ticks = None,
s_x_ticklabels = None,
):                 
    """
    
    Multiple plot routine.

    model_name                  # Name of the model
    date                        # Date of the model output
    letter                      # Starting letter (main letter)
    n_l                         # Number of letters (mostly one)
    step                        # Letter stepsize (mostly one)
    """
    ######################################################################################

    plt.close('all')

    #General inputs
    model_name_big = model_name.upper()

    suffix_start=rm.get_num_let(letter) # Letter array from start, number and step
    suffix_end = suffix_start + n_l*step 
    alphabet = string.lowercase          
    letters = [(alphabet[i/26-1]+alphabet[i%26] if i>25 else alphabet[i]) 
               for i in range(suffix_start,suffix_end,step)] 

    
    gen_in = {'model_name':model_name, # Input dictionary 
              'model_name_big':model_name_big,
              'letters':letters,
              'letter_true':letter_true,
              'figure_size_x':figure_size_x,
              'figure_size_y':figure_size_y,
              }
    ######################################################################################
    ######################################################################################

    # Directories
    dir_in = myplots.set_paths(output_files_dir, gen_in['model_name'], gen_in['model_name_big'],date, gen_in['letters'], gen_in['letter_true'], n_l)
    pics_dir = dir_in['date_output_dir'] + 'pics'
        
    
    # Variables
    fun_in = myplots.set_immediate_vars(model_name_big, dir_in['run_output_dir'], dir_in['mons_file_name'], dir_in['mons_file_dir'])

    ######################################################################################
    m_in={'varnames' :m_varnames,
          'm_infiles':m_infiles,
          'm_cor_cell_var':m_cor_cell_var,
          'm_befaft':m_befaft,
          'm_first' :  m_first,
          'm_diff' :   m_diff,
          'm_n_rows' : m_n_rows,
          'm_n_cols' : m_n_cols,
          'm_is_subarray':m_is_subarray,
          'm_is_masked':m_is_masked,
          'm_kz_std_low' : m_kz_std_low,
          'm_kz_std_high' : m_kz_std_high, 
          'm_grid_factor' :m_grid_factor,
          'im_left' :m_im_left,
          'im_up' :m_im_up,
          'm_cbar_left_pad' : m_cbar_left_pad,
          'm_cbar_space' : m_cbar_space,
          'm_num_cbar' : m_num_cbar,
          'm_cbar_titles': m_cbar_titles,
          'm_is_show_mons' : m_is_show_mons,
          'm_mons_size' : m_mons_size,
          'm_is_text' : m_is_text,  
          'm_fig_title': m_fig_title,
          'm_fig_title_font': m_fig_title_font,
          'm_cmaps' : m_cmaps,
          'm_cbar_kz_high' : m_cbar_kz_high,
          'm_cbar_kz_low'  : m_cbar_kz_low,
          'm_cbar_kz_res_high'  : m_cbar_kz_res_high,
          'm_cbar_kz_res_low' : m_cbar_kz_res_low,
          'm_cbar_cor_low': m_cbar_cor_low,
          'm_cbar_cor_high': m_cbar_cor_high,
          }

    if f_y_variables_ens is None:
        f_y_variables_ens  = [['rm_kz_aft_' + str(i+1) for i in range(20)], []] # Ens var names
        
    f_in={'f_res_std' : f_res_std,
          'f_x_variable' :f_x_variable,      
          'f_y_vars_mean' : f_y_vars_mean,
          'f_y_variables_ens' :f_y_variables_ens,
          'figure_size_x':figure_size_x,
          'figure_size_y':figure_size_y,
          'f_ax_pos' :f_ax_pos, 
          'f_plot_x_min' : f_plot_x_min,
          'f_plot_x_max' : f_plot_x_max,
          'f_plot_y_min' : f_plot_y_min,
          'f_plot_y_max' : f_plot_y_max,
          'f_markersize' : f_markersize, 
          'f_ax_x_label' : f_ax_x_label,
          'f_ax_y_labels' : f_ax_y_labels,
          'f_line_colors' : f_line_colors, 
          'f_ax_legend_labels' : f_ax_legend_labels,
          'f_ax_legend_cols' : f_ax_legend_cols,
          'f_ax_legend_loc' : f_ax_legend_loc,
          'f_ax_legend_bbox' : f_ax_legend_bbox,
          'f_ax_legend_handle_length' : f_ax_legend_handle_length,
          'f_fig_title': f_fig_title,
          'f_fig_title_font': f_fig_title_font,
          } 

    if f2_av_letters is None:
        f2_av_letters = [i/f2_num_arrays for i in range(f2_num_arrays)]
    if f2_y_variables is None:
        f2_y_variables = ['kz_mean' for i in range(f2_num_arrays)]
    if f2_i is None:
        f2_i = [10 if not i/2 else 22 for i in range(f2_num_arrays)] 
    if f2_j is None:
        f2_j = [16 for i in range(f2_num_arrays)] 
    if f2_befaft is None:
        f2_befaft = ['bef' if not i%2 else 'aft' for i in range(f2_num_arrays)] 
    if f2_corr_letters is None:
        f2_corr_letters = [0 for i in range(f2_corr_num_arrays)]
    if f2_corr_y_variables is None:
        f2_corr_y_variables = ['correlations0004' for i in range(f2_corr_num_arrays)] 
    if f2_corr_i is None:
        f2_corr_i = [ 22 for i in range(f2_corr_num_arrays)]
    if f2_corr_j is None:
        f2_corr_j = [ 16 for i in range(f2_corr_num_arrays)]
    if f2_corr_befaft is None:
        f2_corr_befaft = ['bef' for i in range(f2_corr_num_arrays)] # bef\aft
    if f2_corr_ref_cells is None:
        f2_corr_ref_cells = [[22,16,1] for i in range(f2_corr_num_arrays)]

    f2_in={'f2_x_variable' : f2_x_variable, 
           'f2_num_arrays' : f2_num_arrays, 
           'f2_av_letters' : f2_av_letters, 
           'f2_y_variables' : f2_y_variables,
           'f2_i_want' : f2_i,      
           'f2_j_want' : f2_j,      
           'f2_befaft' : f2_befaft, 
           'f2_array_marker_size' : f2_array_marker_size, 
           'f2_color_arr' : f2_color_arr,
           'f2_corr_num_arrays' : f2_corr_num_arrays, 
           'f2_corr_letters' : f2_corr_letters, 
           'f2_corr_colored' :f2_corr_colored,  
           'f2_corr_y_variables' : f2_corr_y_variables, 
           'f2_corr_i_want' : f2_corr_i,     
           'f2_corr_j_want' : f2_corr_j,     
           'f2_corr_befaft' : f2_corr_befaft,
           'f2_corr_ref_cells' : f2_corr_ref_cells, 
           'f2_corr_ref_var' : f2_corr_ref_var,     
           'f2_num_show_mons' : f2_mons_num_mons, 
           'f2_num_variables_mon' : f2_mons_num_variables, 
           'f2_show_mons' :f2_mons_mons_inds, 
           'f2_y_variables_mon' : f2_mons_y_variables, 
           'f2_num_show_assimstp' : f2_assimstp_num_show, 
           'f2_assimstp_letters' : f2_assimstp_letters, 
           'f2_show_assimstp' : f2_assimstp_show,
           'f2_mon_num_assimstp' :f2_assimstp_mon_nums, 
           'f2_assimstp_var' : f2_assimstp_var,                 
           'f2_assimstp_marker_size' : f2_assimstp_marker_size, 
           'f2_assimstp_show_line' : f2_assimstp_show_line,
           'figure_size_x':figure_size_x,
           'figure_size_y':figure_size_y, 
           'f2_ax_pos' :f2_ax_pos, 
           'f2_ax_x_label' : f2_ax_x_label,
           'f2_ax_1_y_label' : f2_ax_y_label,
           'f2_ax_legend_cols' : f2_ax_legend_cols,
           'f2_ax_legend_or' : f2_ax_legend_or,
           'f2_ax_legend_bbox' : f2_ax_legend_bbox, 
           'f2_ax_corr_legend_cols' : f2_ax_legend_corr_cols,
           'f2_ax_corr_legend_or' : f2_ax_legend_corr_or,
           'f2_ax_corr_legend_bbox' : f2_ax_legend_corr_bbox, 
           'f2_ax_kz_legend_cols' : f2_ax_legend_kz_cols,
           'f2_ax_kz_legend_or' : f2_ax_legend_kz_or,
           'f2_ax_kz_legend_bbox' : f2_ax_legend_kz_bbox,
           'f2_ax_kz_res_legend_cols' : f2_ax_legend_kz_res_cols,
           'f2_ax_kz_res_legend_or' : f2_ax_legend_kz_res_or,
           'f2_ax_kz_res_legend_bbox' : f2_ax_legend_kz_res_bbox,
           'f2_ax_kz_std_legend_cols' : f2_ax_legend_kz_std_cols,
           'f2_ax_kz_std_legend_or' : f2_ax_legend_kz_std_or,
           'f2_ax_kz_std_legend_bbox' : f2_ax_legend_kz_std_bbox,
           'f2_ax_conc_res_legend_cols' : f2_ax_legend_conc_res_cols,
           'f2_ax_conc_res_legend_or' : f2_ax_legend_conc_res_or,
           'f2_ax_conc_res_legend_bbox' : f2_ax_legend_conc_res_bbox, 
           'f2_ax_conc_std_legend_cols' : f2_ax_legend_conc_std_cols,
           'f2_ax_conc_std_legend_or' : f2_ax_legend_conc_std_or,
           'f2_ax_conc_std_legend_bbox' : f2_ax_legend_conc_std_bbox, 
           'f2_is_enforce_axis_input' : f2_is_enforce_axis_input, 
           'f2_plot_x_min' : f2_ax_x_min,
           'f2_plot_x_max' : f2_ax_x_max,
           'f2_plot_y_min' : f2_ax_y_min,
           'f2_plot_y_max' : f2_ax_y_max,
           'f2_ax_corr_y_min' : f2_ax_corr_y_min,
           'f2_ax_corr_y_max' : f2_ax_corr_y_max, 
           'f2_ax_kz_y_min' : f2_ax_kz_y_min,
           'f2_ax_kz_y_max' : f2_ax_kz_y_max,  
           'f2_ax_kz_res_y_min' : f2_ax_kz_res_y_min,
           'f2_ax_kz_res_y_max' : f2_ax_kz_res_y_max, 
           'f2_ax_kz_std_y_min' : f2_ax_kz_std_y_min,
           'f2_ax_kz_std_y_max' : f2_ax_kz_std_y_max,  
           'f2_ax_conc_res_y_min' : f2_ax_conc_res_y_min,
           'f2_ax_conc_res_y_max' : f2_ax_conc_res_y_max,
           'f2_ax_conc_std_y_min' : f2_ax_conc_std_y_min,
           'f2_ax_conc_std_y_max' : f2_ax_conc_std_y_max, 
           'f2_ax_offset_corr' : f2_ax_offset_corr,
           'f2_ax_offset_kz' : f2_ax_offset_kz,
           'f2_ax_offset_kz_res' : f2_ax_offset_kz_res,
           'f2_ax_offset_kz_std' : f2_ax_offset_kz_std,
           'f2_ax_offset_conc_std' : f2_ax_offset_conc_std,
           'f2_ax_offset_conc_res' : f2_ax_offset_conc_res,
           'f2_ax_corr_show_line' : f2_ax_corr_show_line,
           'f2_ax_corr_show_marker' : f2_ax_corr_show_marker,
           'f2_is_show_arrows' : f2_is_show_arrows,
           'f2_fig_title' : f2_fig_title,
           'f2_fig_title_font' : f2_fig_title_font,
           'f2_axis_title' : f2_axis_title,
           } 

    f3_in={'f3_source_file_name' : f3_source_file_name,
           'f3_x_variable' :f3_x_variable,
           'f3_y_variable_mean' : f3_y_variable_mean,
           'f3_num_arrays' : f3_num_arrays,
           'f3_i_want' : f3_i_want,
           'f3_j_want' : f3_j_want,
           'f3_befaft' : f3_befaft,
           'figure_size_x':figure_size_x,
           'figure_size_y':figure_size_y,
           'f3_ax_pos' : f3_ax_pos, 
           'f3_ax_x_label' : f3_ax_x_label,
           'f3_ax_y_label' : f3_ax_y_label,
           'f3_ax_legend_labels' : f3_ax_legend_labels,
           'f3_ax_legend_cols' : f3_ax_legend_cols,
           'f3_ax_legend_bbox' : f3_ax_legend_bbox,
           'f3_markersize' : f3_markersize,   
           'f3_is_enforce_axis_input' : f3_is_enforce_axis_input,
           'f3_plot_x_min' : f3_plot_x_min,
           'f3_plot_x_max' : f3_plot_x_max,
           'f3_plot_y_min' : f3_plot_y_min,
           'f3_plot_y_max' : f3_plot_y_max,
           }
    f3_in['f3_ax_legend_labels'] = [str(f3_in['f3_i_want'][i]).zfill(2)+','+str(f3_in['f3_j_want'][i]).zfill(2) + ' ' + f3_in['f3_befaft'][i] for i in range(f3_in['f3_num_arrays'])]

    if t_source_file_name is None:
        t_source_file_name = model_name_big + '_TRUE_E0_1.vtk'
    
    t_in={'t_source_file_name' : t_source_file_name,
          't_variable_name' : t_variable_name,
          'figure_size_x':figure_size_x,
          'figure_size_y':figure_size_y,
          't_ax_pos' : t_ax_pos,
          't_ax_title' : t_ax_title,
          't_ax_xlabel' : t_ax_xlabel,
          't_ax_ylabel' : t_ax_ylabel,
          't_ax_cbar_pos' : t_ax_cbar_pos,
          't_ax_num_cbar' : t_ax_num_cbar,
          't_ax_low_cbar' : t_ax_low_cbar,
          't_ax_high_cbar' : t_ax_high_cbar,
          't_is_show_mons' : t_is_show_mons,   
          't_mons_size' : t_mons_size,
          't_is_scatter_inds' : t_is_scatter_inds, 
          't_scatter_inds_x' : t_scatter_inds_x,
          't_scatter_inds_y' : t_scatter_inds_y,
          } 

    h_in={'h_file_type':h_file_type,
          'h_sc_cell_vars':h_sc_cell_vars,
          'h_befaft':h_befaft,
          'h_obstimes':h_obstimes,
          'h_variable_name': h_variable_name,
          'h_ax_title': h_ax_title,
          'h_ax_pos': h_ax_pos,
          'h_ax_xlabel':h_ax_xlabel,
          'h_ax_ylabel':h_ax_ylabel,
          'h_width_factors':h_width_factors,
          'h_num_bins':h_num_bins,
          'h_hist_color':h_hist_color,
          'h_hist_normed':h_hist_normed,
          'h_hist_type':h_hist_type,
          'h_cmap':h_cmap,
          'h_cmap_kz':h_cmap_kz,
          'h_cmap_conc':h_cmap_conc,
          'h_n_cols':h_n_cols,
          'h_n_rows':h_n_rows,
          'h_im_up':h_im_up,
          'h_im_left':h_im_left,
          'h_grid_factor':h_grid_factor,
          }
    s_in={'s_source_file_names': s_source_file_names,
          's_variable_names': s_variable_names,
          's_num_input_data':s_num_input_data,
          's_ax_title': s_ax_title,
          's_ax_pos': s_ax_pos,
          's_ax_xlabel':s_ax_xlabel,
          's_ax_ylabel':s_ax_ylabel,
          's_width_factors':s_width_factors,
          's_num_bins':s_num_bins,
          's_is_text':s_is_text,
          's_colors':s_colors,
          's_linewidths':s_linewidths,
          's_size':s_size,
          's_y_ticks':s_y_ticks,
          's_y_ticklabels':s_y_ticklabels,
          's_x_ticks':s_x_ticks,
          's_x_ticklabels':s_x_ticklabels,
          }
    ######################################################################################
    ######################################################################################
    def all_plot( num = 0, is_m = 0, is_f = 0, is_f2= 0, is_f3 = 0, is_t = 0, is_h = 0, is_s = 0, is_show_local = 0):
        if is_m or num == 1:
            # Gather Input
            in_dict = dict(m_in.items() + gen_in.items() + dir_in.items() + fun_in.items())
            # in_dict['fig_m'] = fig
            # Plot figure
            fig = myplots.m_plot(**in_dict)
            # Save figure
            m_pic_name_arr = [m_pic_name + '_' + letter + m_pic_ending]
            if is_save:
                myplots.saving_fig(pics_dir,m_pic_name_arr,[fig])

        if is_f or num == 2:
            in_dict = dict(f_in.items() + gen_in.items() + dir_in.items() + fun_in.items())
            # in_dict['fig_f'] = fig
            fig = myplots.f_plot(**in_dict)
            f_pic_name_arr = [f_pic_name + '_' + letter + f_pic_ending]
            if is_save:
                myplots.saving_fig(pics_dir,f_pic_name_arr,[fig])

        if is_f2 or num == 3:
            in_dict = dict(f2_in.items() + gen_in.items() + dir_in.items() + fun_in.items())
            # in_dict['fig_f2'] = fig
            fig = myplots.f2_plot(**in_dict)
            f2_pic_name_arr = [f2_pic_name + '_' + letter + f2_pic_ending]
            if is_save:
                myplots.saving_fig(pics_dir,f2_pic_name_arr,[fig])

        if is_f3 or num == 4:
            in_dict = dict(f3_in.items() + gen_in.items() + dir_in.items() + fun_in.items())
            # in_dict['fig_f3'] = fig
            fig = myplots.f3_plot(**in_dict)
            f3_pic_name_arr = [f3_pic_name + '_' + letter + f3_pic_ending]
            if is_save:
                myplots.saving_fig(pics_dir,f3_pic_name_arr,[fig])

        if is_t or num == 5:
            in_dict = dict(t_in.items() + gen_in.items() + dir_in.items() + fun_in.items())
            if is_m or is_f or is_f2 or is_f3:
                in_dict['fig_t'] = fig
            fig = myplots.t_plot(**in_dict)
            t_pic_name_arr = [t_pic_name + '_' + letter + t_pic_ending]
            if is_save:
                myplots.saving_fig(pics_dir,t_pic_name_arr,[fig])

        if is_h or num == 6:
            in_dict = dict(h_in.items() + gen_in.items() + dir_in.items() + fun_in.items())
            if is_m or is_f or is_f2 or is_f3:
                in_dict['fig_h'] = fig
            fig = myplots.h_plot(**in_dict)
            h_pic_name_arr = [h_pic_name + '_' + letter + h_pic_ending]
            if is_save:
                myplots.saving_fig(pics_dir,h_pic_name_arr,[fig])

        if is_s or num == 7:
            in_dict = dict(s_in.items() + gen_in.items() + dir_in.items() + fun_in.items())
            if is_m or is_f or is_f2 or is_f3:
                in_dict['fig_s'] = fig
            fig = myplots.s_plot(**in_dict)
            s_pic_name_arr = [s_pic_name + '_' + letter + s_pic_ending]
            if is_save:
                myplots.saving_fig(pics_dir,s_pic_name_arr,[fig])

        #Showing the figure with matplotlib
        if is_show or is_show_local:
            plt.show()
            

        os.chdir(python_dir)

    ############################################################################################
    all_plot(is_m = is_m, is_f = is_f, is_f2 = is_f2, is_f3 = is_f3, is_t = is_t, is_h = is_h, is_s = is_s)
    ############################################################################################

    print('\nDone with plot.py')
    print(time.asctime( time.localtime( time.time())))
