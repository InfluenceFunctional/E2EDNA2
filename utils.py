'''
utilities
'''
import os
import numpy as np
import MDAnalysis as mda
import glob
import argparse
from pdbfixer.pdbfixer import PDBFixer, proteinResidues, dnaResidues, rnaResidues, _guessFileFormat
from simtk.openmm.app import PDBFile
import simtk.unit as unit
from simtk.unit import *
from simtk.openmm import *
from simtk.openmm.app import *
import matplotlib.pyplot as plt


def combinePDB(file1, file2):
    '''
    combine 2 pdb files into one
    ### actually for this one I think we may defer entirely to the docker
    :param file1:
    :param file2:
    :return:
    '''



def get_input():
    '''
    get the command line in put for the run-num. defaulting to a new run (0)
    :return:
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--run_num', type=int, default=0)
    cmd_line_input = parser.parse_args()
    run = cmd_line_input.run_num

    return run


def findLine(file, string):
    # return the line number of a given string, indexing from 1
    f = open(file, 'r')
    text = f.read()
    f.close()
    text = text.split('\n')
    try:
        lineInd = 1
        for line in text:
            if line == string:
                lineNum = lineInd  # index from 1
            lineInd += 1

        return lineNum
    except:
        raise ValueError("String not found in file!")


def replaceText(file, old_string, new_string):
    # search and replace text in a file, then save the new version
    f = open(file, 'r')
    text = f.read()
    f.close()
    text = text.replace(old_string, new_string)
    f = open(file, 'w')
    f.write(text)
    f.close()


def removetwo(target):
    if os.path.exists(target + "_2"):
        os.remove(target)  # delete original
        os.rename(target + "_2", target)  # append updated
    else:
        print("No _2 structure was made!")
        raise ValueError


def copyLine(file, line_number):
    # copy a line of text from a file and return it
    f = open(file, 'r')
    text = f.read()
    f.close()
    return text.split('\n')[line_number - 1]  # copy a line from the file, indexing from 1


def removeLine(file, string):
    '''
    remove every line containing given string from a file
    :param fine:
    :return:
    '''
    f = open(file, 'r')
    text = f.read()
    f.close()
    lines = text.split('\n')
    try:
        for i in range(len(lines)):
            if string in lines[i]:
                lines.pop(i)
    except:
        pass
    text = "\n".join(lines)
    f = open(file, 'w')
    f.write(text)
    f.close()


def addLine(file, string, line_number):
    # add a new line of text to a file
    f = open(file, 'r')
    text = f.read()
    f.close()
    lines = text.split('\n')
    lines.insert(line_number - 1, string)  # replace line ### with the string, indexing from 1
    text = "\n".join(lines)
    f = open(file, 'w')
    f.write(text)
    f.close()


def writeCheckpoint(text):
    '''
    write some output to the checkpoint file
    :return:
    '''
    f = open('checkpoint.txt', 'a')
    f.write('\n' + text)
    f.close()


def evaluateBinding(trajectory):
    '''
    evaluate the docking trajectory to determine whether the DNA binds to the analyte
    :param trajectory:
    :return:
    '''
    u = mda.Universe(trajectory)  # load up the trajectory for analysis
    # do
    # some
    # analysis

    return 1