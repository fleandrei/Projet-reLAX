# -*-coding:Utf-8 -*
import math

a = 1  # les deux constantes utile pour la formule utilisé
b = 1  #

N = 10  # nombre de division de la grille. Avec N=100, cela fait 10 000cases

C = []  # liste qui contiendra les coordonnees des centres

I2 = []  # liste contenant les images de chaque centre
I1 = []  # liste intermédiaire

r = 1 / (2 * float(N))  # "rayon" d'une case

# remplissage de C, contenant l'ensemble des centre des cases

for x in range(0, N):
    for y in range(0, N):
        C.append([(x / float(N) + 1 / (2 * float(N))), y / float(N) + 1 / (2 * float(N))])

for i in range(0, len(C)):  # on convertie en str pour enlever les arrondies douteux
    C[i][0] = str(C[i][0])
    C[i][1] = str(C[i][1])

for i in range(0, len(C)):  # on reconvertie en float, pour permetre les calculs
    C[i][0] = float(C[i][0])
    C[i][1] = float(C[i][1])

# remplissage de I, image de chaque centre, modulo 1

for i in range(0, len(C)):
    I1.append([(C[i][0] + a * math.sin(2 * math.pi * C[i][1])) % 1, (C[i][1]) % 1])
    I2.append([(I1[i][0]) % 1, (I1[i][1] + b * math.sin(2 * math.pi * I1[i][0])) % 1])

# on détermine k
k = 1  # +2*math.pi*(a+a*b)

# "majoration du rayon de l'image"
r1 = r * k

# on cherche les cases qui ont une intersection avec le cercle majorant des images
# pour cela, on regarde si la distance de chaque coin des cases est contenu dans ce cercle
# pour cela, on regarde si la distance du coin au point image est inferieur au rayon r1

V = []  # liste contenant les "voeux" de chaque cases initiale

for w in range(0, len(I2)):  # on parcourt la liste des images des centres de chaque carré
    S = []  # on creer la sous liste vide, qui contient les voeux du w ieme centre
    for i in range(0, N):
        for j in range(0, N):

            d = str(math.sqrt((((I2[w][0] - i / float(N)) ** 2) + (
                        (I2[w][1] - j / float(N)) ** 2))))  # distance entre un coin et le centre image
            d = float(d)  # on repasse en flottant

            d1 = str(
                math.sqrt((((I2[w][0] - (i + 1 / 2) / float(N)) ** 2) + ((I2[w][1] - (j + 1 / 2) / float(N)) ** 2))))
            d1 = float(d1)

            if d < r1:
                S.append((i + N * j) % 100)  # on ajoute la case en bas a gauche du coin
                S.append((i + 1 + N * j) % 100)  # en bas a droite
                S.append((i + N * (j + 1)) % 100)  # en haut a gauche
                S.append((i + 1 + N * (j + 1)) % 100)  # en haut a droite
            if d1 < r1:
                S.append((i + N * j) % 100)  # on ajoute la case dont le centre est dans le cercle cible

    V.append(S)

Vf = []
for i in range(0, len(V)):
    f = []
    for j in range(0, len(V[i])):
        if V[i][j] not in f:
            f.append(V[i][j])
    Vf.append(f)

print(Vf)