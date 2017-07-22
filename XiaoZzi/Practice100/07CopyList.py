# -*- coding:utf-8 -*-
"""
将一个列表的数据复制到另一个列表中
"""
a = [1,2,3]
b = a
print b

#python2
import copy
b = copy.copy(a)
print b

#python3
# b = a.copy()
# print(b)