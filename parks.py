#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:33:27 2018

@author: Melody Shi
"""

import requests
from lxml import html
import pandas as pd

def parks(url):
    """
        Scrapes "nycgovparks.org" to get information of free sports happening in different centers
        and saves the result to a dataframe.
        
        Parameters
        ----------
        url: str
            the link to the webpage
            
        Returns
        -------
        a DataFrame object that contains information including the category, the name of the center,
        the address, weekday, event start time and end time
          
    """
    doc = html.fromstring(requests.get(url).text)
    centers = doc.xpath('//div[contains(@class,"program span4")]')
    entry_list = []
    
    for center in centers:
        category = center.xpath('.//h4')[0].text
        center_name = center.xpath('.//strong')[0].text
        address = center.xpath('.//p/text()[1]')[0]  #unlabelled child tag
        
        #can have multiple weekdays and timeslots
        weekdays = center.xpath('.//strong[@class="day"]') 
        timeslots = center.xpath('.//span[@class="time"]')
        
        #save different schedules for a center as multiple records
        #loop through weekdays and timeslots together, length should match
        for day,timeslot in zip(weekdays,timeslots): 
            day = day.text.strip(":")
            time = timeslot.text.strip().split("-")
            start_time = time[0]
            end_time = time[1]
    
            entry = {
                'category' : category,
                'center_name' : center_name,
                'address': address,
                'day': day,
                'start_time': start_time,
                'end_time': end_time
            }
    
            entry_list.append(entry)
        
    return pd.DataFrame(entry_list)

# main function for testing purpose
if __name__ == "__main__":
    print(parks('https://www.nycgovparks.org/programs/recreation/shape-up-nyc?fbclid=IwAR2fu7flf3TdXJicDvHYsTDBBlI054ECUvKGhAjR6nqKj4CQbiDvURdegLk'))

    
