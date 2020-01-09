# Python software fait avec Visual Studio code, Pygame, GitBash

# Introduction
C'est un jeu en 2D dans lequel le joueur incarne MacGyver. 
Il est enfermé dans un labyrinthe dans lequel il y a une seule sortie laquelle est tenue par un gardien. 
MacGyver doit réunir trois objets pour créer une seringue afin d'endormir le gardien.
Sinon il perd

# Prérequis : 
https://github.com/Keazu/projet-3
Python 3.8

# Installation et utilisation de VirtualEnv
Dans l'invite de commandes écrire ceci:
	pip install virtualenv
	
# Création et atcivation d'un environnement virtuel
	cd <chemin du dossier>
	virtualenv -p python3 env
	#Avec un Mac ou Linux
	source /env/bin/activate
	#Avec un PC
	source env/Scripts/activate
	
# Installation des dépendances (Pygame) dans l'environnement virtuel
	pip install -r requirements.txt
	
# Lancement du jeu
	python3 game.py