#!/usr/bin/python
#-*- coding:Utf-8 -*


'''Fichier principal regroupant tout les autres fichiers. '''
from Mariagepp import *
from Test_Mariage import *
from grand import *
from mariagepremier import *
from plusgrandpp import *
from test import *


def LemMariage(L):
    test=verif(L)
    N=len(L)
    c=0
    if test < 0:
        print("PROBLEME: La liste entrée ne vérifie pas la condition des marriages")
    else:
        L2=[]
        M=[]
        for i in range(N):
            L2.append([i,L[i]])
            M.append(0)
            
        while c < N:
            if test: # Si test=1; donc si on est daans le cas pp+1
                mariagepremier(L2,M)
                c=c+1
                
            else: # Si test = 0; donc si on est dans le cas pp
                L1=L2ToL1(L2)
                pp1=touslespp(L1) #Liste contenant tout les enssemebles de pp
                print("\n\n\n")
                pp2=grand(pp1)    # pp2 est le plus grand pp parmis pp1
                print(pp2)
                print("\n\n")
                pp3= ValToIndice(pp2,L2) #pp3 contient les élèments de pp2 mais avec en plus l'indices des filles qui leur correspond 
                print(pp3)
                
                
        
    
def LisToDic(L):
    n=len(L)
    D={}
    for i in range(n):
        d[i]=L[i]
    return D



'''L2= liste dont les éléments sont de la forme: [indice,[liste des voeux de la fille]] 
La fonction prend en paramètre la liste Lval contenant des voeux de filles et retourne une liste sur le modèle de L2 qui informe donc à la fois sur le voeux en lui même et sur l'indice de la fille correspondante.
L2 contient tout les élèment de la liste avec leur indices ce qui permet à la fonction d'associer les valeurs de Lval au bons indices. '''
def ValToIndice(Lval,L2):
    L=[]                
    L_inter= L2[:]
    for v in Lval:
        t=1
        i=0
        while t>0 and i< len(L_inter):
            if v==L_inter[i][1]:
                L.append([L_inter[i][0],v])
                t=-1
            i=i+1
        L_inter.pop(i-1)
    return L
 


'''Fonction qui transforme une liste L1 de type [[ , ], [],...] en liste L2 de type [[indice,[ , ]], [indice,[]], ...] où "indice" désigne l'indice de l'élèment dans la liste L1 '''
def L1ToL2(L1):
    L2=[]
    n=len(L1)
    for i in range(n):
        
        L2.append([i,L1[i]])
    return L2


'''Attention cette fonction classe les uns à la suite des autre le deuxième élèment des élèments de L2 dans une liste L2. Autrement dit, l'indice d'un élèment dans L1 ne correspond pas forcément à son véritable indice (celui qui est donné dans L2)'''
def L2ToL1(L2):
    n=len(L2)
    L1=[0]*n
    
    for i in range(n):
        L1[i]=L2[i][1]
        
    return L1




Ln=[[4],[1,2],[3],[5],[3,1,7,8],[1],[2],[1,2],[1]]
Lpp=[[1,2],[3],[7,3],[4,5],[6,2,7],[3,1,2],[7,5],[8,9],[8,9]]
Lval=[[3],[1,2]]
L2=L1ToL2(Ln)
print(L2)
print("\n")
print(ValToIndice(Ln,L2))
LemMariage(Lpp)




#def DicToLis(D):
#    K=D.keys()
 #   for 
