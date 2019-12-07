def carta(fichier):
    with open(fichier, "r") as fichier:
        listMap = []
        for ligne in fichier:
            lineMap = []
            for lettre in ligne[: -1]:
                lineMap.append(lettre)
            listMap.append(lineMap)
        return listMap

def coord(fichier):
    carteN = carta(fichier)
    i = 0
    while i < len(carteN):
        j = 0
        while j < len(carteN[i]):
            if carteN[i][j] == "d":
                coordDep = (i, j)
            elif carteN[i][j] == "a":
                coordArr = (i, j)
            else:
                pass
            j += 1
        i += 1
    return (coordDep, coordArr)
