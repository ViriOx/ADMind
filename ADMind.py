#----fonctions----

def image(p_case,p_xstart,p_casesprite):
	p_case += 1
	if p_case >= 6:
		p_case = 0
	for ligne in gameGrid:
		num_case = 0
		for sprite in ligne:
			x =  p_xstart * taille_sprite
			y = 13 * taille_sprite
			if sprite == p_casesprite:
				fenetre.blit(colorsList[p_case],(x,y))
	return p_case

#-----------------


from random import randint
import pygame
from pygame.locals import*

pygame.init()

fenetre = pygame.display.set_mode((527,650))

taille_sprite = 39

#On crée l'interface du jeu en placant un fichier texte dans un tableau (liste de liste)
with open("GameGrid.txt") as fichier:
	gameGrid = []
	for ligne in fichier:
		trial_line = []
		for sprite in ligne:
			if sprite != "\n":
				trial_line.append(sprite)
		gameGrid.append(trial_line)

#Chargement de tous les carrés du jeu
rouge = pygame.image.load("New_red.png").convert_alpha()
bleu = pygame.image.load("New_blue.png").convert_alpha()
orange = pygame.image.load("New_orange.png").convert_alpha()
blanc = pygame.image.load("New_white.png").convert_alpha()
violet = pygame.image.load("New_purple.png").convert_alpha()
jaune = pygame.image.load("New_yellow.png").convert_alpha()
vert = pygame.image.load("New_green.png").convert_alpha()
noir = pygame.image.load("New_black.png").convert_alpha()

#création d'une liste contenant toutes les couleurs
colorsList = (rouge,bleu,orange,blanc,violet,jaune,vert)

#variable de la boucle principale
continuer=1

#BOUCLE DU JEU ENTIER
while continuer:

	#chargement et affichage de l'image
	fond = pygame.image.load("Resizedaccueil.png").convert()
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

	case_1 = 0
	case_2 = 0
	case_3 = 0
	case_4 = 0

	life = 11
	line = 2

	#BOUCLE D'ACCUEIL
	while continuer_accueil:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		#Prise en compte des commandes de l'utilisateur durant le jeu
		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met les variables
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == pygame.QUIT:

				continuer_accueil = 0
				continuer_jeu = 0
				continuer_regles=0
				continuer_fin = 0
				continuer = 0

			elif event.type == KEYDOWN:

				if event.key == K_ESCAPE:
					continuer_accueil = 0
					continuer_jeu = 0
					continuer_regles=0
					continuer_fin = 0
					continuer = 0

				#Lancement du jeu
				elif event.key == K_p:
					continuer_accueil = 0
					continuer_regles = 0
					fond = pygame.image.load("Lastmastermind.png").convert()
					fenetre.blit(fond, (0,0))

				#Lancement des regles
				elif event.key == K_r:
					continuer_accueil=0
					fond = pygame.image.load("Resized_regles.png").convert()
					fenetre.blit(fond, (0,0))

	#BOUCLE DE REGLE
	while continuer_regles:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met les variables
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == pygame.QUIT:

				continuer_accueil = 0
				continuer_regles=0
				continuer_jeu = 0
				continuer_fin = 0
				continuer = 0

			elif event.type == KEYDOWN:
				#Lancement du jeu
				if event.key == K_p:

					continuer_accueil = 0
					continuer_regles = 0

					fond = pygame.image.load("Lastmastermind.png").convert()
					fenetre.blit(fond, (0,0))

				#Lancement du menu
				if event.key == K_ESCAPE:

					continuer_regles=0
					continuer_jeu = 0
					continuer_fin = 0

		pygame.display.flip()

	#BOUCLE DE JEU
	while continuer_jeu:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		#Generation de la solution à trouver
		while len(numberGenerator)<4:
			randomNumber=(randint(0,6))
			if randomNumber not in numberGenerator:
				numberGenerator.append(randomNumber)
		masterCode = str(numberGenerator[0]) + str(numberGenerator[1]) + str(numberGenerator[2])+ str(numberGenerator[3])

		num_ligne = 0
		for ligne in gameGrid:
			num_case = 0
			for sprite in ligne:
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				num_case +=1
			num_ligne +=1

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

						continuer_jeu = 0
						continuer_fin = 0

					#Fait changer la couleur de la premiere case
					elif event.key == K_e:
						case_1 = image(case_1,4,"6")
						#image(case_1,4,"6")


					#Fait changer la couleur de la deuxieme case
					elif event.key == K_r:
						case_2 = image(case_2,5,"7")

					#Fait changer la couleur de la troisieme case
					elif event.key == K_t:
						case_3 = image(case_3,6,"8")

					#Fait changer la couleur de la quatrieme case
					elif event.key == K_y:
						case_ 4 = image(case_4,7,"9")

					#Enclenche la vérification de la combinaison du joueur et son affichage
					elif event.key == K_RETURN:
						print(masterCode)

						right = 0
						wrong = 0

						#On réunit les valeurs dans les cases afin de constituer un code à 4 chiffres (pouvant être identiques)
						challengerCode = str(case_1)+str(case_2)+str(case_3)+str(case_4)

						if life != 1:
							fenetre.blit(colorsList[case_1],(4*taille_sprite,line*taille_sprite))
							fenetre.blit(colorsList[case_2],(5*taille_sprite,line*taille_sprite))
							fenetre.blit(colorsList[case_3],(6*taille_sprite,line*taille_sprite))
							fenetre.blit(colorsList[case_4],(7*taille_sprite,line*taille_sprite))

						#Vérification du code entré
						for g in range(4):
							if challengerCode[g] in masterCode and challengerCode[g] is not masterCode[g]:
								wrong += 1

							if challengerCode[g] is masterCode[g]:
								right += 1

						#Affichage des carrés noirs/blancs
						if life != 1:
							for black in range(right):
								fenetre.blit(noir,((9+black)*taille_sprite,line*taille_sprite))

							for white in range(wrong):
								fenetre.blit(blanc,((9+right+white)*taille_sprite,line*taille_sprite))

						if right != 4:
							line += 1
							life -= 1
						else:
							#affichage de la reponse en haut
							fenetre.blit(colorsList[numberGenerator[0]],(152,32))
							fenetre.blit(colorsList[numberGenerator[1]],(192,32))
							fenetre.blit(colorsList[numberGenerator[2]],(232,32))
							fenetre.blit(colorsList[numberGenerator[3]],(272,32))

							#boucle pour stopper le jeu et visualiser la reponse
							while continuer_gagne:
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

											continuer_jeu = 0
											continuer_fin = 0

										elif event.key == K_RETURN:
											#fermer la boucle jeu et retourner au menu
											continuer_gagne=0
											continuer_jeu = 0

								pygame.display.flip()

							#chargement et affichage de l'image de victoire
							fond = pygame.image.load("Resized_gagne.png").convert()
							fenetre.blit(fond,(0,0))
							fenetre.blit(colorsList[numberGenerator[0]],(192,336))
							fenetre.blit(colorsList[numberGenerator[1]],(232,336))
							fenetre.blit(colorsList[numberGenerator[2]],(272,336))
							fenetre.blit(colorsList[numberGenerator[3]],(312,336))

						if life == 0: #si life=1 car c'est la que le joueur a effectué ces 10 essais
							#affichage de la reponse en haut
							fenetre.blit(colorsList[numberGenerator[0]],(152,32))
							fenetre.blit(colorsList[numberGenerator[1]],(192,32))
							fenetre.blit(colorsList[numberGenerator[2]],(232,32))
							fenetre.blit(colorsList[numberGenerator[3]],(272,32))

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

										#Fait revenir au menu
										if event.key == K_ESCAPE:

											continuer_jeu = 0
											continuer_fin = 0

										elif event.key == K_RETURN:
											#fermer la boucle jeu et retourner au menu
											continuer_perdu=0
											continuer_jeu = 0

								pygame.display.flip()

							#chargement et affichage de l'image de défaite
							fond = pygame.image.load("Resized_perdu.png").convert()
							fenetre.blit(fond,(0,0))
							fenetre.blit(colorsList[numberGenerator[0]],(182,358))
							fenetre.blit(colorsList[numberGenerator[1]],(222,358))
							fenetre.blit(colorsList[numberGenerator[2]],(262,358))
							fenetre.blit(colorsList[numberGenerator[3]],(302,358))

		pygame.display.flip()


	#BOUCLE DE FIN
	while continuer_fin:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met les variables
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == pygame.QUIT:

				continuer_accueil = 0
				continuer_jeu = 0
				continuer_fin=0
				continuer = 0

			elif event.type == KEYDOWN:
				#Retour au menu
				if event.key == K_ESCAPE:
					continuer_fin = 0

		pygame.display.flip()
pygame.quit()