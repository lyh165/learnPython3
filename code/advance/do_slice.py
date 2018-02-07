# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一、切片
"""
取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
"""
L = ['li','yu','hong','good','cool']
"""
取前3个元素，应该怎么做？
笨办法：
"""
print([L[0],L[1],L[2]])
print('---')

"""
之所以是笨办法是因为扩展一下，取前N个元素就没辙了。
取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：
"""
r = []
n = 3
for i in range(n):
	r.append(L[i])
print(r)
print('---')


# 切片
"""
对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
对应上面的问题，取前3个元素，用一行代码就可以完成切片：
"""
print(L[0:3])
print('---')
"""
L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
如果第一个索引是0，还可以省略：
"""
print(L[:3])
print('---')
"""
也可以从索引1开始，取出2个元素出来：
"""
print(L[1:3])
print('---')


# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print(L[-2:])
print(L[-2:-1])
"""
记住倒数第一个元素的索引是-1。
"""

# 二、使用切片
# 切片操作十分有用。我们先创建一个0-99的数列：
L = list(range(100))
print(L)
print('---')
# 可以通过切片轻松取出某一段数列。比如前10个数：
print(L[:10])
# 后10个数：
print(L[-10:])
# 前11-20个数：
print(L[10:20])
# 前10个数，每两个取一个：
print(L[:10:2])
# 所有数，每5个取一个：
print(L[::5])
# 甚至什么都不写，只写[:]就可以原样复制一个list：
print(L[:])



# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
S = (0,1,2,3,4,5)
print(S[:3])

# 三、练习
"""
利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
"""
# def trim(a):

# 	if a=='':
# 		return a
# 	if a[:1] == ' ':
#         a = trim(a[1:])
#     elif a[-1:] == ' ':
#         a = trim(a[:-1])
#     return a

def trim(s):
    if s[:1] == ' ':
        s = trim(s[1:]) # 使用递归方法和切片方法进行处理 如果第一个为空格 那么则s使用递归进行字符串切片 获取之后的字符
    elif s[-1:] == ' ': 
        s = trim(s[:-1]) # 如果最后一个是空格 ，那么 就是用递归方式 进行再一次获取之前的值 
    return s

print(trim(' hello '))

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

