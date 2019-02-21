
# import random
# print("从range(100)返回一个随机数:",random.choice(range(100)))
# print("从列表[1,2,3,5,9]) 返回一个随机元素:",random.choice([1,2,3,5,9]))
# print("从字符串中'Runoob' 返回一个随机字符:",random.choice('Runoob'))

# import random
# print("randrange(1,100,2):",random.randrange(1,100,2))
# print("randrange(100):",random.randrange(100))


# import random
# print("random():",random.random())
# print("random():",random.random())

# import random
# random.seed()
# print("使用默认种子生成随机数:",random.random())
# random.seed(10)
# print("使用整数种子生成随机数:",random.random())
# random.seed("hello",2)
# print("使用字符串种子生成随机数：",random.random())

# import random
# list=[20,16,10,5]
# random.shuffle(list)
# print("随机排序列表：",list)
# random.shuffle(list)
# print("随机排序列表：",list)

# import random
# print("uniform(5,10)的随机浮点数:",random.uniform(5,10))
# print("uniform(7,14)的随机浮点数:",random.uniform(7,14))

# import random
# print("randint(0,10)的随机整数:",random.randint(0,10))
# print("random(0,1000000)的随机整数:",random.randint(0,1000000))

# a="Hello"
# b="Python"
#
# print("a+b输出结果:",a+b)
# print("a*2输出结果:",a*2)
# print("a[4]输出结果:",a[4])
# print("a[1:4] 输出结果:",a[1:4])
#
# if("H" in a):
#     print("H在变量a中")
# else:
#     print("H不在变量a中")

# print (r'\n')
# print (R'\n')

# a="hello world I am Anna"
# print(a.find("Anna",0,29))

# a="hello world I am Anna"
# print(a.index("or",0,25))

# a="hello world I am Anna"
# print(a.count("n",0,25))

# a="hello world I am Anna"
# b=a.replace("l","b",5)
# print(b)

# a="hello world I am Anna"
# b=a.split(" ")
# print(b)

dat = input('请输入某年某月某日，格式为 yyyy-mm-dd ：')
y = int(dat[0:4])  #获取年份
m = int(dat[5:7])  #获取月份
d = int(dat[8:])  #获取日

ly = False

if y%100 == 0:  #若年份能被100整除
    if y%400 == 0:  #且能被400整除
        ly = True  #则是闰年
    else:
        ly = False
elif y%4 == 0:  #其它情况下，若能被4整除
    ly = True  #则为闰年
else:
    ly = False

if ly == True:  #若为闰年，则2月份有29天
    ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0
for i in range(1, 13):  #从1到12逐一判断，以确定月份
    if i == m:
        for j in range(i-1):  #确定月份i之后，则将ms列表中的前i-1项相加
            days += ms[j]
        print('%s是该年份的第%s天。' % (dat, (days + d))) #最后再加上“日”，即是答案
