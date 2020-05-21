#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:28:23 2020

@author: safa
"""
def AVLExecution(ConfNo,Alpha,BaseAVLInputFileName,Directory): 
    import numpy as np
    import os
    os.chdir(Directory)
    ## References
    Ref = dict()
    Ref['S'] = 15.94
    Ref['b'] = 9.96
    Ref['C'] = 1.56
    Ref['Taper'] = 0.2 
    Ref['Xdist'] = 4.4
    Ref['Ydist'] = 0.0
    Ref['Zdist'] = 0.0
    ## Taper Ratio Search
    TaperRatios = np.arange(0.1,1,0.1)
    RootChords = np.zeros((TaperRatios.size,))
    TipChords = np.zeros((TaperRatios.size,))
    for i,tp in enumerate(TaperRatios):
        RootChords[i] = Ref['S']*2/Ref['b']/(1+tp)
        RootChords[i] = round(RootChords[i],2)
        TipChords[i] = RootChords[i]*tp
        TipChords[i] = round(TipChords[i],2)
 
#########################################################         
    ## BASE AVL FORMAT
    BaseFormatFile = open(Directory+'\\'+BaseAVLInputFileName)
    BaseFormatData = list()
    
    for line in BaseFormatFile:
        BaseFormatData.append(line)
        
    BaseFormatFile.close()
       
    NewConfData = BaseFormatData.copy()
    Space = '     '
    ## References
    NewConfData[6] = str(Ref['S'])+Space+str(Ref['C'])+Space+str(Ref['b']) 
    NewConfData[8] = str(Ref['Xdist'])+Space+str(Ref['Ydist'])+Space+str(Ref['Zdist'])    
    ## Wing Root Section
    NewConfData[25] = '0.0'+Space+'0.0'+Space+'0.0'+\
                      Space+str(RootChords[ConfNo])+Space+'0.0'+Space+'0.0'+Space+'0.0' 
    ## Wing Tip Section
    NewConfData[35] = '0.2'+Space+str(Ref['b']/2)+Space+'1.0'+\
                      Space+str(TipChords[ConfNo])+Space+'0.0'+Space+'0.0'+Space+'0.0' 
                      
    ## New Configuration Input File
    NewInpFileName = 'AVLInputConf_'+str(ConfNo)+'.avl'
    NewInpFile = open(Directory+'\\In\\'+NewInpFileName,'w+')
    for line in NewConfData:
        NewInpFile.write(line+'\n')
    NewInpFile.close()
    
#################################################################
    InpFileName = r'In\AVLInputConf_'+str(ConfNo)+'.avl'
    OutFileName = r'Out\AVLOutConf_'+str(ConfNo)+'Alpha'+str(Alpha)
    RunFileName = r'Run\AVLRunConf_'+str(ConfNo)+'Alpha'+str(Alpha)+'.run'
    RunFile = open(RunFileName,'w+')
    
    AVLRunCommand = ['load',InpFileName,'OPER','A A ',str(Alpha),'X','st',OutFileName]
    for line in AVLRunCommand:
        RunFile.write(line+'\n')
    RunFile.close()
       
    CmdCommand = "avl.exe < "+RunFileName
    os.system(CmdCommand)
