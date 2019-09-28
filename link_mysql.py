# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:31:42 2019

@author: DarrenSu
"""

import pymysql;

def link_mysql(data,command):

    #setting 
    db= pymysql.Connect(host='localhost',port=3306,user='root',passwd='N/A',db=data,charset='utf8');
    cursor=db.cursor()
    
    sql=str(command);
    try:
        cursor.execute(sql);
        
        db.commit();
        return  'success';     
    except Exception as e:
        print(e);
        return  'fail';  
    db.close()
    
#for test 
#com="INSERT IGNORE INTO frist_1(ID,title,date,address) values('1','標題','2019-09-10','http//')";
#link_mysql('move_list',com);