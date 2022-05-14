import random 

#__INITIALISATION LISTE__

"""
Tous les chiffres présent sur le plateau seront des tuples dans une liste.
Dans ces tuples, il y a en rang 0 le numéro et en rang 2 sa couleur.
"""

chiffre_sur_plateau = [(0, "vert")]

for i in range(1, 37) :
    if i % 2 == 0 :
        chiffre_sur_plateau.append((i, "noir"))
    else :
        chiffre_sur_plateau.append((i, "rouge"))

#__DIFFERENTES FONCTIONS DE LA PARTIE__

def tirage_roulette() :
	return random.choice(chiffre_sur_plateau)

def gain(type_mise, montant, numero_tire) :
	#------------------------------------------------------------------------------
	# NUMERO UNIQUE
	#------------------------------------------------------------------------------
	
	if type_mise == "U" or type_mise == "u" :
		numero_user = int(input("Quel est le numéro que vous avez choisi ?\n> "))
		if numero_tire[0] == numero_user :
			return montant * 36
		else :
			return -montant
	
	#------------------------------------------------------------------------------
	# PAIR OU IMPAIR
	#------------------------------------------------------------------------------
	
	elif type_mise == "E" or type_mise == "e" :
		choix_user_pair_impair = input("Tapez E pour choisir pairs ou O pour impairs :\n> ")
		if choix_user_pair_impair == "E" or choix_user_pair_impair == "e" :
			if numero_tire[0] % 2 == 0 :
				return montant
			elif numero_tire[0] % 2 != 0 :
				return -montant
		elif choix_user_pair_impair == "O" or choix_user_pair_impair == "o" :
			if numero_tire[0] % 2 != 0 :
				return montant
			elif numero_tire[0] % 2 == 0 :
				return -montant
	
	#------------------------------------------------------------------------------
	# MANQUE PASSE
	#------------------------------------------------------------------------------
		
	elif type_mise == "M" or type_mise == "m":
		numero_user = int(input("Quel est le numéro que vous avez choisi ?\n> "))
		if numero_tire[0] in range(1, 19) and numero_user in range(1, 19) :
			return montant
		else :
			return -montant

		if numero_tire[0] in range(19, 37) and numero_user in range(19, 37):
			return montant
		else :
			return -montant
	
	#------------------------------------------------------------------------------
	# COULEUR
	#------------------------------------------------------------------------------

	elif type_mise == "C" or type_mise == "c" :
		choix_couleur_user = input("Tapez 'R' pour Rouge ou 'N' Pour Noir :\n> ")
		while choix_couleur_user not in ["r", "R", "n", "N"] :
			print("Veuillez réessayer en tapant les lettres proposées.")
			choix_couleur_user = input("Tapez 'R' pour Rouge ou 'N' Pour Noir :\n> ")

		if choix_couleur_user == "r" or choix_couleur_user == "R" :
			choix_couleur_user = "rouge"
		elif choix_couleur_user == "n" or choix_couleur_user == "N" :
			choix_couleur_user = "noir"

		if numero_tire[1] == choix_couleur_user :
			return montant
		else :
			return -montant

	
def partie(credit_user) :
	print("\n\nVous allez maintenant lancer une partie de roulette.\n")
	
	choix_type_mise_user = input("Veuillez faire un choix de mise parmis les suivants :\nU : numéro unique\nE : pair ou impair\nM : Manque ou passe\nC : Couleur\n> ")

	if choix_type_mise_user not in ["U", "E", "M", "C"] and choix_type_mise_user not in ["u", "e", "m", "c"] :
		print("Veuillez faire un choix entre les mises proposées.")
		choix_type_mise_user = input("Veuillez faire un choix de mise parmis les suivants :\nU : numéro unique\nE : pair ou impair\nM : Manque ou passe\nC : Couleur\n> ")

	mise_user = int(input("Quelle est votre mise ?\n> "))
	
	while credit_user - mise_user < 0 :
		print(f"Vous avez entré une mise qui est supérieur à votre crédit. Pour rappel, votre crédit est actuellement de {credit_user}.")
		mise_user = int(input("Quelle est votre mise ?\n> "))
	
	numero_tire = tirage_roulette()
	
	resultat_partie = gain(choix_type_mise_user, mise_user, numero_tire)
	
	
	
	if resultat_partie > 0 :
		print(f"Le numéro tiré eeeeeeesssssttt... le {numero_tire[0]} {numero_tire[1]} !")
		print(f"Bravo ! Vous avez gagné {resultat_partie} points ce qui ramène votre crédit à {credit_user + resultat_partie} ! (Je pense que vous devriez continuer, vous êtes sur une bonne série.)")
	else :
		print(f"Le numéro tiré eeeeeeesssssttt... le {numero_tire[0]} {numero_tire[1]} !")
		print(f"Dommage ! Vous avez perdu ce qui ramène vos points de crédit à {credit_user + resultat_partie}. Retentez votre chance pour récupéré vos mises !")
	
	return resultat_partie
		
#__JEU__
	
print("".center(50, "*"))
print("  JEU DE LA ROULETTE  ".center(50, "*"))
print("".center(50, "*"))

choix_user_continuer = 1
credit = 1000


while choix_user_continuer == 1 :
	print()
	if credit <= 0 :
		print("Dommage ! Vous n'avez plus de crédit pour jouer. Revenez avec de l'argent et vous pourrez jouer.")
		break
	print(f"Votre crédit actuel : {credit}")
	
	credit += partie(credit)

	choix_user_continuer = int(input("Voulez-vous continuer à jouer ?\n(1 = oui ; 2 = non)\n> "))
