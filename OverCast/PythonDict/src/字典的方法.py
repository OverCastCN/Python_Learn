ourDict = dict(zip("hello","12345"))
print ourDict
print ourDict.keys()

print ourDict.values()
print ourDict.get("e")
print ourDict.get("w")
print ourDict.get("w","no found")

ourDict.update(h=9)
print ourDict
ourDict.update(w=3)
print ourDict
print ourDict.setdefault("h")
print ourDict.setdefault("k")
print ourDict.setdefault("k",16)