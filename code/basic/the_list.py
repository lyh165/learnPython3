# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


classmates = ['li','yu','hong']
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
#print(classmates[3]) 
#当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
# IndexError: list index out of range

print(classmates[-1]) #获取索引的最后一个（倒数第一）元素
print(classmates[-2]) #获取索引的倒数第二个元素
print(classmates[-3]) #获取索引的倒数第三个元素
#print(classmates[-4]) 
# print(classmates[-4])  IndexError: list index out of range 越界

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
# 1、append 追加
classmates.append('cool')
print(classmates)

#2、insert 插入 (指定索引 也就是指定所加入的位置)
classmates.insert(0,'my name is')
print(classmates)

#3、pop 删除末尾的元素 或者 删除指定位置的元素
classmates.pop()
print(classmates)

classmates.pop(0)
print(classmates)

#4、替换指定元素 xx[i] = xx
classmates[0] = 'Li'
print(classmates)

#5、list元素可以存储不同类型
Lists = ['python',666,True]
print(Lists)

#6、list元素也可以是另外一个list
ls = ['python','ios',['app','web'],'android']
print(ls)
print('----')
a = ['android','ios']
b = ['php','python',a,'web']
print(a)
print(b)
print(b[2][0],b[2][1])
