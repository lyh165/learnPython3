# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1、while循环
# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum = 0
n = 99
while  n > 0:
	sum = sum + n
	n = n - 2
print(sum)
# 在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。
# 练习 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('hello,',name)

# 2、break
# 在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
"""
n = 1
while  n < 100:
	print(n)
	n = n + 1
print('end')
"""

# 上面的代码可以打印出1~100。如果要提前结束循环，可以用break语句：
n = 1
while  n < 100:
	if n > 10: #当n > 11时,条件满足 执行break
		break #break 语句会结束当前循环
	print(n)
	n = n + 1
print("end")

# 3、continue
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
n = 0
while  n < 10:
	n = n + 1
	print(n)
# 上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：

n = 0
while  n < 10:
	n = n + 1
	if n % 2 == 0: #如果是偶数，执行continue
		continue #continue语句会直接继续下一次循环，后续的print（）语句不会执行
	print(n)
# 4、小结
"""
小结
循环是让计算机做重复任务的有效的方法。
break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。
请试写一个死循环程序。
"""

# 5、死循环
a = 1
while a:
	print("死循环")


