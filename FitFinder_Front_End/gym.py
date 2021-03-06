#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:32:36 2018

@author: Melody Shi
"""
import requests
import sqlite3

def yelp_gym(term="gym",location="Downtown, New York"):
    """
        Makes requests to get response from Yelp API. Account limit: 1000 calls per day.

        Parameters
        ----------
        term: str
            search query, defaults to "gym"
        location: str
            the location query, defaults to "Downtown, New York"

        Returns
        -------
        a response directly returned by Yelp API containing structured data

    """
    search_url = 'https://api.yelp.com/v3/businesses/search'
    parameters = {
        'term' : term,
        'location' : location
    }
    header = {
        'Authorization': 'Bearer p7FmVUMhc0KFHDKGEY8FOKit1nS2Wv1PoUWy0UrDAKKrIO07eAJCXu_wJDbJLMMrot5epyl7isB7eQZ5-vVjcDVmjaDXP_OGS_Y7cWwG9-ApypPUJpfFjPG5N1nUW3Yx'
    }
    response = requests.get(search_url,params=parameters,headers=header).json()
    return response


def gym(term,location):
    """
        Makes requests to get response from Yelp API, extracts information and builds
        a dataframe

        Parameters
        ----------
        term: str
            search query
        location: str
            the location query

        Returns
        -------
        a DataFrame object that contains information including business name, address, rating,
        contact information, etc.

    """
    response = yelp_gym(term=term,location=location)
    entry_list = []
    conn = sqlite3.connect("fitfinder.db")
    c = conn.cursor()

    for business in response['businesses']:
        business_id = business['id']
        name = business['name']
        image_url = business['image_url']
        is_closed = business['is_closed']
        url = business['url']
        review_count = business['review_count']
        rating = business['rating']
        latitude = business['coordinates']['latitude']
        longitude = business['coordinates']['longitude']
        address_1 = business['location']['address1']
        city = business['location']['city']
        zip_code = business['location']['zip_code']
        country = business['location']['country']
        state = business['location']['state']
        phone = business['phone']
        distance = business['distance']

        insert_query = '''INSERT INTO gym_table
    	VALUES ("{business_id}","{name}","{image_url}","{is_closed}","{url}",{review_count},
    	{rating},{latitude},{longitude},"{address_1}","{city}",
    	{zip_code},"{country}","{state}","{phone}",{distance});
        '''.format(business_id=business_id,name=name,image_url=image_url,is_closed=is_closed,
        url = url, review_count = review_count,rating=rating,latitude=latitude,longitude=longitude,
        address_1 = address_1,city = city,
        zip_code=zip_code,country=country,state=state,phone=phone,distance=distance)

        try:
            c.execute(insert_query)
            conn.commit()
        except:
            pass
    return True
