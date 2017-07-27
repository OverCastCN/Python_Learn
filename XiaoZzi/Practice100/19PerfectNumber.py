# coding:utf-8
"""
一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
"""
def prime_sum(i):
    l = []
    for j in range(1,i):
        if i % j == 0:
            l.append(j)
    return sum(l)
for i in range(1,1000):
    if i == prime_sum(i):
        print i