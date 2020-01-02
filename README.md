#Utilisation de GitHub, VirtualEnv, et GitBash
Installer GitBash ou utiliser l'invite de commandes 

#Télécharger ceci 
https://github.com/Keazu/projet-3

# Installation et utilisation de VirtualEnv
Dans GitBash ou l'invite de commandes écrire ceci:
	pip install virtualenv
	
# Création et atcivationd'un environnement virtuel
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
	
# HAVE FUN, No Bugs Certificated