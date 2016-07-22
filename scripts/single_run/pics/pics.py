# coding: utf-8
pt(save_png_fname='pt.png')
import numpy as np
# psc(file_type=['sc','sc'],sc_cell_vars=[[22,16,1],[22,16,1]],befaft=['bef','bef'],obstimes=[range(9,50,3),range(9,50,3)],num_figs=5,save_pics_name='psc_sc.png', width_factors=[1.0,1.7,1.0,2.5],num_input_data=500, num_bins=100,scatter_x_ticks=np.arange(-15,15,0.5),scatter_normed_y_ticks=np.arange(-10,10,1.0),scatter_size=[5])
# psc(file_type=['av','av'],befaft=['bef','bef'],obstimes=[range(9,50,3),range(9,50,3)],num_figs=5,save_pics_name='psc_av.png', width_factors=[2.8,8.0,1.0,2.0],num_input_data=961, num_bins=100,scatter_x_ticks=np.arange(-15,15,0.5),scatter_normed_y_ticks=np.arange(-10,10,1.0),scatter_size=[5], variable_names=[4,3],scatter_colors=[[(i/31)/40.0,(i/31)/40.0,(i/31)/40.0] for i in range(31*31)])
# psc(file_type=['av','av'],befaft=['bef','bef'],obstimes=[range(9,50,3),range(9,50,3)],num_figs=5,save_pics_name='psc_av_lines.png', width_factors=[2.8,8.0,1.0,2.0],num_input_data=961, num_bins=100,scatter_x_ticks=np.arange(-15,15,0.5),scatter_normed_y_ticks=np.arange(-10,10,1.0),scatter_size=[30], variable_names=[4,3],scatter_colors=[[(i/31)/40.0,(i/31)/40.0,(i/31)/40.0] if i/31 in [0,5,10,15,20] else [1,1,1] for i in range(31*31)])
#
#---------------------------------------------------------------------------------------
# 
p(is_m=1, m_first=4, m_diff=3, m_pic_name='p_m_1_1.png', m_cbar_kz_res_low=-1.0, m_cmaps=['jet','Greys','RdBu'])
p(is_m=1, m_first=24, m_diff=3, m_pic_name='p_m_1_2.png', m_cbar_kz_res_low=-1.0, m_cmaps=['jet','Greys','RdBu'])
p(is_m=1, m_first=44, m_diff=3, m_pic_name='p_m_1_3.png', m_cbar_kz_res_low=-1.0, m_cmaps=['jet','Greys','RdBu'])
p(is_m=1, m_first=64, m_diff=3, m_pic_name='p_m_1_4.png', m_cbar_kz_res_low=-1.0, m_cmaps=['jet','Greys','RdBu'])
p(is_m=1, m_first=84, m_diff=3, m_pic_name='p_m_1_5.png', m_cbar_kz_res_low=-1.0, m_cmaps=['jet','Greys','RdBu'])
#
# 
p(is_m=1, m_first=4, m_diff=3, m_pic_name='p_m_2_1.png', m_infiles=['av','cor','cor'],m_varnames=['kz_mean','correlations0004','correlations0004'], m_cor_cell_var=[[10,16,1,3],[10,16,1,3],[22,16,1,3]],m_befaft=['aft','bef','bef'], m_cbar_titles=['Mean','Cor10','Cor22'],m_cmaps=['jet','RdBu','RdBu'],m_cbar_cor_low =-0.4, m_cbar_cor_high=0.4)
p(is_m=1, m_first=24, m_diff=3, m_pic_name='p_m_2_2.png', m_infiles=['av','cor','cor'],m_varnames=['kz_mean','correlations0004','correlations0004'], m_cor_cell_var=[[10,16,1,3],[10,16,1,3],[22,16,1,3]],m_befaft=['aft','bef','bef'], m_cbar_titles=['Mean','Cor10','Cor22'],m_cmaps=['jet','RdBu','RdBu'],m_cbar_cor_low =-0.4, m_cbar_cor_high=0.4)
p(is_m=1, m_first=44, m_diff=3, m_pic_name='p_m_2_3.png', m_infiles=['av','cor','cor'],m_varnames=['kz_mean','correlations0004','correlations0004'], m_cor_cell_var=[[10,16,1,3],[10,16,1,3],[22,16,1,3]],m_befaft=['aft','bef','bef'], m_cbar_titles=['Mean','Cor10','Cor22'],m_cmaps=['jet','RdBu','RdBu'],m_cbar_cor_low =-0.4, m_cbar_cor_high=0.4)
p(is_m=1, m_first=64, m_diff=3, m_pic_name='p_m_2_4.png', m_infiles=['av','cor','cor'],m_varnames=['kz_mean','correlations0004','correlations0004'], m_cor_cell_var=[[10,16,1,3],[10,16,1,3],[22,16,1,3]],m_befaft=['aft','bef','bef'], m_cbar_titles=['Mean','Cor10','Cor22'],m_cmaps=['jet','RdBu','RdBu'],m_cbar_cor_low =-0.4, m_cbar_cor_high=0.4)
p(is_m=1, m_first=84, m_diff=3, m_pic_name='p_m_2_5.png', m_infiles=['av','cor','cor'],m_varnames=['kz_mean','correlations0004','correlations0004'], m_cor_cell_var=[[10,16,1,3],[10,16,1,3],[22,16,1,3]],m_befaft=['aft','bef','bef'], m_cbar_titles=['Mean','Cor10','Cor22'],m_cmaps=['jet','RdBu','RdBu'],m_cbar_cor_low =-0.4, m_cbar_cor_high=0.4)
#
# 
p(is_m=1, m_first=1, m_diff=1, m_pic_name='p_m_3.png', m_infiles=['init'],m_varnames=['kz'], m_cbar_titles=['kz'], m_cmaps=['jet'])
p(is_m=1, m_first=1, m_diff=1, m_pic_name='p_m_4.png', m_infiles=['end'],m_varnames=['kz'], m_cbar_titles=['kz'], m_cmaps=['jet'])
#
# 
p(is_f=1,f_pic_name='p_f.png')
#
# ---------------------------------------------------------------------------------
# 
p(is_f2=1,f2_pic_name='p_f2_1.png', f2_num_arrays=4, f2_ax_offset_kz=0.0,f2_mons_num_mons=2, f2_ax_kz_y_min =-11.0,f2_ax_pos=[0.1,0.1,0.8,0.8], f2_axis_title='Permeabilites at the observation points', f2_ax_x_label='Observation time in days')
p(is_f2=1,f2_pic_name='p_f2_2.png', f2_corr_num_arrays=8,f2_axis_title='Correlations', f2_ax_x_label='Observation time in days', f2_ax_offset_corr=0.0,f2_corr_i=[5,16,27,10,33,5,16,27], f2_corr_j=[5,5,5,16,16,27,27,27])
p(is_f2=1,f2_pic_name='p_f2_3.png', f2_corr_num_arrays=8,f2_axis_title='Correlations', f2_ax_x_label='Observation time in days', f2_ax_offset_corr=0.0,f2_corr_i=[5,16,27,10,33,5,16,27], f2_corr_j=[5,5,5,16,16,27,27,27],f2_corr_ref_cells=[[10,16,1],[10,16,1],[10,16,1],[10,16,1],[10,16,1],[10,16,1],[10,16,1],[10,16,1]])
p(is_f2=1,f2_pic_name='p_f2_4.png', f2_assimstp_num_show=3, f2_axis_title='Update step', f2_ax_x_label='Observation time in days',f2_ax_pos=[0.1,0.1,0.8,0.8], f2_mons_num_mons=1, f2_mons_y_variables=['conc_mean'], f2_ax_legend_bbox=[1.0,0.0], f2_ax_legend_or='lower right')
p(is_f2=1,f2_pic_name='p_f2_5.png', f2_assimstp_num_show=3, f2_axis_title='Update step', f2_ax_x_label='Observation time in days',f2_ax_pos=[0.1,0.1,0.8,0.8], f2_mons_num_mons=1, f2_mons_y_variables=['conc_mean'], f2_ax_legend_bbox=[1.0,0.0], f2_ax_legend_or='lower right',f2_mons_mons_inds=[1], f2_assimstp_mon_nums=[1,1,1])
#
#\---------------------------------------------------------------------------------------------
# 
p(is_h=1, h_file_type='av', h_cmap='jet', h_cmap_kz=[-11,-9], h_hist_normed=False, h_width_factors=[7,30], h_num_bins=50, h_obstimes=range(9,50,3), h_pic_name='p_h_av.png')
p(is_h=1, h_file_type='sc', h_cmap='jet', h_cmap_kz=[-11,-9], h_sc_cell_vars=[22,16,1,4], h_hist_normed=False, h_obstimes=range(9,50,3), h_width_factors=[1.2,1.2], h_num_bins=50, h_pic_name='p_h_sc_1.png')
p(is_h=1, h_file_type='sc', h_cmap='jet', h_cmap_kz=[-11,-9], h_sc_cell_vars=[10,16,1,4], h_hist_normed=False, h_obstimes=range(9,50,3), h_width_factors=[1.2,1.2], h_num_bins=50, h_pic_name='p_h_sc_2.png')