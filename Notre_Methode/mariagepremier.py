#!/usr/bin/python
#-*- coding:Utf-8 -*-
def mariagepremier(L2,M):
    """a utiliser dans le cas P,P+1, et permet d'exaucer le premier voeux de la premiere femme"""
    c=L2.pop(0)
    #print(L2)
    #print(c)
    M[c[0]]=c[1][0]
    for l in L2:
        if M[c[0]] in l[1]:#Boucle servant à supprimer les garçons mariés des voeux des autres filles.
            l[1].pop(l[1].index(M[c[0]]))# index(x) renvoie l'indice de x ds la liste 

    
    
#L=[[0,[1,2,3]],[1,[1,2]],[2,[4,9,2]]]
#M=[0]*len(L)
#mariagepremier(L,M)
#print(M)
#print(L)
