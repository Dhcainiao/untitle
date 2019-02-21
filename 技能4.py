#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#1.有一列分数序列，2／1，3／2，5／3，8／5。。。求出前20项之和
# a=2.0
# b=1.0
# s=0
# for n in range(1,21):
#     s+=a/b
#     t=a
#     a=a+b
#     b=t
# print(s)
# #2.二 输入一个数求1！+2！+3！+4！+n！=？
# Sum=0
# factorial=1
# num=int(input("请输入一个数字："))
# for i in range(1,num+1):
#     factorial=factorial*i
#     Sum+=factorial
# print('阶乘之和：',Sum)
# #3.有四个数字1，2，3，4，能组成多少个互不相同的三位数
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i!=k)and(i!=j)and(j!=k):
#                 print(i,j,k)
#4.实现100-200里面所有的质数字,打印这些质数并且求出个数
# import math #导入math库，以便使用里面的一个求平方根的函数
# l = [101, 103] #因为range函数上限不能小于下线，所以2,3预先加到素数列表中，直接从5开始（因为知道4不是素数）循环
# for i in range(107, 201): #第一层循环，从100到201
#     for j in range(2, int(math.sqrt(i))+1): #第二层循环，逐个判断是否有因子
#         if i%j == 0: #如果出现整除说明有因子
#             break #跳出循环判断下一个
#     else: #如果第二层循环结束还没有跳出的话
#         l.append(i) #说明是素数，加到列表里
# print(" ".join(map(str, l))) #先将列表中的元素变为字符串再用空格连接输出

# import  math
# l=[101,103]
# for i in range(107,201):
#     for j in range(2,int(math.sqrt(i))+1):
#         if i%j==0:
#             break
#     else:
#         l.append(i)
# print(" ".join(map(str,1)))
#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
# a=2
# b=1
# s=0
# for i in range(1,21):
#     s+=a/b
#     t=a
#     a=a+b
#     b=t
# print(s)
# # 2.二 输入一个数求1！+2！+3！+4！+n！=？
#
# Sum=0
# f=1
# num = int(input('请输入一个数字：'))
# for i in range(1,num+1):
#     f = f*i
#     Sum +=f
# print('阶乘之和：',Sum)
#3.有四个数字1，2，3，4，能组成多少个互不相同的三位数
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i!=j)and(i!=k)and(j!=k):
#                print(i,j,k)
# a=[]
# for i in range(100,201):
#     b=0
#     for x in range(2,i-1):
#         if i%x==0:
#             b+=1
#     if b==0:
#         a.append(i)
# print(a)
# print(len(a))

# a=[]
# for i in range(100,201):
#     b=0
#     for x in range(2,i-1):
#         if i%x==0:
#             b+=1
#     if b==0:
#         a.append(i)
# print(a)
# print(len(a))
#电脑随机生成1~100随机数，用户输入一个数字，
# 电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止。
import  random
x=random.randint(1,100) #电脑随机生成1~100随机数
print(x)
num=int(input("请输入一个数："))#用户输入一个数字
# if(x>num):
#     print("小：",(x,num))
# elif(x<num):
#     print("大")
# else:
#     print('猜对')
while x==num:
    print('猜对了:',(x,num))
    break
if(x>num):
    print('小',(x,num))
elif(x<num):
    print("大:",(x,num))

