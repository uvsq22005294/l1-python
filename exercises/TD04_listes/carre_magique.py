carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
print(carre_mag)
print("")
carre_pas_mag = [list(L) for L in carre_mag]
carre_pas_mag[3][2] = 7
print(carre_pas_mag)
print("")


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for L in carre:
        print(L)
    print()
    #return print("", carre[0], "\n", carre[1], "\n", carre[2], "\n", carre[3])


afficheCarre(carre_mag)
print("")
afficheCarre(carre_pas_mag)
print("")


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    somme = sum(carre[0])
    for ligne in range(len(carre)):
        if (ligne != somme):
            print("-1")


print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))
