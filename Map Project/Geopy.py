#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:53:29 2020


Converts address into Latitude and Longitude 


@author: devinpowers
"""
import folium
from geopy.geocoders import Nominatim

# Create Map Object
m = folium.Map(location=[40.7128, -74.0060] , zoom_start=12)

tooltip = 'Click For More Info'


address_list = [["136 Church St, New York City, NY 10001,"],["562 2nd St, New York City, NY"],["4 Pennsylvania Plaza, New York, NY 10001"],
                ['13 W 27th St, New York, NY 10001'],['45 Rockefeller Plaza, New York, NY 10111'], ['405 Lexington Ave, New York, NY 10174'], [
                    'Lincoln Center Plaza, New York, NY 10023'] ]



list_lat_long = []

for address in address_list:
    
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    
    list_lat_long.append([location.latitude, location.longitude])

for index in list_lat_long:
    
    lat, long = index
    
    
    
    folium.Marker([lat, long],
                  popup='<strong>Location</strong>',
                  tooltip=tooltip).add_to(m),
    
    

# Generate map
m.save('map.html')










#print(location.address)




