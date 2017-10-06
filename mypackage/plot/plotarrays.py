#!/usr/bin/python

import os
import numpy as np

# Number for calling different methods
# 0: Classical EnKF
# 1: Damped EnKF
# 2: Normal Score EnKF
# 3: Dual EnKF
# 4: Hybrid EnKF
# 5: Local EnKF
# 6: Iterative EnKF
# 7: Pilot Point EnKF

# Paths
python_dir = os.environ['HOME']+'/PythonDir'

num_methods = {
    1000:8,
    100:8,
    }
num_jobs = {
    1000:num_methods[1000]*4,
    100:num_methods[100]*3,
    }

# Names
# --------------------------------------------------------------------
names_methods = {
    0:'EnKF',
    1:'Damped',
    2:'NS-EnKF',
    3:'DualEnKF',
    4:'Hyb-EnKF',
    5:'LEnKF',
    6:'IEnKF',
    7:'PP-EnKF',
    }
longnames_methods = {
    0:'EnKF',
    1:'Damped EnKF',
    2:'Normal Score EnKF',
    3:'Dual EnKF',
    4:'Hybrid EnKF',
    5:'Local EnKF',
    6:'Iterative EnKF',
    7:'Pilot Point EnKF'
    }

# Indices RMSE-sorted, low to high
# --------------------------------------------------------------------
indsorts = {
    'wavebc':{
        1000:{
            50:  [1,6,5,4,3,2,0],
            70:  [1,4,6,5,3,0,2],
            100: [1,4,6,0,3,5,2],
            250: [1,4,3,0,6,2,5],
            },
        100:{
            500: [1,4,6,0,3,2,5],
            1000:[1,4,6,0,3,2,5],
            2000:[1,4,6,0,3,2,5],
            }
        }
    }

# Indices of ensemble sizes
# --------------------------------------------------------------------
indens = {
    'wavebc':{
        1000:{
            50:0,
            70:1,
            100:2,
            250:3,
            },
        100:{
            500:0,
            1000:1,
            2000:2,
            },
        },
    'wave':{
        1000:{
            50:0,
            70:1,
            100:2,
            250:3,
            },
        100:{
            500:0,
            1000:1,
            2000:2,
            },
        },
    }

# Methods
# --------------------------------------------------------------------
# method_dats: Date of the output directory
# method_lets: Letter of first output directory
# method_nums: Number of output directories
# method_obss: Number of observation intervals
# method1000_*: Jobs with 1000 synthetic experiments
# method*_wavebc_*: Jobs with WAVEBC no-flow boundary condition

# Classical EnKF
normal_dats = {50:'2015_06_10',70:'2015_12_17',100:'2015_06_11',
               250:'2015_06_11',500:'2015_06_16',1000:'2015_06_16',2000:'2015_06_17'}
normal_lets = {50:'b',70:'dkl',100:'b',250:'cx',500:'cx',1000:'gt',2000:'b'}
normal_nums = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:100}
normal_obss = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:100}

normal1000_dats = {50:'2015_11_26',70:'2015_12_17',100:'2015_11_26',250:'2015_11_26'}
normal1000_lets = {50:'b',70:'mhf',100:'aln',250:'bxz'}
normal1000_nums = {50:1000,70:1000,100:1000,250:1000}
normal1000_obss = {50:100,70:100,100:100,250:100}

# 500, 1000, 2000
normal_wavebc_dats = {500:'2016_07_22',1000:'2016_07_22',2000:'2016_07_22'}
normal_wavebc_lets = {500:'b',1000:'aln',2000:'bxz'}
normal_wavebc_nums = {500:100,1000:100,2000:100}
normal_wavebc_obss = {500:100,1000:100,2000:100}

# 50, 70, 100, 250
normal1000_wavebc_dats = {50:'2016_03_24',70:'2016_03_24',100:'2016_03_24',250:'2016_03_24'}
normal1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
normal1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
normal1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Damping
damping01_dats = {50:'2015_07_16',70:'2015_12_17',100:'2015_07_16',
                  250:'2015_07_16',500:'2015_07_17',1000:'2015_07_17',2000:'2015_07_17'}
damping01_lets = {50:'kp',70:'ewx',100:'ol',250:'sh',500:'kp',1000:'ol',2000:'sh'}
damping01_nums = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:100}
damping01_obss = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:100}

damping1000_dats = {50:'2015_11_27',70:'2015_12_17',100:'2015_11_27',250:'2015_11_27'}
damping1000_lets = {50:'b',70:'ntr',100:'aln',250:'bxz'}
damping1000_nums = {50:1000,70:1000,100:1000,250:1000}
damping1000_obss = {50:100,70:100,100:100,250:100}

damping_wavebc_dats = {500:'2016_07_22',1000:'2016_07_22',2000:'2016_07_22'}
damping_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
damping_wavebc_nums = {500:100,1000:100,2000:100}
damping_wavebc_obss = {500:100,1000:100,2000:100}

damping1000_wavebc_dats = {50:'2016_04_01',70:'2016_04_01',100:'2016_04_01',250:'2016_04_01'}
damping1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
damping1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
damping1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Normal Score
normalscoreverynew_dats = {50:'2015_10_01',70:'2015_12_17',100:'2015_10_01',
                           250:'2015_10_01',500:'2015_10_01',1000:'2015_10_01',2000:'2015_10_01'}
normalscoreverynew_lets = {50:'b',70:'gjj',100:'cx',250:'gt',500:'kp',1000:'ol',2000:'sh'}
normalscoreverynew_nums = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:34}
normalscoreverynew_obss = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:100}

normalscore1000_dats = {50:'2015_12_05',70:'2015_12_17',100:'2015_12_05',250:'2015_12_05'}
normalscore1000_lets = {50:'b',70:'pgd',100:'aln',250:'bxz'}
normalscore1000_nums = {50:1000,70:1000,100:1000,250:1000}
normalscore1000_obss = {50:100,70:100,100:100,250:100}

normalscore_wavebc_dats = {500:'2016_07_22',1000:'2016_07_22',2000:'2016_07_22'}
normalscore_wavebc_lets = {500:'kut',1000:'mhf',2000:'ntr'}
normalscore_wavebc_nums = {500:100,1000:100,2000:100}
normalscore_wavebc_obss = {500:100,1000:100,2000:100}

normalscore1000_wavebc_dats = {50:'2016_06_15',70:'2016_06_15',100:'2016_06_15',250:'2016_06_15'}
normalscore1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
normalscore1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
normalscore1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Dual
dual_dats = {50:'2015_07_15',70:'2015_12_17',100:'2015_07_15',
             250:'2015_07_15',500:'2015_07_15',1000:'2015_07_15',2000:'2015_07_15'}
dual_lets = {50:'b',70:'hvv',100:'cx',250:'gt',500:'kp',1000:'ol',2000:'sh'}
dual_nums = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:100}
dual_obss = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:100}

dual1000_dats = {50:'2015_12_05',70:'2015_12_17',100:'2015_12_05',250:'2015_12_05'}
dual1000_lets = {50:'dkl',70:'qsp',100:'ewx',250:'gjj'}
dual1000_nums = {50:1000,70:1000,100:1000,250:1000}
dual1000_obss = {50:100,70:100,100:100,250:100}

dual_wavebc_dats = {500:'2016_07_21',1000:'2016_07_21',2000:'2016_07_21'}
dual_wavebc_lets = {500:'b',1000:'aln',2000:'bxz'}
dual_wavebc_nums = {500:100,1000:100,2000:100}
dual_wavebc_obss = {500:100,1000:100,2000:100}

dual1000_wavebc_dats = {50:'2016_07_06',70:'2016_07_06',100:'2016_07_06',250:'2016_07_06'}
dual1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
dual1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
dual1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Hybrid
hybrid_dats = {50:'2015_10_02',70:'2015_12_17',100:'2015_10_02',
               250:'2015_10_02',500:'2015_10_02',1000:'2015_10_02',2000:'2015_10_02'}
hybrid_lets = {50:'b',70:'jih',100:'cx',250:'gt',500:'kp',1000:'ol',2000:'sh'}
hybrid_nums = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:100}
hybrid_obss = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:100}

hybrid1000_dats = {50:'2015_12_15',70:'2015_12_17',100:'2015_12_15',250:'2015_12_15'}
hybrid1000_lets = {50:'b',70:'sfb',100:'aln',250:'bxz'}
hybrid1000_nums = {50:1000,70:1000,100:1000,250:1000}
hybrid1000_obss = {50:100,70:100,100:100,250:100}

hybrid_wavebc_dats = {500:'2016_07_21',1000:'2016_07_21',2000:'2016_07_21'}
hybrid_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
hybrid_wavebc_nums = {500:100,1000:100,2000:100}
hybrid_wavebc_obss = {500:100,1000:100,2000:100}

hybrid1000_wavebc_dats = {50:'2016_07_06',70:'2016_07_06',100:'2016_07_06',250:'2016_07_06'}
hybrid1000_wavebc_lets = {50:'ewx',70:'gjj',100:'hvv',250:'jih'}
hybrid1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
hybrid1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Localisation
localisation_dats = {50:'2015_06_23',70:'2015_12_17',100:'2015_06_23',
                     250:'2015_06_23',500:'2015_06_24',1000:'2015_06_24',2000:'2015_06_24'}
localisation_lets = {50:'b',70:'kut',100:'cx',250:'gt',500:'b',1000:'cx',2000:'gt'}
localisation_nums = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:100}
localisation_obss = {50:100,70:100,100:100,250:100,500:100,1000:100,2000:100}

localisation1000_dats = {50:'2015_12_18',70:'2015_12_17',100:'2015_12_18',250:'2015_12_18'}
localisation1000_lets = {50:'b',70:'trn',100:'aln',250:'bxz'}
localisation1000_nums = {50:1000,70:1000,100:1000,250:1000}
localisation1000_obss = {50:100,70:100,100:100,250:100}

localisation_wavebc_dats = {500:'2016_07_21',1000:'2016_07_21',2000:'2016_07_21'}
localisation_wavebc_lets = {500:'kut',1000:'mhf',2000:'ntr'}
localisation_wavebc_nums = {500:100,1000:100,2000:100}
localisation_wavebc_obss = {500:100,1000:100,2000:100}

localisation1000_wavebc_dats = {50:'2016_07_07',70:'2016_07_07',100:'2016_07_07',250:'2016_07_07'}
localisation1000_wavebc_lets = {50:'kut',70:'mhf',100:'ntr',250:'pgd'}
localisation1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
localisation1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Iterative
newiterative4_dats = {50:'2015_12_11',70:'2016_02_09',100:'2015_12_11',
                      250:'2015_12_11',500:'2015_12_11',1000:'2015_12_11',2000:'2015_12_11'}
newiterative4_lets = {50:'b',70:'b',100:'aln',250:'bxz',500:'dkl',1000:'ewx',2000:'gjj'}
newiterative4_nums = {50:99,70:100,100:88,250:22,500:16,1000:8,2000:4}
newiterative4_obss = {50:5050,70:5050,100:5050,250:5050,500:5050,1000:5050,2000:5050}

iterative1000_dats = {50:'2016_01_07',70:'2016_01_14',100:'2016_01_21',250:'2016_01_28'}
iterative1000_lets = {50:'b',70:'b',100:'b',250:'b'}
iterative1000_nums = {50:1000,70:1000,100:1000,250:1000}
iterative1000_obss = {50:5050,70:5050,100:5050,250:5050}

iterative_wavebc_dats = {500:'2016_08_12',1000:'2016_08_15',2000:'2016_08_15'}
iterative_wavebc_lets = {500:'b',1000:'b',2000:'cx'}
iterative_wavebc_nums = {500:100,1000:100,2000:100}
iterative_wavebc_obss = {500:5050,1000:5050,2000:5050}

iterative1000_wavebc_dats = {50:'2016_07_27',70:'2016_07_27',100:'2016_07_28',250:'2016_07_29'}
iterative1000_wavebc_lets = {50:'b',70:'aln',100:'b',250:'b'}
iterative1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
iterative1000_wavebc_obss = {50:5050,70:100,100:100,250:100}

# Pilot Point
pilot_wavebc_dats = {500:'2017_09_22',1000:'2017_09_22',2000:'2017_09_22'}
pilot_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
pilot_wavebc_nums = {500:100,1000:100,2000:100}
pilot_wavebc_obss = {500:100,1000:100,2000:100}

pilot1000_wavebc_dats = {50:'2017_09_22',70:'2017_09_22',100:'2017_09_22',250:'2017_09_22'}
pilot1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
pilot1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
pilot1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Dictionaries
dats = {
    'wavebc': {
        1000: {
            0:normal1000_wavebc_dats,
            1:damping1000_wavebc_dats,
            2:normalscore1000_wavebc_dats,
            3:dual1000_wavebc_dats,
            4:hybrid1000_wavebc_dats,
            5:localisation1000_wavebc_dats,
            6:iterative1000_wavebc_dats,
            7:pilot1000_wavebc_dats,
            },
        100: {
            0:normal_wavebc_dats,
            1:damping_wavebc_dats,
            2:normalscore_wavebc_dats,
            3:dual_wavebc_dats,
            4:hybrid_wavebc_dats,
            5:localisation_wavebc_dats,
            6:iterative_wavebc_dats,
            7:pilot_wavebc_dats,
            },
        },
    'wave': {
        1000: {
            0:normal1000_dats,
            1:damping1000_dats,
            2:normalscore1000_dats,
            3:dual1000_dats,
            4:hybrid1000_dats,
            5:localisation1000_dats,
            6:iterative1000_dats,
            },
        100: {
            0:normal_dats,
            1:damping01_dats,
            2:normalscoreverynew_dats,
            3:dual_dats,
            4:hybrid_dats,
            5:localisation_dats,
            6:newiterative4_dats,
            },
        }
    }
lets = {
    'wavebc': {
        1000: {
            0:normal1000_wavebc_lets,
            1:damping1000_wavebc_lets,
            2:normalscore1000_wavebc_lets,
            3:dual1000_wavebc_lets,
            4:hybrid1000_wavebc_lets,
            5:localisation1000_wavebc_lets,
            6:iterative1000_wavebc_lets,
            7:pilot1000_wavebc_lets,
            },
        100: {
            0:normal_wavebc_lets,
            1:damping_wavebc_lets,
            2:normalscore_wavebc_lets,
            3:dual_wavebc_lets,
            4:hybrid_wavebc_lets,
            5:localisation_wavebc_lets,
            6:iterative_wavebc_lets,
            7:pilot_wavebc_lets,
            },
        },
    'wave': {
        1000: {
            0:normal1000_lets,
            1:damping1000_lets,
            2:normalscore1000_lets,
            3:dual1000_lets,
            4:hybrid1000_lets,
            5:localisation1000_lets,
            6:iterative1000_lets,
            },
        100: {
            0:normal_lets,
            1:damping01_lets,
            2:normalscoreverynew_lets,
            3:dual_lets,
            4:hybrid_lets,
            5:localisation_lets,
            6:newiterative4_lets,
            },
        }
    }
nums = {
    'wavebc': {
        1000: {
            0:normal1000_wavebc_nums,
            1:damping1000_wavebc_nums,
            2:normalscore1000_wavebc_nums,
            3:dual1000_wavebc_nums,
            4:hybrid1000_wavebc_nums,
            5:localisation1000_wavebc_nums,
            6:iterative1000_wavebc_nums,
            7:pilot1000_wavebc_nums,
            },
        100: {
            0:normal_wavebc_nums,
            1:damping_wavebc_nums,
            2:normalscore_wavebc_nums,
            3:dual_wavebc_nums,
            4:hybrid_wavebc_nums,
            5:localisation_wavebc_nums,
            6:iterative_wavebc_nums,
            7:pilot_wavebc_nums,
            },
        },
    'wave': {
        1000: {
            0:normal1000_nums,
            1:damping1000_nums,
            2:normalscore1000_nums,
            3:dual1000_nums,
            4:hybrid1000_nums,
            5:localisation1000_nums,
            6:iterative1000_nums,
            },
        100: {
            0:normal_nums,
            1:damping01_nums,
            2:normalscoreverynew_nums,
            3:dual_nums,
            4:hybrid_nums,
            5:localisation_nums,
            6:newiterative4_nums,
            },
        }
    }

num_obss = {
    'wavebc': {
        1000: {
            0:normal1000_wavebc_obss,
            1:damping1000_wavebc_obss,
            2:normalscore1000_wavebc_obss,
            3:dual1000_wavebc_obss,
            4:hybrid1000_wavebc_obss,
            5:localisation1000_wavebc_obss,
            6:iterative1000_wavebc_obss,
            7:pilot1000_wavebc_obss,
            },
        100: {
            0:normal_wavebc_obss,
            1:damping_wavebc_obss,
            2:normalscore_wavebc_obss,
            3:dual_wavebc_obss,
            4:hybrid_wavebc_obss,
            5:localisation_wavebc_obss,
            6:iterative_wavebc_obss,
            7:pilot_wavebc_obss,
            },
        },
    'wave': {
        1000: {
            0:normal1000_obss,
            1:damping1000_obss,
            2:normalscore1000_obss,
            3:dual1000_obss,
            4:hybrid1000_obss,
            5:localisation1000_obss,
            6:iterative1000_obss,
            },
        100: {
            0:normal_obss,
            1:damping01_obss,
            2:normalscoreverynew_obss,
            3:dual_obss,
            4:hybrid_obss,
            5:localisation_obss,
            6:newiterative4_obss,
            },
        }
    }

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
