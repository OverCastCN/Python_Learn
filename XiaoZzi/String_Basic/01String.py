#coding:utf-8

"""
如果一个01串任意两个相邻位置的字符都是不一样的,我们就叫这个01串为交错01串。
例如: “1”,”10101”,”0101010”都是交错01串。
小易现在有一个01串s,小易想找出一个最长的连续子串,并且这个子串是一个交错01串。
小易需要你帮帮忙求出最长的这样的子串的长度是多少
"""

a = '010000100011010101011'

l = []
for start in range(len(a)-1):
    for end in range(start, len(a)-1):
        i = end
        if a[i+1] == a[i]:
            break
    l.append(a[start:end+1])
print l

max_length = max(map(len, l))
for i in l:
    if len(i) == max_length:
        print i
print max_length
