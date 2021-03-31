#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:58:46 2021

@author: antonomaz
"""


import re, glob , spacy, json, sklearn
from sklearn.neighbors import DistanceMetric
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances
from sklearn import metrics

def lire_fichier (chemin):
    f = open(chemin , encoding = 'utf−8')
    chaine = f.read ()
    f.close ()
    return chaine


def liste_resultats(texte):
    nlp = spacy.load("fr_core_news_sm")
    #nlp = spacy.load('fr_core_news_lg')
    #nlp = spacy.load('fr_core_news_md')
    doc = nlp(texte)
    list_resultats =[]
    #list_en_g=[]
    for ent in doc.ents:
        if ent.label_=="LOC":
            #en_g = ent
            #list_eng = [ent.text.strip(), ent.label_]
            #list_eng = [ent.text.strip(),ent.start_char,ent.end_char,ent.label_]
            #list_eng = [ent.text.strip(),ent.label_]
            # list_eng = [ent.text.strip()]
            # list_eng = [ent.text]
            # list_resultats.append(list_eng)
            list_resultats.append(ent.text)
            
            
            #list_resultats.append(set([ent.text,ent.label_,ent.start_char,ent.end_char]))
            #print(list_resultats)
            #print(ent.text, ent.label_)
    #print(list_resultats)
    return (list_resultats)



    
    
# ## MAIN

# ## Récupération du texte de chaque fichier  

ocr = lire_fichier("./data_ocr/AIMARD_OCR/Aimard_OCR.txt")
propre = lire_fichier("./data/AIMARD_PP/Aimard_txt_propre_alignement.txt")


## Récupération des informations de sortie,

resultat1 = str(liste_resultats(ocr))
print(resultat1)


resultat2 = str(liste_resultats(propre))
print(resultat2)



#DISTANCES
# lire_fichier_ocr = chaine_1_a

# lire_fichier_pp = chaine_2_a



lire_fichier_ocr = resultat1

lire_fichier_pp = resultat2

liste_name =["jaccard", "braycurtis","dice", "cosinus"] 
metric_name=0
n_max=1
liste_n_max=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


liste_resultat_dist=[]
liste_resultat_dist2=[]
liste_resultats =[]
count=0


# print(X) 

for metric_name in liste_name :
    # print(metric_name)
    liste_resultat_dist2=[]
    for n_max in liste_n_max: 
        V = CountVectorizer(ngram_range=(1,n_max ), analyzer='char') 
        X = V.fit_transform([lire_fichier_pp, lire_fichier_ocr]).toarray()
        if metric_name!= "cosinus" :  
            dist = DistanceMetric.get_metric(metric_name)     
            distance_tab1=dist.pairwise(X)
            liste_resultat_dist2.append(distance_tab1[0][1])
        else: 
            distance_tab1=sklearn.metrics.pairwise.cosine_distances(X) 
            liste_resultat_dist2.append(distance_tab1[0][1])
       
    liste_resultat_dist.append(liste_resultat_dist2)
        
print(liste_resultat_dist)


# plt.title("EN_dico_geo")
# x=liste_n_max
# y1=liste_resultat_dist[0]
# y2=liste_resultat_dist[1]
# y3=liste_resultat_dist[2]
# # y4=liste_resultat_dist[3]
# # y5=liste_resultat_dist[4]
# plt.plot(x,y1,label="Jaccard")
# plt.plot(x,y2,label="braycurtis")
# # plt.plot(x,y3,label="matching")
# # plt.plot(x,y4,label="sokalsneath")
# plt.plot(x,y3,label="dice")
# plt.ylabel("Distances")
# plt.xlabel("n_max")
# plt.axis([0, 11, 0, 1])
# plt.legend()
# plt.show()


w =open("./OUTPUT_dist/EN_AIMARD_cos.json", "w")
w.write(json.dumps( liste_resultat_dist , indent = 2))
w.close()
