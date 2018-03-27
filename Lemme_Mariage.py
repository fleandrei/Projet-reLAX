#!/usr/bin/python
#-*- coding:Utf-8 -*


'''Fichier principal regroupant tout les autres fichiers. '''
from mariagepp import *
from ppoupas import *
from Test_Mariage import *
from grand import *
from mariagepremier import *
from plusgrandpp import *
from test import *


#éviter les listes trop longues 
def LemMariage(L):
    condition=verif(L) #Vérifie si la liste L vérifie la condition des mariages: renvoie un nbr positif si oui et -1 sinon
    N=len(L)
    nb_filles_mariees=0 #compteur du nombre de couples mariés
    if condition < 0:
        print("PROBLEME: La liste entrée ne vérifie pas la condition des marriages")
        
    else:


        Pas_mariees=[] #Liste de liste contenant : numéro de la fille,liste des voeux des filles_non_mariées 
        Maris=[]  #Garçons mariés en fonctions des filles en indice
        for i in range(N):
            Pas_mariees.append([i,L[i]])
            Maris.append([0])
            
        while nb_filles_mariees < N:
            condition=ppoupas(L)
            #print(condition)
            if condition==False: # Si condition=1; donc si on est daans le cas pp+1; 
                mariagepremier(Pas_mariees,Maris)
                nb_filles_mariees=nb_filles_mariees+1
                
            else: # Si condition = 0; donc si on est dans le cas pp
                Non_mariees=L2ToL1(Pas_mariees)  #Pas maries contient juste la liste des voeux des filles non mariés, sans le numéro de filles
                Ens_de_pp=touslespp(Non_mariees) #Liste contenant tout les ensembles de pp
                Plus_grand_pp=grand(Ens_de_pp)    
                Plus_grand_pp_indices= ValToIndice(Plus_grand_pp,Pas_mariees) #Plus_grand_pp_indicés les voeux de filles associés avec le numéro de la fille (qui est l'indice dans dans la liste initialement (L) rentré en paramètre de la fonction) ie de la forme [numéro de la fille,[voeux de la fille]]
                PP_maries=mariagepp(Plus_grand_pp)
                for i in range(0,len(PP_maries)):
                    Maris[Plus_grand_pp_indices[i][0]]=PP_maries[i]
                  
                    for voeux_filles in Pas_mariees:
                        if  Plus_grand_pp_indices[i][1] == voeux_filles[1] :
                            Pas_mariees.pop(Pas_mariees.index(voeux_filles))
                          
              
                for i in range(0,len(PP_maries)):              
                    for j in range(0,len(Pas_mariees)):
           
                        if Maris[Plus_grand_pp_indices[i][0]] in Pas_mariees[j][1]:
                            Pas_mariees[j][1].pop(Pas_mariees[j][1].index(Maris[Plus_grand_pp_indices[i][0]]))
                         


                nb_filles_mariees=nb_filles_mariees+len(PP_maries)
            L=L2ToL1(Pas_mariees)
    	return(Maris)
    
            

        
    
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
                L.append([L_inter[i][0],v[:]])
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
        L1[i]=L2[i][1][:]
        
    return L1




Ln=[[4],[1,2],[3],[5],[3,1,7,8],[1],[2],[1,2],[1]]
Lpp=[[1,2,3,5,46],[46,42,45,56],[1,2,3],[2,1],[3,2],[54,78,99,62],[99],[19,97],[19,97]]
Lval=[[3],[1,2]]
L2=L1ToL2(Ln)
#print(L2)
#print("\n")
#print(ValToIndice(Ln,L2))
print(LemMariage(Lpp))




#def DicToLis(D):
#    K=D.keys()
 #   for 
