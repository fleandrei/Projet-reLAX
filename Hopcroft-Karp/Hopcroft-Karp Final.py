#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

def Mariage(Liste_total_voeux) : #Fonction principale

#"""Prend en entrée une liste [[garçon1,garçon2,...],[garçon3,garçon4,...],...] où chaque sous liste correspond à la liste de voeux d'une fille
#Renvoie une liste sous la forme [garçon1,garçon3,...] où chaque garçon a été marié à la fille d'indice correspondant"""


	#if verif(Liste_total_voeux)<0 :

		#print("La condition du lemme des mariages n'est pas vérifiée, on ne peut pas réaliser le mariage")

		#return(-1)

	#else :


		#On réalise un premier mariage arbitraire
		M=Phase_1(Liste_total_voeux)  

		#On crée une liste des garçons
		Garcons=recherche_garcons(Liste_total_voeux)


		#On crée des listes recensants les sommets libres de notre graphe
		Liste_sommets_libres_filles=recherche_sommets_libres_filles(M)
		Liste_sommets_libres_garcons=recherche_sommets_libres_garcons(M,Garcons)


		#Tant qu'il reste des filles qui n'ont pas été mariés, ie des sommets libres de filles
		while len(Liste_sommets_libres_filles)>0 :

			Liste_garcons_desirees=Liste_filles_to_garcons(Liste_total_voeux,Garcons)

			[M_checkpoint,Liste_garcons_desirees_checkpoint]=creation_checkpoint(M,Liste_garcons_desirees,Liste_sommets_libres_garcons,Liste_sommets_libres_filles)

			#On cherche un chemin reliant deux sommets libres
			chemin=Dijkstra(M_checkpoint,Liste_garcons_desirees_checkpoint,Liste_sommets_libres_garcons,Liste_sommets_libres_filles) 
			#Puis on réalise la différence symétrique entre ce chemin et notre couplage afin d'obtenir un nouveau couplage
			M=difference_symetrique(chemin,M)
		
			#Mise à jour des sommets libres
			Liste_sommets_libres_filles=recherche_sommets_libres_filles(M)
			Liste_sommets_libres_garcons=recherche_sommets_libres_garcons(M,Garcons)


		return(M)

def recherche_garcons(Liste_total_voeux) : 

	#Renvoie la liste de tous les garçons présents
	Liste_garcons=[]

	#On parcours la liste total des voeux des filles
	for i in range(0,len(Liste_total_voeux)) : 
		for j in range(0,len(Liste_total_voeux[i])) :	

			#Si le garçon n'a pas encore été ajouté, alors on l'ajoute
			if (Liste_total_voeux[i][j] in Liste_garcons) == False : 
				Liste_garcons.append(Liste_total_voeux[i][j])


	return(Liste_garcons)

def Liste_filles_to_garcons(Liste_total_voeux,Liste_garcons): 
# Retourne la liste des garcons en fonction des filles sous la forme
# L=[[garcon1,[filles qui ont choisi le garcon1]],[garcon2,[filles qui ont choisi le garcon2]]]
	Liste_garcons_desirees=[]


	for garcon in Liste_garcons :
		Liste_garcons_desirees.append([garcon,[]])



	for k in range(0,len(Liste_garcons_desirees)) :
			for fille in range(0,len(Liste_total_voeux)) : 
				for i in range(0,len(Liste_total_voeux[fille])) :	
					if Liste_total_voeux[fille][i]==Liste_garcons_desirees[k][0] :
						Liste_garcons_desirees[k][1].append(fille)

	return(Liste_garcons_desirees)




def appartient_ss_liste(elts,Mariage_arbitraire) :
	#Recherche si un élément appartient à une sous liste de Mariage arbitraire

	appartenance=False

	for L in Mariage_arbitraire :
		if L==[elts] :
			appartenance=True

	return(appartenance)


def Phase_1(Liste_total_voeux) :

	#On marie arbitrairement les filles avec des garçons
	#Renvoie une liste de la forme [[A],[B]] où le garcon A a été marié à la fille 1, et le garcon B a été marié à la fille 2

	Mariage_arbitraire=[]

	for i in range(0,len(Liste_total_voeux)) : #On parcours la liste total des voeux des filles
		j=0
		appartenance=True

		#Tant qu'on trouve un garçon qui a été marié
		while appartenance==True and j<len(Liste_total_voeux[i]) : 
			if appartient_ss_liste(Liste_total_voeux[i][j],Mariage_arbitraire)==False :
				appartenance=False
				j-=1

			j+=1
			#On regarde le garçon suivant


		if j<len(Liste_total_voeux[i]) :  #Si le garçon n'a pas été marié, on le marie
			Mariage_arbitraire.append([Liste_total_voeux[i][j]])	

		else : #Si tous les garçons ont été marié, on ajoute une liste vide, qui sera un sommet libre
			Mariage_arbitraire.append([])


	return(Mariage_arbitraire)


def MaJ_Graphe(Liste_total_voeux,Mariage_arbitraire) : 
#On peut représenter sous forme de graphe la relation de voeux entre les garçons et les filles
#Dès qu'on a marié (temporairement) une fille à un garçon on doit supprimer le trait, ie mettre à jour Liste_total_voeux
	
	MaJ_Liste_voeux=[]
	MaJ_Liste_voeux[:]=Liste_total_voeux

	for fille in range(0,len(Liste_total_voeux)) :
		k=0
		while k<len(MaJ_Liste_voeux[fille]) : 
			if len(Mariage_arbitraire[fille])!=0 and Mariage_arbitraire[fille][0]==MaJ_Liste_voeux[fille][k] : 
				MaJ_Liste_voeux[fille].pop(k)
				k-=1
			k+=1	

		
	return(MaJ_Liste_voeux)		




#Un sommet libre est une fille ou un garçon qui n'a pas été marié

def recherche_sommets_libres_filles(Mariage_arbitraire) :

	#Renvoie la liste des sommets libres chez les filles

	Liste_sommets_libres_filles=[]

	for i in range(1,len(Mariage_arbitraire)) : 


		if Mariage_arbitraire[i]==[] :   #Si la fille n'a pas été arbitrairement marié
			Liste_sommets_libres_filles.append(i)  #Alors c'est un sommet libre

	return(Liste_sommets_libres_filles) 


def recherche_sommets_libres_garcons(Mariage_arbitraire,Liste_garcons) : 

#Renvoie la liste des sommets libres chez les garçons

	Liste_sommets_libres_garcons=[]

	for i in range(0,len(Liste_garcons)) : 

		if appartient_ss_liste(Liste_garcons[i],Mariage_arbitraire)==False :
			Liste_sommets_libres_garcons.append(Liste_garcons[i])

	return(Liste_sommets_libres_garcons)



def creation_checkpoint(Mariage_arbitraire,Liste_garcons_desirees,Liste_sommets_libres_garcons,Liste_sommets_libres_filles) :

	Mariage_arbitraire_checkpoint=[]
	Mariage_arbitraire_checkpoint=copy.deepcopy(Mariage_arbitraire)

	#Insertion du checkpoint des filles libres

	for i in range(0,len(Mariage_arbitraire)) : 
		if len(Mariage_arbitraire[i])==0:
			Mariage_arbitraire_checkpoint[i].append("C_F")  #Par convention on l'appelle C_F



	#Insertion du checkpoint des garçons libres

	Liste_garcons_desirees_checkpoint=[]
	Liste_garcons_desirees_checkpoint=copy.deepcopy(Liste_garcons_desirees)


	for G in Liste_garcons_desirees_checkpoint : 
		if G[0] in Liste_sommets_libres_garcons:
			G[1].append("C_G")


	return(Mariage_arbitraire_checkpoint,Liste_garcons_desirees_checkpoint)



def init_dist(Mariage_arbitraire_checkpoint,Liste_garcons_desirees_checkpoint,Liste_sommets_libres_garcons) :

	#On initialise la distance comme si on avait parcouru un tour de boucle


	dist=[["G","C_F","inf"]]

	dist=dist + [["F",i,"inf"] for i in range(len(Mariage_arbitraire_checkpoint))]

	for G in Liste_garcons_desirees_checkpoint :
		if G[0] in Liste_sommets_libres_garcons :
			dist.append(["G",G[0],1])
		else :
			dist.append(["G",G[0],"inf"])

	dist.append(["F","C_G",0])

	return(dist)

def init_pred(dist) : 

	#On initialise la liste des précedesseurs comme si on avait parcouru un tour de boucle

	pred=[]
	pred=copy.deepcopy(dist)

	for L in pred :
		if L[2]==1 :
			L[2]="C_G" 
		else :
			L[2]=-1

	return(pred)

def init_Tas(Liste_sommets_libres_garcons) :

	Tas=[]

	for sommet_libre in Liste_sommets_libres_garcons :
		Tas.append(["G",sommet_libre,1])

	return(Tas)

def Extract_Min_Tas(Tas) :

	Min=0  #Min est l'indice du plus petit (en fonction de la distance) élément dans le tas 

	for i in range(1,len(Tas)) :
		if Tas[i][2]<Tas[Min][2] :
			Min=i

	return(Tas.pop(Min))

def Voisins_non_visite(Noeud_de_depart,Noeuds_visites,Mariage_arbitraire_checkpoint,Liste_garcons_desirees_checkpoint) :

	Voisins_a_visiter=[]

	if Noeud_de_depart[0]=="F" :   #Si le noeud de départ est une fille
		for i in range(len(Mariage_arbitraire_checkpoint)) :
			if i==Noeud_de_depart[1] :
				Voisins_a_visiter.append(Mariage_arbitraire_checkpoint[i][0])

		for i in range(len(Voisins_a_visiter)) :
			Voisins_a_visiter[i]=["G",Voisins_a_visiter[i]]


	else :   #Si le noeud de départ est un garçon

		for L in Liste_garcons_desirees_checkpoint :
	
			if L[0]==Noeud_de_depart[1] :
					Voisins_a_visiter[:]=L[1]



		if "C_G" in Voisins_a_visiter :
			Voisins_a_visiter.pop(Voisins_a_visiter.index("C_G"))


		for i in range(len(Mariage_arbitraire_checkpoint)) :

			if Mariage_arbitraire_checkpoint[i][0]==Noeud_de_depart[1] and (i in Voisins_a_visiter) :
				Voisins_a_visiter.pop(Voisins_a_visiter.index(i))

		
		for i in range(len(Voisins_a_visiter)) :
			Voisins_a_visiter[i]=["F",Voisins_a_visiter[i]]


	#Il faut enlever les noeuds déjà visités

	i=0
	while i<len(Voisins_a_visiter) :
		for Noeuds in Noeuds_visites :
				if Noeuds==Voisins_a_visiter[i] :
					Voisins_a_visiter.pop(i)
					i-=1
					break  #Au cas où si Voisins_a_visiter qui est vide
		i+=1	



	return(Voisins_a_visiter)

def recherche_indice_dist_pred(Noeud,dist) :

	indice=0

	while dist[indice][0]!=Noeud[0] or dist[indice][1]!=Noeud[1] :
		indice+=1

	return(indice)

def MaJ_Tas(Tas,indice,dist) :

	Dans_le_Tas=False

	for elts in Tas :
		if elts[0]==dist[indice][0] and elts[1]==dist[indice][1] :
			elts[2]=dist[indice][2]
			Dans_le_Tas=True

	if Dans_le_Tas==False :
		Tas.append(dist[indice][:])

def creation_chemin_from_pred(pred,chemin,Noeud_precedent) :


	if Noeud_precedent=="C_G" :
		return(chemin)

	else : 
		if Noeud_precedent==chemin[-1][0] :  #Si le noeud précédent est un garçon
			for elts in pred :
				if elts[0]=="G" and elts[1]==Noeud_precedent :
					chemin.append([Noeud_precedent,elts[2]])
					break
			return(creation_chemin_from_pred(pred,chemin,chemin[-1][1]))

		else  :   #Si le noeud précedent est une fille
			for elts in pred :
				if elts[0]=="F" and elts[1]==Noeud_precedent :
					chemin.append([elts[2],Noeud_precedent])
					break
			return(creation_chemin_from_pred(pred,chemin,chemin[-1][0]))		

def creation_chemin_from_sommets(pred,Liste_sommets_libres_filles) :

	chemin=[]


	for elts in pred : 
		print(elts[0])
		print(elts[1])
		print(elts[2])
		print(pred[0][2])
		print("\n")
		if elts[0]=="F" and (elts[1] in Liste_sommets_libres_filles) and elts[2]!=-1 :
			chemin.append([elts[2],elts[1]])
			break
	print(chemin)
	return(creation_chemin_from_pred(pred,chemin,chemin[0][0]))

def creation_chemin_from_checkpoint(pred) :

	chemin=[]

	for elts in pred :

		if elts[0]=="F" and elts[1]==pred[0][2] :  #Car C_F est le premier élément de pred
			chemin.append([elts[2],elts[1]])
			break

	return(creation_chemin_from_pred(pred,chemin,chemin[0][0]))


def Dijkstra(Mariage_arbitraire_checkpoint,Liste_garcons_desirees_checkpoint,Liste_sommets_libres_garcons,Liste_sommets_libres_filles) :
	
	dist=init_dist(Mariage_arbitraire_checkpoint,Liste_garcons_desirees_checkpoint,Liste_sommets_libres_garcons)
	pred=init_pred(dist)
	Tas=init_Tas(Liste_sommets_libres_garcons)   #En initialisant le tas de cette façon, on réalise déjà un tour de boucle
	Noeuds_visites=[["F","C_G"]]  

	while len(Tas)!=0 and ["G","C_F"] not in Noeuds_visites : 




		Noeud_de_depart=Extract_Min_Tas(Tas)
		Noeud_de_depart.pop()
		Noeuds_visites.append(Noeud_de_depart)
		Voisins_a_visiter=Voisins_non_visite(Noeud_de_depart,Noeuds_visites,Mariage_arbitraire_checkpoint,Liste_garcons_desirees_checkpoint)

		for Voisins in Voisins_a_visiter :
			indice_voisin=recherche_indice_dist_pred(Voisins,dist)
			indice_depart=recherche_indice_dist_pred(Noeud_de_depart,dist)
			if dist[indice_voisin][2]=="inf" :
				dist[indice_voisin][2]=dist[indice_depart][2]+1
				pred[indice_voisin][2]=Noeud_de_depart[1]
				Tas.append(dist[indice_voisin][:])

			else : 
				d=dist[indice_depart][2]+1 
				if d<dist[indice_voisin][2] :
					dist[indice_voisin][2]=d
					pred[indice_voisin][2]=Noeud_de_depart[1]
					MaJ_Tas(Tas,indice_voisin,dist)




	if pred[0][2]==-1 :  #C_F est placé à l'indice 0 dans la liste pred

		chemin=creation_chemin_from_sommets(pred,Liste_sommets_libres_filles)

	else : 

		chemin=creation_chemin_from_checkpoint(pred)

	chemin.pop()  #On retire le chemin jusqu'à C_G

	chemin.reverse()


	
	return(chemin) 


def chemin_en_liste_voeux(chemin,Mariage_arbitraire_checkpoint) : 


	chemin_converti=[[]]*len(Mariage_arbitraire_checkpoint)

	for i in range(0,len(chemin)):
	
		if len(chemin_converti[chemin[i][1]])==0 :

			chemin_converti[chemin[i][1]]=[chemin[i][0]]

		else :
			chemin_converti[chemin[i][1]].append(chemin[i][0])
	

	return(chemin_converti)

def difference_symetrique(chemin,Mariage_arbitraire) : 
# Renvoie la diffèrence symétrique entre le graphe du mariage arbitraire et le chemin 
	
	Nouveau_mariage_arbitraire=chemin_en_liste_voeux(chemin,Mariage_arbitraire)

	for i in range(0,len(Nouveau_mariage_arbitraire)) :
		if len(Nouveau_mariage_arbitraire[i])==0 and len(Mariage_arbitraire[i])!=0 :
			Nouveau_mariage_arbitraire[i]=[Mariage_arbitraire[i][0]]

		elif len(Nouveau_mariage_arbitraire[i])==2 :

			for j in range(0,2) :
				if Nouveau_mariage_arbitraire[i][j]==Mariage_arbitraire[i][0] :
					Nouveau_mariage_arbitraire[i].pop(j)


	return(Nouveau_mariage_arbitraire) 

def test(L): 
    #'''Fonction qui prend une liste de filles en paramètre (une fille étant 
   # repésentée par une sous liste contenant ses voeux).
   # On renvoie: 
   # - 1 si il y a au total plus de garçons que de filles
   # - 0 si il y a au total autant de filles que de garçons
   # - (-1) si il y a au total plus de filles que de garçons. (Dans ce cas la 
   # condition des mariages n'est pas vérifiée'''
    
    T=[]        #Liste contenant l'ensemble des garçons contenus dans L
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


def verif(L):
    #'''Fonction récurssive prenant en paramètre une liste de filles avec leurs 
    #voeux respectifs et détermine si la condition de mariages est vérifiée.
   # La fonction va vérifier avec la fonction test() tous les sous 
   # enssembles de L. 
   # Elle renvoie:
   # - 1 si la condition des mariages est vérifiée et si il y a plus de garçons 
   # que de filles.
   # - 0 si la condition des mariages est vérifiée et si il y a autant de garçon
  #  que de filles.
   # - (-1) si la condition des mariages n'est pas vérifiée car il existe un sous
   # ensemble de L dans lequel il y'a plus de filles que de garçons.
   # '''
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


#Listes pour tester


Lval=[[3],[1,2]]
L=[[1,2,3,4,5],[4,5,3],[2,3],[1,5],[1,3,5]]
V1=[[10,11,13],[10,12,13],[13],[10,13]]
V2=[[10],[12,13],[11,15],[10,12],[12,14],[11,14,15,16],[11,13,14,16]]
Ln=[[4],[1,2],[3],[5],[3,1,7,8],[1],[2],[1,2],[1]]
Lpp=[[1,2,3,5,46],[46,42,45,56],[1,2,3],[2,1],[3,2],[54,78,99,62],[99],[19,97],[19,97]]
Lv2=[[2, 4, 23, 25, 26, 45, 47, 48], [57, 68, 62, 77, 79, 82, 4, 6, 18], [27, 29, 32, 49, 42, 54, 60, 64, 66], [70, 83, 85, 8, 10, 13, 21, 34, 36], [44, 56, 58, 65, 67, 79, 85, 87, 89], [12, 15, 28, 36, 38, 40, 59, 50, 52], [69, 71, 73, 88, 80, 82, 18, 20, 22], [31, 43, 44, 52, 64, 67, 73, 74, 77], [9, 1, 3, 22, 24, 36, 45, 46, 49], [66, 69, 61, 76, 77, 81, 4, 15, 17], [17, 10, 38, 31, 33, 52, 54, 56], [64, 76, 77, 84, 86, 97, 19, 13, 25], [34, 36, 47, 56, 58, 69, 77, 79, 70], [87, 99, 90, 15, 27, 29, 38, 40, 41], [50, 61, 65, 71, 72, 86, 90, 92, 95], [29, 21, 33, 42, 43, 57, 63, 67, 69], [76, 88, 80, 93, 96, 98, 23, 36, 38], [47, 59, 51, 69, 71, 73, 89, 81, 83], [15, 18, 10, 39, 31, 43, 51, 53, 55], [73, 75, 76, 83, 85, 96, 10, 22, 24], [24, 26, 45, 47, 48, 67, 60, 62], [79, 82, 84, 99, 92, 4, 26, 28, 39], [49, 42, 54, 63, 65, 77, 84, 86, 88], [94, 6, 8, 20, 33, 35, 45, 57, 58], [67, 79, 70, 88, 80, 91, 7, 9, 1], [36, 38, 40, 59, 51, 62, 71, 72, 75], [81, 93, 96, 0, 2, 4, 30, 42, 44], [53, 64, 68, 74, 87, 89, 95, 98, 90], [22, 23, 25, 44, 46, 59, 66, 60, 62], [89, 81, 83, 99, 91, 3, 26, 37, 31], [30, 32, 52, 54, 56, 74, 76, 78], [86, 98, 99, 6, 8, 19, 33, 35, 47], [56, 58, 69, 78, 70, 83, 99, 92, 94], [9, 11, 14, 37, 49, 41, 50, 61, 65], [72, 85, 87, 94, 96, 8, 12, 16, 18], [41, 43, 56, 65, 67, 79, 87, 89, 81], [98, 0, 2, 17, 19, 11, 47, 59, 51], [60, 72, 73, 81, 93, 95, 2, 3, 5], [38, 30, 32, 51, 53, 65, 74, 75, 78], [95, 96, 90, 5, 7, 10, 33, 44, 46], [46, 48, 67, 60, 62, 81, 83, 85], [93, 5, 6, 13, 15, 26, 48, 41, 53], [63, 65, 77, 85, 87, 99, 6, 8, 0], [16, 28, 20, 44, 56, 58, 67, 79, 70], [89, 91, 94, 0, 2, 15, 29, 21, 22], [58, 50, 62, 71, 73, 86, 93, 96, 98], [3, 16, 19, 22, 24, 27, 53, 64, 67], [75, 88, 80, 98, 0, 2, 18, 10, 12], [44, 45, 48, 66, 60, 72, 80, 82, 84], [2, 4, 5, 12, 14, 25, 47, 51, 53], [53, 55, 74, 76, 77, 97, 98, 91], [8, 11, 13, 28, 21, 33, 55, 57, 69], [78, 70, 83, 90, 94, 6, 13, 15, 17], [23, 35, 37, 50, 61, 64, 73, 85, 87], [96, 8, 0, 17, 19, 20, 36, 38, 30], [65, 67, 79, 88, 80, 91, 0, 2, 3], [10, 22, 24, 39, 31, 33, 69, 71, 73], [82, 94, 95, 3, 15, 18, 24, 25, 29], [51, 52, 54, 74, 75, 88, 96, 99, 91], [17, 10, 12, 27, 20, 32, 55, 66, 69], [68, 61, 81, 83, 85, 3, 5, 7], [15, 27, 28, 35, 37, 48, 62, 64, 76], [85, 87, 99, 7, 9, 12, 29, 20, 23], [38, 40, 43, 66, 78, 70, 89, 91, 94], [1, 14, 16, 22, 25, 37, 41, 44, 46], [71, 72, 85, 93, 96, 8, 16, 18, 10], [27, 39, 31, 44, 48, 40, 74, 88, 80], [99, 1, 2, 10, 22, 24, 31, 32, 34], [66, 69, 61, 80, 82, 94, 3, 5, 6], [24, 26, 29, 34, 36, 47, 61, 73, 75], [75, 77, 96, 98, 91, 18, 12, 14], [21, 33, 35, 42, 44, 56, 78, 79, 82], [90, 94, 6, 14, 16, 28, 35, 37, 39], [45, 57, 59, 71, 85, 87, 96, 8, 0], [18, 20, 21, 39, 31, 42, 58, 50, 52], [87, 89, 91, 0, 2, 13, 22, 23, 27], [32, 44, 47, 52, 53, 56, 82, 93, 95], [4, 17, 19, 25, 39, 31, 45, 49, 41], [73, 74, 76, 95, 99, 1, 19, 11, 13], [31, 33, 35, 41, 43, 54, 77, 80, 82], [82, 84, 3, 5, 7, 26, 27, 20], [37, 49, 42, 57, 59, 62, 84, 86, 98], [7, 9, 12, 29, 22, 34, 40, 44, 46], [50, 63, 66, 89, 90, 93, 1, 14, 16], [25, 37, 39, 46, 48, 59, 65, 67, 69], [92, 96, 8, 17, 19, 21, 39, 31, 32], [49, 51, 53, 68, 60, 62, 98, 0, 2], [11, 23, 24, 33, 44, 47, 53, 54, 57], [89, 81, 83, 3, 4, 16, 25, 26, 20], [46, 49, 41, 56, 59, 61, 84, 96, 97], [97, 90, 18, 12, 14, 32, 34, 36], [44, 56, 57, 64, 66, 78, 99, 93, 5], [14, 16, 28, 36, 38, 40, 58, 59, 52], [67, 79, 71, 95, 7, 9, 18, 20, 21], [30, 42, 45, 51, 54, 66, 71, 72, 75], [0, 1, 13, 22, 25, 37, 44, 47, 49], [56, 68, 60, 73, 77, 79, 4, 17, 19], [27, 39, 31, 49, 51, 53, 60, 61, 63], [95, 98, 90, 19, 11, 23, 32, 34, 35], [53, 55, 56, 63, 65, 76, 90, 2, 4]]
Lv3=[[2, 3, 12, 14, 18, 21, 23], [8, 6, 15, 18, 19, 4, 1], [12, 14, 15, 22, 24, 21, 8, 10, 11], [19, 16, 24, 4, 6, 8, 11, 18, 15], [4, 1, 12, 14, 11, 18, 20, 22], [8, 5, 18, 16, 24, 2, 4], [14, 12, 22, 24, 21, 5, 7], [18, 15, 22, 3, 0, 14, 16], [20, 23, 0, 5, 12, 14, 17, 24, 21], [6, 7, 5, 18, 16, 17, 24, 1, 3], [14, 11, 20, 22, 24, 1, 8, 5], [16, 18, 15, 3, 0, 2, 12, 14], [24, 22, 4, 9, 6, 15, 23, 20], [1, 4, 6, 11, 18, 15, 24, 2], [12, 14, 11, 20, 22, 24, 1, 7, 5], [15, 17, 1, 3, 7, 14, 12], [22, 24, 9, 6, 8, 18, 15], [0, 3, 5, 10, 13, 21, 4, 1], [8, 5, 12, 17, 20, 21, 0, 7, 9], [18, 15, 17, 1, 3, 0, 7, 13, 11], [22, 23, 8, 5, 7, 13, 16, 18], [3, 1, 10, 13, 14, 24, 21], [7, 9, 11, 17, 19, 16, 3, 5], [14, 11, 19, 24, 1, 3, 6, 13, 10], [24, 21, 7, 5, 13, 15, 17]]


L16=[[1, 2, 0, 5, 7, 9, 10, 15, 13, 14], [10, 11, 9, 13, 15, 12, 2, 6, 7, 4, 8, 14], [1, 3, 4, 6, 11, 8, 9, 14, 12, 13, 15, 5], [11, 8, 14, 12, 1, 3, 0, 6, 7, 9, 10, 15], [7, 5, 6, 11, 9, 15, 12, 2, 3, 1, 10], [12, 14, 15, 13, 3, 1, 4, 8, 10, 11, 0], [7, 5, 10, 8, 13, 14, 12, 0, 1, 3, 9], [13, 15, 0, 2, 4, 5, 7, 8, 9, 14, 12, 1], [10, 11, 9, 14, 15, 1, 2, 7, 5, 12], [3, 0, 2, 6, 7, 5, 11, 14, 12, 13, 4], [10, 11, 12, 14, 3, 0, 2, 7, 4, 5, 15, 13], [3, 1, 7, 4, 10, 8, 9, 14, 12, 2, 0, 5, 6], [12, 13, 15, 0, 2, 7, 5, 10, 11, 9, 3], [5, 6, 4, 8, 10, 11, 13, 0, 2, 7], [12, 13, 3, 0, 5, 7, 4, 6, 9, 11, 8, 1], [5, 7, 9, 10, 12, 14, 15, 1, 2, 6, 11]]
L36=[[2, 3, 13, 15, 16, 18, 26, 28], [2, 4, 0, 15, 17, 14, 27, 29, 24], [5, 0, 9, 12, 14, 22, 29, 25, 27], [1, 10, 6, 14, 23, 19, 25, 27, 35], [11, 7, 8, 23, 19, 21, 27, 29, 31], [7, 9, 17, 20, 21, 18, 29, 32, 33], [8, 10, 19, 21, 23, 25, 33, 34], [9, 10, 7, 22, 23, 20, 33, 35, 31], [11, 7, 15, 18, 20, 28, 35, 31, 33], [7, 16, 12, 21, 29, 25, 31, 34, 0], [17, 13, 14, 29, 25, 27, 33, 30, 2], [13, 15, 18, 26, 27, 24, 30, 2, 3], [14, 16, 25, 27, 29, 31, 3, 5], [15, 17, 13, 28, 29, 26, 3, 5, 1], [17, 14, 22, 24, 27, 35, 5, 1, 4], [13, 22, 18, 27, 35, 31, 1, 4, 6], [23, 19, 20, 30, 32, 34, 3, 0, 8], [20, 21, 24, 32, 34, 30, 0, 8, 10], [20, 22, 32, 33, 35, 1, 9, 11], [21, 23, 19, 34, 30, 32, 10, 11, 8], [18, 20, 28, 30, 33, 5, 6, 7, 10], [21, 29, 24, 33, 5, 1, 8, 10, 12], [29, 25, 28, 0, 2, 4, 10, 6, 14], [26, 27, 30, 2, 4, 1, 6, 14, 16], [27, 28, 2, 4, 0, 8, 15, 17], [27, 29, 26, 4, 0, 3, 16, 17, 14], [24, 26, 34, 0, 3, 11, 12, 14, 16], [27, 35, 31, 4, 6, 7, 14, 16, 18], [30, 31, 34, 6, 8, 10, 17, 13, 20], [32, 35, 1, 9, 11, 7, 13, 21, 22], [33, 34, 8, 10, 6, 14, 22, 23], [34, 35, 32, 11, 7, 9, 22, 18, 20], [30, 33, 5, 7, 9, 17, 18, 21, 23], [33, 5, 1, 10, 12, 14, 20, 23, 25], [0, 2, 4, 12, 14, 17, 23, 19, 26], [2, 5, 7, 15, 17, 13, 19, 27, 28]]
L49=[[2, 3, 19, 15, 17, 25, 33, 29], [41, 37, 46, 9, 11, 20, 21, 24, 26], [33, 41, 37, 6, 0, 10, 19, 21, 23], [31, 33, 35, 40, 42, 43, 15, 18, 20], [21, 30, 32, 37, 40, 42, 12, 7, 9], [24, 27, 22, 29, 38, 40, 2, 3, 13], [15, 17, 25, 33, 29, 38, 36, 45, 46], [8, 10, 26, 21, 23, 31, 40, 35], [48, 43, 3, 16, 18, 26, 28, 30, 32], [39, 48, 42, 12, 7, 16, 25, 34, 29], [36, 39, 48, 46, 6, 1, 22, 24, 26], [34, 36, 37, 44, 46, 6, 19, 14, 16], [31, 33, 28, 35, 44, 46, 8, 10, 19], [21, 23, 32, 39, 35, 44, 42, 2, 4], [14, 16, 32, 34, 30, 37, 46, 48], [5, 1, 10, 22, 24, 33, 41, 37, 39], [45, 5, 0, 18, 20, 22, 32, 41, 35], [43, 45, 5, 3, 12, 7, 28, 30, 33], [41, 42, 44, 1, 3, 13, 24, 27, 22], [37, 40, 35, 42, 1, 3, 14, 16, 25], [28, 30, 38, 46, 48, 1, 6, 8, 10], [26, 23, 38, 40, 36, 44, 4, 5], [11, 13, 16, 34, 30, 39, 48, 42, 45], [3, 12, 13, 25, 27, 28, 38, 47, 42], [0, 3, 12, 9, 19, 20, 35, 36, 39], [47, 0, 1, 8, 9, 19, 31, 33, 28], [44, 45, 48, 6, 8, 10, 21, 23, 31], [41, 36, 45, 3, 5, 8, 12, 15, 17], [33, 29, 45, 47, 42, 1, 10, 12], [18, 20, 22, 41, 37, 46, 5, 0, 2], [9, 18, 20, 31, 33, 35, 44, 4, 6], [13, 8, 18, 15, 25, 27, 48, 43, 44], [4, 13, 8, 14, 16, 25, 37, 40, 35], [1, 3, 5, 12, 14, 16, 34, 29, 38], [46, 42, 2, 10, 11, 14, 18, 21, 23], [39, 35, 2, 4, 5, 7, 16, 18], [24, 26, 34, 47, 43, 3, 11, 13, 9], [14, 24, 26, 37, 39, 48, 1, 11, 12], [20, 15, 24, 22, 31, 33, 5, 0, 2], [9, 19, 14, 27, 22, 31, 43, 45, 48], [7, 9, 12, 17, 27, 22, 40, 35, 44], [4, 0, 9, 16, 18, 27, 25, 34, 29], [46, 47, 8, 10, 12, 20, 23, 25], [31, 32, 41, 5, 6, 9, 18, 20, 14], [21, 31, 33, 43, 46, 6, 7, 17, 19], [26, 21, 29, 28, 37, 40, 11, 13, 8], [16, 26, 21, 34, 29, 37, 1, 2, 5], [14, 16, 17, 24, 34, 29, 46, 42, 2], [10, 13, 15, 22, 24, 33, 31, 40, 36]]
L64=[[2, 3, 21, 22, 17, 25, 35, 37], [44, 46, 55, 3, 5, 15, 23, 19, 29], [37, 38, 32, 47, 48, 51, 7, 8, 11], [20, 30, 24, 32, 33, 44, 49, 52, 54], [10, 13, 15, 31, 25, 27, 34, 45, 47], [53, 55, 57, 14, 8, 18, 27, 28, 39], [46, 40, 42, 55, 49, 59, 10, 20, 21], [31, 33, 35, 41, 43, 53, 0, 2, 4], [8, 10, 27, 29, 30, 42, 44], [50, 52, 62, 9, 12, 21, 30, 24, 35], [43, 45, 47, 53, 63, 56, 13, 23, 16], [25, 36, 38, 46, 40, 49, 56, 57, 60], [16, 18, 21, 38, 32, 33, 41, 51, 54], [58, 61, 7, 19, 23, 25, 33, 35, 46], [52, 55, 49, 60, 56, 2, 16, 26, 28], [36, 47, 41, 48, 50, 60, 14, 9, 11], [21, 16, 33, 35, 37, 55, 50], [57, 59, 5, 23, 18, 28, 37, 39, 41], [48, 51, 53, 60, 6, 7, 19, 29, 31], [32, 43, 45, 53, 54, 56, 6, 0, 2], [31, 25, 26, 44, 46, 40, 48, 57, 59], [1, 3, 13, 26, 29, 39, 40, 41, 51], [59, 60, 63, 3, 6, 8, 30, 33, 34], [43, 52, 55, 61, 56, 2, 20, 22, 17], [28, 30, 46, 42, 44, 62, 56], [6, 1, 11, 30, 31, 34, 43, 45, 55], [63, 58, 60, 2, 12, 14, 25, 36, 38], [47, 48, 51, 58, 61, 7, 13, 15, 8], [37, 39, 33, 50, 53, 55, 62, 0, 2], [15, 9, 19, 33, 35, 45, 54, 48, 58], [1, 3, 4, 10, 12, 22, 36, 47, 41], [49, 59, 61, 4, 5, 8, 27, 29, 31], [35, 36, 53, 48, 50, 4, 6], [13, 14, 17, 36, 38, 47, 50, 52, 62], [6, 7, 2, 8, 18, 20, 32, 41, 44], [53, 63, 57, 0, 3, 13, 18, 21, 23], [44, 46, 40, 56, 58, 61, 4, 14, 8], [22, 16, 26, 47, 41, 51, 59, 62, 0], [15, 9, 11, 16, 18, 28, 43, 52, 55], [56, 2, 3, 10, 12, 22, 33, 35, 37], [41, 43, 60, 62, 56, 11, 13], [19, 21, 31, 43, 45, 54, 63, 58, 4], [12, 14, 15, 22, 24, 27, 46, 48, 51], [59, 5, 7, 15, 9, 20, 25, 27, 29], [49, 52, 54, 7, 1, 2, 10, 21, 23], [27, 30, 32, 54, 48, 58, 2, 4, 15], [22, 16, 18, 31, 25, 35, 49, 59, 61], [5, 8, 10, 17, 19, 28, 40, 42, 44], [54, 49, 2, 4, 6, 17, 19], [26, 28, 38, 49, 51, 61, 6, 7, 10], [18, 20, 22, 29, 38, 32, 53, 62, 56], [1, 12, 14, 22, 23, 25, 39, 33, 36], [56, 58, 60, 13, 15, 9, 17, 26, 29], [34, 35, 47, 59, 62, 0, 9, 10, 20], [27, 30, 24, 36, 39, 41, 56, 2, 3], [12, 21, 16, 31, 25, 35, 53, 48, 50], [61, 56, 9, 11, 13, 30, 25], [39, 34, 44, 63, 57, 3, 12, 14, 16], [24, 27, 29, 35, 45, 47, 59, 5, 7], [8, 17, 20, 28, 30, 32, 46, 40, 41], [7, 0, 2, 18, 22, 16, 31, 33, 34], [40, 42, 53, 2, 3, 14, 23, 17, 27], [34, 36, 39, 43, 44, 48, 5, 8, 10], [18, 28, 31, 37, 32, 42, 60, 61, 56]]

L225=[[63, 93, 66, 96], [142, 187, 145, 190], [20, 65, 23, 68], [117, 162], [176, 221, 179, 224], [75, 120, 78, 123], [152, 197, 155, 200], [47, 77, 50, 80], [130, 175, 133, 178], [4, 49, 7, 52], [92, 137], [165, 210, 168, 213], [62, 107, 65, 110], [141, 186, 144, 189], [34, 64, 37, 67], [83, 113, 86, 116], [162, 207], [41, 86, 43, 88], [124, 169, 127, 172], [180, 183], [98, 143, 100, 145], [175, 220, 178, 223], [70, 100, 73, 103], [136, 181, 138, 183], [27, 72], [109, 154, 112, 157], [185, 188], [82, 127, 85, 130], [163, 208], [54, 84, 57, 87], [91, 121, 93, 123], [170, 215, 173, 218], [48, 93, 51, 96], [145, 190, 148, 193], [24, 27], [106, 151], [181, 183], [76, 106, 78, 108], [158, 203, 160, 205], [33, 78, 35, 80], [132, 177], [207], [90, 135, 93, 138], [169, 214, 172, 217], [62, 92, 65, 95], [111, 141, 114, 144], [191, 193], [69, 114, 71, 116], [152, 197], [32], [125, 170, 128, 173], [203, 206], [98, 128, 101, 131], [166, 211], [55, 100, 57, 102], [138, 183, 140, 185], [33, 36], [110, 155, 113, 158], [189, 192], [83, 113, 85, 115], [131, 161, 134, 164], [198, 201], [76, 121], [173, 218, 176, 221], [7, 52, 9, 54], [146, 191, 149, 194], [32], [106, 136], [183, 186], [61, 106, 63, 108], [159, 204, 162, 207], [10, 55, 13, 58], [132, 177], [17, 20], [90, 120, 93, 123], [139, 169, 142, 172], [39, 41], [96, 141, 99, 144], [193], [27, 72], [151, 196, 154, 199], [6, 51, 8, 53], [123, 153, 126, 156], [26, 29], [80, 125, 83, 128], [165, 210, 168, 213], [16, 61, 19, 64], [138, 183, 141, 186], [37, 40], [111, 141, 113, 143], [159, 189, 162, 192], [1, 46, 3, 48], [117, 162, 119, 164], [200, 203], [34, 79, 37, 82], [174, 219, 177, 222], [27, 72, 29, 74], [146, 176, 149, 179], [32, 35], [91, 136], [185, 188], [36, 81, 39, 84], [158, 203, 161, 206], [2, 47], [130, 160, 133, 163], [167, 197, 170, 200], [22, 67, 24, 69], [124, 169, 127, 172], [41, 44], [55, 100, 58, 103], [182], [31, 76, 34, 79], [152, 182, 154, 184], [9, 54, 12, 57], [109, 154, 111, 156], [16], [47, 92], [166, 211, 169, 214], [20, 65, 23, 68], [138, 168, 141, 171], [188, 218, 190, 220], [41, 86, 44, 89], [145, 190, 148, 193], [3, 48, 6, 51], [60, 105, 63, 108], [202, 204], [54, 99, 57, 102], [174, 204, 177, 207], [15, 60, 18, 63], [131, 176, 134, 179], [34, 36], [64, 109, 67, 112], [186, 189], [42, 87], [159, 189, 161, 191], [195, 197], [49, 94, 52, 97], [152, 197, 154, 199], [24, 69, 27, 72], [83, 128, 86, 131], [42], [60, 105, 63, 108], [180, 210, 183, 213], [34, 79, 37, 82], [137, 182, 140, 185], [11, 56, 14, 59], [86, 131, 89, 134], [197], [48, 93, 51, 96], [166, 196, 169, 199], [21, 23], [70, 115, 73, 118], [173, 218, 176, 221], [32, 77], [91, 136], [4, 49, 7, 52], [82, 127, 85, 130], [202, 204], [58, 103], [159, 204, 161, 206], [17, 62, 20, 65], [92, 137, 95, 140], [35, 37], [68, 113, 71, 116], [187, 217, 190, 220], [10, 40, 13, 43], [77, 122, 80, 125], [193], [52, 97, 55, 100], [111, 156, 113, 158], [25, 70, 28, 73], [103, 148], [28], [63, 108, 66, 111], [165, 210, 167, 212], [36, 81, 39, 84], [112, 157, 115, 160], [11, 56, 14, 59], [76, 121, 79, 124], [197], [18, 48, 21, 51], [98, 143, 101, 146], [20, 23], [72, 117], [131, 176, 134, 179], [30, 75, 33, 78], [107, 152, 110, 155], [3, 33, 5, 35], [85, 130, 88, 133], [184, 187], [45, 90, 47, 92], [120, 165, 123, 168], [17, 62, 20, 65], [96, 141, 99, 144], [20, 23], [39, 69, 42, 72], [117, 162], [41, 44], [79, 124, 82, 127], [138, 183, 141, 186], [53, 98, 56, 101], [131, 176, 134, 179], [25, 55, 28, 58], [91, 136, 94, 139], [27], [65, 110, 67, 112], [140, 185, 143, 188], [37, 82, 40, 85], [106, 151], [10, 40, 12, 42], [46, 76, 49, 79], [126, 171, 128, 173], [3, 48, 6, 51], [100, 145, 103, 148], [159, 204, 162, 207], [61, 106], [136, 181, 139, 184], [31, 61, 34, 64], [113, 158, 116, 161], [33, 36], [87, 132], [163, 208], [45, 90, 48, 93], [124, 169, 127, 172], [17, 47, 20, 50]]

L900=[[157, 187], [345, 375, 346, 376], [530, 531], [651, 681, 652, 682], [10, 40, 11, 41], [200, 230], [387, 417], [540, 541], [661, 691], [83, 84], [242], [432], [586], [705, 735], [95, 125, 96, 126], [288, 318], [474, 475], [627, 657, 628, 658], [745, 775, 746, 776], [142, 172], [331], [486, 516, 487, 517], [638, 668, 639, 669], [755, 785], [185, 186], [373], [527, 557, 528, 558], [678, 708, 679, 709], [39, 69], [228, 258], [193, 223], [380, 410, 381, 411], [565], [686, 716, 687, 717], [46, 76, 47, 77], [235, 265], [391, 421], [580, 581], [700, 730, 701, 731], [119], [280, 281], [468, 469], [622], [741, 771], [134, 164, 135, 165], [324, 354], [480, 481], [633, 663, 634, 664], [751, 781], [178, 208], [366, 367], [521, 551, 522, 552], [673, 703, 674, 704], [790, 820, 791, 821], [221], [408], [561, 591, 562, 592], [712, 742, 713, 743], [74, 104, 75, 105], [262, 292, 263, 293], [228, 258], [415, 445], [574, 575], [695, 725, 696, 726], [82, 112], [269, 299], [431, 461, 432, 462], [616, 617], [736, 766, 737, 767], [123], [317], [504], [658], [777, 807], [170, 200, 171, 201], [330, 360], [515, 516], [668, 698], [786, 816, 787, 817], [184, 214], [401, 402], [556, 586], [707, 737, 708, 738], [825, 855, 826, 856], [256], [447], [572, 602, 573, 603], [723, 753], [109, 139, 110, 140], [272, 302], [263, 293], [424, 454, 425, 455], [610, 611], [732, 762], [116, 146, 117, 147], [279, 309, 280, 310], [467, 497, 468, 498], [652], [772, 802, 773, 803], [163], [352, 353], [510], [663], [782, 812, 783, 813], [206, 236, 207, 237], [365, 395], [550], [702, 732, 703, 733], [821, 851], [219, 249], [435, 436], [596, 626, 597, 627], [748, 778], [864, 894, 865, 895], [294, 295], [453, 454], [608, 638, 609, 639], [759, 789], [148, 178, 149, 179], [308, 338], [272, 302], [461, 491], [646, 647], [767, 797, 768, 798], [125, 155, 126, 156], [315, 345, 316, 346], [503, 533], [687, 688], [807, 837, 808, 838], [199, 200], [388], [544], [697], [816, 846, 817, 847], [212, 242], [399, 429], [590], [743, 773], [860, 890, 861, 891], [253, 283, 254, 284], [476, 477], [602, 632, 603, 633], [754, 784], [870, 871], [301], [489], [644, 674], [794, 824, 795, 825], [154, 184, 155, 185], [344, 374], [308, 338], [496, 526, 497, 527], [681, 682], [803, 833], [162, 192], [351, 381], [538, 568], [691, 692], [812, 842], [235], [392, 393], [583, 584], [737, 738], [856, 886, 857, 887], [246, 276, 247, 277], [439, 469], [626], [779, 809], [896, 897], [293, 323, 294, 324], [482, 483], [638, 668], [789, 819, 790, 820], [6, 36, 7, 37], [337], [524, 525], [678, 708, 679, 709], [829, 859, 830, 860], [190, 220, 191, 221], [379, 409], [344, 374], [531, 561, 532, 562], [716], [837, 867], [197, 227, 198, 228], [386, 416], [546, 576, 547, 577], [731, 732], [852, 882], [240], [432], [619, 620], [773, 774], [22, 23], [286, 316], [475, 505, 476, 506], [632], [784, 814, 785, 815], [2, 32, 3, 33], [300, 330], [517, 518], [672, 702, 673, 703], [824, 854, 825, 855], [41, 71, 42, 72], [372, 373], [558, 559], [717, 747, 718, 748], [868, 898, 869, 899], [226, 256], [413, 443, 414, 444], [379, 409, 380, 410], [565, 595, 566, 596], [725, 726], [847, 877], [233, 263], [390, 420], [583, 613], [768], [18], [274], [468], [655, 656], [809], [28, 58], [322, 352], [481, 511], [667], [819, 849], [37, 67, 38, 68], [335, 365], [552, 553], [711, 741, 712, 742], [863, 893, 864, 894], [76, 106, 77, 107], [407], [598, 599], [724, 754], [874, 875], [260, 290, 261, 291], [423, 453, 424, 454], [413, 443, 414, 444], [576, 606], [762], [13], [267, 297, 268, 298], [431, 461], [619, 649], [803, 804], [23, 53, 24, 54], [314, 315], [504], [660, 661], [814], [33, 63, 34, 64], [358, 388], [516, 546], [701], [858, 888], [72, 102], [370, 400], [591, 592], [747, 777, 748, 778], [870], [115, 145, 116, 146], [446], [604, 605], [759, 789, 760, 790], [10, 40, 11, 41], [270, 300], [459, 489, 460, 490], [423, 453, 424, 454], [612, 642], [797, 798], [19, 49], [277, 307], [467, 497], [654, 684, 655, 685], [838, 839], [58, 88, 59, 89], [350, 351], [539], [695], [852, 853], [67, 97, 68, 98], [363, 393, 364, 394], [550, 580], [741, 742], [894, 895], [112, 142], [404, 434], [627, 628], [753, 783, 754, 784], [5, 35, 6, 36], [122, 152], [452, 453], [640, 641], [795, 825], [45, 75, 46, 76], [306, 336], [495, 525], [459, 489, 460, 490], [647, 677, 648, 678], [832, 833], [54, 84], [313, 343], [502, 532, 503, 533], [689, 719], [842, 843], [63, 93], [386], [543, 544], [735], [889], [107, 137, 108, 138], [397, 427, 398, 428], [590, 620, 591, 621], [777, 778], [0, 30, 1, 31], [148, 178], [445, 475], [633, 634], [789, 819], [40, 70, 41, 71], [157, 187, 158, 188], [488], [675, 676], [829, 859, 830, 860], [80, 110, 81, 111], [342, 372], [530, 560], [495, 525, 496, 526], [682, 712, 683, 713], [866, 867], [88, 118], [349, 379], [537, 567], [698, 728], [883], [103, 133, 104, 134], [391], [583, 584], [771], [25], [144, 174], [437, 467, 438, 468], [626, 656, 627, 657], [783], [35, 65, 36, 66], [153, 183, 154, 184], [451, 481], [669], [823, 853, 824, 854], [75, 105, 76, 106], [193, 223], [523, 524], [709, 710], [869, 899], [90, 120], [377, 407], [564, 594], [530, 560, 531, 561], [716, 746, 717, 747], [877], [98, 128, 99, 129], [384, 414], [546, 576], [734, 764, 735, 765], [19], [139, 169, 140, 170], [429, 430], [619, 620], [806, 807], [30], [179, 209], [473, 503, 474, 504], [632, 662], [818], [70, 100], [188, 218, 189, 219], [486, 516, 487, 517], [703, 704], [863, 893], [114, 144, 115, 145], [227, 257], [557, 558], [720], [5], [126, 156], [411, 441, 412, 442], [575, 605], [564, 594, 565, 595], [727, 757, 728, 758], [13], [134, 164, 135, 165], [418, 448, 419, 449], [582, 612, 583, 613], [770, 800], [54, 55], [175, 205], [466], [655, 656], [811, 812], [65], [184, 214, 185, 215], [509, 539], [667, 697], [856, 857], [109, 139, 110, 140], [223, 253], [521, 551], [743], [899], [121, 151], [267, 297], [597, 598], [756], [11, 41], [161, 191, 162, 192], [421, 451], [611, 641], [575, 605], [763, 793, 764, 794], [48, 49], [170, 200], [428, 458, 429, 459], [618, 648], [805, 835, 806, 836], [89], [180, 210], [502], [660, 661], [846], [104], [218, 248, 219, 249], [514, 544, 515, 545], [705, 735, 706, 736], [893], [145, 175, 146, 176], [263, 293, 264, 294], [560, 590], [779], [5, 35], [156, 186, 157, 187], [273, 303], [603, 604], [791, 792], [46, 76], [197, 227], [457, 487, 458, 488], [646, 676, 647, 677], [611, 641], [799, 829], [83, 84], [205, 235], [464, 494, 465, 495], [653, 683, 654, 684], [810, 840], [98, 99], [218, 248, 219, 249], [537, 538], [694, 695], [886, 887], [140, 141], [259, 289], [548, 578, 549, 579], [742, 772], [28, 29], [151, 181, 152, 182], [299, 329], [596, 626, 597, 627], [785], [40, 70], [192, 222], [309, 339], [639, 640], [826, 827], [80, 110, 81, 111], [231, 261], [493, 523], [681, 711], [646, 676, 647, 677], [833, 863, 834, 864], [117, 118], [213, 243, 214, 244], [500, 530], [688, 718], [849, 879, 850, 880], [134, 135], [254, 284, 255, 285], [542], [735], [22, 23], [176], [295, 325], [588, 618, 589, 619], [778, 808], [34], [186, 216, 187, 217], [305, 335], [602, 632], [820], [74, 104, 75, 105], [226, 256], [344, 374], [674, 675], [860, 861], [90, 120, 91, 121], [241, 271], [528, 558], [690, 720], [681, 711, 682, 712], [842, 872, 843, 873], [128, 129], [250, 280], [535, 565], [697, 727, 698, 728], [15, 16], [170, 171], [290, 320, 291, 321], [581], [771], [58], [181, 182], [300, 330, 301, 331], [625, 655], [783, 813, 784, 814], [68, 69], [221, 251], [339, 369, 340, 370], [637, 667, 638, 668], [854, 855], [114, 144, 115, 145], [266, 296], [378, 408], [708, 709], [871, 872], [126, 156, 127, 157], [277, 307], [562, 592, 563, 593], [726, 756, 727, 757], [715, 745, 716, 746], [879], [164, 165], [286, 316], [569, 599], [733, 763, 734, 764], [21, 51, 22, 52], [205, 206], [326, 356], [617, 618], [806, 807], [62, 63], [215, 216], [335, 365, 336, 366], [630, 660, 631, 661], [818, 848], [108], [261, 291], [378, 408, 379, 409], [672, 702], [894, 895], [120, 150, 121, 151], [272, 302, 273, 303], [418, 448, 419, 449], [749], [7, 8], [162, 192], [313, 343], [572, 602, 573, 603], [762, 792], [726, 756, 727, 757], [14, 44, 15, 45], [200], [321, 351], [580, 610], [769, 799, 770, 800], [56, 86, 57, 87], [210, 211], [330, 360, 331, 361], [653], [811, 812], [101, 102], [255, 256], [374, 404, 375, 405], [665, 695, 666, 696], [857, 887], [144], [297, 327], [414, 444, 415, 445], [711, 741, 712, 742], [0, 1], [156, 186], [308, 338], [424, 454, 425, 455], [755], [42, 43], [197, 227], [348, 378], [608, 638, 609, 639], [797, 827, 798, 828], [762, 792, 763, 793], [50, 80], [234, 235], [356, 386], [616, 646], [804, 834, 805, 835], [60, 90, 61, 91], [249, 250], [370, 400], [688, 689], [845, 846], [137, 138], [291, 292], [410, 440, 411, 441], [699, 729, 700, 730], [893, 894], [150], [302, 332, 303, 333], [420, 450, 421, 451], [747, 777, 748, 778], [36], [191, 221, 192, 222], [343, 373], [460, 490], [790, 791], [77, 78], [231, 261], [382, 412], [644, 674, 645, 675], [832, 862], [797, 827, 798, 828], [84, 114, 85, 115], [243, 244], [365, 395], [651, 681, 652, 682], [839, 869], [101, 131], [286], [406, 436], [693], [886], [173, 174], [327, 328], [446, 476, 447, 477], [740, 770], [29, 59], [185, 186], [337, 367, 338, 368], [456, 486], [753, 783, 754, 784], [71], [225, 255, 226, 256], [377, 407], [495, 525], [825, 826], [116, 117], [242, 272], [392, 422, 393, 423], [679, 709], [841, 871, 842, 872], [832, 862, 833, 863], [94, 124], [280], [401, 431, 402, 432], [686, 716], [849, 879], [137, 167], [321, 322], [442, 472], [732, 733], [22], [209], [332, 333], [451, 481, 452, 482], [776, 806], [34, 64, 35, 65], [219, 220], [372, 402], [490, 520, 491, 521], [788, 818, 789, 819], [105], [265, 295, 266, 296], [417, 447, 418, 448], [533, 563, 534, 564], [859, 860], [122, 123], [278, 308], [428, 458, 429, 459], [713, 743], [877, 878], [841, 871, 842, 872], [130, 160, 131, 161], [315, 316], [437, 467], [695, 725], [15], [172, 202, 173, 203], [357], [477, 507], [768, 769], [57, 58], [213, 214], [366, 367], [486, 516, 487, 517], [781, 811, 782, 812], [69, 99], [259, 260], [412, 442, 413, 443], [530, 560], [823, 853], [145, 146], [271, 301, 272, 302], [423, 453, 424, 454], [540, 570], [870, 871], [158, 159], [313, 343, 314, 344], [464, 494], [724, 754], [13, 43, 14, 44], [877, 878], [166, 196], [351], [472, 502, 473, 503], [731, 761], [20, 50, 21, 51], [207, 237, 208, 238], [361], [481, 511, 482, 512], [804, 805], [62, 63], [253], [407], [525, 555, 526, 556], [816, 846, 817, 847], [108, 138, 109, 139], [295, 296], [448, 478, 449, 479], [566, 596], [863, 893], [151, 152], [307, 337, 308, 338], [459, 489], [576, 606], [6, 7], [194], [348, 378], [499, 529], [760, 790], [48, 78, 49, 79], [13, 43, 14, 44], [201, 231], [385, 386], [506, 536, 507, 537], [767, 797], [55, 85, 56, 86], [211, 241, 212, 242], [401], [521, 551, 522, 552], [839], [101, 102], [289], [443], [562, 592], [855, 885, 856, 886], [144, 174, 145, 175], [301, 302], [454, 484], [572, 602], [29], [187, 188], [342, 372, 343, 373], [494, 524], [611, 641, 612, 642], [41, 42], [228, 229], [387, 417], [537, 567, 538, 568], [795, 825, 796, 826], [83, 113], [49, 79], [235, 265, 236, 266], [395], [516, 546, 517, 547], [802, 832, 803, 833], [60, 90], [252, 282, 253, 283], [437], [557, 587, 558, 588], [843, 844], [137, 138], [325], [478, 479], [597, 627, 598, 628], [891, 892], [150, 180, 151, 181], [336, 337], [488, 518, 489, 519], [607, 637], [4, 34, 5, 35], [222], [376, 406, 377, 407], [532, 562, 533, 563], [646, 676], [76, 77], [268], [393, 423], [544, 574], [830, 860], [93, 123], [83, 113, 84, 114], [245, 275, 246, 276], [431, 432], [552, 582, 553, 583], [837, 867], [100, 130, 101, 131], [288, 318, 289, 319], [473], [593, 623], [884], [173, 174], [330], [483, 484], [603, 633], [27, 57, 28, 58], [185, 215, 186, 216], [370, 371], [527, 557, 528, 558], [641, 671, 642, 672], [39, 69, 40, 70], [261], [417, 447], [569, 599], [685, 715], [115, 116], [274], [429, 459], [580, 610], [869, 899], [129, 159], [93, 123], [281, 311, 282, 312], [467], [588, 618, 589, 619], [846, 876, 847, 877], [136, 166, 137, 167], [323, 353, 324, 354], [508], [628, 658, 629, 659], [20], [208, 209], [364, 365], [517, 518], [637, 667], [32, 62, 33, 63], [219, 249, 220, 250], [411], [563, 593, 564, 594], [681, 711, 682, 712], [74, 104], [297], [423, 453], [575, 605], [691, 721, 692, 722], [121, 122], [309, 310], [464, 494, 465, 495], [615, 645], [875, 876], [164, 194, 165, 195], [129, 159], [317, 347], [502], [623, 653, 624, 654], [882, 883], [172, 202], [358, 388, 359, 389], [512], [632, 662, 633, 663], [55, 56], [213, 214], [404, 405], [558, 559], [677, 707], [67, 97, 68, 98], [260, 290], [447], [570, 600], [717, 747, 718, 748], [114, 144, 115, 145], [303], [458, 488, 459, 489], [610, 640, 611, 641], [727, 757], [157, 158], [345], [499, 529], [650, 680], [11, 41, 12, 42], [199, 229, 200, 230]]



print("Mariage :")

print(Mariage(Lv2))

#s=str(Mariage(L900))

#fichier=open("L900.txt","w")
#fichier.write(s)
#fichier.close()


