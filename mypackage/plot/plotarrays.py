#!/usr/bin/python

import os
import numpy as np

# Paths
python_dir = os.environ['HOME']+'/PythonDir'

num_methods = 7
num_jobs = num_methods*3

num_methods1000 = 8
num_jobs1000 = num_methods1000*4

# Names
# --------------------------------------------------------------------
names_methods = ['EnKF',
                     'Damped',
                     'NS-EnKF',
                     'DualEnKF',
                     'Hyb-EnKF',
                     'LEnKF',
                     'IEnKF',
                     'PP-EnKF']
longnames_methods = ['EnKF',
                         'Damped EnKF',
                         'Normal Score EnKF',
                         'Dual EnKF',
                         'Hybrid EnKF',
                         'Local EnKF',
                         'Iterative EnKF',
                         'Pilot-Point EnKF']


# Methods
# --------------------------------------------------------------------
# method_dats: Date of the output directory
# method_lets: Letter of first output directory
# method_nums: Number of output directories
# method_obss: Number of observation intervals
# method1000_*: Jobs with 1000 synthetic experiments
# method*_wavebc_*: Jobs with WAVEBC no-flow boundary condition

# Classical EnKF
normal_dats = ['2015_06_10','2015_12_17','2015_06_11',
               '2015_06_11','2015_06_16','2015_06_16','2015_06_17']
normal_lets = ['b','dkl','b','cx','cx','gt','b']
normal_nums = [100,100,100,100,100,100,100]
normal_obss = [100 for i in range(6)]

normal1000_dats = ['2015_11_26','2015_12_17','2015_11_26','2015_11_26']
normal1000_lets = ['b','mhf','aln','bxz']
normal1000_nums = [1000,1000,1000,1000]
normal1000_obss = [100 for i in range(4)]

# 500, 1000, 2000
normal_wavebc_dats = ['2016_07_22','2016_07_22','2016_07_22']
normal_wavebc_lets = ['b','aln','bxz']
normal_wavebc_nums = [100,100,100]
normal_wavebc_obss = [100 for i in range(3)]

# 50, 70, 100, 250
normal1000_wavebc_dats = ['2016_03_24','2016_03_24','2016_03_24','2016_03_24']
normal1000_wavebc_lets = ['b','aln','bxz','dkl']
normal1000_wavebc_nums = [1000,1000,1000,1000]
normal1000_wavebc_obss = [100 for i in range(4)]

# Damping
damping01_dats = ['2015_07_16','2015_12_17','2015_07_16',
                  '2015_07_16','2015_07_17','2015_07_17','2015_07_17']
damping01_lets = ['kp','ewx','ol','sh','kp','ol','sh']
damping01_nums = [100,100,100,100,100,100,100]
damping01_obss = [100 for i in range(6)]

damping1000_dats = ['2015_11_27','2015_12_17','2015_11_27','2015_11_27']
damping1000_lets = ['b','ntr','aln','bxz']
damping1000_nums = [1000,1000,1000,1000]
damping1000_obss = [100 for i in range(4)]

damping_wavebc_dats = ['2016_07_22','2016_07_22','2016_07_22']
damping_wavebc_lets = ['ewx','gjj','hvv']
damping_wavebc_nums = [100,100,100]
damping_wavebc_obss = [100 for i in range(3)]

damping1000_wavebc_dats = ['2016_04_01','2016_04_01','2016_04_01','2016_04_01']
damping1000_wavebc_lets = ['b','aln','bxz','dkl']
damping1000_wavebc_nums = [1000,1000,1000,1000]
damping1000_wavebc_obss = [100 for i in range(4)]

# Normal Score
normalscoreverynew_dats = ['2015_10_01','2015_12_17','2015_10_01',
                           '2015_10_01','2015_10_01','2015_10_01','2015_10_01']
normalscoreverynew_lets = ['b','gjj','cx','gt','kp','ol','sh']
normalscoreverynew_nums = [100,100,100,100,100,100,34]
normalscoreverynew_obss = [100 for i in range(6)]

normalscore1000_dats = ['2015_12_05','2015_12_17','2015_12_05','2015_12_05']
normalscore1000_lets = ['b','pgd','aln','bxz']
normalscore1000_nums = [1000,1000,1000,1000]
normalscore1000_obss = [100 for i in range(4)]

normalscore_wavebc_dats = ['2016_07_22','2016_07_22','2016_07_22']
normalscore_wavebc_lets = ['kut','mhf','ntr']
normalscore_wavebc_nums = [100,100,100]
normalscore_wavebc_obss = [100 for i in range(3)]

normalscore1000_wavebc_dats = ['2016_06_15','2016_06_15','2016_06_15','2016_06_15']
normalscore1000_wavebc_lets = ['b','aln','bxz','dkl']
normalscore1000_wavebc_nums = [1000,1000,1000,1000]
normalscore1000_wavebc_obss = [100 for i in range(4)]

# Dual 
dual_dats = ['2015_07_15','2015_12_17','2015_07_15',
             '2015_07_15','2015_07_15','2015_07_15','2015_07_15']
dual_lets = ['b','hvv','cx','gt','kp','ol','sh']
dual_nums = [100,100,100,100,100,100,100]
dual_obss = [100 for i in range(6)]

dual1000_dats = ['2015_12_05','2015_12_17','2015_12_05','2015_12_05']
dual1000_lets = ['dkl','qsp','ewx','gjj']
dual1000_nums = [1000,1000,1000,1000]
dual1000_obss = [100 for i in range(4)]

dual_wavebc_dats = ['2016_07_21','2016_07_21','2016_07_21']
dual_wavebc_lets = ['b','aln','bxz']
dual_wavebc_nums = [100,100,100]
dual_wavebc_obss = [100 for i in range(3)]

dual1000_wavebc_dats = ['2016_07_06','2016_07_06','2016_07_06','2016_07_06']
dual1000_wavebc_lets = ['b','aln','bxz','dkl']
dual1000_wavebc_nums = [1000,1000,1000,1000]
dual1000_wavebc_obss = [100 for i in range(4)]

# Hybrid
hybrid_dats = ['2015_10_02','2015_12_17','2015_10_02',
               '2015_10_02','2015_10_02','2015_10_02','2015_10_02']
hybrid_lets = ['b','jih','cx','gt','kp','ol','sh']
hybrid_nums = [100,100,100,100,100,100,100]
hybrid_obss = [100 for i in range(6)]

hybrid1000_dats = ['2015_12_15','2015_12_17','2015_12_15','2015_12_15']
hybrid1000_lets = ['b','sfb','aln','bxz']
hybrid1000_nums = [1000,1000,1000,1000]
hybrid1000_obss = [100 for i in range(4)]

hybrid_wavebc_dats = ['2016_07_21','2016_07_21','2016_07_21']
hybrid_wavebc_lets = ['ewx','gjj','hvv']
hybrid_wavebc_nums = [100,100,100]
hybrid_wavebc_obss = [100 for i in range(3)]

hybrid1000_wavebc_dats = ['2016_07_06','2016_07_06','2016_07_06','2016_07_06']
hybrid1000_wavebc_lets = ['ewx','gjj','hvv','jih']
hybrid1000_wavebc_nums = [1000,1000,1000,1000]
hybrid1000_wavebc_obss = [100 for i in range(4)]

# Localisation
localisation_dats = ['2015_06_23','2015_12_17','2015_06_23',
                     '2015_06_23','2015_06_24','2015_06_24','2015_06_24']
localisation_lets = ['b','kut','cx','gt','b','cx','gt']
localisation_nums = [100,100,100,100,100,100,100]
localisation_obss = [100 for i in range(6)]

localisation1000_dats = ['2015_12_18','2015_12_17','2015_12_18','2015_12_18']
localisation1000_lets = ['b','trn','aln','bxz']
localisation1000_nums = [1000,1000,1000,1000]
localisation1000_obss = [100 for i in range(4)]

localisation_wavebc_dats = ['2016_07_21','2016_07_21','2016_07_21']
localisation_wavebc_lets = ['kut','mhf','ntr']
localisation_wavebc_nums = [100,100,100]
localisation_wavebc_obss = [100 for i in range(3)]

localisation1000_wavebc_dats = ['2016_07_07','2016_07_07','2016_07_07','2016_07_07']
localisation1000_wavebc_lets = ['kut','mhf','ntr','pgd']
localisation1000_wavebc_nums = [1000,1000,1000,1000]
localisation1000_wavebc_obss = [100 for i in range(4)]

# Iterative
newiterative4_dats = ['2015_12_11','2016_02_09','2015_12_11',
                      '2015_12_11','2015_12_11','2015_12_11','2015_12_11']
newiterative4_lets = ['b','b','aln','bxz','dkl','ewx','gjj']
newiterative4_nums = [99,100,88,22,16,8,4]
newiterative4_obss = [5050 for i in range(6)]

iterative1000_dats = ['2016_01_07','2016_01_14','2016_01_21','2016_01_28']
iterative1000_lets = ['b','b','b','b']
iterative1000_nums = [1000,1000,1000,1000]
iterative1000_obss = [5050 for i in range(4)]

iterative_wavebc_dats = ['2016_08_12','2016_08_15','2016_08_15']
iterative_wavebc_lets = ['b','b','cx']
iterative_wavebc_nums = [100,100,100]
iterative_wavebc_obss = [5050 for i in range(3)]

iterative1000_wavebc_dats = ['2016_07_27','2016_07_27','2016_07_28','2016_07_29']
iterative1000_wavebc_lets = ['b','aln','b','b']
iterative1000_wavebc_nums = [1000,1000,1000,1000]
iterative1000_wavebc_obss = [5050 for i in range(4)]

# Pilot Point
pilot1000_wavebc_dats = ['2017_09_22','2017_09_22','2017_09_22','2017_09_22']
pilot1000_wavebc_lets = ['b','aln','bxz','dkl']
pilot1000_wavebc_nums = [1000,1000,1000,1000]
pilot1000_wavebc_obss = [100 for i in range(4)]

# Collecting information
dats = np.array([normal_dats, damping01_dats, normalscoreverynew_dats, dual_dats, hybrid_dats, 
                     localisation_dats,newiterative4_dats])
lets = np.array([normal_lets, damping01_lets, normalscoreverynew_lets, dual_lets, hybrid_lets, 
                     localisation_lets,newiterative4_lets])
nums = np.array([normal_nums, damping01_nums, normalscoreverynew_nums, dual_nums, hybrid_nums, 
                     localisation_nums,newiterative4_nums])
num_obss = np.array([normal_obss,damping01_obss,normalscoreverynew_obss, dual_obss, hybrid_obss,
                         localisation_obss,newiterative4_obss])

dats1000 = [normal1000_dats,damping1000_dats,normalscore1000_dats,dual1000_dats,hybrid1000_dats,
            localisation1000_dats, iterative1000_dats]
lets1000 = [normal1000_lets,damping1000_lets,normalscore1000_lets,dual1000_lets,hybrid1000_lets,
            localisation1000_lets, iterative1000_lets]
nums1000 = [normal1000_nums,damping1000_nums,normalscore1000_nums,dual1000_nums,hybrid1000_nums,
            localisation1000_nums, iterative1000_nums]
num_obss1000 = [normal1000_obss,damping1000_obss,normalscore1000_obss,dual1000_obss,hybrid1000_obss,
                    localisation1000_obss,iterative1000_obss]

dats_wavebc = [normal_wavebc_dats,damping_wavebc_dats,
                       normalscore_wavebc_dats,dual_wavebc_dats,
                       hybrid_wavebc_dats,localisation_wavebc_dats, iterative_wavebc_dats]
lets_wavebc = [normal_wavebc_lets,damping_wavebc_lets,
                       normalscore_wavebc_lets,dual_wavebc_lets,
                       hybrid_wavebc_lets,localisation_wavebc_lets, iterative_wavebc_lets]
nums_wavebc = [normal_wavebc_nums,damping_wavebc_nums,
                       normalscore_wavebc_nums,dual_wavebc_nums,
                       hybrid_wavebc_nums,localisation_wavebc_nums, iterative_wavebc_nums]

dats1000_wavebc = [normal1000_wavebc_dats,damping1000_wavebc_dats,
                       normalscore1000_wavebc_dats,dual1000_wavebc_dats,
                       hybrid1000_wavebc_dats,localisation1000_wavebc_dats, iterative1000_wavebc_dats,
                       pilot1000_wavebc_dats]
lets1000_wavebc = [normal1000_wavebc_lets,damping1000_wavebc_lets,
                       normalscore1000_wavebc_lets,dual1000_wavebc_lets,
                       hybrid1000_wavebc_lets,localisation1000_wavebc_lets, iterative1000_wavebc_lets,
                       pilot1000_wavebc_lets]
nums1000_wavebc = [normal1000_wavebc_nums,damping1000_wavebc_nums,
                       normalscore1000_wavebc_nums,dual1000_wavebc_nums,
                       hybrid1000_wavebc_nums,localisation1000_wavebc_nums, iterative1000_wavebc_nums,
                       pilot1000_wavebc_nums]

# Flat arrays
dates = np.concatenate(dats)    
letters = np.concatenate(lets)  
sizes = np.concatenate(nums)    

dates_wavebc = np.concatenate(dats_wavebc)    
letters_wavebc = np.concatenate(lets_wavebc)  
sizes_wavebc = np.concatenate(nums_wavebc)    

dates1000 = np.concatenate(dats1000)
letters1000 = np.concatenate(lets1000)
sizes1000 = np.concatenate(nums1000)

dates1000_wavebc = np.concatenate(dats1000_wavebc)
letters1000_wavebc = np.concatenate(lets1000_wavebc)
sizes1000_wavebc = np.concatenate(nums1000_wavebc)



# Other methods
# --------------------------------------------------------------------
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

