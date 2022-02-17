carte = [[0, 0, 0, 'A', 0],#A pour le point d'arrivée
         [0, 0, 1, 1, 0],
         [0, 0, 0, 'X', 0]] #X pour le point où se trouve le joueur

cartePourLeJoueur= [[0, 0, 0, 0, 0],#A pour le point d'arrivée
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]] #X pour le point où se trouve le joueur

coordonneesJoueur = [2, 3] #Troisième liste, quatrième élément, avec un décalage d'indice

def bougerJoueurAdroite(coordonneesJoueur, carte, cartePourLeJoueur) :
    if coordonneesJoueur[1] + 1 < len(carte[coordonneesJoueur[0]]) : #Il faut que la liste soit plus grande que l'absicce des coordonnées du joueur.
        ajouterTraceJoueurSurSaCarte(cartePourLeJoueur, coordonneesJoueur)
        return [coordonneesJoueur[0], coordonneesJoueur[1] + 1]
    else :
        print("Vous ne pouvez pas bouger, vous êtes déjà au bord de la carte !")
        return coordonneesJoueur

def bougerJoueurEnHaut(coordonneesJoueur, carte, cartePourLeJoueur) :
    if coordonneesJoueur[0] > 0 :
        ajouterTraceJoueurSurSaCarte(cartePourLeJoueur, coordonneesJoueur)
        return [coordonneesJoueur[0] -1, coordonneesJoueur[1] ]
    else :
        print("Vous ne pouvez pas bouger, vous êtes déjà au bord de la carte !")
        return coordonneesJoueur

def recupererInformationCaseJoueur(coordonneesJoueur, carte):
    return carte[coordonneesJoueur[0]][coordonneesJoueur[1]]

def afficherCartePourLeJoueur(cartePourLeJoueur, coordonneesJoueur):
    print("Voici votre carte :")
    carte = ""
    for i in range(len(cartePourLeJoueur)):
        for j in range(len(cartePourLeJoueur[0])):
            if [i, j] == coordonneesJoueur :
                carte += 'X'
            else :
                carte += str(cartePourLeJoueur[i][j])
        carte += '\n'
    print(carte)
    print("V marque les passages où vous êtes passé")
    print("X marque votre localisation")

def ajouterTraceJoueurSurSaCarte( cartePourLeJoueur, coordonneesJoueur ) :
    cartePourLeJoueur[coordonneesJoueur[0]][coordonneesJoueur[1]] ='V'

    return cartePourLeJoueur

coordonneesJoueur =  bougerJoueurAdroite(coordonneesJoueur, carte, cartePourLeJoueur)
print(coordonneesJoueur)
coordonneesJoueur =  bougerJoueurAdroite(coordonneesJoueur, carte, cartePourLeJoueur) #On ne bougera pas
print(coordonneesJoueur)

print(recupererInformationCaseJoueur(coordonneesJoueur, carte))
coordonneesJoueur =  bougerJoueurEnHaut(coordonneesJoueur, carte, cartePourLeJoueur)

afficherCartePourLeJoueur(cartePourLeJoueur, coordonneesJoueur)
