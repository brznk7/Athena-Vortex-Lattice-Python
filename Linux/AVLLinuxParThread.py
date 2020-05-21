#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:31:03 2020

@author: safa
"""

from NewConfPar import NewConf
import threading as th

BaseAVLInputFileName = 'test.avl'
Directory = '/home/safa/Desktop/Athena-Vortex-Lattice-Python-master/AVL Files/In/'

    
AlphaRange = [0,3,6,9,12,15] 
ConfNum = 9
threads = list()
for conf in range(ConfNum):
    for alpha in AlphaRange:
        ## creating threads
        threads.append(th.Thread(target=NewConf,args=(conf,alpha,BaseAVLInputFileName,Directory)))

## starting threads
for thread in threads:
    thread.start()
    
## waiting to all threads to stop
for thread in threads:
    thread.join()
    