#coding:utf-8
"""
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
a = raw_input()
if a[::1] == a[::-1]:
    print '%s is palindrome number' % a
else:
    print '%s is not palindrome number' % a


"""
有 3 个回文数字，第一个是两位数，第二个是三位数。
将这两个数字相加得到第三个数字，这是个四位数。请问第三个数字式多少？
"""
def is_palindrome(x):
    x = str(x)
    if x[::1] == x[::-1]:
        return True
    else:
        return False

for i in range(10,100):
    if is_palindrome(i):
        for j in range(100,1000):
            if is_palindrome(j):
                y = i + j
                if is_palindrome(y) and len(str(y)) == 4:
                    print i, j, y