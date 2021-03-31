#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:08:32 2021

@author: antonomaz
"""
import glob , json

import matplotlib.pyplot as plt
import numpy as np


with open('./AUDOUX/TXT_AUDOUX_COS10.json') as json_data: 
    lst_TXT_dist= json.load(json_data)
    print('lst_TXT_dist', lst_TXT_dist)
    
with open('./AUDOUX/EN_AUDOUX_10cos.json') as json_data: 
    lst_EN_dist= json.load(json_data)
    print('lst_EN_dist', lst_EN_dist)

liste_n_max=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


x=liste_n_max
y1= lst_TXT_dist[0]
y2= lst_TXT_dist[1]
y3= lst_TXT_dist[2]
y8= lst_TXT_dist[3]
y4= lst_EN_dist[0]
y5= lst_EN_dist[1]
y6= lst_EN_dist[2]
y7= lst_EN_dist[3]
plt.plot(x,y1,label="Jaccard", linestyle='dotted')
plt.plot(x,y2,label="braycurtis", linestyle='dotted')
plt.plot(x,y3,label="dice", linestyle='dotted', color ="darkgreen")
plt.plot(x,y8,label="cosinus", linestyle='dotted', color ="red")
plt.plot(x,y4,label="Jaccard REN", color ="blue")
plt.plot(x,y5,label="braycurtis REN", color ="orange")
plt.plot(x,y6,label="dice REN", color ="darkgreen")
plt.plot(x,y7,label="cosinus REN", color ="red")


plt.ylabel("Distances")
plt.xlabel("n_max")
plt.axis([0, 11, 0, 1])
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.show()