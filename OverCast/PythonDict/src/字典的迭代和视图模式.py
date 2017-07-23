#coding:utf-8

# 字典的迭代：
ourDict = dict(zip("hello","12345"))
print ourDict.iteritems()
print ourDict.iterkeys()
print ourDict.itervalues()

item = ourDict.iteritems()
key = ourDict.iterkeys()
value = ourDict.itervalues()

print item.next()
print item.next()
print item.next()
print item.next()
# 停止迭代报错
print item.next()
