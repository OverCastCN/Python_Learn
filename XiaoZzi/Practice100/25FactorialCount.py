#coding:utf:8
"""
求1+2!+3!+...+20!的和
"""
ss = 0
for i in range(1,21):
    s = i
    for j in range(1,i):
        s = s * j
    print s
    ss += s
print ss

"""
利用递归的方法求5！
"""
def f(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * f(n-1)
print f(5)