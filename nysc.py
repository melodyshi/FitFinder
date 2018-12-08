"""
Created TUE DEC 4th 14:35:39  2018

@uthor : Albert Peraza
"""
import pickle
from lxml import html
import pandas as pd
import requests
from datetime import timedelta, date 


def daterange(start_date, end_date):
    """
        This function is used to web scrape the New York Sports club website which
        has a particular format. The Url requires the format MM/DD in order to scrape for classes
        each day. The nodes also require the format MM-DD in order to scrape information from the classes
        each day.
    """
    result = []
    for n in range(int ((end_date - start_date).days)):
        result.append( start_date + timedelta(n) )
    return result

def nysc(url, param):
    """
        Scrapes https://www.newyorksportsclubs.com/classes to get information of fitness classes
        occurring in New York Sport Club gyms in the New York area. We collect the name of the class,
        the address, room location within the gym, the date the class occurs, the length of the class,
        and links to try the class for non-members or reserve the class if you have a membership.
        
        
        Parameters:
            url: str
            param: int
                this will be the used to scrape the nodes
        Returns:
           a list of the information.
    """
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
            'Try' : "https://www.newyorksportsclubs.com" + try_link,
            'Reserve' : reserve_link
        }
        result.append(entry)
          
    return result

def nysc_main():
    """
        Scrpes https://www.newyorksportsclubs.com/classes with the format for the website and nodes.
        We scrape the site from December 4th to December 31st. In order to collect information from the site each date
        the ending of the url must be day=MM/DD, hence the url_param. In order to run the nysc function each day the nodes
        need to have MM-DD.
        
        This function returns the list from the nysc function as a dataframe
    """
    start_date = date(2018, 12, 4)
    end_date = date(2018, 12, 31)
    
    
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
