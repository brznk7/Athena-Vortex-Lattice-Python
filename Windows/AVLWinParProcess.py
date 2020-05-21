# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:06:05 2020

@author: safa
"""

from NewConfPar import AVLExecution
import multiprocessing as mp
import time

StartTime = time.time()
BaseAVLInputFileName = 'test.avl'

InDirectory = r'C:\Users\Dell\Documents\GitHub\Athena-Vortex-Lattice-Python\Windows\AVL Files'   
AlphaRange = [0,3,6,9,12,15] 
ConfNum = 9
processes = list()
processCount = 0
if __name__ == '__main__':
    for conf in range(ConfNum):
        for alpha in range(len(AlphaRange)):
            ## creating processes
            processes.append(mp.Process(target=AVLExecution,args=(conf,alpha,BaseAVLInputFileName,InDirectory)))
            
    ## starting process
    for process in processes:
        process.start()
    
    ## wait until all processes finish
    for process in processes:
        process.join()
        