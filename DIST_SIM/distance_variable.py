#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:58:46 2021

@author: antonomaz
"""


import re, glob , spacy, json
from sklearn.neighbors import DistanceMetric
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances

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

ocr = lire_fichier("./data_ocr/DUTRONC_OCR/2_dutronc_noise")
propre = lire_fichier("./data/DUTRONC_PP/0_dutronc_clean")


# # Récupération des informations de sortie,

resultat1 = str(liste_resultats(ocr))
print(resultat1)


resultat2 = str(liste_resultats(propre))
print(resultat2)


# #Pontuation

# chaine_ocr= resultat1
# chaine_1 = chaine_ocr.replace("'",'')
# chaine_1_a = chaine_1.replace(",",'')
# # print(chaine_1_a)

# chaine_pp= resultat2
# chaine_2 = chaine_pp.replace("'",'')
# chaine_2_a = chaine_2.replace(",",'')
# # print(chaine_2_a)

# DISTANCE
# lire_fichier_ocr = chaine_1_a

# lire_fichier_pp = chaine_2_a



lire_fichier_ocr = resultat1

lire_fichier_pp = resultat2

liste_name =["jaccard", "braycurtis","dice"] 
metric_name=0
n_max=1
liste_n_max=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


liste_resultat_dist=[]
liste_resultat_dist2=[]
liste_resultats =[]
count=0


for metric_name in liste_name :
    # print(metric_name)
    liste_resultat_dist2=[]
    for n_max in liste_n_max: 
        dist = DistanceMetric.get_metric(metric_name)
        V = CountVectorizer(ngram_range=(1,n_max ), analyzer='char')
        X = V.fit_transform([lire_fichier_pp, lire_fichier_ocr]).toarray()
        distance_tab=dist.pairwise(X)
        liste_resultat_dist2.append(distance_tab[0][1])
        # print(distance_tab[0][1])
    liste_resultat_dist.append(liste_resultat_dist2)

print(liste_resultat_dist)


# plt.title("EN_dico_geo")
x=liste_n_max
y1=liste_resultat_dist[0]
y2=liste_resultat_dist[1]
y3=liste_resultat_dist[2]
# y4=liste_resultat_dist[3]
# y5=liste_resultat_dist[4]
plt.plot(x,y1,label="Jaccard")
plt.plot(x,y2,label="braycurtis")
# plt.plot(x,y3,label="matching")
# plt.plot(x,y4,label="sokalsneath")
plt.plot(x,y3,label="dice")
plt.ylabel("Distances")
plt.xlabel("n_max")
plt.axis([0, 11, 0, 1])
plt.legend()
plt.show()


# w =open("./OUTPUT_dist/EN_dico_geo_distance.json", "w")
# w.write(json.dumps( liste_resultat_dist , indent = 2))
# w.close()
