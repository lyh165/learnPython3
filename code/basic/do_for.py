# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 循环 for
"""
要计算1+2+3，我们可以直接写表达式：
1 + 2 + 3

要计算1+2+3+...+10，勉强也能写出来。
但是，要计算1+2+3+...+10000，直接写表达式就不可能了。
为了让计算机能计算成千上万次的重复运算，我们就需要循环语句。
"""

# 1、Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
names = ['li','yu','hong']
for name in names:
	print(name)
# 所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
# 2、再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print(sum)

# 3、如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
lists = list(range(5))
print(lists)

sum = 0
for x in range(101):
	sum = sum + x
print(sum)
