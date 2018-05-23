# -*-coding:Utf-8 -*
import math



def Lax():
    a = 1  # les deux constantes utile pour la formule utilisé
    b = 1  #

    N = 10 # nombre de division de la grille. Avec N=100, cela fait 10 000cases
    N1 = 5 # nombre de sous-division de chaque case

    r =math.sqrt(2)/(N1*N)       #rayon



    I = []  # liste contenant les images de chaque centre
    Z=[]
    C = []



    ### createur de liste ###
    for i in range(0,N*N):
        for j in range(0,N1*N1):
            Z.append(j)
        C.append(Z)
        I.append(Z)
        Z=[]

    #print(C)


    ### remplissage des sous-centre###
    for x in range(0, N):
        for y in range(0, N):
            i=0
            for x1 in range(0, N1):
                 for y1 in range(0, N1):
                    C[y*N+x][i]=[float(((x*N1)+x1)+1/(2*(N1+N)))/(N*N1),float(((y*N1)+y1)+1/(2*(N1+N)))/(N*N1)]
                    i=i+1
    #print(C)


    ### remplissage de I, image de chaque sous-centre, modulo 1 ###
    #print(I2)
    for i in range(0, len(C)):
        for j in range(0,len(C[i])):
            x=C[i][j][0]
            y=C[i][j][1]
            I[i][j]=[(x%1 +a*math.sin(2*math.pi*(y+b*math.sin(2*math.pi*(x)%1))%1))%1,(y+b*math.sin(2*math.pi*(x)%1)) %1]
    #print("salut")
    #print(I)


    # on détermine k
    k = 1+2*math.pi*(a+a*b)

    # "majoration du rayon de l'image"
    #r = r * 4


    V=[]

    for w in range(0, len(I)):  # on parcourt la liste des images des centres de chaque carré
        for x in range (0,len(I[w])):
            print(I[w][x])
            S = []  # on creer la sous liste vide, qui contient les voeux du w ieme centre
            for i in range(0, N): #x
                for j in range(0, N): #y

                    if (((I[w][x][0])-r>i/N) and ((I[w][x][0])-r<(i+1)/N)):  #on ajoute ceux dont le coin en vas a gauche de l'ensemble d'arrivé se trouve dans une case
                        if (((I[w][x][1]) - r > j/N) and ((I[w][x][1]) - r < (j+1)/ N)):
                            S.append(j*N+i)

                    if (((I[w][x][0])+r>i/N) and ((I[w][x][0])+r<(i+1)/N)):  #on ajoute ceux dont le coin en vas a droite
                        if (((I[w][x][1]) - r > j/N) and ((I[w][x][1]) - r < (j+1)/ N)):
                            S.append(j*N+i)

                    if(((I[w][x][0]) - r > i/N) and ((I[w][x][0]) - r < (i+1)/ N)):  # on ajoute ceux dont le coin en haut a gauche
                        if (((I[w][x][1]) + r > j/N) and ((I[w][x][1]) + r < (j+1)/ N)):
                            S.append(j * N + i)

                    if (((I[w][x][0]) + r > i/N) and ((I[w][x][0]) + r < (i+1)/ N)):  # dont le coin en haut a droite
                         if (((I[w][x][1]) + r > j/N) and ((I[w][x][1]) + r < (j+1)/ N)):
                            S.append(j * N + i)


        V.append(S)


    Vf = []
    for i in range(0, len(V)):
        f = []
        for j in range(0, len(V[i])):
            if V[i][j] not in f:
                f.append(V[i][j])
        Vf.append(f)

    print(Vf)

    print(len(Vf))
    S = str(Vf)
    fichier = open("chaine.txt", "w")
    fichier.write(S)
    fichier.close()






Lax()









