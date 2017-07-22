# -*- coding:utf-8 -*-
"""
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""
l = []
def toPrimeRec(n):
    for i in range(2,n):
        if n % i == 0:
            n = n / i
            l.append(str(i))
            return toPrimeRec(n)
    else:
        l.append(str(n))

n = int(raw_input())
toPrimeRec(n)
print l
# for i in range(len(l)):
#     if i == 0:
#         print 'n =',l[i],
#     else:
#         print '*',l[i],
print '%d=' %n + '*'.join(l)
