ourDict = {'a':1,'b':2,'c':3,'d':4,'l':[1,2]}

otherDict = ourDict.copy()
ourDict["a"]=2
# 'l'部分的地址一个内存地址，
ourDict["l"][1] ='a'
print ourDict
print otherDict