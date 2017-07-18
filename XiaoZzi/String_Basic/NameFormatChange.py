# -*- coding:utf-8 -*-
"""
读取人名列表文件names.txt,将每个人名转换为单词首字母大写，其它字母小写的格式
文件操作：
f = open(filename,mode)
    --mode有r(读，默认)，w（写）等
按行读取文件内容：
for line in f：
关闭文件：
f.close()
写文件
f.write(str)
更多说明：
https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
"""

f = open('names','r')
"""
人名的每个单词首字母大写
"""
for line in f:
    line = line.strip() #解决两个回车的问题，去掉前后空格回车
    # print line #print本身有一个回车，加之文件有一个回车
    print line.title()
print '--------------------------------------------------------------------'

"""
为什么把代码写在这个地方是读取不到line2的，需要再次open一个f2?
"""
# for line2 in f:
#     line2 = line2.strip()
#     if line2[::1].lower() == line2[::-1].lower():
#         print line2

f.close()

f2 = open('names','r')
"""
判断人名是否为回文，比如Bob,忽略大小写
"""
for line2 in f2:
    line2 = line2.strip()
    if line2[::1].lower() == line2[::-1].lower():
        print line2

print '--------------------------------------------------------------------'

f2.close()

#使用递归判断是否回文
def is_panlindrom_rec(name):
    if len(name) <=1:
        return True
    else:
        if name[0:] != name[:-1]:
            return False
        else:
            return is_panlindrom_rec(name[1:-1])
#使用index判断是否回文
def is_panlindrom(name):
    low = 0
    high = len(name)
    while low < high:
        if name[low] != name[high]:
            return False
        low += 1
        high -= 1
    return True

"""
判断人名是否含有C.A模式
"""
import re

f3 = open('names')

pattern = '(C.A)'

for line3 in f3:
    name = line3.strip()
    result = re.search(pattern, name)
    if result:
        print 'Find in {}'.format(name)

f3.close()