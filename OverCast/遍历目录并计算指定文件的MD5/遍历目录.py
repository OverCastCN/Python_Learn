#!/usr/bin/python
# coding:utf-8

import os
import md5

def dirlist(path):
    filelist = os.listdir(path)
    File = open(u'test.txt', 'a+')
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath)
        else:
            if filepath.endswith('.ppt'):

                File.write(filepath.encode('utf-8')+'\n')

    File.close()
    return

if __name__ == '__main__':
    dirlist(u"F:\\BaiduNetdiskDownload\\C语言从入门到精通")