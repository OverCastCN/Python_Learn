#coding:utf:8
"""
求1+2!+3!+...+20!的和
"""
s = 1
ss = 0
for i in range(1,21):
    for j in range(1,i):

        s = 1
        k = i * j
        s = s * k
    print s
#     ss += s
# print ss