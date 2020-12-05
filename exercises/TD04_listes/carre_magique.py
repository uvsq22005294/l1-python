carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
print(carre_mag)
print()

carre_pas_mag = [list(L) for L in carre_mag]
carre_pas_mag[3][2] = 7
print(carre_pas_mag)
print()


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in range(len(carre)):
        print(carre[i])


afficheCarre(carre_mag)
print()
afficheCarre(carre_pas_mag)
print()


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    som = sum(carre[0])
    for L in carre:
        if sum(L) != som:
            return -1
    return som


print(testLignesEgales(carre_mag))
print()
print(testLignesEgales(carre_pas_mag))
print()


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    col = [L[0] for L in carre]
    som = sum(col)
    for i in range(1, len(carre)):
        col = [L[i] for L in carre]
        if sum(col) != som:
            return -1
    return som


print(testColonnesEgales(carre_mag))
print()
print(testColonnesEgales(carre_pas_mag))
print()


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    diag = []
    for i in range(len(carre)):
        x = carre[i][i]
        diag.append(x)
        print(diag)
    som = sum(diag)
    diag2 = []
    z = 3
    for j in range(len(carre)):
        y = carre[j][j + z]
        z -= 1
        diag2.append(y)
        print(diag2)
        if (sum(diag) != som):
            return -1
    return som


'''def testDiagonalesEgales(carre):

  n = len(carre)
  diag = [carre[i][i] for i in range(n)]
  anti_diag = [carre[i][n - 1 - i] for i in range(n)]
  som = sum(diag)
  if som == sum(anti_diag):
    return som
  else:
    return -1
    
print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))'''


print(testDiagonalesEgales(carre_mag))
print()
print(testDiagonalesEgales(carre_pas_mag))
print()


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if (testLignesEgales(carre) == testColonnesEgales(carre) == testDiagonalesEgales(carre)):
        return True
    else:
        return False


print(estCarreMagique(carre_mag))
print()
print(estCarreMagique(carre_pas_mag))
print()
