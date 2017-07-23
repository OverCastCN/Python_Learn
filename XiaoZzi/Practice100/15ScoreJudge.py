# -*- coding:utf-8 -*-
"""
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
"""
score = int(raw_input('请输入一个百分制分数：'))
p = ''
if score > 100 or score < 0:
    print '分数无效'
elif score >= 90:
    p = 'A'
elif score >= 60:
    p = 'B'
else:
    p = 'C'
print '%d属于%s' %(score,p)