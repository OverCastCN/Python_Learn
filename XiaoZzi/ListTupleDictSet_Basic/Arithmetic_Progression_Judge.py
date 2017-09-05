#coding:utf-8

a = raw_input()
source_array = map(int, a.split())
source_array.sort()

fall = []
for j in range(len(source_array)-1):
    fall.append(source_array[j+1]-source_array[j])
if len(set(fall)) == 1:
    print 'is arithmetic progression'
else:
    print 'is not arithmetic progression'