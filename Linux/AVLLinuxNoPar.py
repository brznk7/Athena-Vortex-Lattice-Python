#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:31:03 2020

@author: safa
"""

from NewConf import CreateConfData,CreateConfFile
import subprocess as sp


Ref,RootChords,TipChords = CreateConfData()
BaseAVLInputFileName = 'test.avl'
Directory = '/home/safa/Desktop/Athena-Vortex-Lattice-Python-master/Parallel/AVL Files/In/'
def AVLExecution(ConfNo,Alpha):
    InDirectory = './AVL Files/In/'
    InpFileName = InDirectory+'AVLInputConf_'+str(ConfNo)+'.avl'
    OutDirectory = './AVL Files/Out/'
    OutFileName = OutDirectory+'AVLOutConf_'+str(ConfNo)+'Alpha'+str(Alpha)
    
    AVLCommand = 'load'+'\n'\
                 +InpFileName+'\n'\
                 +'OPER'+'\n'\
                 +'A A '+str(Alpha)+'\n'\
                 +'X'+'\n'\
                 +'st'+'\n'\
                 +OutFileName
    avl = sp.Popen(['avl'],
           stdin=sp.PIPE,stdout=sp.PIPE, 
           stderr=None, 
           universal_newlines=True)
    
    avl.communicate(AVLCommand)
    
AlphaRange = [0,3,6,9,12,15] 
for conf in range(RootChords.size):
    for alpha in AlphaRange:
        CreateConfFile(Ref,RootChords,TipChords,conf,BaseAVLInputFileName,Directory) 
        AVLExecution(conf,alpha)