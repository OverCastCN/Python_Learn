example = range(10)
example.append(1)
print example

example = range(10)
example.append([1,2])
print example

example = range(10)
example.extend([1,2])
print example

example = range(10)
example.insert(0,"a")
print example

example = range(10)
example.insert(-1,"a")
print example

example = range(10)
print example

example = range(10)
print example.pop()

example = range(10)
print example.pop(3)

example = list("abcde")
example.remove("a")
print example

example = list("helloworld")
print example.count("l")
print example.index("o")


example = list("helloworld")
print example
example.reverse()
print example
example.sort()
print example