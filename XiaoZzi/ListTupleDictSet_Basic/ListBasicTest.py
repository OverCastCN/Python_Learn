#coding:utf-8
"""
 使用http://www.pythontutor.com/可以查看代码的执行过程
"""
lst = [1,2.3]
lst.extend([4,5,6])
print lst
l = [1,2,3]

print l.append(4)

t = ('a', 'b', ('A', 'B'))
print len(t)
dict = {'123':123,'345':345}
# dict[0][0] = 4
# print dict[0][0]

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key,v in d.items():
    print key,':',v

a = set(['A','B','C'])
for i in a:
    print i

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
# print d.itervalues()
# for v in d.itervalues():
#     print v
# print d.values()
print d.items()
print d.iteritems()
for x in d.iteritems():
    print x[0],':',x[1]
#
# lst = []
# # s = 0
# for i in range(10):
#     lst.append(float(raw_input()))
#     # s += lst[i]
# print sum(lst)/len(lst)

"""
列表赋值
"""
a = [0,1,2,3,4,5,6]
# b = a
# b = a[:]
# b[1] = 100
a.insert(1,a.pop(2))
print a
"""
直接查找
"""
def search(lst,i):
    for a in range(len(lst)):
        if lst[a] == i:
            return a
        else:
            return -1
"""
二分查找
"""
def bi_search(lst,i):
    min = 0
    max = len(lst) -1
    while min <= max:
        mid = (min + max)/2
        if i == lst[mid]:
            return mid
        elif i > lst[mid]:
            min = mid + 1
        else:
            max = mid - 1
    return -1
print bi_search(a,1)

"""
列表排序
"""
#直接排序，如果元素小往前插入后删除
lst = [2,5,8,1,3,6,9]
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst.insert(i,lst.pop(min_index))#添加元素后删除

selection_sort(lst)
print lst
#直接排序，如果元素小进行交换
lst2 = [2,5,8,1,3,6,9]
def swap(lst,i,j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
def select_sort2(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                swap(lst,i,j)
select_sort2(lst2)
print lst2
#冒泡排序，如果元素大排到最后
lst3 = [2,5,8,1,3,6,9]
def buble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                swap(lst,j,j+1)
buble_sort(lst3)
print lst3
"""
列表嵌套及排序
"""
x = [[5,4,7,3],[4,8,9,7],[5,1,2,3]]
print len(x)
print x[1]
print x[1][2]
# def f(a):
#     return a[1]
x.sort(key=lambda a:a[1],reverse=True)
print x
"""
表达式
"""
print sum(i for i in range(1,7) if 6 % i == 0)

"""
DSU,根据单词的长度对一个单词列表进行排序
"""
words = ['ade','segbb','ad']
def sort_by_length(words):
    #decorate
    t = []
    for word  in words:
        t.append((len(word),word))
    #sort
    t.sort(reverse = True)
    #undecorate
    res = []
    for length,word in t:
        res.append(word)
    return res

words.sort(key=lambda x:len(x),reverse=True)
print words
