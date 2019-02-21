#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# （1）通过代码随机生成1000个样本的arg序列（arg是由ABCD四个字母随机组成的）
# ，生成文件名为num.txt，文件的具体格式如下[20分]：
import random
arg='ABCD'
a=open('num.txt','w')#写入文本
for i in range(1,1001):
    s=''
    for j in range(20):#循坏20次
        s+=random.choice(arg)
    a.write('S'+str(i).zfill(5)+'\t'+s+'\n')
a.close()
# # （2从num.txt生成的500条数据中随机取出一条例如S00003		ABACADAAABABTBTAACAC）；
# # 和生成的1000条数据进行一一比对，但是最后附加相似度数据项；
dict1={}
dict2={}
b=open('num.txt','r')#读取文本
for i in b:
    i=i.replace('\n','')
    dict1[i]=0
b.close()
# searchResult.txt样本数据的顺序需要按着和输入样本的相似度降序排序：
# （输入样本应该出现在第一行）[26分]