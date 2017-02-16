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