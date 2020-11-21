def fonction(continent, pays, ville):
    print(ville, pays, ".", continent)


print(fonction("", "France", "Paris"))


def fonction(argument):
    """Affiche quatre fois la valeur de son argument moins 2 si l'argument est supérieur à 1 et qui affiche -2 sinon."""
    if (argument > 1):
        print((4 * argument) - 2)
    else:
        print(-2)
    return


help(fonction)


var_glob = 9


def division(var_loc):
    return (var_glob // var_loc)


print(division(2))
