# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一、关键字参数
"""
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
"""

def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)
person('li',20)
person('li',33,city='GZ')
person('li',33,gender='F',city='GZ')
print('---')

"""
关键字参数有什么用？它可以扩展函数的功能。
比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。
试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
"""
extra = {'city':'BJ','job':'IT'}
person('h',22,city=extra['city'],job=extra['job'])
print('===')
# 简化写法
extra1 = {'city':'GZ','job':'IT'}
person('y',23,**extra1)
print('---')
# 二、命名关键字参数
"""
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
仍以person()函数为例，我们希望检查是否有city和job参数：
"""
def person1(name,age,**kw):
	if 'city' in kw:
		# 有city参数
		print('有city参数')
		pass
	if 'job' in kw:
		# 有job参数
		print('有job参数')
	else:
		print('没有job参数')
	print('name:',name,'age:',age,'other:',kw)
person1('s',34,city='SZ',addr='SG',zipcpde=123)	
print('---')
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person2(name, age, *, city, job):
	print(name, age, city, job)
person2('q',21,city='bj',job='it')
print('---')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person3(name,age,*args,city,job):
	print(name,age,args,city,job)
# person3('Jack', 24, 'Beijing', 'Engineer') # TypeError: person3() missing 2 required keyword-only arguments: 'city' and 'job'
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：



# 命名关键字参数可以有缺省值，从而简化调用：
def person4(name,age,*,city="GZ",job):
	print(name,age,city,job)
person4('s',11,job='it')

"""
使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
"""
def person5(name,age,city,job):
	# 缺少*, city和job被视为位置参数
	pass


# 三、参数组合
"""
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

比如定义一个函数，包含上述若干种参数：
"""

def f1(a,b,c=0,*args,**kw): 
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):# a,b是必选,c是默认，*是可变参数，d是命名关键字参数 **kw是关键字参数
	print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
print('---')
f2(1,2,d=33,ext=None)

print('~~~~')

# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = (1,2,3,4)
kw = {'d':44,'x':'y'}
f1(*args,**kw)
print('---')

args = (1,2,3)
kw = {'d':55,'x':'q'}
f2(*args,**kw)
print('---')
"""
所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
"""

"""
四、练习:
以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：


"""
def product(*x): # x是一个list 或者是一个tuple
    if x==():
        raise TypeError('参数不能为空')
    else:
        for i in x:
            if not isinstance(i,(int,float)):
                raise TypeError('类型错啦，只能是int和float')
    result=x[0]
    if len(x)==1:
        pass
    elif len(x)==0:
        return 0
    else:
        i=1
        while i<len(x): # 遍历数组 看数组的长度 然后一个一个进行乘积
            result=result*x[i] 
            i=i+1
    return result

# print(product())
# print(product('A'))

print(product(2))
print(product(1,2,3))


"""
五、小结
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
"""