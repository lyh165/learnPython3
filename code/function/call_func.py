# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 1、函数 
"""
Python内置了很多有用的函数，我们可以直接调用。
要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：
"""

print(abs(100))
print(abs(-200))
print(abs(-200.33))

# 2、调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个：
# print(abs(-200,100)) # TypeError: abs() takes exactly one argument (2 given)

# 3、如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型：
# print(abs('a')) # TypeError: bad operand type for abs(): 'str'
# 4、而max函数max()可以接收任意多个参数，并返回最大的那个：
print(max(1,-20))
print(max(1,-20,33,-55))

print('-------------')
# 数据类型转换
# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：

print(int('123'))
print(int(12.34))

print(float('12.34'))
print(str(1.3344))
print(str(100))
print(bool(1)) # true
print(bool('')) # false
print('-------------')


# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs #变量a指向abs函数
print(a(-55))

# 练习
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
print(hex(33)) # 0x21

"""
小结
调用Python的函数，需要根据函数定义，传入正确的参数。如果函数调用出错，
一定要学会看错误信息，所以英文很重要！
"""