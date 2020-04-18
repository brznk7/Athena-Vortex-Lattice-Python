# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:17:44 2020

@author: safa
"""

import os
import numpy as np

AlphaRange = np.arange(0,10,1)
## CREATE AVL RUN FILE
RunFileName = 'AVLRun.run'

for alpha in AlphaRange:   
    OutFileName = 'Out\AVLOut'+'_Alpha'+str(alpha)+'.st'
    file = open(RunFileName,'w+')
    file.write('load AVLINput.avl\n')
    file.write('OPER\n')
    file.write('A A '+str(alpha)+'\n')
    file.write('X\n')
    file.write('ST\n')
    file.write(OutFileName+'\n')
    file.write('QUIT')
    file.close()
    ## EXECUTION
    os.system("avl.exe < AVLRun.run")


