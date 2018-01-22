# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# tuple 
# 另一种有序列表叫元组：tuple。tuple和list非常类似，
# 但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

# 1、 tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t = (1,2)
print(t)

# 2、定义一个空的tuple
t = ()
print(t)

# 3、定义一个只有一个元素的tuple。注意这个是错误写法
t = (1)
print(t)
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
#因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

# 3、定义一个只有一个元素的tuple。正确写法
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
print(t)

# 4、定义一个可变的tuple (tuple是不可变的 可变的只不过是list)
t = ('a','b',['C','D'])
t[2][0] = 'L'
t[2][1] = 'Y'
print(t)

# 5、练习
'''
打印apple
python
lisa
'''
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

# 小结 
"""
list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
"""

