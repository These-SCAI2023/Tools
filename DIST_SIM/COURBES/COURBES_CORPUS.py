#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:08:32 2021

@author: antonomaz
"""
import glob , json

import matplotlib.pyplot as plt
import numpy as np


with open('./AUDOUX_distances.json') as json_data: 
    dist =json.load(json_data)

# for i in dist.items():
    # print(i)

print(list(dist))
# print("  ",dist['txt']["OCR--propre"])
# print("  ", dist['txt']["OCR--OCR"])



dic_plot = {}
for cle, dic in dist.items(): 
    
    print("l'élément de clé", cle)
    
    for version, modele in dic.items():
        print("  ",version )
        
    
        
        
        for name_metric, liste in modele.items():
            print("      ", name_metric)
            
            plt.plot(liste, label=name_metric)
        name_fig = "%s_%s.png"%(version, cle)
        print(" nom de la figure ", name_fig)
        plt.legend(loc='upper left')
#        plt.legend
        plt.savefig("%s_%s.png"%(version, cle))
        plt.clf()
        
        
                    # x=liste_n_max
# y1= dist[1]
# y2= dist[1]
# y3= dist[2]
# y4= dist[3]
# y5= dist[4]
# y6= dist[5]
# # y7= lst_EN_dist[3]
# plt.plot(x,y1,label="Jaccard", linestyle='dotted')
# plt.plot(x,y2,label="braycurtis", linestyle='dotted')
# plt.plot(x,y3,label="dice", linestyle='dotted', color ="darkgreen")
# # plt.plot(x,y8,label="cosinus", linestyle='dotted', color ="red")
# plt.plot(x,y4,label="Jaccard REN", color ="blue")
# plt.plot(x,y5,label="braycurtis REN", color ="orange")
# plt.plot(x,y6,label="dice REN", color ="darkgreen")
# # plt.plot(x,y7,label="cosinus REN", color ="red")


# plt.ylabel("Distances")
# plt.xlabel("n_max")
# plt.axis([0, 11, 0, 1])
# plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
# plt.show()
            # print(liste)
        
        
            
            
            
            
           


        
    # lst_TXT_dist= json.load(json_data)
    # print('lst_TXT_dist', lst_TXT_dist)
    
# with open('./AUDOUX_CORPORA/') as json_data: 
#     lst_EN_dist= json.load(json_data)
#     print('lst_EN_dist', lst_EN_dist)

# liste_n_max=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


