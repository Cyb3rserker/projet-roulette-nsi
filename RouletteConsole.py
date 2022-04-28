import random
import csv

# Fonctions 
def listeLogin(liste) :
    """
    Crée une liste de tout les pseudos présents dans la liste mise en argument .
    liste = list --> a = list
    """
    a = []
    for i in range(1,len(liste)) :
        l = liste[i][1]
        a.append(l)
    return a

def choixLigne(user) :
    """
    Renvoie le numéro de la ligne sur laquelle est présente l'utilisateur en argument .
    user = str --> i = int
    """
    for i in range(len(allLogin)) :
        if user == allLogin[i] :
            return i

def ajoutUser(email, pseudo, mdp, liste) :
    """
    Renvoie une liste contenant les anciennes ligne du fichier csv avec une liste en plus contenant les nouvelles données 
    utilisateur .
    email = str / pseudo = str / mdp = str / liste = list --> newliste --> list
    """
    newListe = []
    for ligne in liste :
        newListe.append(ligne)
    newListe.append([email,pseudo,mdp,"Utilisateur","10000", "0"])
    return newListe

# Définition Marqueurs 
Cursor = 0

# Définition Gains
zero = 0
rouge = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
noir = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
pair = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
impair = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
manque = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
passe = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

# Définition fichier utilisateur
userFile = open("userRoulette.csv", "r")
userList = list(csv.reader(userFile, delimiter=";"))
allLogin = listeLogin(userList)

# Bienvenue
print("Bienvenue à la Roulette Magique !") # Page de base
while Cursor == 0 :
    choixConnexion = input("Voulez-vous vous Connecter(1) ou vous Enregistrer(2) : ")
    if choixConnexion == "1" or choixConnexion == "2" :
        Cursor = 1
    else :
        print("Choix incorrect !")
choixConnexion = int(choixConnexion)

# Page de login
Cursor = 0
if choixConnexion == 1: 

    # Login du pseudo
    while Cursor == 0: 
        login = input("Votre pseudo : ")
        if login in allLogin :
            Cursor = 1
        else : 
            print("Pseudo inconnu !")
    Cursor = 0
    ligneUser = choixLigne(login)+1

    # Login Mot de passe
    while Cursor == 0: 
        password = input("Votre mot de passe : ")
        if password == userList[ligneUser][2]:
            Cursor = 1
        else :
            print("Mot de passe incorrect !")
    Cursor = 0
    print("Bienvenue ,", login, "!")

# Page d'enregistrement
elif choixConnexion == 2: 

    # Nouveau Mail
    while Cursor == 0: 
        nouveauMail = input("Entrez votre eMail : ")
        if "@" in nouveauMail and "." in nouveauMail : # Vérification syntaxe eMail valide
            Cursor = 1
        else :
            print("Format eMail incorrect !")
    Cursor = 0

    # Nouveau Pseudo
    while Cursor == 0: 
        nouveauPseudo = input("Entrez un pseudo : ")
        if nouveauPseudo in allLogin : # Vérification que le pseudo n'est pas déjà pris
            print("Pseudo déjà pris !")
        else :
            Cursor = 1
    Cursor = 0

    # Ajout du Mot de passe
    while Cursor == 0: 
        nouveauPass1 = input("Entrez un nouveau mot de passe (6 caractères minimum) : ")
        if len(nouveauPass1) >=6 : # Vérification de la longueur du mot de passe
            Cursor = 1
        else:
            print("Trop peu de caractères")
    Cursor = 0

    # Vérification du mot de passe une deuxième fois
    while Cursor == 0: 
        nouveauPass2 = input("Entrez à nouveau votre mot de passe : ")
        if nouveauPass2 == nouveauPass1:
            Cursor = 1
        else:
            print("Mot de passe incorrect !")
    Cursor = 0

# Création du nouveau fichier csv contenant le nouvel utilisateur