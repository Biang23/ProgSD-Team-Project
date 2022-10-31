#!/usr/bin/env python
# coding: utf-8


#pip install folium
#pip install clipboard


import random

import folium
import numpy as np


#create rent stations position of N numbers
def rent_loc_data(N):
    rent_loc = np.array(
    [
        np.random.uniform(low=55.85732210734671, high=55.86637739884676, size=N),
        np.random.uniform(low=-4.263585011923924, high=-4.247555719230547, size=N),
    ]
    ).T
    return rent_loc,N

#create bikes position of N numbers 
def bike_loc_data(N):
    bike_loc = np.array(
    [
        np.random.uniform(low=55.85732210734671, high=55.86637739884676, size=N),
        np.random.uniform(low=-4.263585011923924, high=-4.247555719230547, size=N),
    ]
    ).T
    return bike_loc,N

#draw the map for rent station 
def drawMapCenter(x,y):
    folium_map = folium.Map(
        location=[x, y],
        zoom_start=15,
        attr='default'
    )
    return folium_map

#draw the map for bikes
def drawMapCenter_operator(x,y):
    folium_map1 = folium.Map(
        location=[x, y],
        zoom_start=15,
        attr='default'
    )
    return folium_map1


#draw the map for rent station  data form:[[x,y],[x1,y1]]
def drawMapPoints(n,points, folium_map):
    cnt = 0
    i = 1
    popups = [i for i in range(n + 1)]
    for point in points:
        #print(point)
        if cnt < 30:
            xx = point[0]
            yy = point[1]
            for i in popups:
                folium.Marker([xx, yy],popup=popups[i]).add_to(folium_map)
            cnt += 1
    #print(folium_map)
 
    return folium_map

#draw the map for bikes position 
def drawMapBikePoints(bike_points, folium_map1):
    for bike_point in bike_points:
        #print(point)
        xx = bike_point[0]
        yy = bike_point[1]
        folium.Marker([xx, yy]).add_to(folium_map1)
    print(folium_map1)
 
    return folium_map1
    
    
    

#draw the user position
def draw_user(folium_map):
    x = random.uniform(55.85732210734671, 55.86637739884676)
    y = random.uniform(-4.263585011923924,-4.247555719230547)
    folium.Marker([x,y],icon=folium.Icon(color='red', icon='info-sign')).add_to(folium_map)
    return folium_map





# In[3]:


#folium_map1 = drawMapCenter_operator(55.86275307588229, -4.254684920519296)
#bike_points,n = bike_loc_data(100)
#drawMapBikePoints(bike_points,folium_map1)

