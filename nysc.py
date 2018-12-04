
# coding: utf-8

# In[1]:


import pickle
from lxml import html
from xml.etree import ElementTree
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import requests
from datetime import timedelta, date 


def daterange(start_date, end_date):
    result = []
    for n in range(int ((end_date - start_date).days)):
        result.append( start_date + timedelta(n) )
    return result

def nysc(url, param):
    site = html.fromstring(requests.get(url).text)
    node = "//div[@class=' toggle-{} row']".format(param)
    classes = site.xpath(node)

    result = []
    for c in classes:

        name = c.xpath(".//a[@class='bigger']/text()")[0].strip()
        address = c.xpath(".//span[@class='address']")[0].text_content()
        room = c.xpath(".//span[@class='room']/text()")
        date = c.xpath(".//div[@class='cell cell-head']/text()")[1].strip()
        time = c.xpath(".//span[@class='big']")[0].text_content()
        length = c.xpath(".//li[@class='table-list-item'][3]/text()")[0].strip()
        try_link = c.xpath(".//div[@class='button-wrapper']/a[1]")[0].get("href")
        reserve_link = c.xpath(".//div[@class='button-wrapper']/a[2]/@href")

        entry = {
            'name' : name,
            'address' : address,
            'room' : room,
            'date' : date,
            'time' : time,
            'length' : length,
            'Try' : try_link,
            'Reserve' : reserve_link
        }
        result.append(entry)
          
    return result

def nysc_main():
    start_date = date(2018, 12, 4)
    end_date = date(2019, 12, 3)

    urls = []
    nodes = []

    class_url="https://www.newyorksportsclubs.com/classes?day={}"

    all_results = []
    for single_date in daterange(start_date, end_date):
        url_param = single_date.strftime("%m/%d")
        node_param = single_date.strftime("%-m-%-d")
        url = class_url.format(url_param)
        results = nysc(url, node_param)
        all_results.extend(results)
    return pd.DataFrame(all_results)
if __name__ == "__main__":
    df = nysc_main()
    with open("nysc.pk","wb") as f:
        pickle.dump(df,f)

