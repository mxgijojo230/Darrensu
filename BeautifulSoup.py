# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:18:36 2019

@author: Darren
"""

import bs4 
import requests

uri='https://www.ptt.cc/bbs/movie/index.html'
html=requests.get(uri);

def search_title(soup,research,i):    
    data=soup.find_all(class_="title");
    date=soup.find_all('div',class_="date");
    for j,title in enumerate(data) :
        if title.find('a'):            
            a_title = title.a;
            str_title=title.a.string;
            if research in str_title:
                if not(a_title.string.startswith('Re')or a_title.string.startswith('Fw')): 
                    i=i+1;
                    print("#{} 時間:{}   名稱:{}\n 網址:{}".format(i,date[j].string,str_title,a_title.get("href")));
        
        

#check internet
if html.status_code != requests.codes.ok:
    print("無法連線");
else:
    soup= bs4.BeautifulSoup(html.content,"html.parser");


while True:
    i=0;
    try:
        research="["+str(input("請輸入搜尋的標題 or Q離開:"))
        if research=="[Q":
            print("結束搜尋");
            break      
        search_title(soup,research,i);  
    except:
        print("輸入型態錯誤請重新輸入");
      

        

                  