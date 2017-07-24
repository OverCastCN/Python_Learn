# coding:utf-8
import io
f = open('PracticeFile','w')
f.write('q')
# f.flush()
# print f.read()
# f.write('q')
# list = f.readlines()
# print list
f.close()

print io.DEFAULT_BUFFER_SIZE

f2 = open('PracticeFile')
iter_f = iter(f2)
lines = 0
for line in iter_f:
    lines += 1
print lines

list_f = []
for i in range(10):
    list_f[i] = open('PracticeFile','r')
    print '%d:%d' % (i,list_f[i].fileno())