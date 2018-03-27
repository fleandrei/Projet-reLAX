#!/usr/bin/python
# -*- coding: utf-8 -*-


#L=[[1,2,3,4,5],[4,5,3],[2,3],[1,5],[1,3,5]]
#L=[[1,4],[1,3],[2,3],[4,2]]


def mariagepp(Liste_total_voeux) :  #Liste_total_voeux est une liste de liste des voeux par filles. Le premier élément correspond aux voeux de la première fille


	if len(Liste_total_voeux)==0 :


		return(Liste_total_voeux)

	else :

		Liste_garcons=liste_des_garcons(Liste_total_voeux)   #On extrait chaque garçon que l'on réunie dans une liste

		Liste_occurences=[]  #On crée une listes des occurences, où le premier élément est l'occurence du premier voeux de Liste_voeux

	
		for i in range(0,len(Liste_garcons)) :
			occurence=nb_occurence(Liste_total_voeux,Liste_garcons[i])
			Liste_occurences.append(occurence)

		#On sélectionne maintenant les éléments avec la plus petite occurence
		
		min_occurences=min_liste(Liste_occurences)

		#On sélectionne le garçon contenue dans la plus petite liste des voeux d'une fille


		futur_mari=Liste_garcons[min_occurences[0]]

		voeux_future_mariee=plus_petite_liste_voeux(Liste_total_voeux,Liste_garcons[min_occurences[0]])  
                
 		


		for i in range(1,len(min_occurences)) :
			if len(plus_petite_liste_voeux(Liste_total_voeux,Liste_garcons[min_occurences[i]]))<len(voeux_future_mariee) :

				
		#On décide arbitrairement de choisir le premier garçon appartenant à la liste de voeux la plus petite, plutôt que de tirer au sort parmi tous les garçons appartenant à des petites listes de voeux de même taille
				voeux_future_mariee=plus_petite_liste_voeux(Liste_total_voeux,Liste_garcons[min_occurences[i]])

				futur_mari=Liste_garcons[min_occurences[i]]

		


		#On retire la liste de voeux de la mariée
		position=voeux_future_mariee.pop()
	
		Liste_total_voeux.pop(position)

		#On retire de la liste des voeux de chaque fille le garcon nouvellement marié
 		

		for i in range(0,len(Liste_total_voeux)) :

		

			Liste_total_voeux[i]=supp_elts_liste(Liste_total_voeux[i],futur_mari)




		#On mari la fille et on réapplique le même processus sur les filles restantes



		return(ajout_elts(mariagepp(Liste_total_voeux),futur_mari,position))





def liste_des_garcons(Liste_total_voeux):


	Liste_garcons=[]   #C'est de l'ensemble des garçons retenue par des filles

	for i in range(0,len(Liste_total_voeux)) :
		for j in range(0,len(Liste_total_voeux[i])) :
			if appartenance(Liste_garcons,Liste_total_voeux[i][j])==False :
				Liste_garcons.append(Liste_total_voeux[i][j])



	return(Liste_garcons) 





def nb_occurence(Liste_total_voeux,voeux) : #Renvoie le nombre de fois que le voeux apparaît dans la liste des voeux d'une fille


	occurence=0   #Nombre d'occurence

	for i in range(0,len(Liste_total_voeux)):
		for j in range(0,len(Liste_total_voeux[i])) :
			if Liste_total_voeux[i][j]==voeux :
				occurence+=1



	return(occurence)





def appartenance(Liste,elts) : #Vérifie si un élément appartient à la liste

	appartient=False    #Booléen qui devient vraie si un élément appartient à la liste

	for i in range(0,len(Liste)) :
		if Liste[i]==elts :
			appartient=True


	return(appartient)




def min_liste(L):   #Renvoie la liste des indices des éléments minimums de la liste L

	min=L[0]
	indice=[]


	if len(L)>0 :

		#On recherche le minimum

		for i in range(1,len(L)):
			if L[i]<min :
				min=L[i]
				
 		#On sauvegarde les indices où le minimum est présent

 		for i in range(0,len(L)):
 			if L[i]==min :
 				indice.append(i)


	return(indice)



def plus_petite_liste_voeux(Liste_total_voeux,voeux) :  #Recherche la plus petite sous liste de Liste_total_voeux dans laquelle apparaît un voeux.
       													#Le dernier élément de la liste renvoyé est la position de la liste de voeux de la fille dans Liste_total_voeux
	k=0
	trouve=False

	

	while trouve==False : #Tant qu'on a pas trouvé la première liste contenant le voeux


		if appartenance(Liste_total_voeux[k],voeux)==True :
	
			plus_petite_sousliste=Liste_total_voeux[k][:]
			position=k
			trouve=True

		k+=1


	for i in range(k,len(Liste_total_voeux)) :
		if appartenance(Liste_total_voeux[i],voeux)==True and len(Liste_total_voeux[i])<len(plus_petite_sousliste):  #Si 2 sous-listes sont de même taille
			plus_petite_sousliste=Liste_total_voeux[i][:]                 		#On décide arbitrairement de choisir la première, cela évite de faire de l'aléatoire inutilement
			position=i

	plus_petite_sousliste.append(position)


	return(plus_petite_sousliste)


def supp_elts_liste(L,elts) :  #Supprime un élément de la liste L

	i=0

	while i<len(L): 

		if L[i]==elts :
			L.pop(i)
			#i+=1
		i+=1



	return(L)



def ajout_elts(L,elts,position) : #On ajoute un élément à la position souhaitée

	#On sauvegarde dans une liste les éléments de la position (inclus) jusqu'à la fin de la liste

	M=[]

	for i in range(position,len(L)) :
		M.append(L[i])


	#On efface les éléments le liste jusqu'à la position (exclus)

	L=L[:position]

 	#On ajoute l'éléments et on reconstitue la liste

	L.append(elts)
	L=L+M



	return(L)



#print("Voeux des filles à marier :" )
#print(L)

#print("Résultat du mariage : ")

#print(mariagepp(L))
#print(mariagepp(M))



