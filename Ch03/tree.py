# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 09:17:51 2018

@author: suxiaolin
"""

from numpy import *
import numpy as np
import math

def calcShannonEnt (dataSet):
    SampleLen = len(dataSet)
    Entropy = 0.0
    categoryList =np. array(dataSet)[:,-1]
    categorySet = set(categoryList)
    ProbDic ={}
    for category in categorySet:
        ProbDic[category]=0
    for data in dataSet:
        for category in categorySet:
            if data[-1]==category:
                ProbDic[category]= ProbDic[category]+1
                continue
    for value in ProbDic.values():
         probability = float(value)/SampleLen
         Entropy = Entropy + probability*math.log2(probability)
    Entropy = -Entropy
    return Entropy
    
def createDataSet():
    dataSet = [[1,1,'yes'],
            [1,1,'yes'],
            [1,0,'no'],
            [0,1,'no'],
            [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels

def splitDataSet(dataSet,axis,value):   #划分数据集
    TargetDataList= []
    TargetData = []
    for SingleData in dataSet:
        if (SingleData[axis]==value):
            TargetData = SingleData[:axis]
            TargetData.extend(SingleData[axis+1:])
            TargetDataList.append(TargetData)
    return TargetDataList
        
def chooseBestFeatureToSplit(dataSet):  #选择最好的划分方式
    FeatureSum = len(dataSet[0])-1  #特征总数
    dataSetArray = np.array(dataSet)  #列表转化为数组
    BestFeature = 0
    EntropyLeast = 100
    for i in range(FeatureSum):
#        print(i)
        EntropySum = 0.0
        ClassifyList =   dataSetArray[:,i]
        #print (ClassifyList)
        ClassifySet = set(ClassifyList)
#       print (ClassifySet)
        for j in ClassifySet:
            print (j)
            TargetDataList = splitDataSet(dataSet, i ,j)
            prob = len(TargetDataList)/float(len(dataSet))
#            print (TargetDataList)
#            EntropySum += prob*calcShannonEnt(TargetDataList)
        if (EntropySum<EntropyLeast):
            BestFeature = i
#    print (BestFeature)
    return BestFeature
           
    

#==============================================================================

# def chooseBestFeatureToSSplit(dataSet):  #选择最好的划分方式
# def majorityCnt(classList):  #多数表决
# def createTree(dataSet,labels):
#==============================================================================


if __name__ == "__main__":
    dataSet,Labels = createDataSet()
    chooseBestFeatureToSplit(dataSet)
    