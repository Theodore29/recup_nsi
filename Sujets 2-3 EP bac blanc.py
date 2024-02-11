#Sujet 3 :

#Exercice 1

ex=[1, 2, 4, 6, 6]

def a_doublon(liste):
    for i in range(len(liste) - 1):
        if liste[i] == liste[i + 1]:
            return True
    return False

#Exercice 2
def voisinage(n, ligne, colonne):
    voisins =[]
    for l in range(max(0,ligne-1), min(n, ligne+2)):
        for c in range(max(0, colonne), min(n, colonne+2)):
            if (l,c) != (ligne,colonne):
                voisins.append((l,c))
    return voisins

def incremente_voisins(grille, ligne, colonne):
    """ Incrémente de 1 toutes les cases voisines d'une bombe."""
    voisins + grille[l][c]

    for l, c in voisins:
        if grille[l][c] != "*" :
            voisins +=1

def genere_grille(bombes):
    n=len(bombes)
    grille = [[0 for colonne in range(n)] for ligne in range(n)]

    for ligne, colonne in bombes:
        grille[ligne][colonne] = "*"

    return grille


#Sujet 2 :
val_coef=[(8, 2), (12, 0), (13.5, 1), (5, 0.5)]

def moyenne(valeur):
    for i in range(len(valeur)):
        for j in valeur[0][i]:
            somme_coeff = []
            somme_coeff.append(valeur[i][1])
    print(somme_coeff)