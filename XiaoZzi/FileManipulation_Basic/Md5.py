# coding:utf-8
import hashlib
import os

def fun(path):
        for d_files in os.listdir(path):
            d_files = os.path.join(path,d_files)
            if os.path.isfile(d_files):
                if os.path.splitext(d_files)[1] != '.md5':
                    m1 = hashlib.md5()
                    m1.update(d_files.encode('utf-8'))
                    f = open('md5.txt','a')
                    f.write(str(m1) + ':' + d_files.encode('utf-8'))
                    f.write('\n')
                    f.close()
            else:
                fun(d_files)

path = unicode('D:\\My Work\\直播测试','utf-8')
fun(path)