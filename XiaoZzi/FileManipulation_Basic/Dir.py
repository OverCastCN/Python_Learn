#coding:utf-8
import os

def getFileName(path):
    print path
    f_list = os.listdir(path)
    for i in f_list:
        i = os.path.join(path, i)
        if os.path.isfile(i):
            if os.path.splitext(i)[1] == '.txt':
                filepath = open('dir.txt','a')
                filepath.write(i.encode('utf-8'))
                filepath.write('\n')
                filepath.close()
        elif os.path.isdir(i):
            getFileName(i)

if __name__ == '__main__':
    # path = unicode('F:\\My Study\\性能测试Loadrunner','utf-8')
    path = unicode('D:\\My Study\\Python\\XiaoZzi\\Python_Learn\\XiaoZzi\\FileManipulation_Basic','utf-8')
    # path = unicode('F:\\My Study\\linux学习笔记','utf-8')
    # path = unicode(r'F:\My Study\linux学习笔记\test','utf-8')
    getFileName(path)

    print os.path.isfile(r'D:\\My Study\\Python\\XiaoZzi\\Python_Learn\\XiaoZzi\\FileManipulation_Basic\\dir.txt')
    p = unicode('D:\\My Study\\Python\\XiaoZzi\\Python_Learn\\XiaoZzi\\FileManipulation_Basic\\语法.txt','utf-8')
    print os.path.isfile(p)
    print os.path.isfile (u'D:\\My Study\\Python\\XiaoZzi\\Python_Learn\\XiaoZzi\\FileManipulation_Basic\\语法.txt')
