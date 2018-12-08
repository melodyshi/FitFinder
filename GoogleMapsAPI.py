#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 12:33:12 2018

@author: AlbertPeraza
"""

import requests
    

def call_google_maps(address):
    """
        Makes requests to get response from Google Maps Geocoding API.
        Account limit: Unlimited until google credits run out.
        
        Parameters:
            address: str
            
        Returns:
            a response from Google Maps Geocoding API containing structured 
            data
        
    """
    
    google_maps_url = 'https://maps.googleapis.com/maps/api/geocode/json' 
    api_key = 'AIzaSyD9I99AhO7IUXDoXe6z_zZWW6hiW2kGL5o'
    params = {
        'address': address,
        'key' : api_key,
        'region': 'usa',
    }
    req = requests.get(google_maps_url, params=params)
    
    results = req.json()
    
    if 'results' in results and len(results['results'])>0:
        result = results['results'][0]
        return result
    else:
        return None
    
def get_lat_lon(address):
    """
        Calls the google maps function to get structured data and then we 
        generate the Latitude and Longitude of the address
        
        Parameters:
            address: str
                search query
        Returns:
            The Latitude and Longitude given by the Geocoding API.
            If there is no Latitude or Longitude it defaults to New York's 
            Latitude and Longitude
            
    """
    google_result = call_google_maps(address)
    try:
        coordinates = google_result['geometry']['location']
        lat = coordinates['lat']
        lon = coordinates['lng']
    except:
        lat = "40.7128"
        lon = "74.0060"
    return lat,lon

def get_postal_code(address):
    """
        Calls the google maps function to get structured data and then we 
        generate the postal code of the address
        
        Parameters:
            address: str
                search query
        Returns:
            The postal code given by the Geocoding API.
            If there is no postal code it defaults the postal code to 0000000
    """
    google_result = call_google_maps(address)
    try:
        long_name = google_result['address_components'][-1:][0]
        postal_code = long_name.get('long_name')
    except:
        postal_code = "000000"
    return postal_code
