#coding:utf-8
"""
两位整数相乘形成的最大回文数是 9009 = 99 × 91。编写程序，求得任意输入的 n 位整数相乘形成的最大回文数。
"""
# a = int(raw_input())
#
# b = 10 ** a - 1
#
# lst = []
# for i in range(b ** 2):
#     if str(i)[::1] == str(i)[::-1]:
#         lst.append(i)
#
# lst2 = []
# for j in lst:
#     for k in range(2,b+1):
#         if j % k == 0 and j/k <= b:
#             lst2.append(j)
#
# print lst2[-1]


"""
输入单词若字母相同算作一类，按类分行输出，由小到大排列
"""
def get_new_str_sort(s):
    l = list(s)
    l.sort()
    s = ''.join(l)
    return s

s = ''
dict = {}
for line in iter(raw_input,''):
    sort_s = get_new_str_sort(line)
    if sort_s in dict:
        dict[sort_s].append(line)
    else:
        dict[sort_s] = [line]
print dict

lst=[]
len_lst=[]
new_dic={};

for (k,v) in  dict.items():
    #v.sort()
    one_len=len(v)
    if one_len in new_dic:
        new_dic[one_len].append(v[0])
    else:
        new_dic[one_len]=[v[0]]
    if one_len not in len_lst:
        len_lst.append(one_len)
len_lst.sort(reverse=True)
print new_dic
print len_lst

all_word=[]
for word_num in len_lst:
    for keys in new_dic[word_num]:
        new_keys=get_new_str_sort(keys);
        print ' '.join(dict[new_keys])
