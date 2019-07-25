# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:54:13 2018

@author: Administrator
"""

import jieba
txt = open("content.txt", encoding="utf-8").read()
stopwords = [line.strip() for line in open("content1.txt",encoding="utf-8").readlines()]
'''for ch in'!"：。，！.':
    txt=txt.replace(ch," ")'''
words  = jieba.lcut(txt) 
counts = {}

for word in words:
    if word not in stopwords:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 

f = open("content-wfa.txt","a+",encoding='utf-8')
for i in range(40):
    word, count = items[i]
    f.write(word+"\t")
    f.write(str(count)+"\n")
    print ("%s\t\t%d"%(word,count))
f.close()