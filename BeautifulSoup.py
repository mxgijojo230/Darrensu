# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 18:21:12 2019

@author: Darren
"""

import bs4 
import requests
import datetime
import json
import link_mysql

##設定回上層的目錄
#import sys
#sys.path.append("..")
##抓取上層中的function
import dict_range


uri1='https://www.ptt.cc/bbs/movie/index.html'
search_uri='';
ppt="https://www.ptt.cc"
num=1;

#dict 格式設定
articles=[];

#抓取時間
now= datetime.datetime.strptime('12/30','%m/%d');
now_date=datetime.date.today();
year= now_date.year;

def dict_sort(listC,dict_string):            
    dict_string=str(dict_string);
    max_num=0;
    for h,c in enumerate(listC):
        max_num= c[dict_string];
        for x,d in enumerate(listC):
            if max_num>d[dict_string] and x>h:
                max_num=d[dict_string];
                list2=listC[h];
                listC[h]=listC[x];
                listC[x]=list2;          
    return(listC);
    
            
  
        
#搜尋title
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
                    date_list=str(year)+'/'+str(date[j].string);
                    #存入list
                    articles.append({'title':str_title,
                                     'href':a_title.get("href"),
                                     'date':date_list,
                                     });  
                    #print(articles);             
    if num >1:
        pag=soup.find("div",class_="btn-group btn-group-paging");
        a_pags=pag.find_all("a");
        for a_pag in a_pags:
            if '上頁' in a_pag.string:
                global search_uri;
                search_uri=a_pag.get("href");
    return         
                
              
#確認網址及抓取html
def check_uri(uri):
    html=requests.get(uri);
    #check internet
    if html.status_code != requests.codes.ok:
        print("無法連線");
    else:
        soup= bs4.BeautifulSoup(html.content,"html.parser");    
        return soup;

while True:
    i=0;
    try:
        research="["+str(input("請輸入搜尋的標題 or Q離開: "))     
        if research=="[Q":
            print("結束搜尋");
            break;
        num=int(input("請輸入要搜尋幾頁: "));
        for x in range(0,num):
            if x==0:
                print("---------------第1頁--------------")
                soup=check_uri(uri1);
                search_title(soup,research,i);     
            else:
                print("---------------第{}頁--------------".format(x+1))
                soup=check_uri(ppt+search_uri);
                search_title(soup,research,i);                
    except Exception as e:
        print(e);
#排列組合
dict_range.dict_sort(articles,"href");
#寫入mysql 資料庫中
for count,article in enumerate(articles):
    sql="INSERT IGNORE INTO frist_1(ID,title,date,address) values('"+str(count+1)+"','"+article['title']+"','"+article['date']+"','"+article['href']+"')"
    print(link_mysql.link_mysql('move_list',sql));


print(json.dumps(articles,indent=1,ensure_ascii=False))
     
