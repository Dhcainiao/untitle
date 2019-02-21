#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# （一）随机mtDNA序列（50分）
# （1）．使用代码随机生成20000个样本的mtDNA序列（mtDNA是由AGCT四个字母随机组成的），生成文件名为dnaData.txt，文件的具体格式如下[20分]：
# S00001	AGCT….CTAG
# S00002    TTAG….AGCT
# ……………………………………………….
# S20000    ATAG….TGAT
# 评分标准：
# ①样本编号必须连续，且从S00001到S20000（5分）
# ②样本的mtDNA序列的长度必须为20（5分）
# ③每个位置的氨基酸(A、G、C、T)必须随机生成（5分）
# ④按照格式将数据存入文件（5分）
# （2） 编写一个函数，该函数有两个输入，一个为前面产生的dnData.txt样本文件，一个是某一个样本的编号（假定该样本的编号一定存在于dnData.txt中,例如S00003		ATAGAGTAATAGTGTAAGAT）；函数输出一个文件，文件名为searchResult.txt。 searchResult.txt的格式和dnData.txt的格式基本一致，但是最后附加相似度数据项；
# searchResult.txt样本数据的顺序需要按着和输入样本的相似度降序排序：（输入样本应该出现在第一行）[30分]。
# 例：S00001		    AGCTACGTACTTATAGCTAG
#     S00002		TTAGACGTAGTTATAGAGCT
# 两个mtDNA序列的相似度为：两个序列中字母相同的个数。
# 样本S00002与样本S00001的相似度为11
# 样本S00003与样本S00002的相似度为8
# ①正确生成searchResult.txt文件（7分）
# ②searchResult.txt文件中的第一行应为输入样本（5分）
# ③searchResult.txt文件中应存在20000条样本（5分）
# ④searchResult.txt文件中，先后按照降序排列（8分）
# ⑤求出并输出所有相似度的平均数（5分）
import random
seed = "ACGT"
s = ""
with open('dna.txt','w') as f:
    for i in range(2000):
        f.write("S" +str(i+1).zfill(4)+"  " )
        for j in range(20):
            f.write(random.choice(seed))
        f.write("\n")
def fun(filename,num):
    dict1 = {}
    with open('dna.txt', 'r') as f1:
        for i in range(2000):
            c = f1.readline()
            list1 = c.split("  ")
            dict1[list1[0]] = list1[-1][:-1]
        print(list1)
        print(dict1)
    with open('rest.txt','w') as f2 :
        count,sum1 = 0, 0
        dict2 = {}
        for k, v in dict1.items():
            for i in range(len(v)):
                if v[i] == dict1[num][i]:
                    count += 1
            dict2[k] = count
            sum1 += count
            count = 0
        dict3 = sorted(dict2.items(),key=lambda x:x[1],reverse=True) #字典里的排序 以v排序 x[1]表示value
        for k,v in dict3:
            f2.write('样本%s    与   样本%s的相似度为%d\n'%(k,num,v))
        f2.write('所有样本的平均相似度为%.2f'%(sum1/len(dict2)))
fun("dna.txt",'S0023')


