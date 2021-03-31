#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:49:00 2021

@author: antonomaz
"""



# import nltk, string
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import DistanceMetric
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import CountVectorizer



# vectorizer = TfidfVectorizer()
# vectors = vectorizer.fit_transform(lire_fichier_ocr,lire_fichier_pp)
# result= cosine_similarity(vectors)


# print(vectors)
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import kneighbors_graph

def text_to_graph(text):
    
    
        # use tfidf to transform texts into feature vectors
    
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform()
    
        # build the graph which is full-connected
    

    return vectors 

# Liste_dist_word=[]
# for dist_name in["jaccard", "braycurtis","dice"]: #Ã  dÃ©velopper
#   dist = DistanceMetric.get_metric(dist_name)
#   # V = CountVectorizer(ngram_range=(1, 5), analyzer='char')
#   V = CountVectorizer(analyzer='word')
#   # X = V.fit_transform([str1_lire, str2_lire,str3_lire]).toarray()
#   X = V.fit_transform([lire_fichier_pp, lire_fichier_ocr]).toarray()
#   #X1 = V.fit_transform([str3_lire, str4_lire, str5_lire]).toarray()
#   # X2 = V.fit_transform([str1_lire, str2_lire, str3_lire, str4_lire]).toarray()
#   print("pour X",dist_name)
#   # print(dist.pairwise(X))
#   # print(dist_name)
#   # print(dist.pairwise(X1))
#   # print("pour X2",dist_name)
#   # print(dist.pairwise(X2))
#   distance_tab1=dist.pairwise(X)
#   Liste_dist_word.append(distance_tab1[0][1])
# print(Liste_dist_word)
# w =open("./OUTPUT_dist/EN_DUTRONC_word.json", "w")
# w.write(json.dumps( Liste_dist_word , indent = 2))
# w.close()

ocr = open("./data_ocr/DUTRONC_OCR/2_dutronc_noise_venn")
lire_fichier_ocr = ocr.read()
V_OCR = text_to_graph(lire_fichier_ocr)
print(V_OCR)
propre = open("./data/DUTRONC_PP/0_dutronc_clean_venn")
lire_fichier_pp = propre.read()

