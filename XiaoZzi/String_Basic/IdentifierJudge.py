# -*- coding:utf-8 -*-
"""
判断一个字符串是否为合法python标识符
"""

import keyword

def judge(s):

    if s[0] == '_' or ord(s[0]) in (range(ord('a'),ord('z')+1)  or range(ord('A'),ord('Z')+1)):
        for i in range(len(s)):
            if s[i] != '_' and s[i] not in (range(ord('a'), ord('z') + 1)) or range(ord('A'), ord('Z') + 1) and type(
                    s[i]) != int:
                return False

    elif keyword.iskeyword(s):
        return False

    else:
        return True

s = 'od'
if s[0] != '_' and ord(s[0]) not in (range(ord('a'), ord('z') + 1) or range(ord('A'), ord('Z') + 1)):
    print False
else:
    print True

stopwoed = ''
str = ''
for line in iter(raw_input, stopwoed):
    str += line + ' '
arr = str.split()
for i in range(len(arr)):
    print judge(arr[i])