# -*- coding:utf-8 -*-
"""
编写vowel_count函数，计算一个字符串中元音字母（aeiou或AEIOU）的数目
"""

def vowel_count(a):
    count = 0
    for i in a:
        if i in 'aeiouAEIOU':
            count += 1
    print count

teststring = 'helloworld aeiou yt AEIOU'
vowel_count(teststring)


