#coding:utf-8
"""
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""
a = raw_input('请输入一个不多于5位的正整数:')
while len(a) > 5:
    print '请输入一个不多于5位的正整数'
    a = raw_input('请输入一个不多于5位的正整数:')
print '它是%d位数'%len(a)
def f(a):
    if len(a) > 0:
        print a[-1]
        return f(a[0:-1])
f(a)