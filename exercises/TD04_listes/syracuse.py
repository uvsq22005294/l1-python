def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste_entier = []
    while (n != 1):
        if (n % 2 == 0):
            return n // 2
        elif (n % 2 == 1):
            return n * 3 + 1
    return liste_entier.append(n)


print(syracuse(3))
print(syracuse)
