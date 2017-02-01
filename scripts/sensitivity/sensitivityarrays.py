#!/usr/bin/python

###############################################################################
#                      Variables for Sensitivity Analysis                     #
###############################################################################

# Different runs ##############################################################
runs = [['cubey','2017_01_15','a','2017_01_15',range(1000)],
        ['cubey','2017_01_31','a','2017_01_31',range(1000)],
        ['cubey','2017_01_31','aln','2017_01_31',range(1001,2000)],
        ['cubey','2017_01_31','bxz','2017_01_31',range(2001,3000)],
        ['cubey','2017_01_30','a','2017_01_30',range(1000)],
        ['cubey','2017_01_30','aln','2017_01_30',range(1001,2000)],
        ['cubey','2017_01_30','bxz','2017_01_30',range(2001,3000)],
        ['cubey','2017_01_30','dkl','2017_01_30',range(3001,4000)]]
        

# Sensitivity analysis: Varied variables ######################################
sensitivity_varnames = {'cubey_2016_12_13_a':'Thermal conductivity deprecated',
                        'cubey_2016_12_14_a':'Thermal conductivity deprecated',
                        'cubey_2016_12_14_aln':'Thermal conductivity deprecated',
                        'cubey_2016_12_14_bxz':'Thermal conductivity deprecated',
                        'cubey_2017_01_15_a':'Volumetric heat capacity',
                        'cubey_2017_01_16_a':'Volumetric heat capacity deprecated',
                        'cubey_2017_01_16_aln':'Volumetric heat capacity deprecated',
                        'cubey_2017_01_16_bxz':'Volumetric heat capacity deprecated',
                        'cubey_2017_01_31_a':'Volumetric heat capacity',
                        'cubey_2017_01_31_aln':'Volumetric heat capacity',
                        'cubey_2017_01_31_bxz':'Volumetric heat capacity',
                        'cubey_2017_01_30_a':'Thermal conductivity',
                        'cubey_2017_01_30_aln':'Thermal conductivity',
                        'cubey_2017_01_30_bxz':'Thermal conductivity',
                        'cubey_2017_01_30_dkl':'Thermal conductivity',}

# Cubey: Unit numbers #########################################################
unit_numbers = {'cubey_2016_12_13_a': 1,
                        'cubey_2016_12_14_a':2,
                        'cubey_2016_12_14_aln':7,
                        'cubey_2016_12_14_bxz':3,
                        'cubey_2017_01_15_a':1,
                        'cubey_2017_01_16_a':2,
                        'cubey_2017_01_16_aln':7,
                        'cubey_2017_01_16_bxz':3,
                        'cubey_2017_01_31_a':2,
                        'cubey_2017_01_31_aln':7,
                        'cubey_2017_01_31_bxz':3,
                        'cubey_2017_01_30_a':1,
                        'cubey_2017_01_30_aln':2,
                        'cubey_2017_01_30_bxz':7,
                        'cubey_2017_01_30_dkl':3,}

# Cubey: Unit names ###########################################################
unit_names =  {1:'Sand, outside',
               2:'Sand, inside',
               7:'Hull, large tube',
               3:'Inside, small tube'}

# Sensitivity analysis: Strings of Ranges #####################################
sensitivity_ranges = {'cubey_2016_12_13_a':r'1.5-3.0 $\frac{W}{mK}$ deprecated',
                      'cubey_2016_12_14_a':r'0.5-1.5 $\frac{W}{mK}$ deprecated',
                      'cubey_2016_12_14_aln':r'1.0-3.0 $\frac{W}{mK}$ deprecated',
                      'cubey_2016_12_14_bxz':r'0.1-1.1 $\frac{W}{mK}$ deprecated',
                      'cubey_2017_01_15_a':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_01_16_a':r'0.5-3.5 $\frac{J}{Km^3}$ deprecated',
                      'cubey_2017_01_16_aln':r'0.5-3.5 $\frac{J}{Km^3}$ deprecated',
                      'cubey_2017_01_16_bxz':r'0.5-3.5 $\frac{J}{Km^3}$ deprecated',
                      'cubey_2017_01_31_a':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_01_31_aln':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_01_31_bxz':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_01_30_a':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_01_30_aln':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_01_30_bxz':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_01_30_dkl':r'0.1-3.1 $\frac{W}{mK}$',}


# Sensitivity analysis: Default numbers #######################################
default_jobs = {'cubey_2017_01_15_a':101,
                'cubey_2017_01_31_a':101,
                'cubey_2017_01_31_aln':168,
                'cubey_2017_01_31_bxz':168,
                'cubey_2017_01_30_a':834,
                'cubey_2017_01_30_aln':301,
                'cubey_2017_01_30_bxz':634,
                'cubey_2017_01_30_dkl':76,}

default_values = {'cubey_2017_01_15_a':r'0.8 $10^6 \frac{J}{Km^3}$',
                  'cubey_2017_01_31_a':r'0.8 $10^6 \frac{J}{Km^3}$',
                  'cubey_2017_01_31_aln':r'1.0 $10^6 \frac{J}{Km^3}$',
                  'cubey_2017_01_31_bxz':r'1.0 $10^6 \frac{J}{Km^3}$',
                  'cubey_2017_01_30_a':r'2.6 $\frac{W}{mK}$',
                  'cubey_2017_01_30_aln':r'1.0 $\frac{W}{mK}$',
                  'cubey_2017_01_30_bxz':r'2.0 $\frac{W}{mK}$',
                  'cubey_2017_01_30_dkl':r'0.325 $\frac{W}{mK}$',}


# CUBEY: Measurement points ###################################################
obs_longlabels = {0:'North(out)',            # Outer ring
                  1:'Northwest(out)',
                  2:'West(out)',
                  3:'Southwest(out)',
                  4:'South(out)',
                  5:'Southeast(out)',
                  6:'East(out)',
                  7:'Northeast(out)',
                  8:'North(in)',            # Inner ring
                  9:'Northwest(in)',
                  10:'West(in)',
                  11:'Sinhwest(in)',
                  12:'Sinh(in)',
                  13:'Sinheast(in)',
                  14:'East(in)',
                  15:'Northeast(in)',}

obs_shortlabels = {0:'NN',            # Outer ring
                   1:'NW',
                   2:'WW',
                   3:'SW',
                   4:'SS',
                   5:'SE',
                   6:'EE',
                   7:'NE',
                   8:'nn',            # Inner ring
                   9:'nw',
                   10:'ww',
                   11:'sw',
                   12:'ss',
                   13:'se',
                   14:'ee',
                   15:'ne',}
