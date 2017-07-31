# coding:utf-8
"""
已知txt中md5的值，从一个目录中得到这些文件，拷贝到另一个文件夹
"""
import hashlib
import os
import shutil

l = []
def getdir_md5(dirpath,md5path):  #目录地址，MD5文件地址，拷贝文件到哪个地址
    for d_file in os.listdir(dirpath):
        d_file = os.path.join(dirpath,d_file)
        if os.path.isfile(d_file):
            if os.path.splitext(d_file)[1] != '.md5':
                m = open(d_file,'rb')
                m1 = hashlib.md5()
                m1.update(m.read())
                h = m1.hexdigest()   #求出目录地址里文件的MD5值
                # print 'strh',str(h)
                for i in getmd5_list(md5path): #遍历给出的md5的列表
                    # print 'i',i
                    if str(h) == i:  #判断与求出的目录中的文件的md5值是否相等
                        print 'equal',i
                        print d_file
                        l.append(d_file)
                        print len(l)
                        break
                        # shutil.copy(d_file,targetpath)   #如果相等，copy到targetpath
                        # print str(h)
                        # print 'd_file:',d_file
                        # print 'targetpath',targetpath
                        # pass
                m.close()

        if os.path.isdir(d_file):
            getdir_md5(d_file,md5path)   #如果是子目录，需要递归
    # print l

    return l

def getmd5_list(md5path):   #得到md5文件中的md5,返回MD5组成的列表
    lst = []
    f = open(md5path,'r')
    a = f.readlines()
    for i in range(len(a)):
        lst.append(a[i].strip())
    f.close()
    # print lst
    return lst


a = u'D:\\My Work\\直播测试'
b = 'Rmd5.txt'
c = u'D:\\My Work\\直播测试\\md5'

getdir_md5(a,b)
for i in getdir_md5(a,b):
    # shutil.copy(i,c)
    pass

