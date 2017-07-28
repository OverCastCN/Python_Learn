#coding:utf-8
"""
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
a = raw_input()
if a[::1] == a[::-1]:
    print '%s is palindrome number' % a
else:
    print '%s is not palindrome number' % a