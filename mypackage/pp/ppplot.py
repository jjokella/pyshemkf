#!/usr/bin/python

# Paths
python_dir = '/home/jk125262/PythonDir_Cluster'
input_file_dir = '/home/jk125262/PythonDir_Cluster/exec/pp'

# Modules
import os
import numpy as np
from numpy import linalg as la
from scipy import stats
import matplotlib as mpl
mpl.use('GTKAgg')        # do this before importing pylab
import pylab
import matplotlib.pyplot as plt
import time
import gtk
import gobject

from mypackage.pp import calc


def make_plot(ip_last,dp,xs,ns,Gss,beta_pri,Hy,Gyy,R,zy,Xy,Xs,Gssy,Gsy,Gys,zs_rand,xy,privar,Qbb,Gss_prior,Gyy_prior,Gys_prior,zs_prior,estvar_prior,zs,zs_post,estvar_post,varss,ips,time_time,is_animate,is_kalman):
    #Calculate the matrices for all pilot points

    if is_kalman:
        jp,zsp,estvar,estvarp,xp,zp,zsp_post_j,Gss_post_j = calc.get_zsp_kalman(ip_last,dp,xs,ns,Gss_prior,zs_prior,Hy,R,zy,Gyy_prior,Gys_prior,Gssy)
        figtitle = 'Kalman'
    else:
        jp, zsp, Gsspy, estvar, estvarp, xp, zp, zsp_johannes, Gsspy_johannes, zp_johannes = calc.get_zsp(ip_last,dp,xs,ns,Gss,beta_pri,Hy,Gyy,R,zy,Xy,Xs,Gssy,Gsy,Gys)
        figtitle = 'Kriging'

    # Initializing figure and axes
    fig = plt.figure(figsize = [18,18])
    plt.suptitle(figtitle)
    ax = fig.add_subplot(2,1,1)     # (2,1,1)
    ax_k = fig.add_subplot(2,1,2)
    # ax_a = fig.add_subplot(4,2,5)
    # ax_ad = fig.add_subplot(4,2,6)
    # ax_c = fig.add_subplot(4,2,7)

    # plot data
    line1, = ax.plot(xs,zs_rand,'-g')
    line2, = ax.plot(xy,zy,'ob')
    line1k, = ax_k.plot(xs,zs_rand,'-g')
    line2k, = ax_k.plot(xy,zy,'ob')
    # plot kriging prior
    line3, = ax.plot(xs,beta_pri*Xs, 'k-')
    line4, = ax.plot(xs,beta_pri*Xs+2.5*np.sqrt(privar+Qbb), 'k:')
    line5, = ax.plot(xs,beta_pri*Xs-2.5*np.sqrt(privar+Qbb), 'k:')
    # plot kalman prior
    line3k, = ax_k.plot(xs,zs_prior, 'k-')
    line4k, = ax_k.plot(xs,zs_prior+2.5*np.sqrt(estvar_prior), 'k:')
    line5k, = ax_k.plot(xs,zs_prior-2.5*np.sqrt(estvar_prior), 'k:')
    # plot kriging estimate
    line6, = ax.plot(xs,zs, 'b-')
    line7, = ax.plot(xs,zs+2.5*np.sqrt(estvar), ':b')
    line8, = ax.plot(xs,zs-2.5*np.sqrt(estvar), ':b')
    # plot Kalman estimate
    line6k, = ax_k.plot(xs,zs_post, '-',color='b')
    line7k, = ax_k.plot(xs,zs_post+2.5*np.sqrt(estvar_post), ':',color='b')
    line8k, = ax_k.plot(xs,zs_post-2.5*np.sqrt(estvar_post), ':',color='b')
    # plot kriging pilot point estimate
    line9,  = ax.plot(xp,zp, 'or')
    line10, = ax.plot(xs,zsp, 'r')
    line11, = ax.plot(xs,zsp+2.5*np.sqrt(estvarp), ':r')
    line12, = ax.plot(xs,zsp-2.5*np.sqrt(estvarp), ':r')
    # plot Kalman pilot point estimate
    line9,  = ax_k.plot(xp,zp, 'or')
    line10, = ax_k.plot(xs,zsp, 'r')
    line11, = ax_k.plot(xs,zsp+2.5*np.sqrt(estvarp), ':r')
    line12, = ax_k.plot(xs,zsp-2.5*np.sqrt(estvarp), ':r')

    # # plot the stupid criteria: a
    # line1_a, = ax_a.plot(range(0,ip_last,dp),aestvar_record[range(0,ip_last,dp)],'b')
    # line2_a, = ax_a.plot([0,nptot*dp],[prior_aestvar,prior_aestvar],'b:')
    # line3_a, = ax_a.plot(range(0,ip_last,dp),aestvarp_record[range(0,ip_last,dp)],'r')

    # # plot the stupid criteria: ad
    # line1_ad, = ax_ad.plot([0,nptot*dp],[prior_adestvar,prior_adestvar],'b:')
    # line2_ad, = ax_ad.plot(range(0,ip_last,dp),adestvarp_record[range(0,ip_last,dp)],'r')

    # # plot the stupid criteria: c
    # line1_c, = ax_c.plot([0,nptot*dp],[prior_cestvar,prior_cestvar],'b:')
    # line2_c, = ax_c.plot(range(0,ip_last,dp),cestvarp_record[range(0,ip_last,dp)],'r')

    # Set axis titles, limits
    ax.set_title('Kriging: best estimate and 95% CI')
    ax.set_xlabel('x')
    ax.set_label('s')
    ax.set_ylim(beta_pri + 3*(np.sqrt(varss+Qbb+R[0,0]))*np.array([-1,1]))

    ax_k.set_title('Kalman: best estimate and 95% CI')
    ax_k.set_xlabel('x')
    ax_k.set_label('s')
    ax_k.set_ylim(beta_pri + 3*(np.sqrt(varss+Qbb+R[0,0]))*np.array([-1,1]))

    # ax_a.set_title('a-criterion')
    # ax_a.set_xlim([0,aestvar_record.size])
    # ax_a.set_ylim([0,prior_aestvar*1.1])

    # ax_ad.set_title('ad_criterion')
    # ax_ad.set_xlim([0,adestvar_record.size])
    # ax_ad.set_ylim([0,prior_adestvar*1.1])

    # ax_c.set_title('c-criterion')
    # ax_c.set_xlim([0,cestvar_record.size])
    # ax_c.set_ylim([0, prior_cestvar*1.1])

    def animate():
        # Loop over pilot points
        for ip in ips:
            # Calculation of matrices for specific number of pilot points
            # get_zsp(ip) 
            # get_zsp_kalman(ip)
            # jp,zsp,estvar,estvarp,xp,zp,zsp_post_j,Gss_post_j = calc.get_zsp_kalman(ip,dp,xs,ns,Gss_prior,zs_prior,Hy,R,zy,Gyy_prior,Gys_prior,Gssy)
            jp, zsp, Gsspy, estvar, estvarp, xp, zp, zsp_johannes, Gsspy_johannes, zp_johannes = calc.get_zsp(ip,dp,xs,ns,Gss,beta_pri,Hy,Gyy,R,zy,Xy,Xs,Gssy,Gsy,Gys)

            # plot kriging estimate
            line9.set_xdata(xp)
            line9.set_ydata(zp)
            line10.set_xdata(xs)
            line10.set_ydata(zsp)
            line11.set_xdata(xs)
            line11.set_ydata(zsp+2.5*np.sqrt(estvarp))
            line12.set_xdata(xs)
            line12.set_ydata(zsp-2.5*np.sqrt(estvarp))
            # # plot the stupid criteria: a
            # line1_a.set_xdata(jp)
            # line1_a.set_ydata(aestvar_record[jp])
            # line3_a.set_xdata(jp)
            # line3_a.set_ydata(aestvarp_record[jp])
            # # plot the stupid criteria: ad
            # line2_ad.set_xdata(jp)
            # line2_ad.set_ydata(adestvarp_record[jp])
            # # plot the stupid criteria: c
            # line2_c.set_xdata(jp)
            # line2_c.set_ydata(cestvarp_record[jp])

            # Draw the updated figure
            fig.canvas.draw()

        # Time output
        print("Wall time: " + str(time.time()-time_time) + ',  ' + time.asctime( time.localtime( time.time())))
        # print('FPS:' + str(nptot/(time.time()-tstart)))
        # Exiting gobject by returning False
        return False

    # Start animation
    if is_animate:
        gobject.idle_add(animate)
    plt.show()                   
    return
