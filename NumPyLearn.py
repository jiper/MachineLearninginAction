# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:17:49 2018

@author: suxiaolin
"""


#学习numpy要建立起面向向量变成的思想

import numpy as np
#通过二维列表创建二维数组
List1 = [[1,2],[3,4],[5,6]]
Array1 = np.array(List1)

#array的维数
print (Array1.shape)

#sum函数，求和函数
Array2 = Array1.sum(axis=1)   #每行求和
Array3 = Array1.sum()  #所有元素求和
Array4 = Array1.sum(axis=0)  #没列求和

##tile函数
#原型numpy.tile(A,reps)
#tile共有2个参数，A指待输入数组，reps则决定A重复的次数。整个函数用于重复数组A来构建新的数组。
Array4= np.tile(Array1,[3,2])  #行重复3次，列重复2此

#argsort函数
y=Array2.argsort()  #将Array2中的元素从小到大排列，提取其对应的index(索引)，然后输出到y。

#dict.get(key, default=None)
Dic1={'name':'jian','age':28}
sex = Dic1.get('sex',0)
#key -- 字典中要查找的键。
#default -- 如果指定键的值不存在时，返回该默认值值。

#==============================================================================
# 1. 按键值对对字典进行排序
# sorted(iterable,key,reverse)，sorted一共有iterable,key,reverse这三个参数。
# 其中iterable表示可以迭代的对象，例如可以是dict.items()、dict.keys()
# ，key是一个函数，用来选取参与比较的元素，reverse则是用来指定排序是倒序还是顺序
# ，reverse=true则是倒序，reverse=false时则是顺序，默认时reverse=false。
#sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
#==============================================================================
