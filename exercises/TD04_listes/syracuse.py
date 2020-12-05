# n = 3: (3; 10; 5; 16; 8; 4; 2; 1)
def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = []
    while (n != 1):
        liste.append(n)
        if (n % 2 == 0):
            n = n // 2
        elif (n % 2 == 1):
            n = n * 3 + 1
    liste.append(1)
    return liste


print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(2, n_max + 1):
        syracuse(i)
    return True


print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    syracuse(n)
    temps_vol = len(syracuse(n)) - 1
    return temps_vol


print("Le temps de vol de", 3, "est", tempsVol(3))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste = []
    for i in range(2, n_max):
        liste.append(tempsVol(i))
    return liste


print(tempsVolListe(100))

print(max(tempsVolListe(10000)))


def altMax(n_max):
    """ Retourner l'altitude maximale entre 2 et n_max"""
    liste = []
    for i in range(2, n_max + 1):
        liste.extend(syracuse(i))
    return max(liste)


print(altMax(10000))
