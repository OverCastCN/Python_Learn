# -*- coding:utf-8 -*-
def pig(s):
    s = s.lower()
    if s[0] in 'aeiou':
        return s + 'hay'
    elif s[0:2] == 'qu':
        # for i in range(0, len(s)):
            # if s[i] == 'u':
            #     return s[1:i] + s[i+1:-1] + 'qu'
       return s[2:] + 'quay'
    else:
        for j in range(1, len(s)):
            if s[j] in 'aeiouy':
                return s[j:] + s[0:j] +'ay'

# a = raw_input()
# b = a.split()
# for i in range(0,len(b)):
#     print pig(b[i]),

s1 = raw_input()
index = 0
s2 = ''

while index < len(s1) - 1:
    if s1[index] > s1[index + 1]:
        s2 += s1[index]
    else:
        s2 = s2 * 2

    index += 1

print s2

f = open('names2.txt')
count = []
maxlength = 0
for line in f:
    line = line.strip()
    if line[::1] == line[::-1]:
        count.append(line)
for i in range(len(count)):
    if len(count[i]) > len(count[maxlength]):
        count[maxlength] = count[i]
print count[maxlength]
f.close()