# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
一、在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回。

我们以自定义一个求绝对值的my_abs函数为例：
"""

"""
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(-99))
"""

"""
当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
"""
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

"""
请自行测试并调用my_abs看看返回结果是否正确。

请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。

在Python交互环境中定义函数时，注意Python会出现...的提示。函数定义结束后需要按两次回车重新回到>>>提示符下：
"""

"""
二、空函数
如果想定义一个什么事也不做的空函数，可以用pass语句：
"""

def nop():
	pass
"""
pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
pass还可以用在其他语句里，比如：
"""

# if age>=18:
#	pass

# 三、参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
# my_abs(1,2) # TypeError: my_abs() takes 1 positional argument but 2 were given

# 但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别：
# my_abs('A') #  raise TypeError('bad operand type')
# TypeError: '>=' not supported between instances of 'str' and 'int'

# abs('A')
# TypeError: bad operand type for abs(): 'str'

#四、返回多个值
"""
函数可以返回多个值吗？答案是肯定的。
比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
"""

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

"""
import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
然后，我们就可以同时获得返回值：
"""
x,y = move(100,100,60,math.pi / 6)
print(x,y)
# 但其实这只是一种假象，Python函数返回的仍然是单一值：

"""
原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
"""

"""
五、小结
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
"""

"""
六、练习
提示:一元二次方程公式 
https://baike.baidu.com/item/%E4%B8%80%E5%85%83%E4%BA%8C%E6%AC%A1%E6%96%B9%E7%A8%8B/7231190?fr=aladdin#4

请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。

提示：计算平方根可以调用math.sqrt()函数：
"""
import math
print('2的²是',math.sqrt(2))

def quadratic(a,b,c):
"""
△ = b²-4ac
①当 △ > 0时，方程有两个不相等的实数根；
②当 △ = 0时，方程有两个相等的实数根；
③当 △ < 0时，方程无实数根，但有2个共轭复根。
"""	
    d = b*b - 4*a*c # △读“德尔塔”
    if a==0:
        print('a≠0是一元二次方程的前提条件')
        return None
    if d>0:
        sqrt = math.sqrt(d)
        return (-b+sqrt)/(2*a),(-b-sqrt)/(2*a)
    elif d==0:
        return -b/(2*a)
    else :
        print('无解')

print('quadratic(2,3,1) = ',quadratic(2,3,1))
print('quadratic(1,3,-4) = ',quadratic(1,3,-4))
"""
求根公式法
用求根公式法解一元二次方程的一般步骤为：
①把方程化成一般形式  ，确定a，b，c的值（注意符号）；
②求出判别式  b²-4ac 的值，判断根的情况；
③在  b²-4ac>=0（注：此处△读“德尔塔”）的前提下，把a、b、c的值代入公式 进行计算，求出方程的根。
 2x² + 3x + 1 = 0 
 △ =   b²-4ac >0
x1 = -b - △ / 2a  
x1 = -3 - 1 / 4
x1 = -1

x2 = -b + △ / 2a
x2 = -3 + 1 / 4
x2 = -0.5

 1x² + 3x - 4 = 0

"""
if quadratic(2,3,1) !=(-0.5,-1):
	print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


