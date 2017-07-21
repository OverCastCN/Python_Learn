# -*- coding:utf-8 -*-

"""
随意输入几个整数，请把这几个数由小到大输出。
"""

l = []
str = ''
stop = ''
for i in iter(raw_input,stop):
    str += i + ' '
    print str
str = str.split()
for j in str:
    l.append(int(j))
print l
l.sort()
print l

"""
随意输入三个整数x,y,z,把这三个数由小到大输出
"""
li = []
for i in range(3):
     a = int(raw_input('Integer:'))
     li.append(a)
li.sort()
print li