# coding:utf-8
import io
import sys
import codecs
f3 = codecs.open('PracticeFile','w','utf-8')
print f3.encoding
f3.close()

print type(sys.stdin)
print sys.stdin.mode
# sys.stdin.read()
print sys.argv

f = open('PracticeFile','w')
f.write('股份')
# f.flush()
# print f.read()
# f.write('q')
# list = f.readlines()
# print list
print f.fileno()
print f.tell()
print f.mode
print f.closed
f.close()

print io.DEFAULT_BUFFER_SIZE

f2 = open('PracticeFile')
iter_f = iter(f2)
lines = 0
for line in iter_f:
    lines += 1
print lines

# list_f = []
# for i in range(10):
#     list_f[i] = open('PracticeFile','r')
#     print '%d:%d' % (i,list_f[i].fileno())