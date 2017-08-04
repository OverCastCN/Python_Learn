#coding:utf-8
"""
打印菱形
"""
for i in range(8):
    if i % 2 != 0:
        print ('*  ' * i).center(50)
j = 5
while j > 0:
    if j % 2 != 0:
        print ('*  ' * j).center(50)
    j -= 1