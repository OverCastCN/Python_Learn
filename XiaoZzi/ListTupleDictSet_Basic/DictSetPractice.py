#coding:utf-8
"""
计算一个字符串中字母出现的次数
"""


s = 'hudhufhipaa'

d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print d

"""
计算富文本emma.txt中出现的最频繁的单词
"""


f = open('emma.txt')

word_frea = {}

for line in f:
    words = line.strip().split()
    for word in words:
        if word in word_frea:
            word_frea[word] += 1
        else:
            word_frea[word] = 1

freq_word = []
for word, freq in word_frea.items():
    freq_word.append((freq, word))
freq_word.sort(reverse=True)

for freq, word in freq_word[:10]:
    print word

f.close()

"""
生成一个新字典，其键为原字典的值，值为原字典的键
"""

d1 = {'zhang':123,'wang':456,'Li':123,'Zhao':456}
d2 = {}

for name, room in d1.items():
    if room in d2:
        d2[room].append(name)
    else:
        d2[room] = [name]
print d2


"""
中文分词,正向最大匹配分词
"""
def load_dict(filename):
    word_dict = set()
    max_len = 1
    f = open(filename)
    for line in f:
        word = unicode(line.strip(),'utf-8')
        word_dict.add(word)
        if len(word) > max_len:
            max_len = len(word)
    return max_len,word_dict

def fmm_word_seg(sent,max_len,word_dict):
    begin = 0
    words = []
    sent = unicode(sent,'utf-8')

    while begin < len(sent):
        for end in range(begin + max_len,begin,-1):
            if sent[begin:end] in word_dict:
                words.append(sent[begin:end])
                break
        begin = end
    return words

max_len, word_dict = load_dict('lexicon.dic')
sent = raw_input('Input a sentence:')
words = fmm_word_seg(sent,max_len,word_dict)
for word in words:
    print word

# a = {{1, 2}, {3, 4}}
a = {[1, 2], [3, 4]}
# a = (1,2,3)
print a
