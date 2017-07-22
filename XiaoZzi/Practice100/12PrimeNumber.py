# -*- coding:utf-8 -*-
"""
判断101-200之间有多少个素数，并输出所有素数。
"""
def isPrime(i):
    for j in range(2,i):
        if i % j == 0:
            return False
    else:
        return True
count = 0
for i in range(101,201):
    if isPrime(i):
        count += 1
        print i
print 'The total is',count
