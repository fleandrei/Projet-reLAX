#-*- coding: utf-8 -*-


def test(L):
	""" Renvoie 0 s'il y a autant de filles que de garçons, ie pp, 1 si s'il y a plus de filles que de garçons, ie p,p+1, et -1 s'il y a moins de garçons que de filles, ie la condition du lemme des mariages n'est pas respectée"""
	T=[]
	for i in range (len(L)):
		for j in range (len(L[i])):
			if L[i][j] not in T:
				T.append(L[i][j])
	if len(T)<len(L):
		return(-1)
	elif len(T)==len(L):
		return(0)
	else:					#len(T)>len(L)
		#print(T)
		return(1)









#L=[[3,4]]
#print("Résultat de test :")
#print(test(L))
