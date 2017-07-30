#coding:utf-8
"""
编写程序，输入帕斯卡三角形的高度 n，然后生成杨辉三角的三角形。
"""
def triangles():
    L = [1]
    while True:
        # yield L
        L.append(0)
        # L = [L[i - 1] + L[i] for i in range(len(L))]
        for i in range(len(L)):
            L = [L[i -1] + L[i]]
        print L

n=0
for t in triangles():
    for j in t:
        print j,
    n = n + 1
    if n == 6:
        break
