#coding:utf-8
"""
按相反的顺序输出列表的值。
"""

a = ['11', '22', '33', '44']
# a.reverse()
# for i in range(len(a)):
#     print a[i]

for i in a[::-1]:
    print i

lst = [1,2,3]
for j in lst:
    print j

"""
输出整个列表包含逗号。
"""
print  ','.join(n for n in a)