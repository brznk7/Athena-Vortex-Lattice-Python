#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:31:03 2020

@author: safa
"""

from NewConfPar import NewConf
import multiprocessing as mp

BaseAVLInputFileName = 'test.avl'
Directory = '/home/safa/Desktop/Athena-Vortex-Lattice-Python-master/AVL Files/In/'

    
AlphaRange = [0,3,6,9,12,15] 
ConfNum = 9
processes = list()
if __name__ == '__main__':
    for conf in range(ConfNum):
        for alpha in AlphaRange:
            ## creating processes
            processes.append(mp.Process(target=NewConf,args=(conf,alpha,BaseAVLInputFileName,Directory)))
    
    ## starting processes
    for process in processes:
        process.start()
        
    ## waiting to all processes to stop
    for process in processes:
        process.join()
    