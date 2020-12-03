def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = []
    while (n != 1):
        if(n % 2 == 0):
            x = n // 2
            liste.append(x)
        elif(n % 2 == 1):
            x = n * 3 + 1
            liste.append(x)
        return liste
    return liste


print(syracuse(3))
print(syracuse)
