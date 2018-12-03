#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:15:34 2018

@author: WK
"""
import pickle
from lxml import html
from xml.etree import ElementTree
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns
import statsmodels.formula.api as smf

def get_schedule(url):
    doc = html.fromstring(requests.get(url).text)
    address = doc.xpath('//div[@class="studio-address"]')[0].text
    location = doc.xpath('//div[@class="studio-address"]')[1].text
    classes = doc.xpath('//@aria-label')

    result = []
    
    results = []
    for c in classes:
        if 'Mon' in c[0:3]:
            results.append(c)
        elif 'Tue' in c[0:3]:
            results.append(c)
        elif 'Wed' in c[0:3]:
            results.append(c)
        elif 'Thu' in c[0:3]:
            results.append(c)
        elif 'Fri' in c[0:3]:
            results.append(c)
        elif 'Sat' in c[0:3]:
            results.append(c) 
        elif 'Sun' in c[0:3]:
            results.append(c)

    for r in results:
        entry = {
            'location': location,
            'address': address,
            'date' : r.split(',', 1)[0],
            'time' : (r.split(',', 1)[1]).split('M', 1)[0],
            'class' : (r.split(',', 1)[1]).split('class', 1)[0],
            'instructor' :  (r.split(',', 1)[1]).split('with', 1)[1],
        }
        result.append(entry)
    
    return result

def concat_df(studios):
    dfs = []
    for i in studios:
        for j in i:
            dfs.append(pd.DataFrame(get_schedule(j)))
    df = dfs[0]
    for i in dfs[1:]:
        df = df.append(i, ignore_index=True)
    return df      

def soulcycle():
    date_list = ['01','08','15','22','29']
    urls_19 = ['https://www.soul-cycle.com/find-a-class/studio/30/2018-12-{}/'.format(i) for i in date_list]
    urls_bp = ['https://www.soul-cycle.com/find-a-class/studio/1034/2018-12-{}/'.format(i) for i in date_list]
    urls_c = ['https://www.soul-cycle.com/find-a-class/studio/1042/2018-12-{}/'.format(i) for i in date_list]
    urls_54 = ['https://www.soul-cycle.com/find-a-class/studio/1036/2018-12-{}/'.format(i) for i in date_list]
    urls_63 = ['https://www.soul-cycle.com/find-a-class/studio/213/2018-12-{}/'.format(i) for i in date_list]
    urls_83 = ['https://www.soul-cycle.com/find-a-class/studio/3/2018-12-{}/'.format(i) for i in date_list]
    urls_fd = ['https://www.soul-cycle.com/find-a-class/studio/1018/2018-12-{}/'.format(i) for i in date_list]
    urls_gc = ['https://www.soul-cycle.com/find-a-class/studio/1088/2018-12-{}/'.format(i) for i in date_list]
    urls_noho = ['https://www.soul-cycle.com/find-a-class/studio/19/2018-12-{}/'.format(i) for i in date_list]
    urls_nomad = ['https://www.soul-cycle.com/find-a-class/studio/1022/2018-12-{}/'.format(i) for i in date_list]
    urls_soho = ['https://www.soul-cycle.com/find-a-class/studio/21/2018-12-{}/'.format(i) for i in date_list]
    urls_t = ['https://www.soul-cycle.com/find-a-class/studio/4/2018-12-{}/'.format(i) for i in date_list]
    urls_us = ['https://www.soul-cycle.com/find-a-class/studio/9/2018-12-{}/'.format(i) for i in date_list]
    urls_60 = ['https://www.soul-cycle.com/find-a-class/studio/1069/2018-12-{}/'.format(i) for i in date_list]
    urls_77 = ['https://www.soul-cycle.com/find-a-class/studio/1/2018-12-{}/'.format(i) for i in date_list]
    urls_92 = ['https://www.soul-cycle.com/find-a-class/studio/1029/2018-12-{}/'.format(i) for i in date_list]
    urls_wv = ['https://www.soul-cycle.com/find-a-class/studio/20/2018-12-{}/'.format(i) for i in date_list]
    
    studios = [urls_19,
    urls_bp,
    urls_c,
    urls_54,
    urls_63,
    urls_83,
    urls_fd,
    urls_gc,
    urls_noho,
    urls_nomad,
    urls_soho,
    urls_t,
    urls_us,
    urls_60,
    urls_77,
    urls_92,
    urls_wv]
    
    df = concat_df(studios)
    return df

if __name__ == "__main__":
    df = soulcycle()
    with open("soulcycle.pk","wb") as f:
        pickle.dump(df,f)
