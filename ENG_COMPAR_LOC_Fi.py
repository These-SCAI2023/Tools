#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:53:04 2021

@author: antonomaz
"""

import spacy
import sys
import glob


def nombre_eng_ligne(tab_L_data):
  list_result = [[]]
  compt=0
  compt1=0
  # list_result[compt].append(tab_L_data[0][0])
  # list_result[compt].append("nombre d'entité nommée")
  # list_result[compt].append(tab_L_data[0][2])
  # list_result[compt].append("nombre d'entité nommée")
  for ligne in tab_L_data:
    if compt1 == 0:
      compt1=compt1+1
      continue
    list_result.append([])
    list_result[compt].append(ligne[1])
    list_result[compt].append(len(ligne[1]))
    list_result[compt].append(ligne[3])
    list_result[compt].append(len(ligne[3]))
    ##Pour tableau représentation
    # list_result.append([])
    # list_result[compt].append(str(ligne[1]))
    # list_result[compt].append(str(len(ligne[1])))
    # list_result[compt].append(str(ligne[3]))
    # list_result[compt].append(str(len(ligne[3])))
    compt=compt+1
  return (list_result)

def compare_eng(tab_resultat):
  count_ligne=0
  VP, FP, FN, AUTRE = [], [], [], []
  for ligne in tab_resultat:
    if len(ligne) == 0:
      continue
    taillemin =  min(ligne[1], ligne[3])
    #print(count_ligne)
    count_ligne=count_ligne+1
    if taillemin == 0:
      if count_ligne == (len(tab_resultat)-1):
        break
      else:
        continue
    for i in range (0, taillemin):
      a=ligne[0][i]
      b= ligne[2][i]
      if str(a) == str(b) :
        VP.append(b)
      else:
        if len(str(b)) == 1 or len(str(a))==1 :
          #https://fr.wikipedia.org/wiki/Liste_de_toponymes_courts#Une_lettre
          AUTRE.append(b)
        else:
          carac_1_a,carac_2_a,carac_3_a = str(a)[0],str(a)[1],str(a)[-1]
          #print("carac_1_a,carac_2_a,carac_3_a",carac_1_a,carac_2_a,carac_3_a)
          carac_1_b,carac_2_b,carac_3_b = str(b)[0],str(b)[1],str(b)[-1]
          #print("carac_1_b,carac_2_b,carac_3_b",carac_1_b,carac_2_b,carac_3_b)
          if carac_1_a == carac_1_b and carac_2_a == carac_2_b and carac_3_a == carac_3_b:
            FN.append(b)
          else:
            FP.append(b)    
  return(VP,FP,FN,AUTRE)



ner_model = spacy.load("fr_core_news_sm")
# ner_model = spacy.load('fr_core_news_lg')
#ner_model = spacy.load('fr_core_news_md')

L = [[]]
for num_path, path in enumerate(sorted(glob.glob("./data/data_Audoux/*"))):
#for num_path, path in enumerate(sorted(glob.glob("dico_geo_data/*"))):
  print(path)
  L[0].append(path)
  L[0].append("ents")
  f = open(path)
  lignes = f.readlines()
  f.close()
  for cpt, l in enumerate(lignes):
    if (cpt+1)==len(L):
      L.append([])
    doc = ner_model(l)
    L[cpt+1].append(l)
    #print(doc.ents)
    if doc.ents == ():
        # ent = doc.ents
        ent = str(doc.ents)
    else:
        listeent=[]
        ent=str()
        # ent=()
        for enty in doc.ents:
            if enty.label_=="LOC":#recupérer que les LOC
                listeent.append(enty)
                listeent.append(enty.label_)
            # else:
            #     listeent.append(enty.label_)
            #     listeent.append(enty.text)
        # ent=tuple(listeent)
        ent=str(tuple(listeent))
   #ent = str(doc.ents)
    #print(ent)
    # if num_path>0:
    #   if ent!=L[cpt+1][1]:
    #     if len(ent)>5:
    #       ent = "<strong>%s</strong>"%ent
    #     else:
    #       ent= "<lignestrong>FN: %s</strong>"%ent
    L[cpt+1].append(ent)
    #L[cpt+1].append(doc.ents)


s = "<table border = '1'>\n"
for ligne in L:
  s+="<tr><td>%s</td></tr>\n"%("</td> <td>".join(ligne))
s+="</table>"
w = open("output_reslta_cpt_eng_locuuuusm_lg.html", "w")
w.write(s)
w.close()
# -

# result_tab=nombre_eng_ligne(L)
# #print(result_tab)

# result_VP,result_FP,result_FN,result_AUTRE=compare_eng(result_tab)
# print("result_VP")
# print(result_VP)
# print("result_FP")
# print(result_FP)
# print("result_FN")
# print(result_FN)
# print("result_AUTRE")
# print(result_AUTRE)

# VP = len(result_VP)
# FP = len(result_FP)
# FN = len(result_FN)
# precison = 100*VP/(VP+FP)
# rappel = 100*VP/(VP+FN)
# F_mesure = (2*precison*rappel)/(precison+rappel)

# print("precison",precison)
# print("rappel",rappel)
# print("F_mesure",F_mesure)

# import pandas as pd
# tab = pd.DataFrame({"Precision":[precison,precison],"Recall":[rappel,rappel],"F-Mesure":[F_mesure,F_mesure]},index = ["model1","model2"])
# tab

