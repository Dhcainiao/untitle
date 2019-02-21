#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# f = open('test.txt', 'w')
# f.write('hello world,i am here!')
# f.close()

# f=open('test.txt','r')
# content=f.read(5)
# print(content)
# print("-"*30)
# content=f.read()
# print(content)
# f.close()

# f=open('test.txt','r')
# content=f.readlines()
# print(type(content))
# i=1
# for temp in content:
#     print("%d:%s"%(i,temp))
#     i+=1
# f.close()

# f=open('test.txt','r')
# content=f.readline()
# print("1:%s"%content)
# content=f.readline()
# print("2:%s"%content)

# f=open('test.txt','r')
# con=f.read(3)
# print("读取的数据是:",con)
# position=f.tell()
# print("读取当前的位置：",position)
# print("-"*10)
# con=f.read(3)
# print("读取的数据收是：",con)
# position=f.tell()
# print("读取当前的位置:",position)
# f.close()

# f=open("test.txt","r")
# str=f.read(30)
# print("读取的数据是:",str)
# #查找当前位置
# position=f.tell()
# print("当前文件位置：",position)
# #重新设置位置
# f.seek(5,0)
# #查找当前位置
# position = f.tell()
# print("当前文件位置：",position)
# f.close()
#
# f=open("test.txt","r")
# position=f.tell()
# print("当前文件位置：",position)
# #重新设置位置
# f.seek(0,2)
# #读取到的数据为：文件最后3个字节数据
# str=f.read()
# print("读取的数据：",str)
#
# f.close()

# import os
# os.rename("毕业论文.txt","毕业论文-最终版.txt")

# import os
# os.remove("毕业论文-最终版.txt")

# import os
# os.mkdir("小王")
# print(os.getcwd())
# os.chdir("F:/")
# print(os.getcwd())
# os.rmdir("小王")
# try:
#    print ('-----test--1---')
#    open('123.txt','r')
#    print ('-----test--2---')
# except FileNotFoundError:
# print("文件不存在")


