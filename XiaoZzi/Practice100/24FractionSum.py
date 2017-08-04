#coding:utf-8
"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
a = 2.0
b = 1.0
s = a/b
for i in range(19):
    a, b = a+b, a
    s += a/b
print s
