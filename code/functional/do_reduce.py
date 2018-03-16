# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# reduce函数
"""
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""
from functools import reduce

#一、方说对一个序列求和，就可以用reduce实现：
def add(x,y):
	return x + y
print(reduce(add,[1,3,5,7,9]))
print('对一个序列求和，可以用reduce---\n')
# 当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。

"""
二、果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
"""
def fn(x,y):
	return x * 10 + y
print(reduce(fn,[1,3,5,7,9]))
print('把序列[1, 3, 5, 7, 9]变换成整数13579---\n')
#三、个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：

def char2num(s):
	digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	return digits[s]

print(reduce(fn,map(char2num,'13579')))
print('str转换为int的函数---\n')

#四、整理成一个str2int的函数就是：
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn,map(char2num,s))
print(str2int('23132'))
print('一个str2int---\n')
"""
简单来说，编程中提到的 lambda 表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
这一用法跟所谓 λ 演算（题目说明里的维基链接）的关系，有点像原子弹和质能方程的关系，差别其实还是挺大的。
lambda 匿名函数
lambda x,y : x * 10 + y
意思是 一个匿名函数 存入两个参数 返回 x * 10 + y
"""
from functools import reduce
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def char2num(s):
	return DIGITS[s]

def str2int(s):
	return reduce(lambda x,y: x * 10 + y,map(char2num,s))

print('lambda匿名函数:str2int--',str2int('2223'))
print('\n')

# 练习一
"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
"""

def normalize(name):
    str=''
    for i,v in enumerate(name): # 遍历数组 根据每个字符的第一位去判断
        if(i==0):
            str+=v.upper(); # 将第一个字符转成大写
        else:
            str+=v.lower(); # 将 之后的字符转成小写
    return str

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
print('---\n')
# 练习二
"""
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""
def multi(x,y):
    return x*y

def prod(L):
	return reduce(multi,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

print('---\n')

# 练习三
"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
"""
# map
# def str2float(s):



# reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def f(x, y):
    return x * 10 + y
def str2int(ss):
    return DIGITS[ss]
def str2float(s):
	s1 = s.split('.') # 将存进来的数 以 .进行分割 然后获取整数和小数部分
	num1 = reduce(f, map(str2int, s1[0]))
	num2 = reduce(f, map(str2int, s1[1]))/(10**len(s1[1])) # 10的3次方 = 1000
	return num1 + num2

print(str2float('123.222'))