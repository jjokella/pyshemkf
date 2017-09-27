#!/usr/bin/python

# Plot routine for forward pics

import matplotlib as mpl
from matplotlib import cm            # Colormap commands (cm.get_cmap())
from matplotlib import colors
from matplotlib import pyplot as plt # ?
import numpy as np
import exceptions               # ?

from mypackage.run import pythonmodule as pm
from mypackage.plot import plotarrays as pa
from mypackage.plot import mycolors
from mypackage.plot import grids
from mypackage.plot import specs as sc

import arrays as ea



def plot(ax,
         which_methods = [0,1,2,3,4,5,6],
         which_res = 'endres',
         stat_method = 'mean',
         is_1000 = True,                         # 1000er or 100er job
         is_wavebc = True,
         is_std = 0,                         # Show std?
         std_method = 'std',
         pic_format = 'pdf',      #'png' or 'eps' or 'svg' or 'pdf'
         figpos = [0.15,0.3,0.8,0.6],               #xbeg, ybeg, xrange, yrange
         ylims = [0.28,0.82],
         yticks = [0.3,0.4,0.5,0.6,0.7,0.8],
         num_pack = 4,                     # Number of methods in pack
         formatsos = ['o','v','s','p','o','v','s','p'],
         coleros = [(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),
                        (1.0,1.0,1.0),(1.0,1.0,1.0),(1.0,1.0,1.0),(1.0,1.0,1.0)],
         markersize = 10,
         markeredgesize = 1.5,
         fontleg = 30,                              #18
         fonttit = 40,
         fontlab = 40,
         fonttic = 30,
             ):
    """
    A plotting function for statistics of residual distributions.

    Parameters
    ----------
    ax : Axes
        The axes to draw to.

    which_methods : array of ints
        The methods to be printed, in this order.

    which_res : string
        'endres' - use residuals after EnKF run
        'begres' - use residuals before EnKF run

    stat_method : string
        'mean' - Means
        'std' - Standard deviation
        'stdm' - Standard deviation of the mean
        'median' - Median or 50 Percentile
        'q25' - 25 Percentile
        'q75' - 75 Percentile

    is_1000 : boolean
        True - Jobs/Ensemble Sizes for which 1000 runs exist
               typically, 50, 70, 100, 250
        False - Jobs/Ensemble Sizezs for which 100 runs exist
               typically, 500, 1000, 2000

    is_wavebc : boolean
        True - Model wavebc
        False - Model wave

    is_std : boolean
        True - Show errorbars of standard deviation
        False - No errorbars

    std_method : string
        Standard deviation to use
        'std' - Standard deviation
        'stdm' - Standard deviation of mean

    pic_format : string
        Format of the picture
        'pdf' - pdf-format
        'eps' - eps-format
        'png' - png-format
        'jpg' - jpg-format
        'svg' - svg-format

    figpos : array of floats
        Four numbers
        xbeg, ybeg, xrange, yrange

    More input specifying plot parameters.

    Returns
    -------
    ax : Axes
        Axes containing plot.

    pic_name : string
        Containing proposed saving location for Figure.
    """

    # Ensemble sizes (could be read in from array maybe)
    which_enssize =  ([50,70,100,250] if is_1000 else
                          ([500,1000,2000] if is_wavebc else [50,70,100,250,500,1000,2000]))

    num_methods = np.array(which_methods).size

    # Legend
    legend_input = pa.longnames_methods
    legend_input = np.array([legend_input[i].ljust(18) for i in range(len(legend_input))])
    legend_input = legend_input[which_methods]

    # Load array
    str_1000 = '1000' if is_1000 else ''
    str_wavebc = 'wavebc' if is_wavebc else ''
    var = np.load(pm.py_output_filename('errorplot',which_res,stat_method+str_1000+'_'+str_wavebc+'_'+'_'.join([str(i) for i in which_methods]),'npy'))

    # Standard deviation
    if is_std:
        std = np.load(pm.py_output_filename('errorplot',which_res,std_method+str_1000+'_'+str_wavebc+'_'+'_'.join([str(i) for i in which_methods]),'npy'))


    ax.set_prop_cycle("color",['k'])
    ax.set_position(figpos)

    for ienssize,ensemble_size in enumerate(which_enssize):
        # x positions, up to 15 methods
        x = np.delete(np.arange(0,16),
                    np.arange(0,16,num_pack+1)) #Skip every (num_pack+1)-th

        varplot = var[:,ienssize]
        stdplot = std[:,ienssize]

        # Plot
        puntos = []                            #Contains plotted points
        ax.plot(x[:len(varplot)],varplot,'k-',label=3)
        for iplot in range(num_methods):
            punto, = ax.plot(x[iplot],varplot[iplot], formatsos[iplot], lw = 2, ms = markersize,
                             label = legend_input[iplot],
                             c = coleros[iplot],mew =markeredgesize)
            puntos.append(punto)
            # Text
            if iplot == range(num_methods)[-1]:
                ax.text(x[iplot]+0.5,
                             varplot[iplot]-0.005 if ensemble_size == 2000 else varplot[iplot],
                             r'$n_{e}$ = '+str(ensemble_size),
                             verticalalignment='center',
                             horizontalalignment='left',
                             size = 20)
            # Error
            if is_std:
                ax.errorbar(x[iplot],varplot[iplot],yerr = stdplot[iplot],
                            fmt = formatsos[iplot], lw = 2, ms = markersize, label = 'this',
                                mfc = coleros[iplot],
                                mew = markeredgesize,
                                mec = 'black')

        # Legend
        num_inleg = num_pack
        num_legs = num_methods/num_inleg + int(bool(np.mod(num_methods,num_inleg)))
        num_inlastleg = np.mod(num_methods,num_inleg) if np.mod(num_methods,num_inleg) else num_inleg
        leginds = [num_inleg-1+i*num_inleg if i<num_legs-1 else num_inleg-1+(i-1)*num_inleg+num_inlastleg
                   for i in range(num_legs)] #last indices of a group of indices
        legranges = [num_inleg if i<num_legs-1 else num_inlastleg
                     for i in range(num_legs)]

        for ileg in range(len(leginds)):
            xleg = 0.15 + ileg*0.8/num_legs
            first_legend = ax.legend(handles = [puntos[i] for i in range(leginds[ileg]-legranges[ileg]+1,
                                                                         leginds[ileg]+1)],
                                      bbox_to_anchor = [xleg,
                                                        0.00,
                                                        0.8/num_legs,
                                                        0.3],
                                      bbox_transform=plt.gcf().transFigure,
                                      # loc = [0.0,1.0],
                                      mode = 'expand',
                                      # labelspacing = 1.0,
                                      ncol =1, numpoints = 1,
                                      fontsize = fontleg,
                                      framealpha = 1.0, markerscale = 1.0)
            ax.add_artist(first_legend)


        # Lines
        for xline in range(0,16,num_pack+1):
            ax.vlines(xline,0.0,1.0, linestyles = 'dotted')

        for yline in yticks:
            ax.hlines(yline,0,20,linestyles = 'dotted')

        ax.hlines(0.62,0,20,linestyles = 'dashed')


    # Style
    ax.set_xlim([0,num_legs*(num_pack+1)])
    ax.set_ylabel(r'RMSE [$\log(\frac{1}{m^2})$]',fontsize = fontlab, labelpad = 10)
    ax.tick_params(direction = 'in', length = 6,
                   width = 1, labelsize = fonttic,
                   top = 'off', right = 'off', bottom = 'off',
                   pad = 8)
    ax.set_xticks([])
    ax.set_yticks(yticks)
    ax.get_xaxis().set_visible('off')
    ax.set_ylim(ylims)

    # Name to save
    pic_name = pm.py_output_filename(ea.tag,which_res,stat_method+str_1000+'_'+str_wavebc+'_'+'_'.join([str(i) for i in which_methods]),pic_format)


    return ax, pic_name
