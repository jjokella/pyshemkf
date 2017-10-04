#!/usr/bin/python

# Plot routine for numcomp pics

import matplotlib as mpl
from matplotlib import cm            # Colormap commands (cm.get_cmap())
from matplotlib import colors
from matplotlib import pyplot as plt # ?
from matplotlib import mlab

import numpy as np
import exceptions               # ?

from mypackage.run import pythonmodule as pm
from mypackage.plot import plotarrays as pa
from mypackage.plot import mycolors
from mypackage.plot import grids
from mypackage.plot import specs as sc

import arrays as na

def plot(ax,
         which_methods,
         which_methods_left,
         which_methods_right,
         which_res = 'endres',
         model = 'wavebc',
         n_runs = 1000,
         method = 'ttest',
         enssize = 50,
         n_syn = 1,                       #number of synthetic studies
         n_syn_bold = 1,
         n_comparisons = 10000,
         pic_format = 'pdf',
         bar_colors = ['black','white','grey'],
):

    # Check
    for imethod in which_methods_left:
        if not imethod in which_methods:
            raise exceptions.RuntimeError('Wrong methods in wrong_methods_left')
    for imethod in which_methods_left:
        if not imethod in which_methods:
            raise exceptions.RuntimeError('Wrong methods in wrong_methods_right')

    # Both methods in one array
    show_methods = [which_methods_left,
                        which_methods_right]
    # Number of bars and patches
    num_bars = len(show_methods[0])
    num_patches = 3*num_bars

    # Ticklabels (names)
    ytick1 = [pa.longnames_methods[show_methods[0][i]] for i in range(num_bars)]
    ytick2 = [pa.longnames_methods[show_methods[1][i]] for i in range(num_bars)]
    
    # Load probabilities
    probs = np.load(pm.py_output_filename(na.tag,'probs_'+which_res,model+'_'+str(n_runs)+'_'+method+'_'+str(enssize)+'_'+str(n_syn)+'_'+'_'.join([str(i) for i in which_methods]),'npy'))

    # Load probabilities for bold labels
    probs_bold = np.load(pm.py_output_filename(na.tag,'probs_'+which_res,model+'_'+str(n_runs)+'_'+method+'_'+str(enssize)+'_'+str(n_syn_bold)+'_'+'_'.join([str(i) for i in which_methods]),'npy'))

    ax.set_position([0.3,0.05,0.4,0.75])
    ax.set_frame_on(False)

    # Patch arrays for plt.barh()
    in_bottom = np.zeros(num_patches)
    in_height = np.zeros(num_patches)
    in_width = np.zeros(num_patches)
    in_left = np.zeros(num_patches)
    in_color = ['' for i in range(num_patches)]
    for i in range(num_patches):
        in_bottom[i] = num_bars-i/3
        in_height[i] = 0.8
        in_width[i] = probs[show_methods[0][i/3],
                            show_methods[1][i/3]][np.mod(i,3)]
        in_left[i] = np.sum(probs[show_methods[0][i/3],
                                  show_methods[1][i/3]][0:np.mod(i,3)])
        in_color[i] = bar_colors[np.mod(i,3)]

    # Plot patches in bars
    ax.barh(bottom = in_bottom,
            height = in_height,
            width = in_width,
            left = in_left,
            color = in_color,
            edgecolor = 'k')

    # H_0 labels inside bar
    if method == "ttest":
        for i in range(1,num_bars+1):
            if in_left[3*i-1]-in_left[3*i-2] > 0.15:
                ax.text(in_left[3*i-2]   +0.4*(in_left[3*i-1]-in_left[3*i-2]),
                        in_bottom[3*i-2] +0.3,
                        "$H_0$",
                        fontsize = 20)

    # Axis 1
    ax.tick_params(direction = 'out', length = 0,
                   width = 1, labelsize = 20,
                   top = 'off', bottom = 'off',
                   labelright = 'off',
                   pad = 8)
    ax.set_xlim([-0.01,1.01])
    ax.set_ylim([0.9,num_bars+0.8])
    ax.set_xticks([])
    ax.set_yticks([num_bars-i +0.4 for i in range(num_bars)])
    ax.set_yticklabels(ytick1)

    # Twin Axis 2
    ax2 = ax.twinx()
    ax2.set_position([0.3,0.05,0.4,0.75])
    ax2.set_frame_on(False)
    ax2.tick_params(direction = 'out', length = 0,
                   width = 1, labelsize = 20,
                   top = 'off', bottom = 'off',
                   labelleft = 'off',labelright = 'on',
                   labelcolor = 'black',
                   pad = 8)
    ax2.set_xlim([-0.01,1.01])
    ax2.set_ylim([0.9,num_bars+0.8])
    ax2.set_xticks([])
    ax2.set_yticks([num_bars-i +0.4 for i in range(num_bars)])
    ax2.set_yticklabels(ytick2)

    # Boldness of axislabels
    for i in range(num_bars):
        if(probs_bold[show_methods[0][i],show_methods[1][i]][0] == 1):
            ax.yaxis.get_majorticklabels()[i].set_weight('bold')
        elif(probs_bold[show_methods[0][i],show_methods[1][i]][2] == 1):
            ax2.yaxis.get_majorticklabels()[i].set_weight('bold')
        else:
            ax.yaxis.get_majorticklabels()[i].set_style('italic')
            ax2.yaxis.get_majorticklabels()[i].set_style('italic')

    # Saving location
    pic_name = pm.py_output_filename(na.tag,'probs_'+which_res,model+'_'+str(n_runs)+'_'+method+'_'+str(enssize)+'_'+str(n_syn)+'_'+'_'.join([str(i) for i in which_methods]),pic_format)
    
    return ax, pic_name
