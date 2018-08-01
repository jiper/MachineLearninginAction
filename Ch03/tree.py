# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 09:17:51 2018

@author: suxiaolin
"""

from numpy import *
import numpy as np
#def calcShannonEnt (dataSet):
    
    
def createDataSet():
    dataSet = [[1,1,'yes'],
            [1,1,'yes'],
            [1,0,'no'],
            [0,1,'no'],
            [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels


dataSet,Labels = createDataSet()
SampleLen = len(dataSet)
category =np. array(dataSet)[:,2]