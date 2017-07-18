ourList = range(20)
print  ourList
print  ourList[0]
print  ourList[-1]
print  ourList[0:10]
print  ourList[:13]
print  ourList[0:]
print  ourList[:]
print  ourList[0:10:2]
print  ourList[::2]
print  ourList[::-1]

ourList[0]  = 'a'
print  ourList

ourList[1:3]  = 'a','b'
print  ourList

del ourList[-1]
print  ourList