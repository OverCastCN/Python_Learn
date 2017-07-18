# -*- coding:utf-8 -*-
"""
countBy为负数
"""

a = 'abcdefg hijklmn opqrst'
print a[::-1]
print a[:4:-1]
print a[:4:]
print a[:-4:-1]

#结论：左开右闭，按照start和finish的索引（正数左边从0，负数右边从-1），确定子串
#      根据countBy绝对值确定间距，根据正负判断正向逆向

"""
字符串更改：replace(old,new),生成一个新的子串
"""
s = 'hello'
s = s.replace('l','L')
print s

"""
子串查找：find
"""
print s.find('LL')
print s.find('LLA')
print s.find('a')

#结论：找到要查找的字符串，返回第一个字母的索引，如果没有返回-1

"""
字符串分割
"""
print a.split()
print a.split(' ', 1)
#结论：默认以空格为分割，从做到右，每遇到分隔符进行一次分割，进行num次分割