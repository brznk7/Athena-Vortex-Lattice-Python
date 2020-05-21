# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:06:05 2020

@author: safa
"""

from CreateConfData import CreateConfData
from NewConfPar import AVLExecution
import threading as th
import time
import numpy as np


## References
Ref = {'S':8,'B':10,'C':1}
SpanRange = np.arange(7,11,1)
TaperRatioRange = np.arange(0,1.1,0.1)
ConfSearchData = CreateConfData(Ref['S'],SpanRange,TaperRatioRange)

StartTime = time.time()
BaseAVLInputFileName = 'test.avl'

InDirectory = r'C:\Users\Dell\Documents\GitHub\Athena-Vortex-Lattice-Python\Windows\AVL Files'   
AlphaRange = [0,3,6,9,12,15] 


threads = list()
if __name__ == '__main__':
    for conf in ConfSearchData.index:
        for alpha in range(len(AlphaRange)):
            ## creating threads
            GeomData = {'Span':ConfSearchData.Span[conf],\
                        'TaperRatio':ConfSearchData.TaperRatio[conf],\
                        'Croot':ConfSearchData.Croot[conf],\
                        'Ctip':ConfSearchData.Ctip[conf],\
                        'Xtip':ConfSearchData.Xtip[conf]}
            threads.append(th.Thread(target=AVLExecution,args=(conf,alpha,BaseAVLInputFileName,InDirectory,GeomData,Ref)))
            
    for i in range(int(len(threads)/8)):  
        ThreadChunk = threads[8*i:8*(i+1)]                    
        ## starting threads
        for thread in ThreadChunk:
            thread.start()
            
        ## waiting until all threads finish
        for thread in ThreadChunk:
            thread.join()
        