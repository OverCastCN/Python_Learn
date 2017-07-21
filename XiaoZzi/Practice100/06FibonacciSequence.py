# -*- coding:utf-8 -*-
"""
题目：斐波那契数列。
"""
#方法一：
def f1(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a
# 输出了第10个斐波那契数列
# print f1(10)
#方法二：
def f2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f2(n -1) + f2(n - 2)
# print f2(10)
#方法三：如果你需要输出指定个数的斐波那契数列，可以使用以下代码：
def f3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
# 输出前 10 个斐波那契数列
print f3(10)
#方法四：
def f4(n):
    list = [1,1,2]
    if n <= 3:
        print list[n]
    else:
        for i in range(n-3):
            list[i % 3] = list[(i - 1) % 3] + list[(i - 2) % 3]
            print list[i % 3],
f4(10)
