#coding:utf-8
"""
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""
def f(s):
    if len(s) > 0:
        print s[-1]
        f(s[0:-1])
f('abc')
a = 'abc'
print a[0:2]