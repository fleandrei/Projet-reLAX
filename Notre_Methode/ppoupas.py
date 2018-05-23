#!/usr/bin/python
#-*- coding: utf-8 -*-

from test import *

def ppoupas(Vf) :  
	"""Renvoie True s'il existe un pp, ie un sous ensemble contenant autant de filles que de garçons, et false sinon"""



	S=[]
	i=0
	if test(Vf)==0:   #Il y a autant de de filles que de garçons => pp
		return(True)   
	
	else :    #On parcours tous les sous ensembles pour chercher les pp
		pp=False

		while i!=len(Vf) and pp==False : 
			S=Vf[:] 
			S.pop(i)	

			if test(S) == 0 and len(S)!=0 :
				pp=True
			elif test(S)!=0 : 
				pp=ppoupas(S)
			i=i+1
			
	return(pp)	

#print(ppoupas([[1],[4]]))		 
