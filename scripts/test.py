#!/usr/bin/python


import os
import numpy as np
import mypackage.plot.plot_functions as pltfct
from mypackage.plot import myplots
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm




letter = 'f'



kz_mean = pltfct.my_vtk_to_numpy('/home/jk125262/shematOutputDir_Cluster/wave_output/2015_03_19/2015_03_19_' + letter + '/enkf_output','assim_variables_E1_aft_' + str(iobs).zfill(4) + '.vtk','kz_res')



resid = [None for i in range(50)]
for iobs in range(1,51,1):
    
    res = pltfct.my_vtk_to_numpy('/home/jk125262/shematOutputDir_Cluster/wave_output/2015_03_19/2015_03_19_' + letter + '/enkf_output','assim_variables_E1_aft_' + str(iobs).zfill(4) + '.vtk','kz_res')
    
    quadsum = 0
    for i in range(1,32,1):
        for j in range(1,32,1):
            quadsum = quadsum + res[i-1,j-1]*res[i-1,j-1]

    resid[iobs-1] = np.sqrt(quadsum/(31*31))

print(resid)
print(np.any(res < 0))

n_pres = 4
partresid = [[None for i in range(50)] for i_pres in range(n_pres)] 
i_in = [range(1,16,1),range(16,32,1),range(1,16,1),range(16,32,1)]
j_in = [range(1,16,1),range(1,16,1),range(16,32,1),range(16,32,1)]

for i_pres in range(n_pres):
    for iobs in range(1,51,1):
    
        res = pltfct.my_vtk_to_numpy('/home/jk125262/shematOutputDir_Cluster/wave_output/2015_03_19/2015_03_19_' + letter + '/enkf_output','assim_variables_E1_aft_' + str(iobs).zfill(4) + '.vtk','kz_res')
    
        quadsum = 0
        for i in i_in[i_pres]:
            for j in j_in[i_pres]:
                quadsum = quadsum + res[i-1,j-1]*res[i-1,j-1]

        partresid[i_pres][iobs-1] = np.sqrt(quadsum/(len(i_in[i_pres])*len(j_in[i_pres])))

    # print(partresid[i_pres])    




this_cmap = cm.get_cmap('jet')
col_norm = colors.normalize(0,n_pres)

mycolors = ['red','green','blue','brown']

plt.plot(resid, c = 'black')
for i_pres in range(n_pres):
    plt.plot(partresid[i_pres], c = mycolors[i_pres])
plt.show()





os.chdir('/home/jk125262/PythonDir_Cluster')



