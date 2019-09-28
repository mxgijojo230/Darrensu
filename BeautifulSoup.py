# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:24:23 2019

@author: DarrenSu
"""
#intcude 所需的module
import bs4 
import urllib.request as res1 

#新增url
html = "https://www.mobile01.com/topiclist.php?f=246"

#加入user-agent
user= res1.Request(html,headers={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"})

#打開網址
with res1.urlopen(user) as resopn:
    data=resopn.read().decode("utf-8");

#使用beautifulsoup分析HTML格式
root=bs4.BeautifulSoup(data,"html.parser")
print(root.div.attrs)
#設定要抓取Html格式中標籤下的檔案
#print(root.title.string)

#使用find尋找Html中需要的部分
#find("標籤",篩選條件)
title=root.find_all("div",class_="c-listTableTd__title") #增加篩選條件
#print(title.a.string)
#進行資料篩選,如果title中有A的話才會把資料印出
with open('mobile.txt','w',encoding = "utf-8") as fopen:
    for check in title:
        if check.a != None:
            fopen.write(check.a.string+"\n")
            print(check.a.string);
            
            