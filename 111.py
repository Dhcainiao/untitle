
# 计算1-100的总和：

# i=0
# sum=0
# while i<=100:
#     sum+=i
#     i+=1
# print(sum)

# i=1
# while i ==1:
#     print("love you very much")

# i=1
# while i<=8:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print("")
#     i+=1
# i=0
# while i <8:
#     print("love you")
#     i+=1
# else:
#     print("end")

# i=0
# while i<100:
#     print("love")
#     if i ==4:
#         break
#     i+=1

# i=0
# while i<10:
#     i+=1
#     if i==4:
#         continue
# print(i)

# list1=['a','b','c','d','e']
# for i in list1:
#     print(i)

# name=['Anna','Lucy','Jacob','Bunny']
# for i in name:
#     if i =='Jacob':
#         break
#     print(i)
# print("循环结束")

# a=['Google','Baidu','Runoob','Taobao','QQ']
# for i in range(len(a)):
#     print(i,a[i])

# for i in range(5):
#     print(i)
# else:
#     print("end")

# for n in range(2,10):
#     print(n)
#     if n == 3:
#         break
#     elif n>3:
#         print("love")

# for letter in 'Runoob':
#     if letter == 'o':
#         pass
#         print('执行pass快')
#     print('当前字母:',letter)
# print("Good bye!")

# a=2.0
# b=1.0
# s=0
# for n in range(1,21):
#     s+=a/b
#     t=a
#     a=a+b
#     b=t
# print(s)

# Sum=0
# factorial=1
# num=int(input('请输入一个数字:'))
# for i in range(1,num+1):
#     factorial=factorial*i
#     Sum+=factorial
# print('阶乘之和:',Sum)

# import math
# Sum=0
# num = int(input('请输入一个数字:'))
# for i in range(1,num+1):
#     F=math.factorial(i)
#     Sum+=F
# print('阶乘之和:',Sum)

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i!=k)and(i!=j)and(j!=k):
#                 print(i,j,k)

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i!=k)and(i!=j)and(j!=k):
#                 print(i,j,k)

import random
x=[random.randint(0,100) for i in range(20)]
print(x)
y=x[::2]
y.sort()
y.reverse()
x[::2]=y
print(x)