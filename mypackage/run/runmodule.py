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
    Runs Scripts with optinal output, input, waiting for it to end
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
            os.chdir('/home/jk125262/PythonDir_Cluster')
            raise exceptions.RuntimeError("Problems in " + str(name))
    



#############################################################
#               CHANGE HASHTAG INPUT
#############################################################
def change_hashtag_input(file_name, hashtag_line, new_input):
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
            file_tmp.write(hashtag_line + '\n')
            file_tmp.write(new_input)
            file_tmp.write("\n\n\n")
        else:
            file_tmp.write(line)
    file_input.close()
    file_tmp.close()
    os.remove(file_name)
    os.rename(file_name_tmp,file_name)

    if hashstr_not_exist:
        print('\n\nThe catchphrase')
        print(hashtag_line)
        print('was not found (or more than once) in')
        print(file_name)
        print('\ntimes found = ')
        print(1-hashstr_not_exist)
        raise exceptions.RuntimeError("Hashtag-catchphrase not found.")
        
    return

#############################################################
#               COMPILEQUICK
#############################################################
def compilequick( vtk_var = 1, omp_var = 1):
    "This function invokes the compilation via compilequick.sh"
    # Should be called in model_directory!
    # Default: vtk_omp compilation
    if vtk_var:
        if omp_var:
            compilation_exec = 'py_compilequick_gnu_vtk_omp.sh'
            output_file_str = 'compilation_vtk_omp.out'
            output_file = open(output_file_str,"w")
        else:
            compilation_exec = 'py_compilequick_gnu_vtk.sh'
            output_file_str = 'compilation_vtk.out'
            output_file = open(output_file_str,"w")
    else:
        if omp_var:
            compilation_exec = 'py_compilequick_gnu_plt_omp.sh'
            output_file_str = 'compilation_plt_omp.out'
            output_file = open(output_file_str,"w")
        else:
            compilation_exec = 'py_compilequick_gnu_plt.sh'
            output_file_str = 'compilation_plt.out'
            output_file = open(output_file_str,"w")

    if os.path.isfile(compilation_exec):
        args = shlex.split(compilation_exec)
        print('\n\n Now compiling to output-file ' + output_file_str + '\n\n')
        process_compile = subprocess.Popen(args, stdout=output_file, stderr=subprocess.STDOUT)
        subprocess.Popen.wait(process_compile)
        output_file.close()
    else:
        print('\n\nThe executable')
        print(compilation_exec)
        print('did not exist in')
        print(os.getcwd())
        raise exceptions.RuntimeError("Fitting Compilequick not found.")

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
    model_name_big = model_name.upper()
    model_dir = "/home/jk125262/shematModelsDir_Cluster/" + model_name + "_model"
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

    return model_name_big, model_dir, input_file, enkf_input_file, true_input_file,\
        true_sgsim_file, sgsim_file, true_log_file, log_file, shell_output_file,\
        init_dist_file_one, init_dist_file_two, init_dist_file_three, observations_file,\
        true_file,true_chem_file


def make_model_dir_tmp(model_name,letter,today):
    os.chdir("/home/jk125262/shematModelsDir_Cluster")
    # Copy everything to temporal directory
    model_dir_name = model_name + '_model_' + today  + '_' + letter
    new_model_dir = "/home/jk125262/shematModelsDir_Cluster/" + model_dir_name
    trash_model_dir = "/home/jk125262/.Trash/"+ model_dir_name
    trash_model_dir_2 = "/home/jk125262/.Trash/"+ model_dir_name + '_2'
    # Check if new_model_dir already exists
    if os.path.isdir(new_model_dir):
        os.chdir('/home/jk125262/PythonDir_Cluster')
        # _2 dir in .Trash exists: Kill it (should be killable by now)
        if os.path.isdir(trash_model_dir_2):
            shutil.rmtree(trash_model_dir_2)
        # dir in .Trash exists: Rename it to _2 dir in .Trash
        if os.path.isdir(trash_model_dir):
            os.rename(trash_model_dir,trash_model_dir_2)
        # Move old new_model_dir to .Trash
        shutil.move(new_model_dir,"/home/jk125262/.Trash")
        # raise exceptions.RuntimeError("New model dir already exists: " + new_model_dir)
    shutil.copytree("/home/jk125262/shematModelsDir_Cluster/" + model_name + '_model',
                    new_model_dir)
    os.chdir(new_model_dir)
    # Change the directory  inside clean_out, move_output
    replace_string('clean_output.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('clean_output_py.sh','/'+model_name+'_model',
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
    replace_string('move_output_py.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('py_compilequick_gnu_plt.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('py_compilequick_gnu_plt_omp.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('py_compilequick_gnu_vtk.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    replace_string('py_compilequick_gnu_vtk_omp.sh','/'+model_name+'_model',
                   '/'+model_name+'_model_' + today  + '_' + letter)
    os.chmod('clean_output.sh',128+256+64)
    os.chmod('clean_output_py.sh',128+256+64)
    os.chmod('compilequick.sh',128+256+64)
    os.chmod('generateobs.sh',128+256+64)
    os.chmod('generatetrues.sh',128+256+64)
    os.chmod('generatetecmon.sh',128+256+64)
    os.chmod('move_output.sh',128+256+64)
    os.chmod('move_output_py.sh',128+256+64)
    os.chmod('py_compilequick_gnu_plt.sh',128+256+64)
    os.chmod('py_compilequick_gnu_plt_omp.sh',128+256+64)
    os.chmod('py_compilequick_gnu_vtk.sh',128+256+64)
    os.chmod('py_compilequick_gnu_vtk_omp.sh',128+256+64)
    os.chmod('veryclean.sh',128+256+64)

    return new_model_dir
    
def delete_model_dir_tmp(model_dir):
    # Delete the temporal directory
    shutil.rmtree(model_dir)


print('\n Done with module : runmodule.py.')
print(time.asctime( time.localtime( time.time())))
