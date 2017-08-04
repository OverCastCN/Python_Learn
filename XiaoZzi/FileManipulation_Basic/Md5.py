# coding:utf-8
"""
遍历目录及其子目录，得到所有文件的md5的值，并输出到txt
"""
import hashlib
import os


"""
方法一使用递归
"""


def fun(path):
        for d_files in os.listdir(path):
            d_files = os.path.join(path,d_files)
            if os.path.isfile(d_files):
                if os.path.splitext(d_files)[1] != '.md5':
                    m = open(d_files,'rb')
                    m1 = hashlib.md5()
                    m1.update(m.read())
                    h = m1.hexdigest()
                    f = open('md5.txt','a')
                    f.write(str(h) + ':' + d_files.encode('utf-8'))
                    f.write('\n')
                    f.close()
                    m.close()
            else:
                fun(d_files)


"""
方法二，使用os.walk(),不需要递归
"""


def oswalk(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file = os.path.join(root,file)
            m = open(file, 'rb')
            m1 = hashlib.md5()
            m1.update(m.read())
            h = m1.hexdigest()
            f = open('md5.txt', 'a')
            f.write(str(h) + ':' + file.encode('utf-8'))
            f.write('\n')
            f.close()
            m.close()

path = u'D:\\My Work\\直播测试'
# fun(path)
oswalk(path)