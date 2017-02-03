#!/usr/bin/python

# Operating system commands
import os
from os import path
import exceptions
import sys
from mypackage.run import runmodule as rm

model_name = 'model'
dat = '1988_11_10'
lets = ['b']

truedat = '1988_11_10'
truelet = 'a'

###############################################################################
#                                     spec                                    #
###############################################################################
def spec(nl=0):
    """
    Specifier-string consisting of
    - model name
    - date
    - letter (number nl in the list)
    - two '_' in between 
    """
    return model_name + '_' + dat + '_' + lets[nl]

###############################################################################
#                                     specl                                   #
###############################################################################
def specl(let=None):
    """
    Specifier-string consisting of
    - model name
    - date
    - letter (specified or first)
    - two '_' in between 
    """
    if let:
        return model_name + '_' + dat + '_' + let
    else:
        return model_name + '_' + dat + '_' + lets[0]

###############################################################################
#                                    nrens                                    #
###############################################################################
def nrens(model_name,dat,let):
    """
    Number of ensemble members for model_name
    """
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'
    input_file = rm.make_file_dir_names(model_name)[2]

    line = rm.read_hashtag_input(output_path+input_file,'# simulate',1)
    first_entry = str.split(line)[0]
    nrens = int(first_entry)

    return nrens
    
###############################################################################
#                                   num_mons                                  #
###############################################################################
def num_mons(model_name,dat,let):
    """
    Number of monitoring points for model_name.
    """
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'
    true_input_file = rm.make_file_dir_names(model_name)[4]

    num_mons = rm.read_records_input(output_path+true_input_file,'# monitor,')

    return num_mons

###############################################################################
#                                  nrobs_int                                  #
###############################################################################
def nrobs_int(model_name,dat,let):
    """
    Number of observation intervals for model_name.
    """
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'
    enkf_input_file = rm.make_file_dir_names(model_name)[3]

    line = rm.read_hashtag_input(output_path+enkf_input_file,'# nrobs_int',1)
    first_entry = str.split(line)[0]
    nrobs_int = int(first_entry)
    return nrobs_int
    
###############################################################################
#                                     locs                                    #
###############################################################################
def locs(model_name,dat,let):
    """
    Single cell location of model_name.
    """
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'
    true_input_file = rm.make_file_dir_names(model_name)[4]
    n_mons = num_mons(model_name,dat,let)
    
    lines = rm.read_hashtag_input(output_path+true_input_file,
                                  '# monitor',
                                  n_mons)
    locs = [[int(str.split(lines)[j]) for j in range(i,i+3)] for i in range(0,4*n_mons,4)]

    return locs

###############################################################################
#                                   variable                                  #
###############################################################################
def variable(model_name,dat,let):
    """
    Single cell variable of model_name.
    
     1: head,  2:temp,  3:conc,  4:kz,  5:lz,  6:por  (inside mem)
    11: head, 12:temp, 13:conc, 14:kz, 15:lz, 16:por  (not inside mem)
    """
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'
    enkf_input_file = rm.make_file_dir_names(model_name)[3]
    n_mons = num_mons(model_name,dat,let)

    lines = rm.read_hashtag_input(output_path+enkf_input_file,'# single cell output,',n_mons)
    fourth_entry = str.split(lines)[3]
    variables = [int(str.split(lines)[i]) for i in range(3,5*n_mons,5)]
    
    return variables[0]


###############################################################################
#                                 num_pres_vel                                #
###############################################################################
def num_pres_vel(model_name,dat,let):
    """
    Number of velocity components for model_name.
    """
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'
    enkf_input_file = rm.make_file_dir_names(model_name)[3]

    num_pres_vel = rm.read_records_input(output_path+enkf_input_file,'# prescribed velocity')

    return num_pres_vel

###############################################################################
#                                      ns                                     #
###############################################################################
def ns(model_name,dat,let):
    """
    First observation time for model_name.
    """
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'
    obs_file = rm.make_file_dir_names(model_name)[13]

    file_input = open(output_path+obs_file,'r')
    file_input.readline()
    ns = int(str.split(file_input.readline())[0])

    # Python starts at 0
    ns = ns-1
    
    return ns

###############################################################################
#                                      nm                                     #
###############################################################################
def nm(model_name,dat,let):
    """
    Difference of observation times for model_name.
    """
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'
    obs_file = rm.make_file_dir_names(model_name)[13]

    n_mons = num_mons(model_name,dat,let)

    file_input = open(output_path+obs_file,'r')
    file_input.readline()
    ns1 = int(str.split(file_input.readline())[0])
    for i in range(n_mons):
        file_input.readline()
    ns2 = int(str.split(file_input.readline())[0])
    nm = ns2-ns1

    return nm

###############################################################################
#                                    units                                    #
###############################################################################
def units(model_name,dat,let,uindex,pindex):
    """
    Read parameters pindex from unit uindex
    pindex:
    1 - Porosity
    4 - Permeability
    8 - Thermal conductivity
    10 - Volumetric heat capacity
    """

    # Define path and file
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'
    input_file = rm.make_file_dir_names(model_name)[2]

    # Read hashtag input
    lines = rm.read_hashtag_input(output_path+input_file,'# units',uindex)

    # Split hashtag input by white space
    split_lines = str.split(lines)

    # Find the number of parameters per line
    num_ps = len(split_lines)/uindex
    # Calculate the index of the right parameter
    right_index = (uindex-1)*num_ps + pindex

    right_entry = split_lines[right_index]

    return right_entry

###############################################################################
#                             Number of time steps                            #
###############################################################################
def nt(model_name,dat,let):
    """
    Read the number of time steps (used in observation file)
    """

    # Define path and file
    output_path = os.environ['HOME']+'/shematOutputDir/'+model_name+'_output/' \
                  + dat + '/' + dat + '_'+ let+ '/'
    input_file = rm.make_file_dir_names(model_name)[2]

    # Read records (number lines in time step input)
    num_time_records = rm.read_records_input(output_path+input_file,'# time periods')

    # Read hashtag input
    lines = rm.read_hashtag_input(output_path+input_file,'# time periods',num_time_records)
    
    # Split hashtag input by white space
    split_lines = str.split(lines)

    # Read entry 3/4 in each line
    right_entries = split_lines[2::4]

    # Sum of the entries
    # -> Adding one accounts for the first time step at time = 0
    nt = sum([int(right_entries[i]) for i in range(len(right_entries))]) + 1

    return nt
