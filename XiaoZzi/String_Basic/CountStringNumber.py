# -*- coding:utf-8 -*-
"""
依次计算一系列给定字符串的字母值，字母值为字符串中每个字母对应的编号值（A对应1，B对应2，以此类推，不区分大小写字母，
非字母字符对应的值为0）的总和。例如，Colin 的字母值为 3 + 15 + 12 + 9 + 14 = 53
输入格式:
一系列字符串，每个字符串占一行。
输出格式：
计算并输出每行字符串的字母值。
"""

"""
python提供两个内置函数ord('char')、chr('int')，实现字符和ASCII的转换
"""
#计算字符串的值
def countnumber(a):
    count = 0
    a = a.lower()
    for i in a:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            count += ord(i)-ord('a')+1
    return count

#获取多行字符串后，换行输出其对应的值
stopword = ''
str = ''
for line in iter(raw_input, stopword):
    str += line + ' '
ar = str.split()
for i in range(len(ar)):
    print countnumber(ar[i])
