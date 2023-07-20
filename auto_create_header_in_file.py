################################################################################
# Script Name: auto_header.py
# Description: Description du script.
#
# Created by: Martin Lechêne
# Date: 19/07/2023
# Version: 1.0
#
import os
import time

# Chemin vers le dossier courant
dossier_courant = "."

# Chemin vers le fichier de sauvegarde
fichier_sauvegarde = "fichiers_traites.py"

# Liste pour stocker les noms de fichiers déjà traités
fichiers_traites = []

# Vérifier si le fichier de sauvegarde existe déjà
if os.path.isfile(fichier_sauvegarde):
    # Charger les noms de fichiers déjà traités à partir du fichier de sauvegarde existant
    with open(fichier_sauvegarde, "r") as f:
        lignes = f.readlines()
        fichiers_traites = [ligne.strip() for ligne in lignes]

# Ouvrir le fichier de sauvegarde en mode ajout pour ajouter les nouveaux noms de fichiers traités
fichier_sauvegarde_mode_ajout = open(fichier_sauvegarde, "a")

# Parcourir tous les fichiers et dossiers dans le dossier courant
for dossier, sous_dossiers, fichiers in os.walk(dossier_courant):
    for fichier in fichiers:
        chemin_fichier = os.path.join(dossier, fichier)

        # Vérifier si le fichier est un fichier Python (.py)
        if fichier.endswith(".py"):
            # Vérifier si le fichier a déjà été traité
            if fichier in fichiers_traites:
                print("Le fichier", chemin_fichier, "a déjà été traité. Passage au fichier suivant.")
                continue

            # Vérifier si le fichier a déjà un en-tête
            with open(chemin_fichier, "r") as f:
                lignes = f.readlines()

            if len(lignes) > 0 and lignes[0].startswith("# Script Name:"):
                print("Le fichier", chemin_fichier, "a déjà un en-tête. Passage au fichier suivant.")
                fichiers_traites.append(fichier)
                continue

            # Créer un en-tête par défaut
            entete = [
                "################################################################################\n",
                f"# Script Name: {fichier}\n",
                "# Description: Description du script.\n",
                "#\n",
                f"# Created by: Martin Lechêne\n",
                f"# Date: {time.strftime('%d/%m/%Y')}\n",
                "# Version: 1.0\n",
                "#\n",
            ]

            # Lire le contenu existant du fichier
            with open(chemin_fichier, "r") as f:
                contenu = f.readlines()

            # Concaténer l'en-tête avec le contenu existant
            nouveau_contenu = entete + contenu

            # Écrire le nouveau contenu dans le fichier
            with open(chemin_fichier, "w") as f:
                f.writelines(nouveau_contenu)

            print("Un en-tête a été ajouté au fichier:", chemin_fichier)

            # Ajouter le nom du fichier traité à la liste des fichiers traités
            fichiers_traites.append(fichier)

# Écrire les noms de fichiers traités dans le fichier de sauvegarde
fichier_sauvegarde_mode_ajout.writelines([fichier + "\n" for fichier in fichiers_traites])

# Fermer le fichier de sauvegarde
fichier_sauvegarde_mode_ajout.close()
