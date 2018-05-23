# -*-coding:Utf-8 -*
import math



def Lax():
    a = 1  # les deux constantes utile pour la formule utilisé
    b = 1  #

    N = 4 # nombre de division de la grille. Avec N=100, cela fait 10 000cases
    N1 = 4 # nombre de sous-division de chaque case


    I2 = []  # liste contenant les images de chaque centre
    #I1 = []  # liste intermédiaire
    Z=[]
    C = []



    ### liste qui contiendra les coordonnees des sous-centres de chaque case ###
    for i in range(0,N*N):
        for j in range(0,N1*N1):
            Z.append(j)
        C.append(Z)
        #I1.append(Z)
        I2.append(Z)
        Z=[]






### remplissage de C, contenant l'ensemble des centre des cases ###

    for x in range(0, N):
        for y in range(0, N):
            i=0
            for x1 in range(0, N1):
                 for y1 in range(0, N1):
                    C[y*N+x][i]=[float(((x*N1)+x1))/(N*N1),float(((y*N1)+y1))/(N*N1)]
                    i=i+1



    ### remplissage de I, image de chaque sous-centre, modulo 1 ###
    #print(I2)
    for i in range(0, len(C)):
        for j in range(0,len(C[i])):
            x=C[i][j][0]
            y=C[i][j][1]
            I2[i][j]=[(x%1 +a*math.sin(2*math.pi*(y+b*math.sin(2*math.pi*(x)%1))%1))%1,(y+b*math.sin(2*math.pi*(x)%1)) %1]



###on détermine dans quel case se trouve le centre de chaque sous-case###
    R=[]
    S=[]
    for i in range(0, N*N):
        for j in range(0,N1*N1):
            x=I2[i][j][0]  #coordonnées de chaque centre des sous-cases, selon x
            y=I2[i][j][1]  #selon y
            for a in range(0,N):
                for b in range(0,N):
                    if ((a/N<x) and (x<(a+1)/N)):
                        if ((b/N<y) and (y<(b+1)/N)):
                            R.append(b*N+a)
        S.append(R)
        R=[]
    #print(S)
    print("Le nombre de Fille est ")
    print(len(S))


###supression des doublons###
    Vf = []
    for i in range(0, len(S)):
        f = []
        for j in range(0, len(S[i])):
            if S[i][j] not in f:
                f.append(S[i][j])
        Vf.append(f)
    print("La liste de Voeux est :")
    print(Vf)

    return(Vf)

Lax()  #appelle la fonction