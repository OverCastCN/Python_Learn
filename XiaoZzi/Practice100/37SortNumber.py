#coding:utf-8
"""
对10个数进行排序
"""
a = raw_input('please input ten number devided by space:')
l = a.split()
lst = []
for i in range(len(l)):
    lst.append(int(l[i]))
for k in range(len(lst) - 1):
    for j in range(len(lst) - 1):
        if lst[j] > lst[j + 1]:
            lst[j],lst[j+1] = lst[j +1],lst[j]
print lst
