#!/usr/bin/python
#-*- coding:Utf-8 -*


'''Fichier principal regroupant tout les autres fichiers. '''
from Mariagepp import *
from Test_Mariage import *



def LemMariage(L):
    test=verif(L)
    if test < 0:
        print("PROBLEME: La liste entrée ne vérifie pas la condition des marriages")
    
    




L=[[4],[1,2],[3],[5],[3,1,7,8],[1],[2]]
LemMariage(L)
