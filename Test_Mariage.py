#!/usr/bin/python
#-*- coding:Utf-8 -*

def test(L): 
    '''Fonction qui prend une liste de filles en paramètre (une fille étant 
    repésentée par une sous liste contenant ses voeux).
    On renvoie: 
    - 1 si il y a au total plus de garçons que de filles
    - 0 si il y a au total autant de filles que de garçons
    - (-1) si il y a au total plus de filles que de garçons. (Dans ce cas la 
    condition des mariages n'est pas vérifiée'''
    
    T=[]        #Liste contenant l'enssemble des garçons contenus dans L
    nl=len(L)
    
    for i in range(nl):
        nlj=len(L[i])
        for j in range(nlj):
            if L[i][j] not in T:
                T.append(L[i][j])
    
    nt=len(T)

    if nt<nl:
        print(L) #Affiche la liste si elle comporte plus de filles que de garçons
        return -1    
    elif nt==nl:
        return 0
    elif nt > nl:
        return 1


L=[[4],[1,2],[3],[5],[3,1,7,8],[1],[2]]




def verif(L):
    '''Fonction récurssive prenant en paramètre une liste de filles avec leurs 
    voeux respectifs et détermine si la condition de mariages est vérifiée.
    La fonction va vérifier avec la fonction test() tous les sous 
    enssembles de L. 
    Elle renvoie:
    - 1 si la condition des mariages est vérifiée et si il y a plus de garçons 
    que de filles.
    - 0 si la condition des mariages est vérifiée et si il y a autant de garçon
    que de filles.
    - (-1) si la condition des mariages n'est pas vérifiée car il existe un sous
    ensemble de L dans lequel il y'a plus de filles que de garçons.
    '''
    c=0       #Compteur d'itérations
    nl=len(L)

    #Si la liste comporte plus de garçons que de filles, alors on 
    #arrète la fonction et en retourne -1 
    TL=test(L) 
    if TL<0:    
        return TL


    condition= 0  #devient négatif si la fonction trouve un sous-enssemble de L
                  #qui invaliderait la condition des mariages.
        

    while condition >=0 and c<nl: #tant que condition>=0 et que toute la 
                                      # liste n'est pas parcourue. 
       
        L_teste=L[:]  
        L_teste.pop(c) # L_teste est égale à L, moins l'élément d'indice c.
        
        condition=test(L_teste)
        if condition<0:
            L_err=L_teste[:]
            continue
        if nl > 2:
            condition=verif(L_teste) #Appel itératif à verif
        c=c+1


    if condition <0:
        return condition
    else:
        return TL
    
                
        
#print(verif(L))
