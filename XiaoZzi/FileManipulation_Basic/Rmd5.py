# coding:utf-8
"""
已知txt中md5的值，从一个目录中得到这些文件，拷贝到另一个文件夹
"""
import hashlib
import os
import shutil

def getdir_md5(cf, md5,ct):  #目录地址，MD5文件地址，拷贝文件到ct地址
    for d_file in os.listdir(cf):
        d_file = os.path.join(cf, d_file)
        if os.path.isfile(d_file):
            if os.path.splitext(d_file)[1] != '.md5':
                m = open(d_file,'rb')
                m1 = hashlib.md5()
                m1.update(m.read())
                h = m1.hexdigest()   #求cf目录里文件md5的值
                for i in getmd5_list(md5): #遍历给出的md5的列表
                    if str(h) == i:  #判断与求出的目录中的文件的md5值是否相等
                        shutil.copy(d_file,ct)   #如果相等，copy到targetpath
                m.close()

        if os.path.isdir(d_file):
            getdir_md5(d_file, md5,ct)   #如果是子目录，需要递归

def getmd5_list(md5path):   #得到md5文件中的md5,返回MD5组成的列表
    lst = []
    f = open(md5path,'r')
    a = f.readlines()
    for i in range(len(a)):
        lst.append(a[i].strip())
    f.close()
    return lst


copy_from = u'D:\\My Work\\直播测试'
md5_id = 'Rmd5.txt'
copy_to = u'D:\\My Work\\md5'

getdir_md5(copy_from,md5_id,copy_to)

