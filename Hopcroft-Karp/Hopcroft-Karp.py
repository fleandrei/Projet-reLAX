#!/usr/bin/python
# -*- coding: utf-8 -*-

def Mariage(Liste_total_voeux) : #Fonction principale

#"""Prend en entrée une liste [[garçon1,garçon2,...],[garçon3,garçon4,...],...] où chaque sous liste correspond à la liste de voeux d'une fille
#Renvoie une liste sous la forme [garçon1,garçon3,...] où chaque garçon a été marié à la fille d'indice correspondant"""


	#if verif(Liste_total_voeux)<0 :

		#print("La condition du lemme des mariages n'est pas vérifiée, on ne peut pas réaliser le mariage")

		#return(-1)

	#else :

		print("Liste de voeux total :")
		print(Liste_total_voeux)
		print("\n")


		#On réalise un premier mariage arbitraire
		M=Phase_1(Liste_total_voeux)  
		#M=[[1], [46], [2], [], [3], [54], [99], [], [97]]


		print("Mariage arbitraire  :")
		print(M)
		print("\n") 	

		#On crée une liste des garçons
		Garcons=recherche_garcons(Liste_total_voeux)


		#On crée des listes recensants les sommets libres de notre graphe
		Liste_sommets_libres_filles=recherche_sommets_libres_filles(M)
		Liste_sommets_libres_garcons=recherche_sommets_libres_garcons(M,Garcons)


		#Tant qu'il reste des filles qui n'ont pas été mariés, ie des sommets libres de filles
		while len(Liste_sommets_libres_filles)>0 :

			#On cherche un chemin reliant deux somets libres
			chemin=chemin_sommets_libres(Liste_sommets_libres_garcons[0],Liste_sommets_libres_filles,Liste_total_voeux,M)
			#Puis on réalise la différence symétrique entre ce chemin et notre couplage afin d'obtenir un nouveau couplage
			M=difference_symetrique(chemin,M)
			print("Chemin :")
			print(chemin)
			print("\n")
			print("\n")
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


def repetition_garcon(chemin) :

	#Vérifie s'il y a des répétitions de garçons dans le chemin d'augmentation 

	repetition=False

	i=0

	while i<(len(chemin)-1) and repetition==False:

		if chemin[-1][0]==chemin[i][0] :
			repetition=True
		i+=1	

	return(repetition)

def repetition_fille(chemin)	: 

	#Vérifie s'il y a des répétitions de filles dans le chemin d'augmentation

	repetition=False

	i=0
	while i<(len(chemin)-1) and repetition==False:


		if chemin[-1][1]==chemin[i][1] :
			repetition=True
		i+=1	

	return(repetition)


def chemin_sommets_libres(Sommet_libre_garcon,Liste_sommets_libres_filles,Liste_total_voeux,Mariage_arbitraire) : 

	#Renvoie le chemin d'augmentation le plus court

	chemin=[]
	MaJ_Liste_voeux=MaJ_Graphe(Liste_total_voeux,Mariage_arbitraire)
	Liste_garcons_desirees=Liste_filles_to_garcons(MaJ_Liste_voeux,recherche_garcons(MaJ_Liste_voeux))

	for L in Liste_garcons_desirees :
		print(L)
		print("\n")
		print(Sommet_libre_garcon)
		print("\n")
		if L[0]==Sommet_libre_garcon :
			for fille in L[1] :
				chemin_provisoire=chemin_sommets_libres_filles([[L[0],fille]],Liste_sommets_libres_filles,Mariage_arbitraire,Liste_garcons_desirees)
				#chemin_provisoire.pop()
				print(chemin_provisoire)
				print("\n")
				if len(chemin_provisoire)<len(chemin) or len(chemin)==0 :
					chemin[:]=chemin_provisoire

	return(chemin)

def chemin_sommets_libres_garcons(chemin,Liste_sommets_libres_filles,Liste_garcons_desirees,Mariage_arbitraire) :

	chemin_plus_court=[]

	chemin_copie=[]
	chemin_copie[:]=chemin


	if repetition_garcon(chemin)==False :

		for L in Liste_garcons_desirees :
			print(L)
			if L[0]==chemin[-1][0] :
				for fille in L[1] :	
					chemin_copie.append([L[0],fille])

					chemin_provisoire=chemin_sommets_libres_filles(chemin_copie,Liste_sommets_libres_filles,Mariage_arbitraire,Liste_garcons_desirees)
					chemin_copie.pop()
					if (len(chemin_provisoire)<len(chemin_plus_court) and len(chemin_provisoire)!=0) or len(chemin_plus_court)==0:
						#if len(chemin_plus_court)!=0 and chemin_plus_court[-1]=="S" :
						 #	print("On return un bon chemin")
						chemin_plus_court[:]=chemin_provisoire


		return(chemin_plus_court)

	else : 

		return([])	

def chemin_sommets_libres_filles(chemin,Liste_sommets_libres_filles,Mariage_arbitraire,Liste_garcons_desirees) :

	chemin_copie=[]
	chemin_copie[:]=chemin

	#print("\n")
	#print(chemin)
	#print("\n")

	if repetition_fille(chemin)==False :   #Si on est pas déjà passé par ce noeud


		if chemin[-1][1] in Liste_sommets_libres_filles : 
			#print("On a trouvé un sommet libre")
			#chemin_copie.append("S")
			#if chemin_copie[-1]=="S" :
			#			 	print("On return un bon chemin")
			return(chemin_copie)

		else :
	
			chemin_plus_court=[]	

			for i in range(0,len(Mariage_arbitraire)) :


				if i==chemin[-1][1]:

					chemin_copie.append([Mariage_arbitraire[i][0],i])

					chemin_provisoire=chemin_sommets_libres_garcons(chemin_copie,Liste_sommets_libres_filles,Liste_garcons_desirees,Mariage_arbitraire)
					chemin_copie.pop()

					if (len(chemin_provisoire)<len(chemin_plus_court) and len(chemin_provisoire)!=0) or len(chemin_plus_court)==0 :
					#	if len(chemin_plus_court)!=0 and chemin_plus_court[-1]=="S" :
					#	 	print("On return un bon chemin")
						chemin_plus_court[:]=chemin_provisoire

			return(chemin_plus_court)

	else :  #Si on est déjà repassé par ce noeud

		return([])  #On renvoie une liste vide

def chemin_en_liste_voeux(chemin,Mariage_arbitraire) : 


	chemin_converti=[[]]*len(Mariage_arbitraire)

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
L100=[[2, 4, 23, 25, 26, 45, 47, 48], [57, 68, 62, 77, 79, 82, 4, 6, 18], [27, 29, 32, 49, 42, 54, 60, 64, 66], [70, 83, 85, 8, 10, 13, 21, 34, 36], [44, 56, 58, 65, 67, 79, 85, 87, 89], [12, 15, 28, 36, 38, 40, 59, 50, 52], [69, 71, 73, 88, 80, 82, 18, 20, 22], [31, 43, 44, 52, 64, 67, 73, 74, 77], [9, 1, 3, 22, 24, 36, 45, 46, 49], [66, 69, 61, 76, 77, 81, 4, 15, 17], [17, 10, 38, 31, 33, 52, 54, 56], [64, 76, 77, 84, 86, 97, 19, 13, 25], [34, 36, 47, 56, 58, 69, 77, 79, 70], [87, 99, 90, 15, 27, 29, 38, 40, 41], [50, 61, 65, 71, 72, 86, 90, 92, 95], [29, 21, 33, 42, 43, 57, 63, 67, 69], [76, 88, 80, 93, 96, 98, 23, 36, 38], [47, 59, 51, 69, 71, 73, 89, 81, 83], [15, 18, 10, 39, 31, 43, 51, 53, 55], [73, 75, 76, 83, 85, 96, 10, 22, 24], [24, 26, 45, 47, 48, 67, 60, 62], [79, 82, 84, 99, 92, 4, 26, 28, 39], [49, 42, 54, 63, 65, 77, 84, 86, 88], [94, 6, 8, 20, 33, 35, 45, 57, 58], [67, 79, 70, 88, 80, 91, 7, 9, 1], [36, 38, 40, 59, 51, 62, 71, 72, 75], [81, 93, 96, 0, 2, 4, 30, 42, 44], [53, 64, 68, 74, 87, 89, 95, 98, 90], [22, 23, 25, 44, 46, 59, 66, 60, 62], [89, 81, 83, 99, 91, 3, 26, 37, 31], [30, 32, 52, 54, 56, 74, 76, 78], [86, 98, 99, 6, 8, 19, 33, 35, 47], [56, 58, 69, 78, 70, 83, 99, 92, 94], [9, 11, 14, 37, 49, 41, 50, 61, 65], [72, 85, 87, 94, 96, 8, 12, 16, 18], [41, 43, 56, 65, 67, 79, 87, 89, 81], [98, 0, 2, 17, 19, 11, 47, 59, 51], [60, 72, 73, 81, 93, 95, 2, 3, 5], [38, 30, 32, 51, 53, 65, 74, 75, 78], [95, 96, 90, 5, 7, 10, 33, 44, 46], [46, 48, 67, 60, 62, 81, 83, 85], [93, 5, 6, 13, 15, 26, 48, 41, 53], [63, 65, 77, 85, 87, 99, 6, 8, 0], [16, 28, 20, 44, 56, 58, 67, 79, 70], [89, 91, 94, 0, 2, 15, 29, 21, 22], [58, 50, 62, 71, 73, 86, 93, 96, 98], [3, 16, 19, 22, 24, 27, 53, 64, 67], [75, 88, 80, 98, 0, 2, 18, 10, 12], [44, 45, 48, 66, 60, 72, 80, 82, 84], [2, 4, 5, 12, 14, 25, 47, 51, 53], [53, 55, 74, 76, 77, 97, 98, 91], [8, 11, 13, 28, 21, 33, 55, 57, 69], [78, 70, 83, 90, 94, 6, 13, 15, 17], [23, 35, 37, 50, 61, 64, 73, 85, 87], [96, 8, 0, 17, 19, 20, 36, 38, 30], [65, 67, 79, 88, 80, 91, 0, 2, 3], [10, 22, 24, 39, 31, 33, 69, 71, 73], [82, 94, 95, 3, 15, 18, 24, 25, 29], [51, 52, 54, 74, 75, 88, 96, 99, 91], [17, 10, 12, 27, 20, 32, 55, 66, 69], [68, 61, 81, 83, 85, 3, 5, 7], [15, 27, 28, 35, 37, 48, 62, 64, 76], [85, 87, 99, 7, 9, 12, 29, 20, 23], [38, 40, 43, 66, 78, 70, 89, 91, 94], [1, 14, 16, 22, 25, 37, 41, 44, 46], [71, 72, 85, 93, 96, 8, 16, 18, 10], [27, 39, 31, 44, 48, 40, 74, 88, 80], [99, 1, 2, 10, 22, 24, 31, 32, 34], [66, 69, 61, 80, 82, 94, 3, 5, 6], [24, 26, 29, 34, 36, 47, 61, 73, 75], [75, 77, 96, 98, 91, 18, 12, 14], [21, 33, 35, 42, 44, 56, 78, 79, 82], [90, 94, 6, 14, 16, 28, 35, 37, 39], [45, 57, 59, 71, 85, 87, 96, 8, 0], [18, 20, 21, 39, 31, 42, 58, 50, 52], [87, 89, 91, 0, 2, 13, 22, 23, 27], [32, 44, 47, 52, 53, 56, 82, 93, 95], [4, 17, 19, 25, 39, 31, 45, 49, 41], [73, 74, 76, 95, 99, 1, 19, 11, 13], [31, 33, 35, 41, 43, 54, 77, 80, 82], [82, 84, 3, 5, 7, 26, 27, 20], [37, 49, 42, 57, 59, 62, 84, 86, 98], [7, 9, 12, 29, 22, 34, 40, 44, 46], [50, 63, 66, 89, 90, 93, 1, 14, 16], [25, 37, 39, 46, 48, 59, 65, 67, 69], [92, 96, 8, 17, 19, 21, 39, 31, 32], [49, 51, 53, 68, 60, 62, 98, 0, 2], [11, 23, 24, 33, 44, 47, 53, 54, 57], [89, 81, 83, 3, 4, 16, 25, 26, 20], [46, 49, 41, 56, 59, 61, 84, 96, 97], [97, 90, 18, 12, 14, 32, 34, 36], [44, 56, 57, 64, 66, 78, 99, 93, 5], [14, 16, 28, 36, 38, 40, 58, 59, 52], [67, 79, 71, 95, 7, 9, 18, 20, 21], [30, 42, 45, 51, 54, 66, 71, 72, 75], [0, 1, 13, 22, 25, 37, 44, 47, 49], [56, 68, 60, 73, 77, 79, 4, 17, 19], [27, 39, 31, 49, 51, 53, 60, 61, 63], [95, 98, 90, 19, 11, 23, 32, 34, 35], [53, 55, 56, 63, 65, 76, 90, 2, 4]]
L25=[[2, 3, 12, 14, 18, 21, 23], [8, 6, 15, 18, 19, 4, 1], [12, 14, 15, 22, 24, 21, 8, 10, 11], [19, 16, 24, 4, 6, 8, 11, 18, 15], [4, 1, 12, 14, 11, 18, 20, 22], [8, 5, 18, 16, 24, 2, 4], [14, 12, 22, 24, 21, 5, 7], [18, 15, 22, 3, 0, 14, 16], [20, 23, 0, 5, 12, 14, 17, 24, 21], [6, 7, 5, 18, 16, 17, 24, 1, 3], [14, 11, 20, 22, 24, 1, 8, 5], [16, 18, 15, 3, 0, 2, 12, 14], [24, 22, 4, 9, 6, 15, 23, 20], [1, 4, 6, 11, 18, 15, 24, 2], [12, 14, 11, 20, 22, 24, 1, 7, 5], [15, 17, 1, 3, 7, 14, 12], [22, 24, 9, 6, 8, 18, 15], [0, 3, 5, 10, 13, 21, 4, 1], [8, 5, 12, 17, 20, 21, 0, 7, 9], [18, 15, 17, 1, 3, 0, 7, 13, 11], [22, 23, 8, 5, 7, 13, 16, 18], [3, 1, 10, 13, 14, 24, 21], [7, 9, 11, 17, 19, 16, 3, 5], [14, 11, 19, 24, 1, 3, 6, 13, 10], [24, 21, 7, 5, 13, 15, 17]]
L64=[[2, 3, 21, 22, 17, 25, 35, 37], [44, 46, 55, 3, 5, 15, 23, 19, 29], [37, 38, 32, 47, 48, 51, 7, 8, 11], [20, 30, 24, 32, 33, 44, 49, 52, 54], [10, 13, 15, 31, 25, 27, 34, 45, 47], [53, 55, 57, 14, 8, 18, 27, 28, 39], [46, 40, 42, 55, 49, 59, 10, 20, 21], [31, 33, 35, 41, 43, 53, 0, 2, 4], [8, 10, 27, 29, 30, 42, 44], [50, 52, 62, 9, 12, 21, 30, 24, 35], [43, 45, 47, 53, 63, 56, 13, 23, 16], [25, 36, 38, 46, 40, 49, 56, 57, 60], [16, 18, 21, 38, 32, 33, 41, 51, 54], [58, 61, 7, 19, 23, 25, 33, 35, 46], [52, 55, 49, 60, 56, 2, 16, 26, 28], [36, 47, 41, 48, 50, 60, 14, 9, 11], [21, 16, 33, 35, 37, 55, 50], [57, 59, 5, 23, 18, 28, 37, 39, 41], [48, 51, 53, 60, 6, 7, 19, 29, 31], [32, 43, 45, 53, 54, 56, 6, 0, 2], [31, 25, 26, 44, 46, 40, 48, 57, 59], [1, 3, 13, 26, 29, 39, 40, 41, 51], [59, 60, 63, 3, 6, 8, 30, 33, 34], [43, 52, 55, 61, 56, 2, 20, 22, 17], [28, 30, 46, 42, 44, 62, 56], [6, 1, 11, 30, 31, 34, 43, 45, 55], [63, 58, 60, 2, 12, 14, 25, 36, 38], [47, 48, 51, 58, 61, 7, 13, 15, 8], [37, 39, 33, 50, 53, 55, 62, 0, 2], [15, 9, 19, 33, 35, 45, 54, 48, 58], [1, 3, 4, 10, 12, 22, 36, 47, 41], [49, 59, 61, 4, 5, 8, 27, 29, 31], [35, 36, 53, 48, 50, 4, 6], [13, 14, 17, 36, 38, 47, 50, 52, 62], [6, 7, 2, 8, 18, 20, 32, 41, 44], [53, 63, 57, 0, 3, 13, 18, 21, 23], [44, 46, 40, 56, 58, 61, 4, 14, 8], [22, 16, 26, 47, 41, 51, 59, 62, 0], [15, 9, 11, 16, 18, 28, 43, 52, 55], [56, 2, 3, 10, 12, 22, 33, 35, 37], [41, 43, 60, 62, 56, 11, 13], [19, 21, 31, 43, 45, 54, 63, 58, 4], [12, 14, 15, 22, 24, 27, 46, 48, 51], [59, 5, 7, 15, 9, 20, 25, 27, 29], [49, 52, 54, 7, 1, 2, 10, 21, 23], [27, 30, 32, 54, 48, 58, 2, 4, 15], [22, 16, 18, 31, 25, 35, 49, 59, 61], [5, 8, 10, 17, 19, 28, 40, 42, 44], [54, 49, 2, 4, 6, 17, 19], [26, 28, 38, 49, 51, 61, 6, 7, 10], [18, 20, 22, 29, 38, 32, 53, 62, 56], [1, 12, 14, 22, 23, 25, 39, 33, 36], [56, 58, 60, 13, 15, 9, 17, 26, 29], [34, 35, 47, 59, 62, 0, 9, 10, 20], [27, 30, 24, 36, 39, 41, 56, 2, 3], [12, 21, 16, 31, 25, 35, 53, 48, 50], [61, 56, 9, 11, 13, 30, 25], [39, 34, 44, 63, 57, 3, 12, 14, 16], [24, 27, 29, 35, 45, 47, 59, 5, 7], [8, 17, 20, 28, 30, 32, 46, 40, 41], [7, 0, 2, 18, 22, 16, 31, 33, 34], [40, 42, 53, 2, 3, 14, 23, 17, 27], [34, 36, 39, 43, 44, 48, 5, 8, 10], [18, 28, 31, 37, 32, 42, 60, 61, 56]]
L49=[[2, 3, 19, 15, 17, 25, 33, 29], [41, 37, 46, 9, 11, 20, 21, 24, 26], [33, 41, 37, 6, 0, 10, 19, 21, 23], [31, 33, 35, 40, 42, 43, 15, 18, 20], [21, 30, 32, 37, 40, 42, 12, 7, 9], [24, 27, 22, 29, 38, 40, 2, 3, 13], [15, 17, 25, 33, 29, 38, 36, 45, 46], [8, 10, 26, 21, 23, 31, 40, 35], [48, 43, 3, 16, 18, 26, 28, 30, 32], [39, 48, 42, 12, 7, 16, 25, 34, 29], [36, 39, 48, 46, 6, 1, 22, 24, 26], [34, 36, 37, 44, 46, 6, 19, 14, 16], [31, 33, 28, 35, 44, 46, 8, 10, 19], [21, 23, 32, 39, 35, 44, 42, 2, 4], [14, 16, 32, 34, 30, 37, 46, 48], [5, 1, 10, 22, 24, 33, 41, 37, 39], [45, 5, 0, 18, 20, 22, 32, 41, 35], [43, 45, 5, 3, 12, 7, 28, 30, 33], [41, 42, 44, 1, 3, 13, 24, 27, 22], [37, 40, 35, 42, 1, 3, 14, 16, 25], [28, 30, 38, 46, 48, 1, 6, 8, 10], [26, 23, 38, 40, 36, 44, 4, 5], [11, 13, 16, 34, 30, 39, 48, 42, 45], [3, 12, 13, 25, 27, 28, 38, 47, 42], [0, 3, 12, 9, 19, 20, 35, 36, 39], [47, 0, 1, 8, 9, 19, 31, 33, 28], [44, 45, 48, 6, 8, 10, 21, 23, 31], [41, 36, 45, 3, 5, 8, 12, 15, 17], [33, 29, 45, 47, 42, 1, 10, 12], [18, 20, 22, 41, 37, 46, 5, 0, 2], [9, 18, 20, 31, 33, 35, 44, 4, 6], [13, 8, 18, 15, 25, 27, 48, 43, 44], [4, 13, 8, 14, 16, 25, 37, 40, 35], [1, 3, 5, 12, 14, 16, 34, 29, 38], [46, 42, 2, 10, 11, 14, 18, 21, 23], [39, 35, 2, 4, 5, 7, 16, 18], [24, 26, 34, 47, 43, 3, 11, 13, 9], [14, 24, 26, 37, 39, 48, 1, 11, 12], [20, 15, 24, 22, 31, 33, 5, 0, 2], [9, 19, 14, 27, 22, 31, 43, 45, 48], [7, 9, 12, 17, 27, 22, 40, 35, 44], [4, 0, 9, 16, 18, 27, 25, 34, 29], [46, 47, 8, 10, 12, 20, 23, 25], [31, 32, 41, 5, 6, 9, 18, 20, 14], [21, 31, 33, 43, 46, 6, 7, 17, 19], [26, 21, 29, 28, 37, 40, 11, 13, 8], [16, 26, 21, 34, 29, 37, 1, 2, 5], [14, 16, 17, 24, 34, 29, 46, 42, 2], [10, 13, 15, 22, 24, 33, 31, 40, 36]]
L36=[[2, 3, 13, 15, 16, 18, 26, 28], [2, 4, 0, 15, 17, 14, 27, 29, 24], [5, 0, 9, 12, 14, 22, 29, 25, 27], [1, 10, 6, 14, 23, 19, 25, 27, 35], [11, 7, 8, 23, 19, 21, 27, 29, 31], [7, 9, 17, 20, 21, 18, 29, 32, 33], [8, 10, 19, 21, 23, 25, 33, 34], [9, 10, 7, 22, 23, 20, 33, 35, 31], [11, 7, 15, 18, 20, 28, 35, 31, 33], [7, 16, 12, 21, 29, 25, 31, 34, 0], [17, 13, 14, 29, 25, 27, 33, 30, 2], [13, 15, 18, 26, 27, 24, 30, 2, 3], [14, 16, 25, 27, 29, 31, 3, 5], [15, 17, 13, 28, 29, 26, 3, 5, 1], [17, 14, 22, 24, 27, 35, 5, 1, 4], [13, 22, 18, 27, 35, 31, 1, 4, 6], [23, 19, 20, 30, 32, 34, 3, 0, 8], [20, 21, 24, 32, 34, 30, 0, 8, 10], [20, 22, 32, 33, 35, 1, 9, 11], [21, 23, 19, 34, 30, 32, 10, 11, 8], [18, 20, 28, 30, 33, 5, 6, 7, 10], [21, 29, 24, 33, 5, 1, 8, 10, 12], [29, 25, 28, 0, 2, 4, 10, 6, 14], [26, 27, 30, 2, 4, 1, 6, 14, 16], [27, 28, 2, 4, 0, 8, 15, 17], [27, 29, 26, 4, 0, 3, 16, 17, 14], [24, 26, 34, 0, 3, 11, 12, 14, 16], [27, 35, 31, 4, 6, 7, 14, 16, 18], [30, 31, 34, 6, 8, 10, 17, 13, 20], [32, 35, 1, 9, 11, 7, 13, 21, 22], [33, 34, 8, 10, 6, 14, 22, 23], [34, 35, 32, 11, 7, 9, 22, 18, 20], [30, 33, 5, 7, 9, 17, 18, 21, 23], [33, 5, 1, 10, 12, 14, 20, 23, 25], [0, 2, 4, 12, 14, 17, 23, 19, 26], [2, 5, 7, 15, 17, 13, 19, 27, 28]]
L16=[[2, 0, 5, 7,1, 9, 10, 15, 13, 14], [11, 9, 13, 15,10, 12, 2, 6, 7, 4, 8, 14], [1, 3, 4, 6, 11, 8, 9, 14, 12, 13, 15, 5], [8, 14, 12, 1, 3, 0, 6,11, 7, 9, 10, 15], [7, 5, 6, 11, 9, 15, 12, 2, 3, 1, 10], [12, 14, 15, 13, 3, 1, 4, 8, 10, 11, 0], [7, 5, 10, 8, 13, 14, 12, 0, 1, 3, 9], [13, 15, 0, 2, 4, 5, 7, 8, 9, 14, 12, 1], [10, 11, 9, 14, 15, 1, 2, 7, 5, 12], [3, 0, 2, 6, 7, 5, 11, 14, 12, 13, 4], [10, 11, 12, 14, 3, 0, 2, 7, 4, 5, 15, 13], [3, 1, 7, 4, 10, 8, 9, 14, 12, 2, 0, 5, 6], [12, 13, 15, 0, 2, 7, 5, 10, 11, 9, 3], [5, 6, 4, 8, 10, 11, 13, 0, 2, 7], [12, 13, 3, 0, 5, 7, 4, 6, 9, 11, 8, 1], [5, 7, 9, 10, 12, 14, 15, 1, 2, 6, 11]]


Lmain12=[[3,4,2,1,5],[1,2,12],[8,9,10,3],[12,5,4,11],[7,8,9,5],[1,2,10,11,6],[1,2,12,11,7,8,9],[8,10,4,3,1],[6,3,9,1,5],[6,7,10,11],[6,7,10,11],[1,12,3,9]]
Lmain13=[[3,4,2,1,5],[1,2,12],[8,13,9,10,3],[12,5,4,11],[7,8,9,13,5],[1,2,10,11,6],[1,2,12,11,7,8,9],[13,8,10,4,3,1],[6,3,9,13,1,5],[6,7,10,11],[6,7,10,11],[1,12,3,9],[4,8,11,13]]

print(Mariage(Lmain13))








