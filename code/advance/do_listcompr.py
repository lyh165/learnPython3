# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

"""
举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
"""
lists = list(range(1,11))
print(lists)
print('1---')
"""
但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
"""
L = []
for x in range(1,11):
	L.append(x * x)
print(L)
print('2---')


# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
list2 = [x * x for x in range(1,11)]
print(list2)
print('3---')
"""
写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，
就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
"""
list3 = [x * x for x in range(1,11) if x%2==0]
print(list3)
print('3---')

# 还可以使用两层循环，可以生成全排列：
list4 = [m+n for m in 'ABC' for n in 'XYZ']
print(list4)
print('4---')

"""
三层和三层以上的循环就很少用到了。

运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
"""
import os #导入os模块
list5 = [d for d in os.listdir('.')] #os.listdir 可以列出文件和目录
print(list5)
print('5---')

# 二、for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
		print(k,'=',v)
print('6---')
# 因此，列表生成式也可以使用两个变量来生成list：
list6 = [k + '=' + v for k,v in d.items()]
print(list6)
print('7---')

# 最后把一个list中所有的字符串变成小写：
L = ['Hello','World','BD','TX']
list7 = [s.lower() for s in L]
print(list7)
print('8---')

# 三、练习
"""
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
"""
L = ['Hello', 'World', 18, 'Apple', None]
# list8 = [s.lower() for s in L]
# print(list8) # AttributeError: 'int' object has no attribute 'lower'

# print('9---')

# 四、使用内建的isinstance函数可以判断一个变量是不是字符串：
x = 'abc'
y = 123
print(isinstance(x,str))
print(isinstance(y,str))


# 练习答案
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s,str)] 
# 遍历L这个list  判断L这个list里面每一个元素是不是str,如果是转成小写

print('L2=',L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')