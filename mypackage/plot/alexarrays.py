#!/usr/bin/python

###############################################################################
#                      Variables for Sensitivity Analysis                     #
###############################################################################

# Sensitivity analysis: Varied variables ######################################
sensitivity_varnames = {'cubey_2016_12_13_a':'Thermal conductivity Unit 1',
                        'cubey_2016_12_14_a':'Thermal conductivity Unit 2',
                        'cubey_2016_12_14_aln':'Thermal conductivity Unit 7',
                        'cubey_2016_12_14_bxz':'Thermal conductivity Unit 3',
                        'cubey_2017_01_15_a':'Volumetric heat capacity Unit 1',
                        'cubey_2017_01_16_a':'Volumetric heat capacity Unit 2',
                        'cubey_2017_01_16_aln':'Volumetric heat capacity Unit 7',
                        'cubey_2017_01_16_bxz':'Volumetric heat capacity Unit 3'}

# Cubey: Units ################################################################
units_names =  {1:'Sand, outside',
                2:'Sand, inside',
                7:'Hull, large tube',
                3:'Inside, small tube'}

# Sensitivity analysis: Strings of Ranges #####################################
sensitivity_ranges = {'cubey_2016_12_13_a':r'1.5-3.0 $\frac{W}{mK}$',
                      'cubey_2016_12_14_a':r'0.5-1.5 $\frac{W}{mK}$',
                      'cubey_2016_12_14_aln':r'1.0-3.0 $\frac{W}{mK}$',
                      'cubey_2016_12_14_bxz':r'0.1-1.1 $\frac{W}{mK}$',
                      'cubey_2017_01_15_a':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_01_16_a':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_01_16_aln':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_01_16_bxz':r'0.5-3.5 $10^6 \frac{J}{Km^3}$'}
