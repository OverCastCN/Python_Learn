#coding:utf-8
"""
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
"""
w = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

a = raw_input('please input the first char:')
l = []
for i in w:
    if i[0] == a:
        l.append(i)
if len(l) == 1:
    print 'It is %s' %l[0]
else:
    b = raw_input('please input the second char:')
    for j in l:
        if j[1] == b:
            print 'It is %s' %j