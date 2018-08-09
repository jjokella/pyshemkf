import numpy as np
# import matplotlib.pyplot as plt

from pskf.tools.plot import specs as sc
import pskf.scripts.singlecell.arrays as sca
# import pskf.scripts.forward.plot as fp
import pskf.scripts.singlecell.read as scr
import pskf.tools.run.pythonmodule as pm

# Switches
is_read = 1
is_plot = 0
is_save = 0
is_show = 0
is_backup = 0

# Specs
model_name = 'wavereal'
dat = '2018_08_09'

let = 'a'

# Read
if is_read:
    numpy_array, numpy_array_name = scr.read(
        model_name,
        dat,
        let,
    )

    np.save(numpy_array_name, numpy_array)
    print('Saved as ' + numpy_array_name)

# Plot
# if is_plot:

#     # Figure
#     fig = plt.figure(1, figsize=[15, 10])

#     # Run plot function
#     ax, pic_name = fp.plot(
#         fig.add_subplot(1, 1, 1),
#         model_name,
#         dat,
#         let,
#     )

#     # Save
#     if is_save:
#         plt.savefig(pic_name)
#         print('Saved as ' + pic_name)

#     # Show
#     if is_show:
#         plt.show()
#     else:
#         plt.clf()

# Backup
if is_backup:
    pm.py_backup(
        pm.python_scripts_dir,
        sca.tag,
        "runplot",
        "ipy",
        sc.specl(model_name,
                 dat,
                 let)
    )
