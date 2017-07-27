# -*- coding:utf-8 -*-
import string
"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""
aplha = 0
space = 0
num = 0
other = 0
a = raw_input()
for i in a:
    if i.isalpha():
        aplha += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        num += 1
    else:
        other += 1
print '中英文字母：',aplha
print '空格：',space
print '数字：',num
print '其它：',other

