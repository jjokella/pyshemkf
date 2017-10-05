# Read routine for errorplot arrays

import os
import numpy as np

from mypackage.plot import plotarrays as pa
from mypackage.run import pythonmodule as pm
from mypackage.numcomp import arrays as na

import exceptions

def read(which_methods,
         which_res = 'endres',
         model = 'wavebc',
         n_runs = 1000,
         method = 'ttest',
         enssize = 50,
         n_syn = 1,
         n_comparisons = 10000,
         cl = 0.95,
         pval = 0.05,
):
    """
    Reads residual arrays at beginning (begres) or
    end (endres) of the EnKF run and calculates
    probability arrays which method is better,
    worse, or if they are even.

    Parameters
    ----------
    which_methods : array int
        Array of integers containing the method specifiers
        from module plotarrays.

    which_res : string
        'endres' - use residuals after EnKF run
        'begres' - use residuals before EnKF run

    model : string
        'wavebc' - Model wavebc
        'wave' - Model wave

    n_runs : integer
        1000 - typically exist for ensemble sizes 50, 70, 100, 250
        100 - typically exist for ensemble sizes 500, 1000, 2000

    method : string
        Which method to use for statistical comparison
        of the subset. If n_syn == 1, the comparison
        always defaults to comparing the residuals.
        'ttest' - Use the T-Test, testing if the
                  two samples belong to the same
                  Gaussian distribution.
        'gauss' - Calculate Gaussian distribution
                  of the difference and calculate
                  its probability to be larger
                  than zero.

    enssize : integer
        Ensemble size of the job. Possibilities: 50,
        70, 100, 250, 500, 1000, 2000

    n_syn : integer
        Number of synthetic studies in subset.

    n_comparisons : integer
        Number of comparisons calculated.

    cl : float
        Confidence level for 'gauss'. If the probability
        weight of the distribution of the difference between
        two methods is larger than cl on one side of zero,
        then the method with the smaller RMSE is considered
        to have performed better.

    pval : float
        If the p-value from the T-Test is smaller than pval
        the Test is considered to be negative, thus a
        significant difference between the distributions is
        assumed, making the method with the smaller RMSE
        performing significantly better.

    Returns
    -------
    probs : array
        Array containing the probabilities.

    probs_name : string
        Containing proposed saving location for array.
    """

    # Checks
    if not n_runs in [100,1000]:
        raise exceptions.RuntimeError('n_runs wrong')
    if not model in ['wavebc','wave']:
        raise exceptions.RuntimeError('model wrong')
    if not method in ['ttest','gauss']:
        raise exceptions.RuntimeError('method wrong')

    if n_runs==1000:
        if not enssize in [50,70,100,250]:
            raise exceptions.RuntimeError('enssize wrong')
        if n_syn>1000:
            raise exceptions.RuntimeError('n_syn wrong')
    else:
        if not enssize in [500,1000,2000]:
            raise exceptions.RuntimeError('enssize wrong')
        if n_syn>100:
            raise exceptions.RuntimeError('n_syn wrong')

    # Load final residuals
    res = np.zeros([len(which_methods),n_runs])
    for i,i_method in enumerate(which_methods):
        res_name = pm.py_output_filename(
            'dists',
            which_res,
            pa.dats[model][n_runs][i_method][enssize]+'_'+pa.lets[model][n_runs][i_method][enssize],
            'npy')
        res[i,0:pa.nums[model][n_runs][i_method][enssize]] = np.load(res_name)

    # Initialize probs array
    probs = np.zeros([len(which_methods),len(which_methods),3])

    # DOCUMENTATION:
    # -------------------------------------------------
    # probs[i,j,0] : Probability that method i is better
    # probs[i,j,1] : Probability that methods are equal
    # probs[i,j,2] : Probability that method j is better
    for ii,ri in enumerate(which_methods):
        for ij,rj in enumerate(which_methods):

            #Every pair only once (symmetry)
            if ij < ij:
                continue

            # Residual arrays for each method
            resi = res[ii,0:pa.nums[model][n_runs][ri][enssize]]
            resj = res[ij,0:pa.nums[model][n_runs][rj][enssize]]

            if [n_syn,n_syn] >= [pa.nums[model][n_runs][ri][enssize],pa.nums[model][n_runs][rj][enssize]]:
                if not n_comparisons == 1:
                    raise exceptions.RuntimeError('Set n_comparisons to 1 if n_syn equal to full number of available studies')

            ni = 0                        #...i better
            ne = 0                        #...equal
            nj = 0                        #...j better


            # Iterate number of comparisons
            for i in range(n_comparisons):

                # Subset of random order
                isi = np.random.permutation(np.arange(pa.nums[model][n_runs][ri][enssize]))[0:n_syn]
                isj = np.random.permutation(np.arange(pa.nums[model][n_runs][rj][enssize]))[0:n_syn]
                resmixi = resi[isi]
                resmixj = resj[isj]

                # Single run
                if n_syn == 1:
                    if resmixi[0] < resmixj[0]:
                        ni = ni + 1
                    elif resmixi[0] > resmixj[0]:
                        nj = nj + 1
                    else:    #It actually happens...
                        ne = ne + 1

                # T-Test
                elif method=="ttest":
                    tv,pv = sp.stats.ttest_ind(resmixi,resmixj,equal_var = False)
                    if pv < pval:     #Significant difference
                        if tv < 0:
                            ni = ni+1
                        else:
                            nj = nj+1
                    else:             #No significant difference
                        ne = ne+1

                # Gaussian difference
                elif method=="gauss":
                    # Means
                    mi = np.mean(resmixi)
                    mj = np.mean(resmixj)
                    # Mean Standard deviations
                    si = np.std(resmixi)/np.sqrt(resmixi.size)
                    sj = np.std(resmixj)/np.sqrt(resmixj.size)

                    # Mean difference and stdev of mean difference
                    m = mj-mi
                    s = np.sqrt(si*si + sj*sj)

                    # Probability bigger than zero
                    pcl = 0.5 + 0.5*sp.special.erf(m/(s*np.sqrt(2)))

                    if pcl > cl:     #i better
                        ni = ni + 1
                    elif pcl < 1-cl:   #j better
                        nj = nj + 1
                    else:    # No significant difference
                        ne = ne+1

            # Output probabilities
            pi = float(ni)/float(ni+ne+nj)       # i better
            pe = float(ne)/float(ni+ne+nj)       # equal
            pj = float(nj)/float(ni+ne+nj)       # j better

            probs[ii,ij,0] = pi
            probs[ii,ij,1] = pe
            probs[ii,ij,2] = pj

            probs[ij,ii,0] = pj
            probs[ij,ii,1] = pe
            probs[ij,ii,2] = pi

    probs_name = pm.py_output_filename(na.tag,'probs_'+which_res,model+'_'+str(n_runs)+'_'+method+'_'+str(enssize)+'_'+str(n_syn)+'_'+'_'.join([str(i) for i in which_methods]),'npy')

    return probs, probs_name
