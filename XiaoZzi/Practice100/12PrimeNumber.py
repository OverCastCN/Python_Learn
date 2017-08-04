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

"""
定义一个 prime() 函数求整数 n 以内（不包括n）的所有素数（1不是素数），并返回一个按照升序排列的素数列表。
使用递归来实现一个二分查找算法函数bi_search()，该函数实现检索任意一个整数在 prime() 函数生成的素数列表中位置（索引）的功能，并返回该位置的索引值，若该数不存在则返回 -1。
"""
l = []
n = int(raw_input())
for j in range(2,n):
    if isPrime(j):
        l.append(j)

def bi_search(lst,i):
    low = 0
    high = len(lst) -1
    while low <= high:
        mid = (low + high) / 2
        if i == lst[mid]:
            return mid
        elif i > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

str = ''
a = iter(raw_input,'')
for i in a:
    str += i + ' '
for j in str.split():
    print bi_search(l, int(j))


