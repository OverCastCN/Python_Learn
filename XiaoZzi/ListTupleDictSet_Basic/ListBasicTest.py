#coding:utf-8
lst = [1,2.3]
lst.extend([4,5,6])
print lst
l = [1,2,3]

print l.append(4)

t = ('a', 'b', ('A', 'B'))
print len(t)
dict = {'123':123,'345':345}
# dict[0][0] = 4
# print dict[0][0]

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key,v in d.items():
    print key,':',v

a = set(['A','B','C'])
for i in a:
    print i

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
# print d.itervalues()
# for v in d.itervalues():
#     print v
# print d.values()
print d.items()
print d.iteritems()
for x in d.iteritems():
    print x[0],':',x[1]
#
# lst = []
# # s = 0
# for i in range(10):
#     lst.append(float(raw_input()))
#     # s += lst[i]
# print sum(lst)/len(lst)

"""
列表赋值
"""
a = [1,2,3,4]
b = a
# b = a[:]
b[1] = 100
print a[1]
