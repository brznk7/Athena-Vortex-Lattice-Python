# -*- coding: utf-8 -*-
"""
Created on Sat May  2 14:31:59 2020

@author: safa
"""

def CreateConfData(Sref,SpanRange,TaperRatioRange):
    import pandas as pnd
    SpanList = list()
    TrList = list()
    CrootList = list()
    CtipList = list()
    XtipList = list()
    for span in SpanRange:
        for tr in TaperRatioRange:
            SpanList.append(span)
            TrList.append(tr)
            CrootList.append(2*Sref/(span*(1+tr)))
            CtipList.append(2*Sref/(span*(1+tr))*tr)
            XtipList.append(2*Sref/(span*(1+tr))*(1-tr)/4)
    Data = {'Span':SpanList,'TaperRatio':TrList,'Croot':CrootList,'Ctip':CtipList,'Xtip':XtipList}
    Frame = pnd.DataFrame(data=Data)
    return Frame