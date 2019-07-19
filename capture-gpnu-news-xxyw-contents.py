# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:52:32 2018

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import bs4
import re
count=0
f = open("urls.txt","r")
for line in f.readlines():
    line = line.strip()
    count+=1
         
    try:
        r = requests.get(line, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print('Error')
        
    soup = BeautifulSoup(r.text, "html.parser")
    s = soup.find_all('div',id=re.compile("^vsb_content"))
    c = open("content1.txt","a+",encoding='utf-8')         
    for i in s:
        c.write(i.get_text())
    c.close()
    print("第%d篇爬取成功！……loading……"%(count))
f.close()
    
print('DONE')