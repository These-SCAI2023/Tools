#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:58:46 2021

@author: antonomaz
"""


import glob , spacy , json
import glob
from sklearn.neighbors import DistanceMetric
from sklearn.feature_extraction.text import CountVectorizer


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

def compte_occ(texte):
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(texte)
    liste_n=[]
    for ent in doc.ents:
        if ent.label_=="LOC":
            liste_n.append(ent)
    return (len(liste_n))


## MAIN

## Récupération du texte de chaque fichier  

ocr = lire_fichier("./data/DUTRONC/2_dutronc_noise")
propre = lire_fichier("./data/DUTRONC/0_dutronc_clean")


## Récupération des informations de sortie,

resultat1 = liste_resultats(ocr)
# #print(resultat1)


resultat2 = liste_resultats(propre)
# print(resultat2)


## Sortie des résultats formats txt

resultat_ocr = str(resultat1)
print(resultat_ocr)
w = open("./output_EN_extract/EN_DUTRONC_OCR", "w")
w.write(resultat_ocr)
w.close()

resultat_txtpp = str(resultat2)
print(resultat_txtpp)
w = open("./output_EN_extract/EN_DUTRONC_PP", "w")
w.write(resultat_txtpp)
w.close()


   
    
##  nombre de EN Géo, dans quel texte
    
# nb_loc = compte_occ(ocr)
# print("**** LE nombre de localité pour le texte 1 : ", nb_loc)
#nb_loc2 = compte_occ(propre)
#print("**** LE nombre de localité pour le texte 2 : ", nb_loc2)


