# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:44:10 2020

@author: safa
"""

import os
Directory = r'C:\Users\Dell\Desktop\Parallel AVL\Python\Out'+'\\'
AllFiles = os.listdir(r'C:\Users\Dell\Desktop\Parallel AVL\Python\Out')

OutFiles = list()
AllRawData = list()
for filename in AllFiles:
    if '.st' in filename:
        OutFiles.append(filename)
        FileToRead = open(Directory+filename,'r')
        RawData = list()
        for line in FileToRead:
            line = line.replace(' ','')
            RawData.append(line)
        AllRawData.append(RawData)
        
        

SearchStr = ['Sref','Cref','Bref',\
             'Xref','Yref','Zref',\
             'Alpha','pb/2V',"p'b/2V",\
             'Beta','qc/2V',\
             'Mach','rb/2V',"r'b/2V",\
             'CXtot','Cltot',"Cl'tot",\
             'CYtot','Cmtot',\
             'CZtot','Cntot',"Cn'tot",\
             'CLtot','CDtot',\
             "CDvis",'CDind',\
             'CLff','CDff',\
             'CYff','e',\
             'camber','aileron','elevator','rudder',\
             'CLa','CLb','CYa','CYb',\
             'Cla','Clb','Cma','Cmb','Cna','Cnb',\
             'CLp','CLq','CLr',\
             'CYp','CYq','CYr',\
             'Clp','Clq','Clr',\
             'Cmp','Cmq','Cmr',\
             'Cnp','Cnq','Cnr',\
             'CLd1','CLd2','CLd3','CLd4',\
             'CYd1','CYd2','CYd3','CYd4',\
             'Cld1','Cld2','Cld3','Cld4',\
             'Cmd1','Cmd2','Cmd3','Cmd4',\
             'Cnd1','Cnd2','Cnd3','Cnd4',\
             'CDff1','CDffd2','CDffd3','CDffd4',\
             'ed1','ed2','ed3','ed4',\
             'Xnp','ClbCnr/ClrCnb']

Dict = dict()
for searchStr in SearchStr:
    for line in RawData:
        if searchStr+'=' in line:
            for i,j in enumerate(line):
                Index = line.find(searchStr)+len(searchStr)+1
                Data = line[Index:Index+i+2]
                try:
                    Data = float(Data)
                    Dict[searchStr] = Data
                except:
                    break
            break
            
    


