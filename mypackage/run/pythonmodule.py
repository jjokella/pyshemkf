#!/usr/bin/python

import sys                      # System variables (PYTHONPATH as list sys.path)
import subprocess  		# To execute shell command (subprocess.Popen)
import os			# Operating system (os.chdir, os.path)
import exceptions  		# Raising exception (raise exceptions.RuntimeError)
import shlex      		# Structure system commands(shlex.split) 
import string     		# Load alphabet (string.alphabet())
import time       		# Timing the execution (time.time(), time.clock())
import shutil

from mypackage.plot import specs as sc


###############################################################################
#                               python_dirs                                   #
###############################################################################
python_dir = os.environ['HOME']+'/PythonDir'
python_scripts_dir = os.environ['HOME']+'/PythonDir/scripts'
python_input_dir = os.environ['HOME']+'/PythonDir/input'
python_output_dir = os.environ['HOME']+'/PythonDir/output'


###############################################################################
#                            python_output_dir                                #
###############################################################################

def py_output_dir(tag,ending):
    """
    Generate Python output director according to
    - tag: The name of the subdirectory of scripts or output
    - ending: Mostly png,eps,npy
    """

    py_output_dir = python_output_dir + "/" \
                    + tag + "/" \
                    + ending

    return py_output_dir
                        
###############################################################################
#                            python_output_filename                           #
###############################################################################

def py_output_filename(tag,filename,spec,ending):
    """
    Generate Python output filename (with specifier)
    according to
    - filename: The filename WITHOUT ENDING
    - tag: The name of the subdirectory of scripts or output
    - ending: Mostly png,eps,npy
    - spec: Output specifier
    """

    py_output_filename = py_output_dir(tag,ending) + "/" \
                         + filename + "_" + spec + "." \
                         + ending

    return py_output_filename

###############################################################################
#                            python_output_filename                           #
###############################################################################

def py_simple_output_filename(filename,tag,ending):
    """
    Generate Python simple output filename (without specifier)
    according to
    - filename: The filename WITHOUT ENDING
    - tag: The name of the subdirectory of scripts or output
    - ending: Mostly png,eps,npy
    """

    py_simple_output_filename = py_output_dir(tag,ending) + "/" \
                                + filename + "." \
                                + ending

    return py_simple_output_filename

###############################################################################
#                            python_script_backup                             #
###############################################################################

def py_script_backup(tag,filename,ending,model_name,dat,let):
    """
    Copy a python script to backup directory and add specifier
    """
    # Script Name
    py_script_file_name = python_scripts_dir + "/" \
                          + tag + "/" \
                          + filename + "." \
                          + ending

    # Possibly create backup directory
    if not os.path.exists(python_scripts_dir+"/"+tag+"/backup"):
        os.mkdir(python_scripts_dir+"/"+tag+"/backup")

    # Backup Script Name
    py_script_backup_file_name = python_scripts_dir + "/" \
                                 + tag + "/" \
                                 + "backup/" \
                                 + filename + "_" + sc.specl(model_name,dat,let)+"." \
                                 + ending


    # Exception if file already exists
    if os.path.isfile(py_script_backup_file_name):
        os.remove(py_script_backup_file_name)
        print('Removed old file: '+py_script_backup_file_name)

    shutil.copyfile(py_script_file_name,py_script_backup_file_name)
    print('Backup as '+py_script_backup_file_name)


