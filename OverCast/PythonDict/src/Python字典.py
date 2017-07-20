# coding:utf-8
# 字典
# zip函数
print "zip函数："
print zip((1,2,3),['a','b','c'])
print zip((1,2,3),['a','b','c'],"cde")
print zip((1,2,3),['a','b','c'],"cdeg")
print
print "dict定义："
print dict([(1,2),('a',1),('b',3)])
print str(dict(zip("abcde",range(1,6)))) + " 这里可以看出字典是无序的"
print
print "fromkeys："
print {}.fromkeys("abcde")
print {}.fromkeys("abcde",range(1,6))

print
print "字典的特点："
ourDict = dict(zip("hello","12345"))
print  ourDict
# 1.以键取值

print ourDict["e"]
print ourDict["l"]
ourDict["l"] = "hi"
print ourDict
print
print  "键的类型："
print {1:'a','a':{2,3},(1,2):3}