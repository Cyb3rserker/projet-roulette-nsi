"""
Notes :
    - Il faut bien executer le code en étant dans le même répertoire
    que userRoulette.csv sinon le code ne marche pas.
"""
"""
Structure de la base de données :
    - données délimitées par ;
    - descripteurs (sur la ligne 0) :
        - Pseudo (index [0][0])
        - MDP (index [0][1])
        - Fonction (index [0][2])
"""
"""
Modifications du 28/04/2022 :
    - changement du mode d'ouverture du fichier userRoulette.csv :
        - le mode r+ permet la lecture et l'écriture, mais requiert 
        l'existence du fichier.
    - eMail :
        - c'est bizarre mdr autant garder seulement le pseudo, puis c'est plus court parce 
        que sinon on devrait avoir 2 modes d'indentifications : avec mail OU avec pseudo.
    - suppression de listeLogin() et allLogin :
        - on peut directement accéder au pseudo des utilisateur avec l'index [ligne][1], 
        la fonction prend de la mémoire et nous embrouillera dans le code je pense. 
        Il faut quand même donner une petite description de la structure de la base 
        de données, ce que j'ai fait à partir de la ligne 1.
    - csv.reader à la définition du fichier utilisateur :
        - j'ai enlever le paramètre delimiter=";" parce que les données de notre fichier 
        sont séparées par des virgules 
    - changement des types pour les choix dans menu :
        - j'ai changer les types des variables choix... parce que la conversion en int peut 
        causer des erreurs facilement si l'utilisateur fait une saisie bizarre, comme juste la 
        touche entrée donc je les ai changer en chaînes de caractères
    - apport de vérification de saisie :
        - il y a pas mal de boucle while avec beaucoup de conditions qui entourent la même 
        variable mais c'est pour la vérification de saisie, comme par exemple l'interdiction 
        de mettre des virgules dans le pseudo ou mdp qui peuvent défoncer la base de données. 
        Je sais que ça peut être un peu dur à lire donc j'ai sauter des lignes entre chaques 
        blocs
"""
import csv

# Définition fichier utilisateur
userFile = open("userRoulette.csv", "r+")
liste_user_fichier = list(csv.reader(userFile))

# Bienvenue
print("Bienvenue à la Roulette Magique !")

drapeau_tout_bon = False
choixConnexion = 0

while drapeau_tout_bon == False :
    choixConnexion = input("Voulez-vous vous Connecter(1) ou vous Enregistrer(2) ?\n> ")
    if choixConnexion != "1" and choixConnexion != "2" : 
        print("Saisie incorrecte.")
        continue

    elif choixConnexion == "1" :
        pseudo_login_user = input("Quelle est votre pseudo ?\n> ")

        while len(pseudo_login_user) == 0 or pseudo_login_user[0] == " " or "," in pseudo_login_user :
            choix_taper_pseudo_ou_main_menu = input("Pseudo non valable. Ne le commencez pas par un espace et mettez au moins 1 caractère. Tapez 1 pour le retaper ou 2 pour retourner au menu principal :\n> ")

            while choix_taper_pseudo_ou_main_menu != "1" and choix_taper_pseudo_ou_main_menu != "2" :
                print("Saisie incorrecte.")
                choix_taper_pseudo_ou_main_menu = input("Tapez 1 pour le retaper ou 2 pour retourner au menu principal :\n> ")

            if choix_taper_pseudo_ou_main_menu == "1" :
                pseudo_login_user = input("Entrez votre pseudo :\n> ") 
                continue

            elif choix_taper_pseudo_ou_main_menu == "2" : break

        liste_pseudo = [liste_user_fichier[i][0] for i in range(1, len(liste_user_fichier))]

        if pseudo_login_user in liste_pseudo :
            index_pseudo_login_user = 0

            for i in range(len(liste_pseudo)) :
                if pseudo_login_user != liste_pseudo[i] :
                    index_pseudo_login_user+=1
                else :
                    break
            
            while 1 :
                mdp_login_user = input("Mot de passe :\n> ")

                if mdp_login_user == liste_user_fichier[index_pseudo_login_user + 1][1]: 
                    drapeau_tout_bon = True
                    print("Accès autorisé.")
                    break

                else :
                    choix_taper_mdp_ou_main_menu = input("Mot de passe incorrect. Taper 1 pour le retaper ou 2 pour retourner au menu principal.\n> ")

                    while choix_taper_mdp_ou_main_menu != "1" and choix_taper_mdp_ou_main_menu != "2" :
                        print("Saisie incorrecte.")
                        choix_taper_mdp_ou_main_menu = input("Tapez 1 pour le retaper ou 2 pour retourner au menu principal.\n> ") 
                    
                    if choix_taper_mdp_ou_main_menu == "1" : continue
                    elif choix_taper_mdp_ou_main_menu == "2" : break
                    # la boucle while va se terminer car on retourne à la condition, qui est devenue fausse

        elif pseudo_login_user not in liste_pseudo :
            print("Pseudo incorrect. Retour au menu principal.")
            continue
    
    elif choixConnexion == "2" :
        pseudo_login_user = input("Entrez un nouveau pseudo :\n> ")

        while len(pseudo_login_user) == 0 or pseudo_login_user[0] == " " or "," in pseudo_login_user :
            choix_taper_pseudo_ou_main_menu = input("Pseudo non valable. Ne le commencez pas par un espace et mettez au moins 1 caractère. Tapez 1 pour le retaper ou 2 pour retourner au menu principal :\n> ")

            while choix_taper_pseudo_ou_main_menu != "1" and choix_taper_pseudo_ou_main_menu != "2" :
                print("Saisie incorrecte.")
                choix_taper_pseudo_ou_main_menu = input("Tapez 1 pour le retaper ou 2 pour retourner au menu principal :\n> ")

            if choix_taper_pseudo_ou_main_menu == "1" :
                pseudo_login_user = input("Entrez un nouveau pseudo :\n> ")
                continue

            elif choix_taper_pseudo_ou_main_menu == "2" : break

        if len(pseudo_login_user) != 0 and pseudo_login_user[0] != " " and "," not in pseudo_login_user :
            liste_pseudo = [liste_user_fichier[i][0] for i in range(1, len(liste_user_fichier))]

            if pseudo_login_user not in liste_pseudo :
                mdp_login_user = input("Entrez votre mot de passe :\n> ") 

                while len(mdp_login_user) == 0 or mdp_login_user[0] == " " or "," in mdp_login_user :
                    choix_taper_mdp_ou_main_menu = input("Mot de passe non valable. Ne le commencez pas par un espace et mettez au moins 1 caractère. Tapez 1 pour le retaper ou 2 pour retourner au menu principal :\n> ")

                    while choix_taper_mdp_ou_main_menu != "1" and choix_taper_mdp_ou_main_menu != "2" :
                        print("Saisie incorrecte.")
                        choix_taper_mdp_ou_main_menu = input("Tapez 1 pour le retaper ou 2 pour retourner au menu principal :\n> ")

                    if choix_taper_mdp_ou_main_menu == "1" :
                        mdp_login_user = input("Entrez votre mot de passe :\n> ") 
                        continue

                    elif choix_taper_mdp_ou_main_menu == "2" : break
                    mdp_login_user = input("Mot de passe non valable. Ne le commencez pas par un espace et mettez au moins 1 caractère :\n> ")

                if len(mdp_login_user) != 0 and mdp_login_user[0] != " " and "," not in mdp_login_user :
                    drapeau_tout_bon = True
                    userFile.write(f"\n{pseudo_login_user},{mdp_login_user},Utilisateur,0")
                    continue

            elif pseudo_login_user in liste_pseudo :
                print("Nom d'utilisateur déjà pris. Retour au menu principal.")
                continue

userFile.close()