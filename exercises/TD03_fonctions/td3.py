'''Fonction 1 :

temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes'''


def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme
    jour, heure, minute, seconde."""
    return temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    '''or (((temps[0] * 24) + temps[1])*60 + temps[2])*60 + temps[3]'''


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui
    correspond au nombre de seconde passé en argument"""
    jours = seconde // 86400
    heures = (seconde % 86400) // 3600
    minutes = ((seconde % 86400) % 3600) // 60
    secondes = ((seconde % 86400) % 3600) % 60
    return (jours, heures, minutes, secondes)


'''or minute = seconde // 60
      seconde %= 60
      heure = minute // 60
      minute %= 60
      jour = heure // 24
      heure %= 24 '''

temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")

print("")

'''Fonction 2 :
fonction auxiliaire ici'''


'''def afficheTemps(temps):
    return temps[0], temps[1], temps[2], temps[3]


temps = (1, 0, 14, 23)


def affichePluriel(val, mot):
    if (val > 0):
        print(val, mot, "s")
    elif (val == 0):
        print(val, mot, "")


print(afficheTemps(affichePluriel))'''


'''Fonction 3:'''


def demandeTemps():
    jour = int(input("Nombre de jour: "))
    heure = int(input("Nombre d'heure: "))
    while heure > 24:
        heure = int(input("Nombre d'heure entre 0 et 24: "))
    minute = int(input("Nombre de minute: "))
    while minute > 60:
        minute = int(input("Nombre de minute entre 0 et 60: "))
    seconde = int(input("Nombre de seconde: "))
    while seconde > 60:
        seconde = int(input("Nombre de seconde entre 0 et 60: "))
    return (((((jour * 24) + heure) * 60) + minute) * 60) + seconde


'''afficheTemps(demandeTemps())'''
print(demandeTemps())
