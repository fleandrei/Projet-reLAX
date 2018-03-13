#!/usr/bin/python
#-*- coding:Utf-8 -*
def grand(K):
        a=K[0]
        for i in range(0,len(K)):
                if (len(K[i])>len(a)):
                        a=K[i]
                        
                        
                        
        return(a)
        
        
K=[[1,2,3],[2],[],[1,2],[],[1,2,3,4,5,6]]

#print(grand(K))
