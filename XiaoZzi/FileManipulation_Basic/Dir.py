#coding:utf-8
import os, sys

def getFileName(path):
    print path
    f_list = os.listdir(path)
    for i in f_list:
        # print i
        i = os.path.join(path, i)
        # print i
        if os.path.isfile(i):
            if os.path.splitext(i)[1] == '.txt':
                filepath = open('filename.txt','a')
                filepath.write(i.encode('utf-8'))
                filepath.write('\n')
                filepath.close()
                print i
        elif os.path.isdir(i):
            # print i
            getFileName(i)

if __name__ == '__main__':
    path = unicode('F:\\My Study\\性能测试Loadrunner','utf-8')
    # path = unicode('F:\\My Study\\linux学习笔记','utf-8')
    # path = unicode(r'F:\My Study\linux学习笔记\test','utf-8')
    getFileName(path)

    # print os.path.isfile('filename.txt')
    # print os.path.isfile('语法.txt')
    # print os.path.isdir('语法.txt')
d = unicode(r'F:\My Study\linux学习笔记\test','utf-8')
for j in os.listdir(d):
    j = os.path.join(d,j)
    if os.path.isfile(j):
        if os.path.splitext(j)[1] == '.txt':
            # print j
            pass