#----fonctions----
#couleur= variable qui correspond a l'index de la liste Listecouleurs 
#p_xstart = multiple de la taille du sprite, qui augmente de 1 la colonne en augmentant de 1
#p_casesprite = chiffre présent dans le fichier texte, donnant la position de l'image
def image(couleur,p_xstart,p_casesprite):
	couleur+= 1
	if couleur> 7:#il n'y a que des couleurs ed 0 à 7 donc il faut revenir à la couleur d'index 0 après celle de 7.
		couleur= 0
	for ligne in gameGrid:#la boucle parcourt le fichier texte GameGrid.
		num_case = 0
		for sprite in ligne:
			x =  p_xstart * taille_sprite
			y = 13 * taille_sprite
			if sprite == p_casesprite: #si elle rencontre le chiffre p_casesprite, elle affiche une image
				fenetre.blit(Listecouleurs[couleur],(x,y))
	return couleur #renvois la variable couleur pour que la fonction puisse fonctionner

#-----------------


from random import randint
import pygame
from pygame.locals import*

pygame.init() #lance le module pygame

fenetre = pygame.display.set_mode((527,650)) #creer une fenetre de dimension (527;650)

taille_sprite = 39 #taille d'une image de pion

#On crée l'interface du jeu en placant un fichier texte dans un tableau (liste de liste)
with open("GameGrid.txt") as fichier:
	gameGrid = []
	for ligne in fichier:
		trial_line = []
		for sprite in ligne:
			if sprite != "\n":#on evite au programme de compter les retours à la ligne
				trial_line.append(sprite)
		gameGrid.append(trial_line)#on creer une liste dans une liste pour former un tableau

#Chargement de tous les images du jeu
rouge = pygame.image.load("Images/rouge.png").convert_alpha()#convert.alpha sert à permettre les textures alpha (transparence)
bleu = pygame.image.load("Images/bleu.png").convert_alpha()
orange = pygame.image.load("Images/orange.png").convert_alpha()
blanc = pygame.image.load("Images/blanc.png").convert_alpha()
violet = pygame.image.load("Images/violet.png").convert_alpha()
jaune = pygame.image.load("Images/jaune.png").convert_alpha()
vert = pygame.image.load("Images/vert.png").convert_alpha()
noir = pygame.image.load("Images/noir.png").convert_alpha()
rose = pygame.image.load("Images/rose.png").convert_alpha()
bravo = pygame.image.load("Images/bravo.png").convert_alpha()
perdu = pygame.image.load("Images/perdu.png").convert_alpha()
miniW = pygame.image.load("Images/mini_blanc.png").convert_alpha()
miniB = pygame.image.load("Images/mini_noir.png").convert_alpha()


#création d'une liste contenant toutes les couleurs
Listecouleurs = (bleu,orange,blanc,violet,jaune,vert,rouge,rose)

#importation des différents sons du jeu :
win = pygame.mixer.Sound("Sons/Win.wav")
switch = pygame.mixer.Sound("Sons/switch.wav")
enter = pygame.mixer.Sound("Sons/enter.wav")
lose = pygame.mixer.Sound("Sons/lose.wav")

#variable de la boucle principale
continuer=1

#Lancement de la musique de jeu
pygame.mixer.music.load("Sons/ADMind Theme.wav")
pygame.mixer.music.play()

pygame.mixer.music.set_volume(0.15)

#BOUCLE DU JEU ENTIER
while continuer:

	#chargement et affichage de l'image de fond de l'accueil
	fond = pygame.image.load("Images/Accueil.png").convert()
	fenetre.blit(fond,(0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle pour reset le jeu
	continuer_jeu = 1
	continuer_accueil = 1
	continuer_regles = 1
	continuer_fin = 1
	continuer_gagne = 1
	continuer_perdu = 1

	numberGenerator = []

	#ces variables représentent les differentes valeurs que vont prendre les cases pour changer de couleur
	#elles sont égales à -1 pour que lors de l'utilisation, elles commencent à 0 pour correspondre à la fonction qui commence par incrémenter
	case_1 = -1
	case_2 = -1
	case_3 = -1
	case_4 = -1
	#Line est le nombre de ligne qui quadrille le jeu, elle est à 11 car elle correspond aux nombres de lignes totales et aux essais
	line = 11

	#BOUCLE D'ACCUEIL
	while continuer_accueil:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		#Prise en compte des commandes de l'utilisateur durant le jeu
		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met les variables
			#de boucle à 0 pour n'en parcourir aucune et fermer le programme
			if event.type == pygame.QUIT:

				continuer_accueil = 0
				continuer_jeu = 0
				continuer_regles=0
				continuer_fin = 0
				continuer = 0

			elif event.type == KEYDOWN: #une boucle qui attend qu'une touche parmis celles programmées soit pressée.

				if event.key == K_ESCAPE:
					continuer_accueil = 0
					continuer_jeu = 0
					continuer_regles=0
					continuer_fin = 0
					continuer = 0

				#Lancement de la boucle jeu (p = play)
				elif event.key == K_p: #si la touche p est pressé
					#lancement du son de la touche ENTREE
					enter.play()

					continuer_accueil = 0
					continuer_regles = 0
					fond = pygame.image.load("Images/Fond_Mastermind.png").convert()#affiche le fond du jeu 
					fenetre.blit(fond, (0,0))

				#Lancement de la boucle regles (r = regles)
				elif event.key == K_r: #si la touche r est pressé
					#lancement du son de la touche ENTREE
					enter.play()

					continuer_accueil=0
					fond = pygame.image.load("Images/Regles.png").convert()#affiche le fond des regles
					fenetre.blit(fond, (0,0))

	#BOUCLE DE REGLE
	while continuer_regles:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met les variables
			#de boucle à 0 pour n'en parcourir aucune et fermer le programme
			if event.type == pygame.QUIT:

				continuer_accueil = 0
				continuer_regles=0
				continuer_jeu = 0
				continuer_fin = 0
				continuer = 0

			elif event.type == KEYDOWN:
				#Lancement du jeu
				if event.key == K_p:
					#lancement du son de la touche ENTREE
					enter.play()

					continuer_accueil = 0
					continuer_regles = 0
					fond = pygame.image.load("Images/Fond_Mastermind.png").convert()
					fenetre.blit(fond, (0,0))

				#Lancement du menu
				if event.key == K_ESCAPE:
					#lancement du son de la touche ENTREE
					enter.play()

					continuer_regles=0
					continuer_jeu = 0
					continuer_fin = 0

		pygame.display.flip()

	#BOUCLE DE JEU
	while continuer_jeu:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		#Generation de la solution à trouver à travers une liste composée de 4 variables correspondant à 4 couleurs
		while len(numberGenerator)<4:
			randomNumber=(randint(0,7))
			if randomNumber not in numberGenerator:
				numberGenerator.append(randomNumber)
		masterCode = str(numberGenerator[0]) + str(numberGenerator[1]) + str(numberGenerator[2])+ str(numberGenerator[3])

		#Prise en compte des commandes de l'utilisateur durant le jeu
		for event in pygame.event.get():

				#Fait quitter le jeu (croix rouge)
				if event.type == pygame.QUIT:

					continuer_accueil=0
					continuer_jeu = 0
					continuer_fin = 0
					continuer = 0

				elif event.type == KEYDOWN:

					#Fait revenir au menu
					if event.key == K_ESCAPE:
						#lancement du son de la touche ENTREE
						enter.play()

						continuer_jeu = 0
						continuer_fin = 0

					#Fait changer la couleur de la premiere case
					elif event.key == K_e:
						#lancement du son de switch
						switch.play()
						case_1 = image(case_1,4,"6")#appelle la fonction
						
					#Fait changer la couleur de la deuxieme case
					elif event.key == K_r:
						#lancement du son de switch
						switch.play()
						case_2 = image(case_2,5,"7")

					#Fait changer la couleur de la troisieme case
					elif event.key == K_t:
						#lancement du son de switch
						switch.play()
						case_3 = image(case_3,6,"8")

					#Fait changer la couleur de la quatrieme case
					elif event.key == K_y:
						#lancement du son de switch
						switch.play()
						case_4 = image(case_4,7,"9")

					#Enclenche la vérification de la combinaison du joueur et son affichage
					elif event.key == K_RETURN:

						#lancement du son de la touche ENTREE
						enter.play()

						print(masterCode) #aide a la résolution pour debug

						#variables qui vont permettre de compter le nombre de couleurs fausses ou bonnes
						right = 0 
						wrong = 0

						#On réunit les valeurs dans les cases afin de constituer un code à 4 chiffres (ne pouvant être identiques)
						challengerCode = str(case_1)+str(case_2)+str(case_3)+str(case_4)

						if line != 1: #on empeche l'affichage de la combinaison du joueur pour la ligne 1 car elle est l'espace entre le plateau et la solution (esthetique)
							fenetre.blit(Listecouleurs[case_1],(4*taille_sprite,line*taille_sprite))
							fenetre.blit(Listecouleurs[case_2],(5*taille_sprite,line*taille_sprite))
							fenetre.blit(Listecouleurs[case_3],(6*taille_sprite,line*taille_sprite))
							fenetre.blit(Listecouleurs[case_4],(7*taille_sprite,line*taille_sprite))

						#Vérification du code entré
							for g in range(4):
								if challengerCode[g] in masterCode and challengerCode[g] is not masterCode[g]: #on vérifie si les variables des listes correspondent et si leurs index sont similaires pour différencier mal et bien placées
									wrong += 1

								if challengerCode[g] is masterCode[g]:
									right += 1

						#Affichage des carrés noirs/blancs
							for black in range(right):
								fenetre.blit(miniB,((9+black)*taille_sprite,line*taille_sprite))

							for white in range(wrong):
								fenetre.blit(miniW,((9+right+white)*taille_sprite,line*taille_sprite))
                                #Right+white est là pour positionner les pions blancs directement à droite des pions

						if right != 4: #si la réponse n'est pas bonne on passe à l'essai suivant
							line -= 1

						else:
							#affichage "gagné"
							fenetre.blit(bravo,(16,23))

							#affichage de la combinaison solution en haut
							fenetre.blit(Listecouleurs[numberGenerator[0]],(152,32))
							fenetre.blit(Listecouleurs[numberGenerator[1]],(192,32))
							fenetre.blit(Listecouleurs[numberGenerator[2]],(232,32))
							fenetre.blit(Listecouleurs[numberGenerator[3]],(272,32))

							#lancement du son de victoire
							win.play()

							#boucle pour stopper le jeu et visualiser la reponse
							while continuer_gagne:
								for event in pygame.event.get():

									#Fait quitter le jeu (croix rouge)
									if event.type == pygame.QUIT:

										continuer_accueil=0
										continuer_jeu = 0
										continuer_fin = 0
										continuer_gagne = 0
										continuer = 0

									elif event.type == KEYDOWN:

										if event.key == K_RETURN:
											#lancement du son de la touche ENTREE
											enter.play()
											#fermer la boucle jeu et lance la fin du jeu
											continuer_gagne=0
											continuer_jeu = 0

								pygame.display.flip()

							#chargement et affichage de l'image de victoire
							fond = pygame.image.load("Images/FinGagne.png").convert()
							fenetre.blit(fond,(0,0))
							#affichage de la solution au mileu de l'écran de fin
							fenetre.blit(Listecouleurs[numberGenerator[0]],(192,336))
							fenetre.blit(Listecouleurs[numberGenerator[1]],(232,336))
							fenetre.blit(Listecouleurs[numberGenerator[2]],(272,336))
							fenetre.blit(Listecouleurs[numberGenerator[3]],(312,336))

						if line == 0: #si line=0 c'est la que le joueur a effectué ses 10 essais
							#affichage "perdu"
							fenetre.blit(perdu,(16,23))
							#affichage de la reponse en haut
							fenetre.blit(Listecouleurs[numberGenerator[0]],(152,32))
							fenetre.blit(Listecouleurs[numberGenerator[1]],(192,32))
							fenetre.blit(Listecouleurs[numberGenerator[2]],(232,32))
							fenetre.blit(Listecouleurs[numberGenerator[3]],(272,32))

							#lancement du son de perte
							lose.play()

							#boucle pour stopper le jeu et visualiser la reponse
							while continuer_perdu:
								for event in pygame.event.get():

									#Fait quitter le jeu (croix rouge)
									if event.type == pygame.QUIT:

										continuer_perdu=0
										continuer_accueil=0
										continuer_jeu = 0
										continuer_fin = 0
										continuer = 0

									elif event.type == KEYDOWN:

										if event.key == K_RETURN:

											#lancement du son de la touche ENTREE
											enter.play()

											#fermer la boucle jeu et lance la fin du jeu
											continuer_perdu=0
											continuer_jeu = 0

								pygame.display.flip()

							#chargement et affichage de l'image de défaite
							fond = pygame.image.load("Images/FinPerdu.png").convert()
							fenetre.blit(fond,(0,0))
							#affichage de la solution au mileu de l'écran de fin
							fenetre.blit(Listecouleurs[numberGenerator[0]],(182,358))
							fenetre.blit(Listecouleurs[numberGenerator[1]],(222,358))
							fenetre.blit(Listecouleurs[numberGenerator[2]],(262,358))
							fenetre.blit(Listecouleurs[numberGenerator[3]],(302,358))

		pygame.display.flip()


	#BOUCLE DE FIN
	while continuer_fin:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met les variables
			#de boucle à 0 pour n'en parcourir aucune et fermer le programme
			if event.type == pygame.QUIT:

				continuer_accueil = 0
				continuer_jeu = 0
				continuer_fin=0
				continuer = 0

			elif event.type == KEYDOWN:
				#Retour au menu
				if event.key == K_ESCAPE:
					#lancement du son de la touche ENTREE
					enter.play()

					continuer_fin = 0

		pygame.display.flip()

pygame.quit()#permet a pygame de comprendre que le programme est fini