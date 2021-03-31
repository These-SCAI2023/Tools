#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:46:18 2021

@author: antonomaz
"""

import re

def ouverture_fichier(filename):
    print("lecture fichier",filename)
    f = open(filename, "r")
    textlu = f.read()
    f.close()
    print("Ecriture OK")
    return textlu

def ecriture_fichier(filename,listeTexte):
    print("Ecriture du fichier",filename)
    w = open(filename, "w")
    for t in range(0,len(listeTexte)):
        w.write(listeTexte[t])
        w.write('\n')
    w.close()
    print("Ecriture OK")

    
def alignement(texte_a_aligner,fichier):
    # liste=[]
    selection_texte=[]
    text_align_point=[]
    texte_align = texte_a_aligner.split(".")
    # liste.append(texte_align)
    for i in texte_align :
        text_align_point.append(i+".")
        
    # print(text_align_point)
    
    for i in range (0,400):
        selection_texte.append(text_align_point[i])
        # print(i,text_align_point[i])
    print(i, selection_texte)
    #écriture de liste2 dans un fichier txt
    nom = fichier + "_align_point_400.txt"
    ecriture_fichier(nom,selection_texte)
    


#main


fichier1 = "./data/AIMARD_OCR2_400L"
# texte1 = ouverture_fichier(fichier1)
texte1 = ouverture_fichier(fichier1+".txt")
texte11 = texte1.replace('\n',' ')
alignement(texte11,fichier1)

# fichier2 = "./data_align/output_resultat_ocr_alignement.txt"
# texte2 = ouverture_fichier(fichier2)
# texte22 = texte2.replace('\n','')
# alignement(texte22,fichier2)
