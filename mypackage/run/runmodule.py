#!/usr/bin/python

import sys                      # System variables (PYTHONPATH as list sys.path)
import subprocess  		# To execute shell command (subprocess.Popen)
import os			# Operating system (os.chdir, os.path)
import exceptions  		# Raising exception (raise exceptions.RuntimeError)
import shlex      		# Structure system commands(shlex.split) 
import string     		# Load alphabet (string.alphabet())
import time       		# Timing the execution (time.time(), time.clock())
import shutil

#############################################################
#                  REPLACE STRING
#############################################################
def replace_string(file_name_input, old_str, new_str):
    "In file_name_input every instance of old_str is replaced by new_str"
    ostr_not_exist = 1
    file_name_tmp = 'filename.tmp'
    file_input = open(file_name_input,'r')
    file_tmp = open(file_name_tmp,'w')
    for line in file_input:
        ostr_exist_check = line.find(old_str)
        if (ostr_exist_check > -1):
            ostr_not_exist = 0
        file_tmp.write(line.replace(old_str,new_str))
    file_input.close()
    file_tmp.close()
    os.remove(file_name_input)
    os.rename(file_name_tmp,file_name_input)

    if ostr_not_exist:
        print('\n\nA replace_string was called, but the string')
        print(old_str)
        print('to be replaced was not found in')
        print(file_name_input)
        sys.exit()
        
    return

#############################################################
#          MAKE TEMP COPY OF INPUTFILE
#############################################################
def make_tmp(file_name_input):
    "Make a tmp file by adding .tmp at the end of the filename (input)."
    file_input = open(file_name_input,'r')
    file_tmp = open(file_name_input + '.tmp','w')
    for line in file_input:
        file_tmp.write(line)
    file_input.close()
    file_tmp.close()

#############################################################
#    RETURN THE INPUTFILE TO THE STATE OF THE TEMP COPY
#############################################################
def get_tmp(file_name_input):
    "Copy the tmp file to the real one and then remove the tmp file."
    file_input = open(file_name_input,'w')
    file_tmp = open(file_name_input + '.tmp','r')
    for line in file_tmp:
        file_input.write(line)
    file_input.close()
    file_tmp.close()
    os.remove(file_name_input + '.tmp')


#############################################################
#        GET INTEGER CORRESPONDING TO ALPHABET LETTER
#############################################################
def get_num_let(let):
    """
    Returns the integer corresponding to the input letter
    """
    alphabet = string.lowercase

    if len(let) == 1:
        return alphabet.index(let)
    if len(let) == 2:
        return 26*(alphabet.index(let[0])) + alphabet.index(let[1]) + 26 
    if len(let) == 3:
        return 26*26*(alphabet.index(let[0])) + 26*(alphabet.index(let[1])) + alphabet.index(let[2]) + 26*26 + 26
    else:
        raise exceptions.RuntimeError('letter does not contain 1,2 or 3 letters')



#############################################################
#     GET ALPHABET LETTER CORRESPONDING TO INTEGER
#############################################################
def get_let_num(num):
    """
    Returns the letter of the alphabet corresponding to the input integer.

    The form of the number is (ii are the indices of the letters in 
    string.lowercase, 0<= ii <=25):

    Length1: i0
    Length2: 26*i0 + i1 + 26 
    Length3: 26^2*i0 + 26*i1 + i2 + 26^2 + 26
    """
    alphabet = string.lowercase

    if num < 26:
        return alphabet[num]
    elif num < 702:
        num = num-26
        return alphabet[num/26] + get_let_num(num%26)
    elif num < 18278:
        num = num-26*26-26
        return alphabet[num/676] + get_let_num((num%676)+26)
    else:
        raise exceptions.RuntimeError('Number too high: Should be < 18278')

#############################################################
#     Run a script
#############################################################
def run_script(path,name,outfile = None,instr = None,wait = None,errout = None):
    """
    Runs Scripts with optional output, input, waiting for it to end
    and Error if execution went wrong.
    """
    os.chdir(path)
    if not outfile:
        proc = subprocess.Popen(name,stdin=subprocess.PIPE)
    else:
        proc = subprocess.Popen(name,stdin=subprocess.PIPE, stdout=outfile)
    
    if instr:
        subprocess.Popen.communicate(proc,input = instr)

    if wait:
        subprocess.Popen.wait(proc)

    if errout:
        if(proc.returncode):
            os.chdir(os.environ['HOME']+'/PythonDir')
            raise exceptions.RuntimeError("Problems in " + str(name))
    



#############################################################
#               CHANGE HASHTAG INPUT
#############################################################
def change_hashtag_input(file_name, hashtag_line, new_input, delete_lines = None):
    "In file_name hashtag_line is found and new_input inserted as next line"
    hashstr_not_exist = 1
    file_name_tmp = 'filename.tmp'
    file_input = open(file_name,'r')
    file_tmp = open(file_name_tmp,'w')
    for line in file_input:
        hashstr_exist_check = line.find(hashtag_line)
        #print(hashstr_exist_check)
        if (hashstr_exist_check > -1):
            hashstr_not_exist = hashstr_not_exist - 1
            file_tmp.write(line)
            file_tmp.write(new_input)
            file_tmp.write("\n\n\n")
            if delete_lines:
                for i in range(delete_lines):
                    file_input.next()
        else:
            file_tmp.write(line)
    file_input.close()
    file_tmp.close()
    os.remove(file_name)
    os.rename(file_name_tmp,file_name)

    if hashstr_not_exist:
        raise exceptions.RuntimeError('Hashtag-catchphrase not found.'
                                      + '\n\nThe catchphrase  '
                                      + hashtag_line 
                                      + '  was found '
                                      + str(1-hashstr_not_exist)
                                      + ' times in'
                                      + file_name)
        
    return

#############################################################
#               READ HASHTAG INPUT
#############################################################
def read_hashtag_input(file_name,hashtag_line,nl):
    """
    Read a number of lines of a hashtag input
    """
    hashstr_not_exist = 1
    try:
        file_input = open(file_name,'r')
    except:
        os.chdir(os.environ['HOME']+'/PythonDir')
        raise
    l = 1
    for line in file_input:
        hashstr_exist_check = line.find(hashtag_line)
        #print(hashstr_exist_check)
        if (hashstr_exist_check > -1):
            hashl = l
            hashstr_not_exist = hashstr_not_exist - 1
        l = l + 1
    file_input.close()

    if hashstr_not_exist:
        raise exceptions.RuntimeError('Hashtag-catchphrase not found.'
                                      + '\n\nThe catchphrase  '
                                      + hashtag_line 
                                      + '  was found '
                                      + str(1-hashstr_not_exist)
                                      + ' times in'
                                      + file_name)

    str_out = ""
    file_input = open(file_name,'r')
    for i in range(hashl):
        file_input.readline()
    for i in range(nl):
        str_out+= file_input.readline()
    file_input.close()
    return str_out


#############################################################
#               READ RECORDS INPUT
#############################################################
def read_records_input(file_name,hashtag_line):
    """
    Read number of records of a hashtag input
    """
    hashstr_not_exist = 1
    try:
        file_input = open(file_name,'r')
    except:
        os.chdir(os.environ['HOME']+'/PythonDir')
        raise
    l = 1
    for line in file_input:
        hashstr_exist_check = line.find(hashtag_line)
        #print(hashstr_exist_check)
        if (hashstr_exist_check > -1):
            hashl = l
            hashstr_not_exist = hashstr_not_exist - 1
        l = l + 1
    file_input.close()

    if hashstr_not_exist:
        raise exceptions.RuntimeError('Hashtag-catchphrase not found.'
                                      + '\n\nThe catchphrase  '
                                      + hashtag_line 
                                      + '  was found '
                                      + str(1-hashstr_not_exist)
                                      + ' times in'
                                      + file_name)

    str_out = ""
    file_input = open(file_name,'r')
    for i in range(hashl-1):
        file_input.readline()
    str_out+= file_input.readline()
    file_input.close()

    records_not_exist_check = 1
    for string in str.split(str_out):
        if string[:7] == 'records':
            records_not_exist_check = 0
            for i in range(len(string)):
                if string[i-1]=='=':
                    num_records = int(string[i:])

    if records_not_exist_check == 1:
        os.chdir(os.environ['HOME']+'/PythonDir')
        raise exceptions.RuntimeError('No records in Hashtag-Input: '+hashtag_line)
                
    return num_records

#############################################################
#               COMPILEQUICK
#############################################################
def compilequick(model_dir, vtk_var = 1, omp_var = 1, fw_var = 0):
    """
    This function is a wrapper organizing different inputs 
    given to py_compilequick.sh, which is called via
    the function rm.run_script.
    """

    # Forward or Simulate 
    if fw_var:
        shem_type = "fw"
        shem_type_name = "fw"
    else:
        shem_type = "sm"
        shem_type_name = "sm_sgsim"

    # Flags
    flags = "nohdf -j16"
    flags_name = ""

    if vtk_var:
        flags += " vtk noplt"
        flags_name += "vtk"
    else:
        flags += " novtk plt"
        flags_name += "plt"

    if omp_var:
        flags += " omp"
        flags_name += "_omp"
    else:
        flags += " noomp"
        flags_name += ""

    compilequick_input = shem_type + "\n" \
      + shem_type_name + "\n" \
      + flags + "\n" \
      + flags_name + "\n"

    # run_script
    compilation_outfile = open('compilation_'+flags_name+'.out',"w")
    run_script(model_dir,'py_compilequick.sh',outfile=compilation_outfile,
                   instr=compilequick_input, wait=True, errout=True)
    compilation_outfile.close()

    return



#############################################################
#               MATLAB CALL
#############################################################
def matlab_call( mfile_name , matlab_dir):
    "This function invokes Matlab to execute mfile_name"
    # Should be called in Matlab_Directory!
    os.chdir(matlab_dir)
    if os.path.isfile(mfile_name):
        args = shlex.split('matlab -nodisplay -nojvm < ' + mfile_name)
        process_matlab = subprocess.Popen(args)
        subprocess.Popen.wait(process_matlab)
        if process_matlab.returncode:
            raise exceptions.RuntimeError("Problems in Matlab Execution of   "\
                + mfile_name)
        else:
            print("\n\n")
    else:
        print('\n\nThe Matlab .m-file')
        print(mfile_name)
        print('did not exist in')
        print(os.getcwd())
        raise exceptions.RuntimeError("Matlab file not found.")

    return



#############################################################
#               CHANGE MATLAB
#############################################################
def change_matlab( mfile_name,
                   output_path,
                   filename,
                   use_dists,
                   means, 
                   standard_deviations,
                   sgsim_switch ):
    "This function changes the Matlab file"
    # Should be called in Matlab_Directory!
    if os.path.isfile(mfile_name):
        mfile_name_tmp = 'mfilename.tmp'
        mfile_input = open(mfile_name,'r')
        mfile_tmp = open(mfile_name_tmp,'w')
        for line in mfile_input:
            output_path_exist_check = line.find("output_path = '")
            filename_exist_check = line.find("filename = '")
            use_dists_exist_check = line.find("use_dists = [")
            means_exist_check = line.find("means = [")
            standard_deviations_exist_check = line.find("standard_deviations = [")
            sgsim_switch_exist_check = line.find("sgsim_switch = ")
            ###print(output_path_exist_check)
            if(output_path_exist_check == 0):
                ###print('Here')
                mfile_tmp.write("output_path = '" + output_path + "';\n")
            elif(filename_exist_check == 0):
                mfile_tmp.write("filename = '" + filename + "';\n")                
            elif(use_dists_exist_check == 0):
                mfile_tmp.write("use_dists = " + use_dists + ";\n") 
            elif(means_exist_check == 0):
                mfile_tmp.write("means = " + means + ";\n") 
            elif(standard_deviations_exist_check == 0):
                mfile_tmp.write("standard_deviations = " + standard_deviations + ";\n") 
            elif(sgsim_switch_exist_check == 0):
                mfile_tmp.write("sgsim_switch = " + sgsim_switch + ";\n") 
            else:
                mfile_tmp.write(line)
        mfile_input.close()
        mfile_tmp.close()
        os.remove(mfile_name)
        os.rename(mfile_name_tmp,mfile_name)
    else:
        print('\n\nThe Matlab .m-file')
        print(mfile_name)
        print('did not exist in')
        print(os.getcwd())

    return




#############################################################
#               MAKE FILE/DIR NAMES
#############################################################

def make_file_dir_names(model_name):
    """
    Export file and directory names which contain model_name.

    Indices of exported files/directories:

     0 - model_name_big
     1 - model_dir
     2 - input_file
     3 - enkf_input_file
     4 - true_input_file
     5 - true_sgsim_file
     6 - sgsim_file
     7 - true_log_file
     8 - log_file
     9 - shell_output_file
    10 - init_dist_file_one
    11 - init_dist_file_two
    12 - init_dist_file_three
    13 - observations_file
    14 - true_file
    15 - true_chem_file
    """
    model_name_big = model_name.upper()
    model_dir = os.environ['HOME']+"/shematModelsDir/" + model_name + "_model"
    input_file = model_name_big
    enkf_input_file = model_name_big + ".enkf"
    true_input_file = model_name_big + "_TRUE"
    true_sgsim_file = "sgsim_k_" + model_name + "_true.par"
    sgsim_file = "sgsim_k_" + model_name + ".par"
    true_log_file = "logk_" + model_name + "_true.dat"
    log_file = "logk_" + model_name + ".dat"
    shell_output_file = model_name + ".out"
    init_dist_file_one="init_dist_" + model_name + "_1.dat"
    init_dist_file_two="init_dist_" + model_name + "_2.dat"
    init_dist_file_three="init_dist_" + model_name + "_3.dat"
    observations_file = "observations_" + model_name_big + ".dat"
    true_file = "True" + model_name_big + ".plt"
    true_chem_file = "True" + model_name_big + "_chem.plt"

    return model_name_big, \
        model_dir, \
        input_file, \
        enkf_input_file, \
        true_input_file,\
        true_sgsim_file, \
        sgsim_file, \
        true_log_file, \
        log_file, \
        shell_output_file, \
        init_dist_file_one, \
        init_dist_file_two, \
        init_dist_file_three, \
        observations_file, \
        true_file, \
        true_chem_file


def make_model_dir_tmp(model_name,letter,today):
    os.chdir(os.environ['HOME']+"/shematModelsDir")
    # Copy everything to temporal directory
    model_dir_name = model_name + '_model_' + today  + '_' + letter
    new_model_dir = os.environ['HOME']+"/shematModelsDir/" + model_dir_name
    trash_model_dir = os.environ['HOME']+"/.Trash/"+ model_dir_name
    trash_model_dir_2 = os.environ['HOME']+"/.Trash/"+ model_dir_name + '_2'
    # Check if new_model_dir already exists
    if os.path.isdir(new_model_dir):
        os.chdir(os.environ['HOME']+'/PythonDir')
        # _2 dir in .Trash exists: Kill it (should be killable by now)
        if os.path.isdir(trash_model_dir_2):
            shutil.rmtree(trash_model_dir_2)
        # dir in .Trash exists: Rename it to _2 dir in .Trash
        if os.path.isdir(trash_model_dir):
            os.rename(trash_model_dir,trash_model_dir_2)
        # Move old new_model_dir to .Trash
        shutil.move(new_model_dir,os.environ['HOME']+"/.Trash")
        # raise exceptions.RuntimeError("New model dir already exists: " + new_model_dir)
    shutil.copytree(os.environ['HOME']+"/shematModelsDir/" + model_name + '_model',
                    new_model_dir)
    os.chdir(new_model_dir)
    # Change the directory  inside clean_out, move_output
    replace_string('clean_output.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('py_clean_output.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('compilequick.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('generateobs.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('generatetecmon.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('generatetrues.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('move_output.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('py_move_output.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('py_compilequick.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    os.chmod('clean_output.sh',128+256+64)
    os.chmod('py_clean_output.sh',128+256+64)
    os.chmod('compilequick.sh',128+256+64)
    os.chmod('generateobs.sh',128+256+64)
    os.chmod('generatetrues.sh',128+256+64)
    os.chmod('generatetecmon.sh',128+256+64)
    os.chmod('move_output.sh',128+256+64)
    os.chmod('py_move_output.sh',128+256+64)
    os.chmod('py_compilequick.sh',128+256+64)
    os.chmod('veryclean.sh',128+256+64)

    return new_model_dir
    
def delete_model_dir_tmp(model_dir):
    # Delete the temporal directory
    shutil.rmtree(model_dir)


# print('\n Done with module : runmodule.py.')
# print(time.asctime( time.localtime( time.time())))
