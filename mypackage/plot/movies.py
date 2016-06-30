import shlex
import exceptions
import os
from mypackage.run import runmodule as rm
from mypackage.plot import myplots
import time
python_dir = os.environ['HOME']+'/PythonDir'

def movie(input_name_test = 'plot_m_b_01_100_av.png', input_names = 'plot_m_b_%02d_100_av.png',
          output_name = 'plot_m_b_100_av.mp4', model_name = 'wave', date = '2015_05_19'):

    # Directory
    pics_dir = os.environ['HOME']+'/shematOutputDir/' + model_name \
        + '_output/' + date + '/pics/'
    
    # Input test
    os.chdir(pics_dir)
    if not os.path.isfile(input_name_test):
        os.chdir(python_dir)
        raise exceptions.RuntimeError('File' + input_name_test +  ' not found in ' + pics_dir + '!!!')
    # Output deletion if exists
    os.chdir(pics_dir)
    if os.path.isfile(output_name):
        os.remove(output_name)
    
    
    # Shell command split by the shlex utility
    arg = shlex.split('ffmpeg -qscale 5 -r 2 -b 9600 -i ' + input_names + ' ' + output_name)

    # The shell command run
    rm.run_script(pics_dir,arg,wait = 1, errout = 1)

    os.chdir(python_dir)

print('\n Done with module : movies.py.')
print(time.asctime( time.localtime( time.time())))
