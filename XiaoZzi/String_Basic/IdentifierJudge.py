# -*- coding:utf-8 -*-
"""
判断一个字符串是否为合法python标识符
输入格式:
一系列字符串，每个字符串占一行。
输出格式：
判断每行字符串是否为合法的 Python 标示符，如果合法则输出 True，否则输出 False。
"""

import keyword

def judge(s):
    if keyword.iskeyword(s):
        return False
    elif s[0] == '_' or ord(s[0]) in (range(ord('a'),ord('z')+1) or range(ord('A'),ord('Z')+1)):
        for i in range(len(s)):
            if s[i] != '_' and ord(s[i]) not in (range(ord('a'), ord('z') + 1) or range(ord('A'), ord('Z') + 1)) and type(
                            s[i]) != int:
                 return False
        return True
    else:
        return False

stopwoed = ''
str = ''
for line in iter(raw_input, stopwoed):
    str += line + ' '
arr = str.split()
for i in range(len(arr)):
    print judge(arr[i])