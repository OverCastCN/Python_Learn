# -*- coding:utf-8 -*-
"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
"""

# %r不知道数据类型编译器自动识别，%s字符串，%d整型

year = int(raw_input('请输入年份：'))
month = int(raw_input('请输入月份：'))
day = int(raw_input('请输入日期：'))

def isleapyear(year):
    if year % 4 == 0 and year % 100 == 0 or year % 400 ==0:
        return True
    else:
        return False

def count_day_of_month(year,month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    else:
        if isleapyear(year):
            return 29
        else:
            return 28

count = 0
if month == 1:
    print '这是这一年的第%d天' %day
if month >1:
    for i in range(1,month):
        count += count_day_of_month(year,i)
    print '这是这一年的第%d天' %(count + day)