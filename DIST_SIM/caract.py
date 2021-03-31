#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:28:35 2021

@author: antonomaz
"""
def lire_fichier (chemin):
    f = open(chemin , encoding = 'utf−8')
    chaine = f.read ()
    f.close ()
    #print(chaine)
    return chaine


    
ref = lire_fichier("./data/dictionnaire_geographie_GALLICA")
h = lire_fichier("./data_ocr/dictionnaire_geographie_ocrspace")
# res_txt_propre = lire_fichiers("./output_propre/*")
# hypothese_ocr = lire_fichiers("./output_ocr/*")
# resultat_wer=wer(res_txt_propre, hypothese_ocr)
# #resultat_wer=wer("/home/antonomaz/Documents/SORBONNE/Doctorat/EXPE_PROGRA_2020_2021/EXPE_COMPARE_TXTBRUIT/test_extraction_propre/output/output_resultat_propre_alignement.txt","/home/antonomaz/Documents/SORBONNE/Doctorat/EXPE_PROGRA_2020_2021/EXPE_COMPARE_TXTBRUIT/test_extraction_propre/output/output_resultat_ocr_alignement.txt")
# print(resultat_wer)

i = 0
y=0
liste_caract=[]
r = ref.split()

#print(r)
for i in r :
    for y in i :
        liste_caract.append(y)
print(liste_caract)


