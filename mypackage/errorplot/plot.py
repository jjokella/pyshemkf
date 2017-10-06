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
         n_runs = 1000,
         which_enssize = [50,70,100,250],
         model = 'wavebc',
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

    n_runs : integer
        1000 - typically exist for ensemble sizes 50, 70, 100, 250
        100 - typically exist for ensemble sizes 500, 1000, 2000

    which_enssize : array of integers
        [50,70,100,250] - possible for 1000 synthetic studies
        [500,1000,2000] - possible for 100 synthetic studies

    model : string
        'wavebc' - Model wavebc
        'wave' - Model wave

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

    # Check
    if n_runs==1000:
        for enssize in which_enssize:
            if not enssize in [50,70,100,250]:
                raise exceptions.RuntimeError('n_runs==1000: Wrong enssize in which_enssize.')
    elif n_runs== 100:
        for enssize in which_enssize:
            if not enssize in [500,1000,2000]:
                raise exceptions.RuntimeError('n_runs==100: Wrong enssize in which_enssize.')
    else:
        raise exceptions.RuntimeError('Wrong n_runs.')

    # Number of methods
    num_methods = len(which_methods)

    # Legend
    legend_input = pa.longnames_methods
    legend_input = np.array([legend_input[i].ljust(18) for i in range(len(legend_input))])
    legend_input = legend_input[which_methods]

    # Load endres
    var = np.load(pm.py_output_filename('errorplot',which_res,stat_method+'_'+str(n_runs)+'_'+model+'_'+'_'.join([str(i) for i in which_methods]),'npy'))

    # Load standard deviation
    if is_std:
        std = np.load(pm.py_output_filename('errorplot',which_res,std_method+'_'+str(n_runs)+'_'+model+'_'+'_'.join([str(i) for i in which_methods]),'npy'))


    ax.set_prop_cycle("color",['k'])
    ax.set_position(figpos)

    for iens,enssize in enumerate(which_enssize):
        # x positions, up to 15 methods
        x = np.delete(np.arange(0,16),
                    np.arange(0,16,num_pack+1)) #Skip every (num_pack+1)-th

        varplot = var[:,iens]
        if is_std:
            stdplot = std[:,iens]

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
                             varplot[iplot]-0.005 if enssize == 2000 else varplot[iplot],
                             r'$n_{e}$ = '+str(enssize),
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

    # Saving location
    pic_name = pm.py_output_filename(ea.tag,which_res,stat_method+str(n_runs)+'_'+model+'_'+'_'.join([str(i) for i in which_methods]),pic_format)

    return ax, pic_name



def quots(ax,
          which_methods = [0,1,2,3,4,5,6],
          which_res = 'endres',
          stat_method = 'mean',
          n_runs = 1000,
          model = 'wavebc',
          enssize = 50,
          pic_format = 'pdf',      #'png' or 'eps' or 'svg' or 'pdf'
          figpos = [0.32,0.2,0.6,0.8],
          # ylims = [0.28,0.82],
          # yticks = [0.3,0.4,0.5,0.6,0.7,0.8],
          ticksize = 20,
          # num_pack = 4,                     # Number of methods in pack
          # formatsos = ['o','v','s','p','o','v','s','p'],
          # coleros = [(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),
          #            (1.0,1.0,1.0),(1.0,1.0,1.0),(1.0,1.0,1.0),(1.0,1.0,1.0)],
          # markersize = 10,
          # markeredgesize = 1.5,
          # fontleg = 30,                              #18
          # fonttit = 40,
          # fontlab = 40,
          # fonttic = 30,
              ):
    """
    A function plotting a grid of quotients of
    statistical measures.

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

    n_runs : integer
        1000 - typically exist for ensemble sizes 50, 70, 100, 250
        100 - typically exist for ensemble sizes 500, 1000, 2000

    model : string
        'wavebc' - Model wavebc
        'wave' - Model wave

    enssize : integer
        Ensemble size of the job. Possibilities: 50,
        70, 100, 250, 500, 1000, 2000

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
        Axes containing quotient matrix.

    pic_name : string
        Containing proposed saving location for Figure.
    """

    # Check
    if n_runs==1000:
        if not enssize in [50,70,100,250]:
            raise exceptions.RuntimeError('enssize wrong')
    else:
        if not enssize in [500,1000,2000]:
            raise exceptions.RuntimeError('enssize wrong')

    # Number of compared methods
    num_methods = len(which_methods)

    # Ensemble size translated to index
    iens = pa.indens[model][n_runs][enssize]

    # Load endres
    var = np.load(pm.py_output_filename('errorplot',which_res,stat_method+'_'+str(n_runs)+'_'+model+'_'+'_'.join([str(i) for i in which_methods]),'npy'))

    # Calculate and sort quots
    quots = np.array(
        [[var[i1,iens]/var[i2,iens] for i1 in range(num_methods)] for i2 in range(num_methods)]
        )

    ax.set_position(figpos)

    # White Rectangles
    for ipm in range(num_methods):
        for jpm in range(num_methods):
            # Diagonal black
            if ipm == jpm:
                quots[ipm,jpm] = 0.0
            # Upper triangle white
            if ipm < jpm:
                quots[ipm,jpm] = None


    ax.imshow(quots,interpolation='nearest',cmap='Greys_r',
              norm = colors.Normalize(vmin=0.8,vmax=1.0,clip=False))

    # Plot: Mostly ticks
    ax.set_xticks([i for i in range(num_methods)])
    ax.set_xticklabels([pa.names_methods[which_methods[i]] for i in range(len(which_methods))], fontsize=ticksize, rotation=90)
    ax.set_yticks([i for i in range(num_methods)])
    ax.set_yticklabels([pa.names_methods[which_methods[i]] for i in range(len(which_methods))], fontsize=ticksize)
    ax.tick_params(length=0)
    ax.set_frame_on(False)


    # Text
    for itext in range(num_methods):
        for jtext in range(num_methods):
            if itext<jtext:
                ntext = quots[jtext,itext]
                ttext = str(ntext)[0:4]
                px = itext-0.35
                py = jtext+0.15
                colero = 'white' if ntext<0.9 else 'black'

                ax.text(px,py,ttext,color = colero,fontsize = 20)

    # Saving location
    pic_name = pm.py_output_filename(ea.tag,'quots_'+which_res,stat_method+str(n_runs)+'_'+model+'_'+'_'.join([str(i) for i in which_methods]),pic_format)

    return ax, pic_name
