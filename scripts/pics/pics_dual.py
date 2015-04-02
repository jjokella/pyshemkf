# coding: utf-8
pt(save_png_fname = 'pt.png')
import numpy as np
p(is_m = 1, m_first = 9, m_diff = 3, m_pic_name = 'p_m_1.png')
p(is_m = 1, m_first = 1, m_diff = 1, m_pic_name = 'p_m_3.png', m_infiles = ['init'],m_varnames = ['kz'], m_cbar_titles = ['kz'], m_cmaps = ['jet'])
p(is_m = 1, m_first = 1, m_diff = 1, m_pic_name = 'p_m_4.png', m_infiles = ['end'],m_varnames = ['kz'], m_cbar_titles = ['kz'], m_cmaps = ['jet'])
p(is_f = 1,f_pic_name = 'p_f.png')
p(is_f2 = 1,f2_pic_name = 'p_f2_1.png', f2_num_arrays = 4, f2_ax_offset_kz = 0.0,f2_mons_num_mons = 2, f2_ax_kz_y_min =-11.0,f2_ax_pos = [0.1,0.1,0.8,0.8], f2_axis_title = 'Permeabilites at the observation points', f2_ax_x_label = 'Observation time in days')
p(is_f2 = 1,f2_pic_name = 'p_f2_2.png', f2_corr_num_arrays = 8,f2_axis_title = 'Correlations', f2_ax_x_label = 'Observation time in days', f2_ax_offset_corr = 0.0,f2_corr_i = [5,16,27,10,33,5,16,27], f2_corr_j = [5,5,5,16,16,27,27,27])
p(is_f2 = 1,f2_pic_name = 'p_f2_3.png', f2_corr_num_arrays = 8,f2_axis_title = 'Correlations', f2_ax_x_label = 'Observation time in days', f2_ax_offset_corr = 0.0,f2_corr_i = [5,16,27,10,33,5,16,27], f2_corr_j = [5,5,5,16,16,27,27,27],f2_corr_ref_cells = [[10,16,1],[10,16,1],[10,16,1],[10,16,1],[10,16,1],[10,16,1],[10,16,1],[10,16,1]])
p(is_f2 = 1,f2_pic_name = 'p_f2_4.png', f2_assimstp_num_show = 3, f2_axis_title = 'Update step', f2_ax_x_label = 'Observation time in days',f2_ax_pos = [0.1,0.1,0.8,0.8], f2_mons_num_mons = 1, f2_mons_y_variables = ['conc_mean'], f2_ax_legend_bbox = [1.0,0.0], f2_ax_legend_or = 'lower right')
p(is_f2 = 1,f2_pic_name = 'p_f2_5.png', f2_assimstp_num_show = 3, f2_axis_title = 'Update step', f2_ax_x_label = 'Observation time in days',f2_ax_pos = [0.1,0.1,0.8,0.8], f2_mons_num_mons = 1, f2_mons_y_variables = ['conc_mean'], f2_ax_legend_bbox = [1.0,0.0], f2_ax_legend_or = 'lower right',f2_mons_mons_inds = [1], f2_assimstp_mon_nums = [1,1,1])
p(is_h = 1, h_file_type = 'av', h_cmap = 'jet', h_cmap_kz = [-11,-9], h_hist_normed = False, h_width_factors = [5,6], h_num_bins = 50, h_obstimes = range(9,50,3), h_pic_name = 'p_h_av.png')
