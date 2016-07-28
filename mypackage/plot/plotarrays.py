#!/usr/bin/python

import os
import numpy as np

# Paths
python_dir = os.environ['HOME']+'/PythonDir'

num_methods = 7
num_jobs = num_methods*7

num_methods1000 = 7
num_jobs1000 = num_methods1000*4

# Date of output directory
normal_dats = ['2015_06_10','2015_12_17','2015_06_11',
               '2015_06_11','2015_06_16','2015_06_16','2015_06_17']
damping01_dats = ['2015_07_16','2015_12_17','2015_07_16',
                  '2015_07_16','2015_07_17','2015_07_17','2015_07_17']
normalscoreverynew_dats = ['2015_10_01','2015_12_17','2015_10_01',
                           '2015_10_01','2015_10_01','2015_10_01','2015_10_01']
dual_dats = ['2015_07_15','2015_12_17','2015_07_15',
             '2015_07_15','2015_07_15','2015_07_15','2015_07_15']
hybrid_dats = ['2015_10_02','2015_12_17','2015_10_02',
               '2015_10_02','2015_10_02','2015_10_02','2015_10_02']
localisation_dats = ['2015_06_23','2015_12_17','2015_06_23',
                     '2015_06_23','2015_06_24','2015_06_24','2015_06_24']
newiterative4_dats = ['2015_12_11','2016_02_09','2015_12_11',
                      '2015_12_11','2015_12_11','2015_12_11','2015_12_11']


normalscore_dats = ['2015_06_11','2015_06_12','2015_06_12','2015_06_19','2015_06_19','2015_06_19']
damping_dats = ['2015_06_13','2015_06_14','2015_06_14','2015_06_22','2015_06_22','2015_06_22']
damping03_dats = ['2015_07_16','2015_07_16','2015_07_16','2015_07_17','2015_07_17','2015_07_17']
normalscorenew_dats = ['2015_09_04','2015_09_04','2015_09_04','2015_09_04','2015_09_04','2015_09_04']
damping02_dats = ['2015_10_05','2015_10_05','2015_10_05','2015_10_05','2015_10_05','2015_10_05']
iterative_dats = ['2015_10_16','2015_10_16','2015_10_16','2015_10_16','2015_10_16','2015_10_16']
iterative_2_dats = ['2015_10_16','2015_10_16','2015_10_16','2015_10_16','2015_10_16','2015_10_16']
newiterative_dats = ['2015_11_18','2015_11_18','2015_11_18','2015_11_18','2015_11_18','2015_11_18']
newiterative2_dats = ['2015_11_23','2015_11_23','2015_11_23','2015_11_23','2015_11_23','2015_11_23']
newiterative3_dats = ['2015_12_08','2015_12_08','2015_12_08','2015_12_09','2015_12_09','2015_12_09']
obs_10_normal_dats = ['2015_07_20','2015_07_20','2015_07_20','2015_07_20','2015_07_20','2015_07_20']
obs_200_normal_dats = ['2015_07_22','2015_07_22','2015_07_22','2015_07_22','2015_07_22','2015_07_22']
lowobsvar_dats = ['2015_07_21','2015_07_27','2015_07_27','2015_07_26','2015_07_26','2015_07_26']

# First letter of runs
normal_lets = ['b','dkl','b','cx','cx','gt','b']
damping01_lets = ['kp','ewx','ol','sh','kp','ol','sh']
normalscoreverynew_lets = ['b','gjj','cx','gt','kp','ol','sh']
dual_lets = ['b','hvv','cx','gt','kp','ol','sh']
hybrid_lets = ['b','jih','cx','gt','kp','ol','sh']
localisation_lets = ['b','kut','cx','gt','b','cx','gt']
newiterative4_lets = ['b','b','aln','bxz','dkl','ewx','gjj']

normalscore_lets = ['gt','b','cx','b','cx','gt']
damping_lets = ['b','b','cx','b','cx','gt']
damping03_lets = ['b','cx','gt','b','cx','gt']
normalscorenew_lets = ['b','cx','gt','kp','ol','sh']
damping02_lets = ['b','cx','gt','kp','ol','sh']
iterative_lets = ['b','cx','gt','kp','ol','sh']
iterative_2_lets = ['b','cx','gt','kp','ol','sh']
newiterative_lets = ['b','cx','gt','kp','ol','sh']
newiterative2_lets = ['b','cx','gt','kp','ol','sh']
newiterative3_lets = ['b','aln','bxz','dkl','ewx','gjj']
obs_10_normal_lets = ['b','cx','gt','kp','ol','sh']
obs_200_normal_lets = ['b','cx','gt','kp','ol','sh']
lowobsvar_lets = ['b','cx','gt','kp','ol','sh']

# Number of runs
normal_nums = [100,100,100,100,100,100,100]
damping01_nums = [100,100,100,100,100,100,100]
normalscoreverynew_nums = [100,100,100,100,100,100,34] 
dual_nums = [100,100,100,100,100,100,100]
hybrid_nums = [100,100,100,100,100,100,100]
localisation_nums = [100,100,100,100,100,100,100]
newiterative4_nums = [99,100,88,22,16,8,4]

normalscore_nums = [100,100,100,70,48,28]  
damping_nums = [100,100,100,100,100,100]
damping03_nums = [100,100,100,100,100,100]
normalscorenew_nums = [100,100,100,40,97,34]
damping02_nums = [100,100,100,100,100,100]
iterative_nums = [100,100,100,100,100,100]
iterative_2_nums = [100,100,100,100,100,100]
newiterative_nums = [100,100,100,100,100,100]
newiterative2_nums = [100,100,100,100,100,100]
newiterative3_nums = [99,100,100,100,100,64]
obs_10_normal_nums = [100,100,100,100,100,100]
obs_200_normal_nums = [100,100,100,100,100,100]
lowobsvar_nums = [100,100,100,100,100,100]

dats = np.array([normal_dats, damping01_dats, normalscoreverynew_dats, dual_dats, hybrid_dats, 
                 localisation_dats,newiterative4_dats])       #bis hier: 1000er
                 # normalscore_dats, damping_dats, damping03_dats, 
                 # normalscorenew_dats, damping02_dats,
                 # iterative_dats, iterative_2_dats, newiterative_dats,newiterative2_dats,
                 # newiterative3_dats,
                 # obs_10_normal_dats, obs_200_normal_dats, lowobsvar_dats])
lets = np.array([normal_lets, damping01_lets, normalscoreverynew_lets, dual_lets, hybrid_lets, 
                 localisation_lets,newiterative4_lets])       #bis hier: 1000er
                 # normalscore_lets, damping_lets, damping03_lets,
                 # normalscorenew_lets, damping02_lets,
                 # iterative_lets, iterative_2_lets, newiterative_lets,newiterative2_lets,
                 # newiterative3_lets,
                 # obs_10_normal_lets, obs_200_normal_lets, lowobsvar_lets])
nums = np.array([normal_nums, damping01_nums, normalscoreverynew_nums, dual_nums, hybrid_nums, 
                 localisation_nums,newiterative4_nums])       #bis hier: 1000er
                 # normalscore_nums, damping_nums, damping03_nums,
                 # normalscorenew_nums, damping02_nums,
                 # iterative_nums, iterative_2_nums, newiterative_nums,newiterative2_nums,
                 # newiterative3_nums,
                 # obs_10_normal_nums, obs_200_normal_nums, lowobsvar_nums])

# Number of observation intervals
num_obss = [[100 for i in range(6)],[100 for i in range(6)],[100 for i in range(6)],[100 for i in range(6)],
            [100 for i in range(6)],[100 for i in range(6)],[5050 for i in range(6)],   #Bis hier: 1000er
            [100 for i in range(6)],[100 for i in range(6)],
            [100 for i in range(6)],[100 for i in range(6)],[100 for i in range(6)],[100 for i in range(6)],
            [100 for i in range(6)],[150 for i in range(6)],[ 55 for i in range(6)],[ 55 for i in range(5)],
            [ 10 for i in range(6)],[200 for i in range(6)],
            [100 for i in range(6)]]                             #Should be almost constant

# 1000er Bundles------------------------------------------------------------
normal1000_dats = ['2015_11_26','2015_12_17','2015_11_26','2015_11_26']
damping1000_dats = ['2015_11_27','2015_12_17','2015_11_27','2015_11_27']
normalscore1000_dats = ['2015_12_05','2015_12_17','2015_12_05','2015_12_05']
dual1000_dats = ['2015_12_05','2015_12_17','2015_12_05','2015_12_05']
hybrid1000_dats = ['2015_12_15','2015_12_17','2015_12_15','2015_12_15']
localisation1000_dats = ['2015_12_18','2015_12_17','2015_12_18','2015_12_18']
iterative1000_dats = ['2016_01_07','2016_01_14','2016_01_21','2016_01_28']

normal1000_wavebc_dats = ['2016_03_24','2016_03_24','2016_03_24','2016_03_24']
damping1000_wavebc_dats = ['2016_04_01','2016_04_01','2016_04_01','2016_04_01']
normalscore1000_wavebc_dats = ['2016_06_15','2016_06_15','2016_06_15','2016_06_15']
dual1000_wavebc_dats = ['2016_07_06','2016_07_06','2016_07_06','2016_07_06']
hybrid1000_wavebc_dats = ['2016_07_06','2016_07_06','2016_07_06','2016_07_06']
localisation1000_wavebc_dats = ['2016_07_07','2016_07_07','2016_07_07','2016_07_07']
iterative1000_wavebc_dats = ['2016_07_27','2016_07_27','','']

normal_wavebc_dats = ['2016_07_22','2016_07_22','2016_07_22']
damping_wavebc_dats = ['2016_07_22','2016_07_22','2016_07_22']
normalscore_wavebc_dats = ['2016_07_22','2016_07_22','2016_07_22']
dual_wavebc_dats = ['2016_07_21','2016_07_21','2016_07_21']
hybrid_wavebc_dats = ['2016_07_21','2016_07_21','2016_07_21']
localisation_wavebc_dats = ['2016_07_21','2016_07_21','2016_07_21']

normal1000_lets = ['b','mhf','aln','bxz']
damping1000_lets = ['b','ntr','aln','bxz']
normalscore1000_lets = ['b','pgd','aln','bxz']
dual1000_lets = ['dkl','qsp','ewx','gjj']
hybrid1000_lets = ['b','sfb','aln','bxz']
localisation1000_lets = ['b','trn','aln','bxz']
iterative1000_lets = ['b','b','b','b']

normal_wavebc_lets = ['b','aln','bxz']
damping_wavebc_lets = ['ewx','gjj','hvv']
normalscore_wavebc_lets = ['kut','mhf','ntr']
dual_wavebc_lets = ['b','aln','bxz']
hybrid_wavebc_lets = ['ewx','gjj','hvv']
localisation_wavebc_lets = ['kut','mhf','ntr']

normal1000_wavebc_lets = ['b','aln','bxz','dkl']
damping1000_wavebc_lets = ['b','aln','bxz','dkl']
normalscore1000_wavebc_lets = ['b','aln','bxz','dkl']
dual1000_wavebc_lets = ['b','aln','bxz','dkl']
hybrid1000_wavebc_lets = ['ewx','gjj','hvv','jih']
localisation1000_wavebc_lets = ['kut','mhf','ntr','pgd']
iterative1000_wavebc_lets = ['b','aln','','']

normal1000_nums = [1000,1000,1000,1000]
damping1000_nums = [1000,1000,1000,1000]
normalscore1000_nums = [1000,1000,1000,1000]
dual1000_nums = [1000,1000,1000,1000]
hybrid1000_nums = [1000,1000,1000,1000]
localisation1000_nums = [1000,1000,1000,1000]
iterative1000_nums = [1000,1000,1000,1000]

normal_wavebc_nums = [100,100,100]
damping_wavebc_nums = [100,100,100]
normalscore_wavebc_nums = [100,100,100]
dual_wavebc_nums = [100,100,100]
hybrid_wavebc_nums = [100,100,100]
localisation_wavebc_nums = [100,100,100]


normal1000_wavebc_nums = [1000,1000,1000,1000]
damping1000_wavebc_nums = [1000,1000,1000,1000]
normalscore1000_wavebc_nums = [1000,1000,1000,1000]
dual1000_wavebc_nums = [1000,1000,1000,1000]
hybrid1000_wavebc_nums = [1000,1000,1000,1000]
localisation1000_wavebc_nums = [1000,1000,1000,1000]
localisation1000_wavebc_nums = [1000,1000,,]   #num_obs 5050


dats1000 = [normal1000_dats,damping1000_dats,normalscore1000_dats,dual1000_dats,hybrid1000_dats,
            localisation1000_dats, iterative1000_dats]
lets1000 = [normal1000_lets,damping1000_lets,normalscore1000_lets,dual1000_lets,hybrid1000_lets,
            localisation1000_lets, iterative1000_lets]
nums1000 = [normal1000_nums,damping1000_nums,normalscore1000_nums,dual1000_nums,hybrid1000_nums,
            localisation1000_nums, iterative1000_nums]

dats1000_wavebc = [normal1000_wavebc_dats,damping1000_wavebc_dats,
                       normalscore1000_wavebc_dats,dual1000_wavebc_dats,
                       hybrid1000_wavebc_dats,localisation1000_wavebc_dats]#, iterative1000_wavebc_dats]
lets1000_wavebc = [normal1000_wavebc_lets,damping1000_wavebc_lets,
                       normalscore1000_wavebc_lets,dual1000_wavebc_lets,
                       hybrid1000_wavebc_lets,localisation1000_wavebc_lets]#, iterative1000_wavebc_lets]
nums1000_wavebc = [normal1000_wavebc_nums,damping1000_wavebc_nums,
                       normalscore1000_wavebc_nums,dual1000_wavebc_nums,
                       hybrid1000_wavebc_nums,localisation1000_wavebc_nums]#, iterative1000_wavebc_nums]


num_obss1000 = [[100 for i in range(6)],[100 for i in range(6)],[100 for i in range(6)],
                [100 for i in range(6)],[100 for i in range(6)],[100 for i in range(6)],
                [5050 for i in range(6)]]

# Flat arrays---------------------------------------------------------------
dates = np.concatenate(dats)           #Dates
letters = np.concatenate(lets)         #Letters
sizes = np.concatenate(nums)           #Number of runs

dates1000 = np.concatenate(dats1000)
letters1000 = np.concatenate(lets1000)
sizes1000 = np.concatenate(nums1000)

# Names---------------------------------------------------------------------
# names = ['EnKF 50', 'EnKF 100', 'EnKF 250', 'EnKF 500', 'EnKF 1000', 'EnKF 2000',
#          'NS-EnKF 50', 'NS-EnKF 100', 'NS-EnKF 250', 'NS-EnKF 500', 'NS-EnKF 1000', 'NS-EnKF 2000',
#          'Dam 0.5 50', 'Dam 0.5 100', 'Dam 0.5 250', 'Dam 0.5 500', 'Dam 0.5 1000', 'Dam 0.5 2000',
#          'LEnKF 50', 'LEnKF 100', 'LEnKF 250', 'LEnKF 500', 'LEnKF 1000', 'LEnKF 2000',
#          'Dual EnKF 50', 'Dual EnKF 100', 'Dual EnKF 250', 'Dual EnKF 500', 'Dual EnKF 1000', 'Dual EnKF 2000',
#          'Dam 0.3 50', 'Dam 0.3 100', 'Dam 0.3 250', 'Dam 0.3 500', 'Dam 0.3 1000', 'Dam 0.3 2000',
#          'Dam 0.1 50', 'Dam 0.1 100', 'Dam 0.1 250', 'Dam 0.1 500', 'Dam 0.1 1000', 'Dam 0.1 2000',
#          'NS-EnKF2 50', 'NS-EnKF2 100', 'NS-EnKF2 250', 'NS-EnKF2 500', 'NS-EnKF2 1000', 'NS-EnKF2 2000',
#          'NS-EnKF3 50', 'NS-EnKF3 100', 'NS-EnKF3 250', 'NS-EnKF3 500', 'NS-EnKF3 1000', 'NS-EnKF3 2000',
#          'Hyb-EnKF 50', 'Hyb-EnKF 100', 'Hyb-EnKF 250', 'Hyb-EnKF 500', 'Hyb-EnKF 1000', 'Hyb-EnKF 2000',
#          'Dam 0.2 50', 'Dam 0.2 100', 'Dam 0.2 250', 'Dam 0.2 500', 'Dam 0.2 1000', 'Dam 0.2 2000',
#          'IEnKF1 50', 'IEnKF1 100', 'IEnKF1 250', 'IEnKF1 500', 'IEnKF1 1000', 'IEnKF1 2000',
#          'IEnKF2 50', 'IEnKF2 100', 'IEnKF2 250', 'IEnKF2 500', 'IEnKF2 1000', 'IEnKF2 2000',
#          'NIEnKF 50', 'NIEnKF 100', 'NIEnKF 250', 'NIEnKF 500', 'NIEnKF 1000', 'NIEnKF 2000',
#          'NIEnKF2 50', 'NIEnKF2 100', 'NIEnKF2 250', 'NIEnKF2 500', 'NIEnKF2 1000', 'NIEnKF2 2000',]
names = [r'EnKF',r'EnKF',r'EnKF',r'EnKF',r'EnKF',r'EnKF',
         r'Dam0.1',r'Dam0.1',r'Dam0.1',r'Dam0.1',r'Dam0.1',r'Dam0.1',
         r'NS-EnKF3',r'NS-EnKF3',r'NS-EnKF3',r'NS-EnKF3',r'NS-EnKF3',r'NS-EnKF3',
         r'DualEnKF',r'DualEnKF',r'DualEnKF2',r'DualEnKF0',r'DualEnKF',r'DualEnKF',
         r'Hyb-EnKF',r'Hyb-EnKF',r'Hyb-EnKF',r'Hyb-EnKF',r'Hyb-EnKF',r'Hyb-EnKF',
         r'LEnKF',r'LEnKF',r'LEnKF2',r'LEnKF',r'LEnKF',r'LEnKF',
         r'NIEnKF4',r'NIEnKF4',r'NIEnKF4',r'NIEnKF4',r'NIEnKF4',r'NIEnKF4',
         # Bis hier: 1000er
         r'NS-EnKF',r'NS-EnKF',r'NS-EnKF',r'NS-EnKF',r'NS-EnKF',r'NS-EnKF',
         r'Dam0.5',r'Dam0.5',r'Dam0.5',r'Dam0.50',r'Dam0.50',r'Dam0.5',
         r'Dam0.3',r'Dam0.3',r'Dam0.3',r'Dam0.3',r'Dam0.3',r'Dam0.3',
         r'NS-EnKF2',r'NS-EnKF2',r'NS-EnKF2',r'NS-EnKF2',r'NS-EnKF2',r'NS-EnKF2',
         r'Dam0.2',r'Dam0.2',r'Dam0.2',r'Dam0.2',r'Dam0.2',r'Dam0.2',
         r'IEnKF1',r'IEnKF1',r'IEnKF1',r'IEnKF1',r'IEnKF1',r'IEnKF1',
         r'IEnKF2',r'IEnKF2',r'IEnKF2',r'IEnKF2',r'IEnKF2',r'IEnKF2',
         r'NIEnKF',r'NIEnKF',r'NIEnKF',r'NIEnKF',r'NIEnKF',r'NIEnKF',
         r'NIEnKF2',r'NIEnKF2',r'NIEnKF2',r'NIEnKF2',r'NIEnKF2',r'NIEnKF2',
         r'NIEnKF3',r'NIEnKF3',r'NIEnKF3',r'NIEnKF3',r'NIEnKF3',r'NIEnKF3',]

names_methods = ['EnKF', 'Dam0.1', 'NS-EnKF3', 'DualEnKF', 'Hyb-EnKF', 
                 'LEnKF',  'NIEnKF4'               # Bis hier: 1000er
                 'NS-EnKF', 'Dam0.5', 
                 'Dam0.3', 'NS-EnKF2', 
                 'Dam0.2', 'IEnKF1', 'IEnKF2', 'NIEnKF', 'NIEnKF2',
                 'NIEnKF3',]


## Iterative hinzufuegen
names1000 = [r'EnKF',r'EnKF',r'EnKF',r'EnKF',r'EnKF',r'EnKF',
             r'Damped',r'Damped',r'Damped',r'Damped',r'Damped',r'Damped',
             r'NS-EnKF',r'NS-EnKF',r'NS-EnKF',r'NS-EnKF',r'NS-EnKF',r'NS-EnKF',
             r'DualEnKF',r'DualEnKF',r'DualEnKF',r'DualEnKF',r'DualEnKF',r'DualEnKF',
             r'Hyb-EnKF',r'Hyb-EnKF',r'Hyb-EnKF',r'Hyb-EnKF',r'Hyb-EnKF',r'Hyb-EnKF',
             r'LEnKF',r'LEnKF',r'LEnKF',r'LEnKF',r'LEnKF',r'LEnKF',
             r'IEnKF',r'IEnKF',r'IEnKF',r'IEnKF',r'IEnKF',r'IEnKF',]

longnames1000 = [r'EnKF',r'EnKF',r'EnKF',r'EnKF',r'EnKF',r'EnKF',
             r'Damped EnKF',r'Damped EnKF',r'Damped EnKF',r'Damped EnKF',r'Damped EnKF',r'Damped EnKF',
             r'Normal Score EnKF',r'Normal Score EnKF',r'Normal Score EnKF',r'Normal Score EnKF',r'Normal Score EnKF',r'Normal Score EnKF',
             r'Dual EnKF',r'Dual EnKF',r'Dual EnKF',r'Dual EnKF',r'Dual EnKF',r'Dual EnKF',
             r'Hybrid EnKF',r'Hybrid EnKF',r'Hybrid EnKF',r'Hybrid EnKF',r'Hybrid EnKF',r'Hybrid EnKF',
             r'Local EnKF',r'Local EnKF',r'Local EnKF',r'Local EnKF',r'Local EnKF',r'Local EnKF',
             r'Iterative EnKF',r'Iterative EnKF',r'Iterative EnKF',r'Iterative EnKF',r'Iterative EnKF',r'Iterative EnKF',]

names_methods1000 = ['EnKF','Damped','NS-EnKF','DualEnKF','Hyb-EnKF','LEnKF','IEnKF']

longnames_methods1000 = ['EnKF','Damped EnKF','Normal Score EnKF','Dual EnKF','Hybrid EnKF','Local EnKF','Iterative EnKF']
