import time

def questionMultiplication(a, b, reponseJoueur) :
    if reponseJoueur == a * b :
        return True
    else :
        return False

progression = 0

numeroCaseFin = 3
continuer = True

while continuer :
    if progression == 0 :
        print("Bienvenu dans notre jeu, vous êtes sur la case ", progression)
        progression = 1
    elif progression == 1 :
        print("Bienvenu sur la case ", progression)
        print("On va tester vos connaissances des tables de multiplication !")
        print("Combien font 7*6 ?")
        reponseJoueur = int(input("Alors ? "))

        JoueurABienRepondu = questionMultiplication(6, 7, reponseJoueur)

        if JoueurABienRepondu :
            print("Félicitation ! Vous passez à la fin du jeu !")
            progression = numeroCaseFin
        else :
            print("Désolé, vous ne pouvez pas continuer... Retour à la case départ dans trois secondes !")
            time.sleep(3)

    elif progression == numeroCaseFin :
        print("Vous avez fini le jeu, félicitation !")
        continuer = False

print("Ce jeu est terminé !")
