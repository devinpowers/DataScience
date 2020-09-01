#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 08:47:20 2020

@author: devinpowers
"""
import folium


# Create Map Object
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

tooltip = 'Click For More Info'


list_of_cord = [[40.71424,	-74.00869],[40.67006,-73.9764], [40.7505,-73.9934]
                ,[40.6826, -73.9754]]

#Creat Markers from list_of_cords
for index in list_of_cord:
    
    lat, long = index
    
    
    
    folium.Marker([lat, long],
                  popup='<strong>Location</strong>',
                  tooltip=tooltip).add_to(m),


# Create Markers from CSV File





# Generate map
m.save('map.html')

