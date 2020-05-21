# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:06:05 2020

@author: safa
"""

from NewConfPar import AVLExecution
import threading as th
import time

StartTime = time.time()
BaseAVLInputFileName = 'test.avl'

InDirectory = r'C:\Users\Dell\Documents\GitHub\Athena-Vortex-Lattice-Python\Windows\AVL Files'   
AlphaRange = [0,3,6,9,12,15] 
ConfNum = 9
threads = list()
if __name__ == '__main__':
    for conf in range(ConfNum):
        for alpha in range(len(AlphaRange)):
            ## creating threads
            threads.append(th.Thread(target=AVLExecution,args=(conf,alpha,BaseAVLInputFileName,InDirectory)))
            
    ## starting threads
    for thread in threads:
        thread.start()
    
    ## wait until all threads finish
    for thread in threads:
        thread.join()
        