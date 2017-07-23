# coding:utf-8
f = open('F:\PythonLearm\Python_Learn\XiaoZzi\FileManipulation_Basic\\PracticeFile','r+')
f.write('q')
f.flush()
print f.read()
f.close()