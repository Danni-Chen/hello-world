# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:47:17 2018

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import bs4

raw = 'http://news.gpnu.edu.cn/index/xxyw'

f = open("urls.txt","a+",encoding='utf-8')
    
urls = []
#titles = []
for i in range(34,0,-1):
    if i == 34:
        url = raw+".htm"
    else:
        url = raw+'/'+str(i)+'.htm'
            
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print('Error')
        break
            
    soup = BeautifulSoup(r.text, "html.parser")
        
    al = soup.find_all('a',target="_blank")
    for a in al:
        href = a.get('href')
        #title = a.get('title')
        u = 'http://news.gpnu.edu.cn/info/'+href[-13:]+'\n'
        #t = title+'\n'
            
        if u not in urls:
            #print(u,t)
            print(u)
            urls.append(u)
            #titles.append(t)
            f.write(u)
            #f.write(t)
f.close()
