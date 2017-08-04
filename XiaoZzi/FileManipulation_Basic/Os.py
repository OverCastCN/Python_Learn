import os
fd = os.open('imooc.txt',os.O_CREAT | os.O_RDWR)
n = os.write(fd,'imooc')
l = os.lseek(fd,0,os.SEEK_SET)
str1 = os.read(fd,2)
print str1
os.close(fd)

print os.path.getsize('imooc.txt')
print os.access('immoc.txt',os.X_OK)