#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:28:23 2020

@author: safa
"""
def AVLExecution(ConfNo,Alpha,BaseAVLInputFileName,Directory,GeomData,Ref): 
    import os
    os.chdir(Directory)

 
#########################################################         
    ## BASE AVL FORMAT
    BaseFormatFile = open(Directory+'\\'+BaseAVLInputFileName)
    BaseFormatData = list()
    
    for line in BaseFormatFile:
        BaseFormatData.append(line)
        
    BaseFormatFile.close()
       
    NewConfData = BaseFormatData.copy()
    Space = '     '  
    ## Wing Root Section
    NewConfData[25] = '0.0'+Space+'0.0'+Space+'0.0'+\
                      Space+str(GeomData['Croot'])+Space+'0.0'+Space+'0.0'+Space+'0.0' 
    ## Wing Tip Section
    NewConfData[35] = str(GeomData['Xtip'])+Space+\
                      str(GeomData['Span']/2)+Space+'1.0'+\
                      Space+str(GeomData['Ctip'])+Space+'0.0'+Space+'0.0'+Space+'0.0' 
                      
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
