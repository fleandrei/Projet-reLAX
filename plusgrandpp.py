
#-*- coding: utf-8 -*-

from test import *



def extractionpp(Vf):
	"""Procédure permettant d'extraire les ensembles pp"""


	Ss=[]  #Liste des sous ensemble
	global pp

	if test(Vf)==0:
		pp.append(Vf)
			

	for i in range(0,len(Vf)) :
		Ss=Vf[:]
		Ss.pop(i)		

		extractionpp(Ss)

def touslespp(Vf):
	"""Renvoie la liste de tous les sous ensembles contenant autant de filles que de garçons, ie les pp"""

	global pp
	pp=[]

	

	extractionpp(Vf)

	return(pp)
	
	
#print(touslespp([[1,2,4],[2],[3]]))

