#coding:utf-8
"""
求100之内的素数。
"""
import math
for i in range(2,100):
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            # print '%d is not prime number' % i
            break
    else:
        print '%d is prime number' % i

