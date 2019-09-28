# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:59:30 2019

@author: DarrenSu
"""
#listC= dict()
#dict_string=dict('string')


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
    