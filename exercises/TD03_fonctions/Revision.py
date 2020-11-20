def tempsEnSeconde(temps):
    return ((temps[0] * 24 + temps[1]) * 60 + temps[2]) * 60 + temps[3]


temps = (4, 38, 24, 26)
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    jours = seconde // 86400
    heures = (seconde % 86400) // 3600
    minutes = ((seconde % 86400) % 3600) // 60
    secondes = ((seconde % 86400) % 3600) % 60
    return (jours, heures, minutes, secondes)


temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")


######################################
def affichePluriel(val, mot):
    if val != 0:
        print(" ", val, mot, end="")
    if val > 1:
        print("s", end="")


def afficheTemps(temps):
    affichePluriel(temps[0], "jour")
    affichePluriel(temps[1], "heure")
    affichePluriel(temps[2], "minute")
    affichePluriel(temps[3], "seconde")
    print("")


afficheTemps((6, 0, 1, 24))
print("")
print("")


#######################################
def demandeTemps():
    jour = int(input("Choisir le nombre de jour: "))

    heure = int(input("Choisir le nombre d'heure: "))
    while (heure > 24 or heure < 0):
        print("Erreur. Choisir un nombre valide entre 0 et 24")
        heure = int(input("Choisir le nombre d'heure: "))

    minute = int(input("Choisir le nombre de minute: "))
    while (minute > 60 or minute < 0):
        print("Erreur. Choisir un nombre valide entre 0 et 60")
        minute = int(input("Choisir le nombre de minute: "))

    seconde = int(input("Choisir le nombre de seconde: "))
    while (seconde > 60 or seconde < 0):
        print("Erreur. Choisir un nombre valide entre 0 et 60")
        seconde = int(input("Choisir le nombre de seconde: "))

    return (jour, heure, minute, seconde)


afficheTemps(demandeTemps())
print("")
print("")


########################################
def sommeTemps(temps1, temps2):
    return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))


afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))
print("")
print("")


########################################
def proportionTemps(temps, proportion):
    return secondeEnTemps(tempsEnSeconde(temps) * proportion)


afficheTemps(proportionTemps((2, 0, 36, 0), 0.2))
print("")
print("")


########################################
import time


def tempsEnDate(temps):
    jour, heure, minute, seconde = temps
    annee = 1970 + jour // 365
    jour %= 365
    return (annee, jour, heure, minute, seconde)


def afficheDate(date=-1):
    if date == -1:
        date = tempsEnDate(secondeEnTemps(int(time.time())))
    annee, jour, heure, minute, seconde = date
    print("Année", annee, end=" ")
    afficheTemps((jour % 365, heure, minute, seconde))


temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()
print("")
print("")


########################################
afficheDate(tempsEnDate(secondeEnTemps(int(time.time()))))
print(time.gmtime(time.time()))
print("")
print("")


########################################
def bisextile(jour):
    annee = 1970
    while (jour >= 0):
        if (annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)):
            print("Année", annee, "bissextile.")
            jour -= 366
        else:
            jour -= 365
        annee += 1
    return


bisextile(20000)
print("")
print("")


########################################
def nombreBisextile(jour):
    annee = 1970
    b = 0
    while (jour >= 0):
        if (annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)):
            b += 1
            jour -= 366
        else:
            jour -= 365
        annee += 1
    return b


def tempsEnDateBisextile(temps):
    jour, heure, minute, seconde = temps
    return tempsEnDate((jour - nombreBisextile(jour), heure, minute, seconde))


temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))
print("")
print("")


########################################
def verifie(liste_temps):
    if (len(liste_temps) != 4):
        print("Liste mal formée.")
        return False
    temps_total = 0
    for elem in liste_temps:
        if (tempsEnSeconde(elem) > tempsEnSeconde((0, 48, 0, 0))):
            return False
        temps_total += tempsEnSeconde(elem)
    return temps_total <= tempsEnSeconde((0, 140, 0, 0))


liste_temps = [[1, 2, 39, 34], [0, 1, 9, 4], [0, 29, 39, 51], [0, 31, 13, 46]]
print(verifie(liste_temps))
print("")
print("")


########################################
