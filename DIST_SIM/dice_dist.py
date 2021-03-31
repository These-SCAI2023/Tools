#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:48:11 2021

@author: antonomaz
"""

from scipy.spatial import distance

ocr = open("./data_ocr/output_AUDOUX_EN_ocr.txt")
lire_fichier_ocr = ocr.read()
ocr= lire_fichier_ocr.split()
# print(ocr)
propre = open("./data/output_AUDOUX_EN_propre.txt")
lire_fichier_pp = propre.read()
pp= lire_fichier_pp.split()
print(pp)

dice_dist = distance.dice(ocr, pp)

print (dice_dist)