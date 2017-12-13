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
    100:'EnKF',
    101:'EnKF',
    102:'EnKF',
    103:'EnKF',
    104:'EnKF',
    105:'EnKF',
    106:'EnKF',
    107:'EnKF',
    108:'EnKF',
    112:'Damped',
    113:'Damped',
    123:'NS-EnKF',
    133:'DualEnKF',
    141:'Hyb-EnKF',
    142:'Hyb-EnKF',
    143:'Hyb-EnKF',
    144:'Hyb-EnKF',
    145:'Hyb-EnKF',
    151:'LEnKF',
    152:'LEnKF',
    153:'LEnKF',
    154:'LEnKF',
    155:'LEnKF',
    163:'IEnKF',
    }
longnames_methods = {
    0:'EnKF',
    1:'Damped EnKF',
    2:'Normal Score EnKF',
    3:'Dual EnKF',
    4:'Hybrid EnKF',
    5:'Local EnKF',
    6:'Iterative EnKF',
    7:'Pilot Point EnKF',
    100:'EnKF: Mini obsvar',
    101:'EnKF: Low obsvar',
    102:'EnKF: High obsvar',
    103:'EnKF: Huge obsvar',
    104:'EnKF: Mega obsvar',
    105:'EnKF: Giga obsvar',
    106:'EnKF: Exa obsvar',
    107:'EnKF: Peta obsvar',
    108:'EnKF: Huge obsvar, no init',
    112:'Damped: 0.5',
    113:'Damped: Huge obsvar',
    123:'NS-EnKF: Huge obsvar',
    133:'DualEnKF: Huge obsvar',
    141:'Hyb-EnKF: 0.25',
    142:'Hyb-EnKF: 0.75',
    143:'Hyb-EnKF: Huge obsvar',
    144:'Hyb-EnKF: 0.25 Huge obsvar',
    145:'Hyb-EnKF: 0.75 Huge obsvar',
    151:'LEnKF: 75m',
    152:'LEnKF: 300m',
    153:'LEnKF: Huge obsvar',
    154:'LEnKF: 75m Huge obsvar',
    155:'LEnKF: 300m Huge obsvar',
    163:'IEnKF: Huge obsvar',
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
            },
        },
    'wavewell':{
        1000:{
            50:  [1,0],
            70:  [1,0],
            100: [1,0],
            250: [1,0],
            },
        100:{
            500: [1,0],
            1000:[1,0],
            2000:[1,0],
            },
        },
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
    'wavewell':{
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

normal_wavebc_dats = {500:'2016_07_22',1000:'2016_07_22',2000:'2016_07_22'}
normal_wavebc_lets = {500:'b',1000:'aln',2000:'bxz'}
normal_wavebc_nums = {500:100,1000:100,2000:100}
normal_wavebc_obss = {500:100,1000:100,2000:100}

normal1000_wavebc_dats = {50:'2016_03_24',70:'2016_03_24',100:'2016_03_24',250:'2016_03_24'}
normal1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
normal1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
normal1000_wavebc_obss = {50:100,70:100,100:100,250:100}

normal_wavewell_dats = {500:'2017_12_10',1000:'2017_12_10',2000:'2017_12_10'}
normal_wavewell_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
normal_wavewell_nums = {500:100,1000:100,2000:100}
normal_wavewell_obss = {500:100,1000:100,2000:100}

normal1000_wavewell_dats = {50:'2017_12_10',70:'2017_12_10',100:'2017_12_10',250:'2017_12_10'}
normal1000_wavewell_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
normal1000_wavewell_nums = {50:1000,70:1000,100:1000,250:1000}
normal1000_wavewell_obss = {50:100,70:100,100:100,250:100}

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

damping_wavewell_dats = {500:'2017_12_09',1000:'2017_12_09',2000:'2017_12_09'}
damping_wavewell_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
damping_wavewell_nums = {500:100,1000:100,2000:100}
damping_wavewell_obss = {500:100,1000:100,2000:100}

damping1000_wavewell_dats = {50:'2017_12_09',70:'2017_12_09',100:'2017_12_09',250:'2017_12_09'}
damping1000_wavewell_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
damping1000_wavewell_nums = {50:1000,70:1000,100:1000,250:1000}
damping1000_wavewell_obss = {50:100,70:100,100:100,250:100}

dampinghalf_wavewell_dats = {500:'2017_12_12',1000:'2017_12_12',2000:'2017_12_12'}
dampinghalf_wavewell_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
dampinghalf_wavewell_nums = {500:100,1000:100,2000:100}
dampinghalf_wavewell_obss = {500:100,1000:100,2000:100}

dampinghalf1000_wavewell_dats = {50:'2017_12_12',70:'2017_12_12',100:'2017_12_12',250:'2017_12_12'}
dampinghalf1000_wavewell_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
dampinghalf1000_wavewell_nums = {50:1000,70:1000,100:1000,250:1000}
dampinghalf1000_wavewell_obss = {50:100,70:100,100:100,250:100}

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

normalscore_wavewell_dats = {500:'2017_12_08',1000:'2017_12_08',2000:'2017_12_08'}
normalscore_wavewell_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
normalscore_wavewell_nums = {500:100,1000:100,2000:100}
normalscore_wavewell_obss = {500:100,1000:100,2000:100}

normalscore1000_wavewell_dats = {50:'2017_12_08',70:'2017_12_08',100:'2017_12_08',250:'2017_12_08'}
normalscore1000_wavewell_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
normalscore1000_wavewell_nums = {50:1000,70:1000,100:1000,250:1000}
normalscore1000_wavewell_obss = {50:100,70:100,100:100,250:100}

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

dual_wavewell_dats = {500:'2017_12_06',1000:'2017_12_06',2000:'2017_12_06'}
dual_wavewell_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
dual_wavewell_nums = {500:100,1000:100,2000:100}
dual_wavewell_obss = {500:100,1000:100,2000:100}

dual1000_wavewell_dats = {50:'2017_12_06',70:'2017_12_06',100:'2017_12_06',250:'2017_12_06'}
dual1000_wavewell_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
dual1000_wavewell_nums = {50:1000,70:1000,100:1000,250:1000}
dual1000_wavewell_obss = {50:100,70:100,100:100,250:100}

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

hybrid_wavewell_dats = {500:'2017_12_05',1000:'2017_12_05',2000:'2017_12_05'}
hybrid_wavewell_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
hybrid_wavewell_nums = {500:100,1000:100,2000:100}
hybrid_wavewell_obss = {500:100,1000:100,2000:100}

hybrid1000_wavewell_dats = {50:'2017_12_05',70:'2017_12_05',100:'2017_12_05',250:'2017_12_05'}
hybrid1000_wavewell_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
hybrid1000_wavewell_nums = {50:1000,70:1000,100:1000,250:1000}
hybrid1000_wavewell_obss = {50:100,70:100,100:100,250:100}

hybridlarge_wavewell_dats = {500:'2017_12_03',1000:'2017_12_03',2000:'2017_12_03'}
hybridlarge_wavewell_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
hybridlarge_wavewell_nums = {500:100,1000:100,2000:100}
hybridlarge_wavewell_obss = {500:100,1000:100,2000:100}

hybridlarge1000_wavewell_dats = {50:'2017_12_03',70:'2017_12_03',100:'2017_12_03',250:'2017_12_03'}
hybridlarge1000_wavewell_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
hybridlarge1000_wavewell_nums = {50:1000,70:1000,100:1000,250:1000}
hybridlarge1000_wavewell_obss = {50:100,70:100,100:100,250:100}

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

localisation_wavewell_dats = {500:'2017_12_07',1000:'2017_12_07',2000:'2017_12_07'}
localisation_wavewell_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
localisation_wavewell_nums = {500:100,1000:100,2000:100}
localisation_wavewell_obss = {500:100,1000:100,2000:100}

localisation1000_wavewell_dats = {50:'2017_12_07',70:'2017_12_07',100:'2017_12_07',250:'2017_12_07'}
localisation1000_wavewell_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
localisation1000_wavewell_nums = {50:1000,70:1000,100:1000,250:1000}
localisation1000_wavewell_obss = {50:100,70:100,100:100,250:100}

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

# Mini Measurement Noise
minimeasnoise_wavebc_dats = {500:'2017_11_14',1000:'2017_11_14',2000:'2017_11_14'}
minimeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
minimeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
minimeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

minimeasnoise1000_wavebc_dats = {50:'2017_11_14',70:'2017_11_14',100:'2017_11_14',250:'2017_11_14'}
minimeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
minimeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
minimeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Low Measurement Noise
lowmeasnoise_wavebc_dats = {500:'2017_11_01',1000:'2017_11_01',2000:'2017_11_01'}
lowmeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
lowmeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
lowmeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

lowmeasnoise1000_wavebc_dats = {50:'2017_11_01',70:'2017_11_01',100:'2017_11_01',250:'2017_11_01'}
lowmeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
lowmeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
lowmeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# High Measurement Noise
highmeasnoise_wavebc_dats = {500:'2017_11_02',1000:'2017_11_02',2000:'2017_11_02'}
highmeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
highmeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
highmeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

highmeasnoise1000_wavebc_dats = {50:'2017_11_02',70:'2017_11_02',100:'2017_11_02',250:'2017_11_02'}
highmeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
highmeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
highmeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Huge Measurement Noise
hugemeasnoise_wavebc_dats = {500:'2017_11_03',1000:'2017_11_03',2000:'2017_11_03'}
hugemeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
hugemeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
hugemeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

hugemeasnoise1000_wavebc_dats = {50:'2017_11_03',70:'2017_11_03',100:'2017_11_03',250:'2017_11_03'}
hugemeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
hugemeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
hugemeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Huge Measurement Noise, no initial boundary condition perturbation
hugemeasnoisenoinit_wavebc_dats = {500:'2017_11_15',1000:'2017_11_15',2000:'2017_11_15'}
hugemeasnoisenoinit_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
hugemeasnoisenoinit_wavebc_nums = {500:100,1000:100,2000:100}
hugemeasnoisenoinit_wavebc_obss = {500:100,1000:100,2000:100}

hugemeasnoisenoinit1000_wavebc_dats = {50:'2017_11_15',70:'2017_11_15',100:'2017_11_15',250:'2017_11_15'}
hugemeasnoisenoinit1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
hugemeasnoisenoinit1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
hugemeasnoisenoinit1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Mega Measurement Noise
megameasnoise_wavebc_dats = {500:'2017_11_04',1000:'2017_11_04',2000:'2017_11_04'}
megameasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
megameasnoise_wavebc_nums = {500:100,1000:100,2000:100}
megameasnoise_wavebc_obss = {500:100,1000:100,2000:100}

megameasnoise1000_wavebc_dats = {50:'2017_11_04',70:'2017_11_04',100:'2017_11_04',250:'2017_11_04'}
megameasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
megameasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
megameasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Giga Measurement Noise
gigameasnoise_wavebc_dats = {500:'2017_11_05',1000:'2017_11_05',2000:'2017_11_05'}
gigameasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
gigameasnoise_wavebc_nums = {500:100,1000:100,2000:100}
gigameasnoise_wavebc_obss = {500:100,1000:100,2000:100}

gigameasnoise1000_wavebc_dats = {50:'2017_11_05',70:'2017_11_05',100:'2017_11_05',250:'2017_11_05'}
gigameasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
gigameasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
gigameasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Exa Measurement Noise
exameasnoise_wavebc_dats = {500:'2017_11_06',1000:'2017_11_06',2000:'2017_11_06'}
exameasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
exameasnoise_wavebc_nums = {500:100,1000:100,2000:100}
exameasnoise_wavebc_obss = {500:100,1000:100,2000:100}

exameasnoise1000_wavebc_dats = {50:'2017_11_06',70:'2017_11_06',100:'2017_11_06',250:'2017_11_06'}
exameasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
exameasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
exameasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# Peta Measurement Noise
petameasnoise_wavebc_dats = {500:'2017_11_07',1000:'2017_11_07',2000:'2017_11_07'}
petameasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
petameasnoise_wavebc_nums = {500:100,1000:100,2000:100}
petameasnoise_wavebc_obss = {500:100,1000:100,2000:100}

petameasnoise1000_wavebc_dats = {50:'2017_11_07',70:'2017_11_07',100:'2017_11_07',250:'2017_11_07'}
petameasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
petameasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
petameasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# dampinghuge Measurement Noise
dampinghugemeasnoise_wavebc_dats = {500:'2017_11_08',1000:'2017_11_08',2000:'2017_11_08'}
dampinghugemeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
dampinghugemeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
dampinghugemeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

dampinghugemeasnoise1000_wavebc_dats = {50:'2017_11_08',70:'2017_11_08',100:'2017_11_08',250:'2017_11_08'}
dampinghugemeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
dampinghugemeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
dampinghugemeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# normalscorehuge Measurement Noise
normalscorehugemeasnoise_wavebc_dats = {500:'2017_11_09',1000:'2017_11_09',2000:'2017_11_09'}
normalscorehugemeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
normalscorehugemeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
normalscorehugemeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

normalscorehugemeasnoise1000_wavebc_dats = {50:'2017_11_09',70:'2017_11_09',100:'2017_11_09',250:'2017_11_09'}
normalscorehugemeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
normalscorehugemeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
normalscorehugemeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# dualhuge Measurement Noise
dualhugemeasnoise_wavebc_dats = {500:'2017_11_10',1000:'2017_11_10',2000:'2017_11_10'}
dualhugemeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
dualhugemeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
dualhugemeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

dualhugemeasnoise1000_wavebc_dats = {50:'2017_11_10',70:'2017_11_10',100:'2017_11_10',250:'2017_11_10'}
dualhugemeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
dualhugemeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
dualhugemeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# hybrid small coefficient
hybridsmall_wavebc_dats = {500:'2017_12_01',1000:'2017_12_01',2000:'2017_12_01'}
hybridsmall_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
hybridsmall_wavebc_nums = {500:100,1000:100,2000:100}
hybridsmall_wavebc_obss = {500:100,1000:100,2000:100}

hybridsmall1000_wavebc_dats = {50:'2017_12_01',70:'2017_12_01',100:'2017_12_01',250:'2017_12_01'}
hybridsmall1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
hybridsmall1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
hybridsmall1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# hybrid large coefficient
hybridlarge_wavebc_dats = {500:'2017_12_02',1000:'2017_12_02',2000:'2017_12_02'}
hybridlarge_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
hybridlarge_wavebc_nums = {500:100,1000:100,2000:100}
hybridlarge_wavebc_obss = {500:100,1000:100,2000:100}

hybridlarge1000_wavebc_dats = {50:'2017_12_02',70:'2017_12_02',100:'2017_12_02',250:'2017_12_02'}
hybridlarge1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
hybridlarge1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
hybridlarge1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# hybridhuge Measurement Noise
hybridhugemeasnoise_wavebc_dats = {500:'2017_11_11',1000:'2017_11_11',2000:'2017_11_11'}
hybridhugemeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
hybridhugemeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
hybridhugemeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

hybridhugemeasnoise1000_wavebc_dats = {50:'2017_11_11',70:'2017_11_11',100:'2017_11_11',250:'2017_11_11'}
hybridhugemeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
hybridhugemeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
hybridhugemeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# hybridhuge Measurement Noise, small coefficient
hybridsmallhugemeasnoise_wavebc_dats = {500:'2017_11_20',1000:'2017_11_20',2000:'2017_11_20'}
hybridsmallhugemeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
hybridsmallhugemeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
hybridsmallhugemeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

hybridsmallhugemeasnoise1000_wavebc_dats = {50:'2017_11_20',70:'2017_11_20',100:'2017_11_20',250:'2017_11_20'}
hybridsmallhugemeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
hybridsmallhugemeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
hybridsmallhugemeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# hybridhuge Measurement Noise, large coefficient
hybridlargehugemeasnoise_wavebc_dats = {500:'2017_11_21',1000:'2017_11_21',2000:'2017_11_21'}
hybridlargehugemeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
hybridlargehugemeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
hybridlargehugemeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

hybridlargehugemeasnoise1000_wavebc_dats = {50:'2017_11_21',70:'2017_11_21',100:'2017_11_21',250:'2017_11_21'}
hybridlargehugemeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
hybridlargehugemeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
hybridlargehugemeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# localisationhuge Measurement Noise
localisationhugemeasnoise_wavebc_dats = {500:'2017_11_12',1000:'2017_11_12',2000:'2017_11_12'}
localisationhugemeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
localisationhugemeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
localisationhugemeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

localisationhugemeasnoise1000_wavebc_dats = {50:'2017_11_12',70:'2017_11_12',100:'2017_11_12',250:'2017_11_12'}
localisationhugemeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
localisationhugemeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
localisationhugemeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# localisation small correlation length
localisationsmallcorrlen_wavebc_dats = {500:'2017_12_05',1000:'2017_12_05',2000:'2017_12_05'}
localisationsmallcorrlen_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
localisationsmallcorrlen_wavebc_nums = {500:100,1000:100,2000:100}
localisationsmallcorrlen_wavebc_obss = {500:100,1000:100,2000:100}

localisationsmallcorrlen1000_wavebc_dats = {50:'2017_12_05',70:'2017_12_05',100:'2017_12_05',250:'2017_12_05'}
localisationsmallcorrlen1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
localisationsmallcorrlen1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
localisationsmallcorrlen1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# localisation large correlation length
localisationlargecorrlen_wavebc_dats = {500:'2017_12_06',1000:'2017_12_06',2000:'2017_12_06'}
localisationlargecorrlen_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
localisationlargecorrlen_wavebc_nums = {500:100,1000:100,2000:100}
localisationlargecorrlen_wavebc_obss = {500:100,1000:100,2000:100}

localisationlargecorrlen1000_wavebc_dats = {50:'2017_12_06',70:'2017_12_06',100:'2017_12_06',250:'2017_12_06'}
localisationlargecorrlen1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
localisationlargecorrlen1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
localisationlargecorrlen1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# localisation small correlation length huge obsvar
localisationsmallcorrhugemeasnoise_wavebc_dats = {500:'2017_12_04',1000:'2017_12_04',2000:'2017_12_04'}
localisationsmallcorrhugemeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
localisationsmallcorrhugemeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
localisationsmallcorrhugemeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

localisationsmallcorrhugemeasnoise1000_wavebc_dats = {50:'2017_12_04',70:'2017_12_04',100:'2017_12_04',250:'2017_12_04'}
localisationsmallcorrhugemeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
localisationsmallcorrhugemeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
localisationsmallcorrhugemeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# localisation large correlation length huge obsvar
localisationlargecorrhugemeasnoise_wavebc_dats = {500:'2017_12_03',1000:'2017_12_03',2000:'2017_12_03'}
localisationlargecorrhugemeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
localisationlargecorrhugemeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
localisationlargecorrhugemeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

localisationlargecorrhugemeasnoise1000_wavebc_dats = {50:'2017_12_03',70:'2017_12_03',100:'2017_12_03',250:'2017_12_03'}
localisationlargecorrhugemeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
localisationlargecorrhugemeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
localisationlargecorrhugemeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}

# iterativehuge Measurement Noise
iterativehugemeasnoise_wavebc_dats = {500:'2017_11_13',1000:'2017_11_13',2000:'2017_11_13'}
iterativehugemeasnoise_wavebc_lets = {500:'ewx',1000:'gjj',2000:'hvv'}
iterativehugemeasnoise_wavebc_nums = {500:100,1000:100,2000:100}
iterativehugemeasnoise_wavebc_obss = {500:100,1000:100,2000:100}

iterativehugemeasnoise1000_wavebc_dats = {50:'2017_11_13',70:'2017_11_13',100:'2017_11_13',250:'2017_11_13'}
iterativehugemeasnoise1000_wavebc_lets = {50:'b',70:'aln',100:'bxz',250:'dkl'}
iterativehugemeasnoise1000_wavebc_nums = {50:1000,70:1000,100:1000,250:1000}
iterativehugemeasnoise1000_wavebc_obss = {50:100,70:100,100:100,250:100}



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
            100:minimeasnoise1000_wavebc_dats,
            101:lowmeasnoise1000_wavebc_dats,
            102:highmeasnoise1000_wavebc_dats,
            103:hugemeasnoise1000_wavebc_dats,
            104:megameasnoise1000_wavebc_dats,
            105:gigameasnoise1000_wavebc_dats,
            106:exameasnoise1000_wavebc_dats,
            107:petameasnoise1000_wavebc_dats,
            108:hugemeasnoisenoinit1000_wavebc_dats,
            113:dampinghugemeasnoise1000_wavebc_dats,
            123:normalscorehugemeasnoise1000_wavebc_dats,
            133:dualhugemeasnoise1000_wavebc_dats,
            141:hybridsmall1000_wavebc_dats,
            142:hybridlarge1000_wavebc_dats,
            143:hybridhugemeasnoise1000_wavebc_dats,
            144:hybridsmallhugemeasnoise1000_wavebc_dats,
            145:hybridlargehugemeasnoise1000_wavebc_dats,
            151:localisationsmallcorrlen1000_wavebc_dats,
            152:localisationlargecorrlen1000_wavebc_dats,
            153:localisationhugemeasnoise1000_wavebc_dats,
            154:localisationsmallcorrhugemeasnoise1000_wavebc_dats,
            155:localisationlargecorrhugemeasnoise1000_wavebc_dats,
            163:iterativehugemeasnoise1000_wavebc_dats,
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
            100:minimeasnoise_wavebc_dats,
            101:lowmeasnoise_wavebc_dats,
            102:highmeasnoise_wavebc_dats,
            103:hugemeasnoise_wavebc_dats,
            104:megameasnoise_wavebc_dats,
            105:gigameasnoise_wavebc_dats,
            106:exameasnoise_wavebc_dats,
            107:petameasnoise_wavebc_dats,
            108:hugemeasnoisenoinit_wavebc_dats,
            113:dampinghugemeasnoise_wavebc_dats,
            123:normalscorehugemeasnoise_wavebc_dats,
            133:dualhugemeasnoise_wavebc_dats,
            141:hybridsmall_wavebc_dats,
            142:hybridlarge_wavebc_dats,
            143:hybridhugemeasnoise_wavebc_dats,
            144:hybridsmallhugemeasnoise_wavebc_dats,
            145:hybridlargehugemeasnoise_wavebc_dats,
            151:localisationsmallcorrlen_wavebc_dats,
            152:localisationlargecorrlen_wavebc_dats,
            153:localisationhugemeasnoise_wavebc_dats,
            154:localisationsmallcorrhugemeasnoise_wavebc_dats,
            155:localisationlargecorrhugemeasnoise_wavebc_dats,
            163:iterativehugemeasnoise_wavebc_dats,
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
        },
    'wavewell':{
        1000: {
            0:normal1000_wavewell_dats,
            1:damping1000_wavewell_dats,
            2:normalscore1000_wavewell_dats,
            3:dual1000_wavewell_dats,
            4:hybrid1000_wavewell_dats,
            5:localisation1000_wavewell_dats,
            112:dampinghalf1000_wavewell_dats,
            142:hybridlarge1000_wavewell_dats,
            },
        100: {
            0:normal_wavewell_dats,
            1:damping_wavewell_dats,
            2:normalscore_wavewell_dats,
            3:dual_wavewell_dats,
            4:hybrid_wavewell_dats,
            5:localisation_wavewell_dats,
            112:dampinghalf_wavewell_dats,
            142:hybridlarge_wavewell_dats,
            },
        },
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
            100:minimeasnoise1000_wavebc_lets,
            101:lowmeasnoise1000_wavebc_lets,
            102:highmeasnoise1000_wavebc_lets,
            103:hugemeasnoise1000_wavebc_lets,
            104:megameasnoise1000_wavebc_lets,
            105:gigameasnoise1000_wavebc_lets,
            106:exameasnoise1000_wavebc_lets,
            107:petameasnoise1000_wavebc_lets,
            108:hugemeasnoisenoinit1000_wavebc_lets,
            113:dampinghugemeasnoise1000_wavebc_lets,
            123:normalscorehugemeasnoise1000_wavebc_lets,
            133:dualhugemeasnoise1000_wavebc_lets,
            141:hybridsmall1000_wavebc_lets,
            142:hybridlarge1000_wavebc_lets,
            143:hybridhugemeasnoise1000_wavebc_lets,
            144:hybridsmallhugemeasnoise1000_wavebc_lets,
            145:hybridlargehugemeasnoise1000_wavebc_lets,
            151:localisationsmallcorrlen1000_wavebc_lets,
            152:localisationlargecorrlen1000_wavebc_lets,
            153:localisationhugemeasnoise1000_wavebc_lets,
            154:localisationsmallcorrhugemeasnoise1000_wavebc_lets,
            155:localisationlargecorrhugemeasnoise1000_wavebc_lets,
            163:iterativehugemeasnoise1000_wavebc_lets,
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
            100:minimeasnoise_wavebc_lets,
            101:lowmeasnoise_wavebc_lets,
            102:highmeasnoise_wavebc_lets,
            103:hugemeasnoise_wavebc_lets,
            104:megameasnoise_wavebc_lets,
            105:gigameasnoise_wavebc_lets,
            106:exameasnoise_wavebc_lets,
            107:petameasnoise_wavebc_lets,
            108:hugemeasnoisenoinit_wavebc_lets,
            113:dampinghugemeasnoise_wavebc_lets,
            123:normalscorehugemeasnoise_wavebc_lets,
            133:dualhugemeasnoise_wavebc_lets,
            141:hybridsmall_wavebc_lets,
            142:hybridlarge_wavebc_lets,
            143:hybridhugemeasnoise_wavebc_lets,
            144:hybridsmallhugemeasnoise_wavebc_lets,
            145:hybridlargehugemeasnoise_wavebc_lets,
            151:localisationsmallcorrlen_wavebc_lets,
            152:localisationlargecorrlen_wavebc_lets,
            153:localisationhugemeasnoise_wavebc_lets,
            154:localisationsmallcorrhugemeasnoise_wavebc_lets,
            155:localisationlargecorrhugemeasnoise_wavebc_lets,
            163:iterativehugemeasnoise_wavebc_lets,
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
        },
    'wavewell':{
        1000: {
            0:normal1000_wavewell_lets,
            1:damping1000_wavewell_lets,
            2:normalscore1000_wavewell_lets,
            3:dual1000_wavewell_lets,
            4:hybrid1000_wavewell_lets,
            5:localisation1000_wavewell_lets,
            112:dampinghalf1000_wavewell_lets,
            142:hybridlarge1000_wavewell_lets,
            },
        100: {
            0:normal_wavewell_lets,
            1:damping_wavewell_lets,
            2:normalscore_wavewell_lets,
            3:dual_wavewell_lets,
            4:hybrid_wavewell_lets,
            5:localisation_wavewell_lets,
            112:dampinghalf_wavewell_lets,
            142:hybridlarge_wavewell_lets,
            },
        },
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
            100:minimeasnoise1000_wavebc_nums,
            101:lowmeasnoise1000_wavebc_nums,
            102:highmeasnoise1000_wavebc_nums,
            103:hugemeasnoise1000_wavebc_nums,
            104:megameasnoise1000_wavebc_nums,
            105:gigameasnoise1000_wavebc_nums,
            106:exameasnoise1000_wavebc_nums,
            107:petameasnoise1000_wavebc_nums,
            108:hugemeasnoisenoinit1000_wavebc_nums,
            113:dampinghugemeasnoise1000_wavebc_nums,
            123:normalscorehugemeasnoise1000_wavebc_nums,
            133:dualhugemeasnoise1000_wavebc_nums,
            141:hybridsmall1000_wavebc_nums,
            142:hybridlarge1000_wavebc_nums,
            143:hybridhugemeasnoise1000_wavebc_nums,
            144:hybridsmallhugemeasnoise1000_wavebc_nums,
            145:hybridlargehugemeasnoise1000_wavebc_nums,
            151:localisationsmallcorrlen1000_wavebc_nums,
            152:localisationlargecorrlen1000_wavebc_nums,
            153:localisationhugemeasnoise1000_wavebc_nums,
            154:localisationsmallcorrhugemeasnoise1000_wavebc_nums,
            155:localisationlargecorrhugemeasnoise1000_wavebc_nums,
            163:iterativehugemeasnoise1000_wavebc_nums,
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
            100:minimeasnoise_wavebc_nums,
            101:lowmeasnoise_wavebc_nums,
            102:highmeasnoise_wavebc_nums,
            103:hugemeasnoise_wavebc_nums,
            104:megameasnoise_wavebc_nums,
            105:gigameasnoise_wavebc_nums,
            106:exameasnoise_wavebc_nums,
            107:petameasnoise_wavebc_nums,
            108:hugemeasnoisenoinit_wavebc_nums,
            113:dampinghugemeasnoise_wavebc_nums,
            123:normalscorehugemeasnoise_wavebc_nums,
            133:dualhugemeasnoise_wavebc_nums,
            141:hybridsmall_wavebc_nums,
            142:hybridlarge_wavebc_nums,
            143:hybridhugemeasnoise_wavebc_nums,
            144:hybridsmallhugemeasnoise_wavebc_nums,
            145:hybridlargehugemeasnoise_wavebc_nums,
            151:localisationsmallcorrlen_wavebc_nums,
            152:localisationlargecorrlen_wavebc_nums,
            153:localisationhugemeasnoise_wavebc_nums,
            154:localisationsmallcorrhugemeasnoise_wavebc_nums,
            155:localisationlargecorrhugemeasnoise_wavebc_nums,
            163:iterativehugemeasnoise_wavebc_nums,
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
        },
    'wavewell':{
        1000: {
            0:normal1000_wavewell_nums,
            1:damping1000_wavewell_nums,
            2:normalscore1000_wavewell_nums,
            3:dual1000_wavewell_nums,
            4:hybrid1000_wavewell_nums,
            5:localisation1000_wavewell_nums,
            112:dampinghalf1000_wavewell_nums,
            142:hybridlarge1000_wavewell_nums,
            },
        100: {
            0:normal_wavewell_nums,
            1:damping_wavewell_nums,
            2:normalscore_wavewell_nums,
            3:dual_wavewell_nums,
            4:hybrid_wavewell_nums,
            5:localisation_wavewell_nums,
            112:dampinghalf_wavewell_nums,
            142:hybridlarge_wavewell_nums,
            },
        },
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
            100:minimeasnoise1000_wavebc_obss,
            101:lowmeasnoise1000_wavebc_obss,
            102:highmeasnoise1000_wavebc_obss,
            103:hugemeasnoise1000_wavebc_obss,
            104:megameasnoise1000_wavebc_obss,
            105:gigameasnoise1000_wavebc_obss,
            106:exameasnoise1000_wavebc_obss,
            107:petameasnoise1000_wavebc_obss,
            108:hugemeasnoisenoinit1000_wavebc_obss,
            113:dampinghugemeasnoise1000_wavebc_obss,
            123:normalscorehugemeasnoise1000_wavebc_obss,
            133:dualhugemeasnoise1000_wavebc_obss,
            141:hybridsmall1000_wavebc_obss,
            142:hybridlarge1000_wavebc_obss,
            143:hybridhugemeasnoise1000_wavebc_obss,
            144:hybridsmallhugemeasnoise1000_wavebc_obss,
            145:hybridlargehugemeasnoise1000_wavebc_obss,
            151:localisationsmallcorrlen1000_wavebc_obss,
            152:localisationlargecorrlen1000_wavebc_obss,
            153:localisationhugemeasnoise1000_wavebc_obss,
            154:localisationsmallcorrhugemeasnoise1000_wavebc_obss,
            155:localisationlargecorrhugemeasnoise1000_wavebc_obss,
            163:iterativehugemeasnoise1000_wavebc_obss,
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
            100:minimeasnoise_wavebc_obss,
            101:lowmeasnoise_wavebc_obss,
            102:highmeasnoise_wavebc_obss,
            103:hugemeasnoise_wavebc_obss,
            105:gigameasnoise_wavebc_obss,
            106:exameasnoise_wavebc_obss,
            107:petameasnoise_wavebc_obss,
            108:hugemeasnoisenoinit_wavebc_obss,
            113:dampinghugemeasnoise_wavebc_obss,
            123:normalscorehugemeasnoise_wavebc_obss,
            133:dualhugemeasnoise_wavebc_obss,
            141:hybridsmall_wavebc_obss,
            142:hybridlarge_wavebc_obss,
            143:hybridhugemeasnoise_wavebc_obss,
            144:hybridsmallhugemeasnoise_wavebc_obss,
            145:hybridlargehugemeasnoise_wavebc_obss,
            151:localisationsmallcorrlen_wavebc_obss,
            152:localisationlargecorrlen_wavebc_obss,
            153:localisationhugemeasnoise_wavebc_obss,
            154:localisationsmallcorrhugemeasnoise_wavebc_obss,
            155:localisationlargecorrhugemeasnoise_wavebc_obss,
            163:iterativehugemeasnoise_wavebc_obss,
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
        },
    'wavewell':{
        1000: {
            0:normal1000_wavewell_obss,
            1:damping1000_wavewell_obss,
            2:normalscore1000_wavewell_obss,
            3:dual1000_wavewell_obss,
            4:hybrid1000_wavewell_obss,
            5:localisation1000_wavewell_obss,
            112:dampinghalf1000_wavewell_obss,
            142:hybridlarge1000_wavewell_obss,
            },
        100: {
            0:normal_wavewell_obss,
            1:damping_wavewell_obss,
            2:normalscore_wavewell_obss,
            3:dual_wavewell_obss,
            4:hybrid_wavewell_obss,
            5:localisation_wavewell_obss,
            112:dampinghalf_wavewell_obss,
            142:hybridlarge_wavewell_obss,
            },
        },
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
