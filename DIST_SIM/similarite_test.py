import re, glob , spacy, json, sklearn
from sklearn.neighbors import DistanceMetric
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances
from sklearn import metrics
# str1 = open("./output_propre/output_resultat_propre_alignement.txt")
# str1_lire=str1.read()
# str1.close()
# str2 = open("./output_ocr/output_resultat_ocr_alignement.txt")
# str2_lire=str2.read()
# str2.close()

# ocr = open("./data_ocr/aimard_resultat_en_ocr_sans_ajout_alignement.txt")
# lire_fichier_ocr = ocr.read()
# propre = open("./data/aimard_resultat_en_propre_alignement.txt")
# lire_fichier_pp = propre.read()

# ocr = open("./data_ocr/aimard_en_ocr_venn.txt")
# lire_fichier_ocr = ocr.read()
# propre = open("./data/aimard_txt_propre_venn")
# lire_fichier_pp = propre.read()

ocr = open("./data/DUTRONC_OCR/2_dutronc_noise")
lire_fichier_ocr = ocr.read()
propre = open("./data/DUTRONC_PP/0_dutronc_clean")
lire_fichier_pp = propre.read()

# ocr = open("./data_ocr/output_AUDOUX_EN_ocr.txt")
# lire_fichier_ocr = ocr.read()
# propre = open("./data/output_AUDOUX_EN_propre.txt")
# lire_fichier_pp = propre.read()



# str1 = open("./data_dutron_txt/0_dutronc_clean")
# str1_lire=str1.read()
# str1.close()

# str2 = open("./data_dutron_txt/1_dutronc_brut")
# str2_lire=str2.read()
# str2.close()






# str3 = "Sur la planÃ¨te Mars il n'y a pas de plan B pour le climat"
# str4 = "Sur la planete Mar il n'y a pas de plan b pour le clima"
# print("************str1", str1_lire,"\n","******************str2", str2_lire)


## SUR MOT 
# Liste_dist_word=[]

# V = CountVectorizer(analyzer='word')
# X = V.fit_transform([lire_fichier_pp, lire_fichier_ocr]).toarray()
# print(X) 
# for dist_name in["jaccard", "braycurtis","dice", "cosinus"]: #Ã  dÃ©velopper
#      print("pour X",dist_name)

#      if dist_name!= "cosinus" :  
#         dist = DistanceMetric.get_metric(dist_name)     
#         distance_tab1=dist.pairwise(X)
       
#      else:
#          distance_tab1=sklearn.metrics.pairwise.cosine_distances(X)
#       # dist = dist_matrix[0][1]
    
#      Liste_dist_word.append(distance_tab1[0][1])
  
# print(Liste_dist_word)
# w =open("./OUTPUT_dist/EN_AUDOUX_word_cos.json", "w")
# w.write(json.dumps( Liste_dist_word , indent = 2))
# w.close()
# 1/0
      

## SUR 10 n-gram de charactère

liste_name =["jaccard", "braycurtis","dice", "cosinus"] 
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

w =open("./OUTPUT_dist/TXT_DUTRONC_COS10.json", "w")
w.write(json.dumps( liste_resultat_dist , indent = 2))
w.close()