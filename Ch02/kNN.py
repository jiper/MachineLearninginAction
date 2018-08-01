# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 15:39:38 2018

@author: JianLinpeng
"""
#from numpy import *
import numpy as np
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir

plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）

def createDataSet():
    group = np.array ([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX, dataSet, labels, k):
    dataSetSize= dataSet.shape[0]
    DiffMat = np.tile(inX,[dataSetSize,1])-dataSet
    DiffSquareMat = DiffMat**2
    DiffSquareSum = DiffSquareMat.sum(axis=1)
    SortNum = DiffSquareSum.argsort()
    LabelDic={}
    for i in range(k):
        VoteLable = labels[SortNum[i]]
        LabelDic[VoteLable]=LabelDic.get(VoteLable,0)+1
    SortedLableCount = sorted(LabelDic.items(),key=operator.itemgetter(1),reverse=True)
    return SortedLableCount[0][0]
        
def file2matrix(filename):
    DataSet=[]
    LabelSet=[]
    with open(filename,'r') as f:
        line=f.readline()
        while line:
            SingleData = []
            Nums = line.split('\t')
            SingleData.append(float(Nums[0]))
            SingleData.append(float(Nums[1]))
            SingleData.append(float(Nums[2]))
            LabelSet.append(int(Nums[3][0]))
            DataSet.append(SingleData)
            line=f.readline()
    DataSet = np.array(DataSet)
    return DataSet,LabelSet
            
   
if __name__ =='__main__':
    datingDataMat,datingLabels = file2matrix("datingTestSet2.txt")
    fig = plt.figure()    
    ax = fig.add_subplot(111)
    plt.xlabel(r'飞行')  
    plt.ylabel(r'冰')  
    plt.legend('x1') 
    ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*np.array(datingLabels),15.0*np.array(datingLabels))
    ax.set_title(r"散点图")
    plt.legend('x1') 
    plt.show()
    