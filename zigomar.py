"""

Fonctions :
    1) import random : Permet d’utiliser les fonctions liées aux nombres aléatoires
    2) random.shuffle(liste) : Mélange aléatoirement les éléments d’une liste ---> Exemple : random.shuffle(sac) → la liste sac est mélangée
    3) random.choice(liste) : Retourne un élément aléatoire de la liste ---> Exemple : random.choice(sac) → choisit un objet au hasard dans sac

Objectif :

    1) Listes.

    2) Boucles.

    3) Fonctions.

    4) Chaînes de caractères.

TODO :

    A) Organiser le travail en modules
    B) Partager le projet sur GitHub avec l'équipe et l'enseignante


Équipier : Isaac Chrétien

https://projets420.gitbook.io/notes-de-cours/exercices-s1-s5/chasse-au-tresor-avec-zigomar

https://chat.mistral.ai/chat

"""

# ============================================================================
# PROJET ZIGOMAR - SAC MAGIQUE
# ============================================================================

import random

class couleuretstyle:  # Fait avec l'aide de StackOverflow
    Cyan = "\033[96m"
    Vert = "\033[92m"
    Rose = "\033[95m"
    Jaune = "\033[93m"
    Bold = "\033[1m"
    Underline = "\033[4m"
    Fin  = "\033[0m"

# ============================================================================
# MODULE 1: GESTION DU SAC
# ============================================================================

def initialiser_sac():
    """
    Cette fonction crée la liste initiale des objets que Zigomar a en main.

    Retourne une liste avec 4 objets de départ.
    Cette fonction initialise l'état de base du programme.
    """
    sac = ["potions scintillantes", "clés mystérieuses", "boules brillantes", "squelettes miniatures"]
    return sac


def afficher_sac(sac):
    """
    Cette fonction affiche le contenu du sac de manière structurée.

    Elle prend en paramètre la liste 'sac' et l'affiche avec une numérotation.
    Cette fonction permet la visualisation du contenu actuel du sac.
    """
    print(f"\n--- SAC DE ZIGOMAR ({len(sac)} objets) ---")

    if len(sac) == 0:
        print("Le sac est vide.")
    else:
        # Boucle for pour afficher chaque objet avec son numéro d'index
        for i in range(len(sac)):
            print(f"{i + 1}. {sac[i]}")

    print("---" + "-" * 30)


def ajouter_objet(sac, objet):
    """
    Cette fonction ajoute un nouvel objet dans le sac.

    Elle utilise la méthode append() pour ajouter l'élément à la fin de la liste.
    """
    sac.append(objet)
    print(f"Zigomar ajoute '{objet}' dans son sac.")


# ============================================================================
# MODULE 2: EXPLORATION ET COLLECTE
# ============================================================================

def partir_exploration():
    """
    Cette fonction simule une exploration où Zigomar découvre de nouveaux objets.

    Elle sélectionne aléatoirement des objets dans une liste prédéfinie.
    Cette fonction utilise le module random pour la génération aléatoire.
    """
    objets_possibles = [
        "épée rouillée", "grimoire ancien", "potion violette", "anneau doré",
        "parchemin mystique", "baguette magique", "pierre précieuse",
        "amulette protectrice", "dague enchantée", "carte au trésor",
        "pièce d'or", "plume d'ange", "bouclier miniature", "miroir magique",
        "sablier éternel", "couronne de fleurs", "bille7magique",
        "cobra en jade", "rubis brillant", "tablette2gravée"
    ]

    # Détermination aléatoire du nombre d'objets trouvés (entre 2 et 5)
    nombre_objets = random.choice([2, 3, 4, 5])
    objets_trouves = []

    # Boucle pour sélectionner les objets sans créer de doublons
    for i in range(nombre_objets):
        objet = random.choice(objets_possibles)
        # Vérification pour éviter les doublons dans la liste des objets trouvés
        if objet not in objets_trouves:
            objets_trouves.append(objet)

    return objets_trouves


def collecter_objets(sac, objets_trouves):
    """
    Cette fonction ajoute tous les objets trouvés dans le sac de Zigomar.

    Elle utilise une boucle for pour traiter chaque objet individuellement.
    Cette fonction coordonne l'ajout multiple d'objets au sac.
    """
    print(f"Zigomar revient d'exploration avec {len(objets_trouves)} nouveaux objets :")
    print(f"  {', '.join(objets_trouves)}")

    # Boucle pour ajouter chaque objet de la liste des objets trouvés
    for objet in objets_trouves:
        ajouter_objet(sac, objet)


# ============================================================================
# MODULE 3: SYSTÈME DE TRI
# ============================================================================

def sac_plein(sac):
    """
    Cette fonction vérifie si le sac contient 15 objets ou plus.

    Elle retourne une valeur booléenne (True si plein, False sinon).
    Cette fonction sert de condition pour déclencher le tri.
    """
    return len(sac) >= 15


def tri_automatique(sac):
    """
    Cette fonction retire automatiquement les objets contenant des chiffres ou la lettre b.
    """
    objets_retires = []
    nouveau_sac = []

    # Parcours de chaque objet présent dans le sac
    for objet in sac:
        contient_chiffre_ou_b = False

        # Examen de chaque caractère de l'objet courant
        for caractere in objet:
            # Test si le caractère est un chiffre OU la lettre 'b' (insensible à la casse)
            if caractere.isdigit() or caractere.lower() == 'b':
                contient_chiffre_ou_b = True
                break  # Sortie anticipée de la boucle

        # Classification de l'objet selon les critères de tri
        if contient_chiffre_ou_b:
            objets_retires.append(objet)
        else:
            nouveau_sac.append(objet)

    # Remplacement du contenu du sac original
    sac.clear()
    for objet in nouveau_sac:
        sac.append(objet)

    return objets_retires


def tri_manuel(sac):
    """
    Cette fonction demande à l'utilisateur d'écrire le nom exact de l'objet à retirer.

    L'utilisateur doit taper le nom complet de l'objet qu'il veut que Zigomar retire.
    Cette fonction gère la validation de la saisie et les cas d'erreur.
    """

    afficher_sac(sac)

    # Boucle de saisie avec validation jusqu'à obtenir un choix valide
    while True:
        objet_choisi = input("Écris le nom exact de l'objet à retirer : ").strip()

        # Vérifier si l'objet existe dans le sac
        objet_trouve = None
        for objet in sac:
            if objet.lower() == objet_choisi.lower():
                objet_trouve = objet
                break

        if objet_trouve:
            # Retirer l'objet du sac
            sac.remove(objet_trouve)
            print(f"\nZigomar retire '{objet_trouve}' en grognant furieusement :")
            print("'C'est de TA FAUTE si je perds mes objets précieux!'")
            print("'Tu m'as FORCÉE à abandonner ce trésor!'")
            return objet_trouve
        else:
            print(f"ERREUR: '{objet_choisi}' n'existe pas dans le sac!")
            print("Vérifiez l'orthographe et réessayez.")


def faire_tri(sac):
    """
    Cette fonction effectue TOUJOURS les deux types de tri dans l'ordre.

    D'abord le tri automatique, puis le tri manuel.
    Cette fonction coordonne les deux modes de tri obligatoires.
    """

    # PREMIER TRI : AUTOMATIQUE
    print(f"{couleuretstyle.Underline}{couleuretstyle.Bold}\nÉTAPE 2 : TRI AUTOMATIQUE{couleuretstyle.Fin}")
    print("\nZigomar retire automatiquement les objets avec la lettre b et/ou des numéros")
    objets_retires_auto = tri_automatique(sac)

    if len(objets_retires_auto) > 0:
        print(f"Objets retirés automatiquement : {', '.join(objets_retires_auto)}")
    else:
        print("Aucun objet ne correspond aux critères de suppression automatique.")


    # DEUXIÈME TRI : MANUEL
    if len(sac) > 0:
        print(f"{couleuretstyle.Underline}{couleuretstyle.Bold}\nÉTAPE 3 : TRI MANUEL{couleuretstyle.Fin}")
        print("\nChoisi un objet a retirer du sac.")
        objet_retire_manuel = tri_manuel(sac)


# ============================================================================
# MODULE 4: MINI-QUIZ
# ============================================================================

def melanger_sac(sac):
    """
    Cette fonction mélange aléatoirement l'ordre des objets dans le sac.

    Elle utilise random.shuffle() qui modifie la liste sur place.
    Cette fonction prépare le sac pour la sélection aléatoire d'un objet.
    """
    random.shuffle(sac)
    print("Mélange des objets du sac...")


def choisir_objet_aleatoire(sac):
    """
    Cette fonction sélectionne un objet au hasard dans le sac.

    Elle utilise random.choice() pour effectuer une sélection aléatoire.
    Cette fonction retourne un élément choisi aléatoirement.
    """
    return random.choice(sac)


def mini_quiz(sac):
    """
    Cette fonction lance le jeu de devinette de Zigomar.

    Elle mélange le sac, sélectionne un objet mystère, et simule la devinette.
    Cette fonction utilise une probabilité de 50% pour la réussite de Zigomar.
    """
    if len(sac) == 0:
        print("Le sac est vide. Impossible de lancer le quiz.")
        return

    print("\n=== MINI-QUIZ DE ZIGOMAR ===")

    # Préparation du quiz : mélange et sélection de l'objet mystère
    melanger_sac(sac)
    objet_mystere = choisir_objet_aleatoire(sac)

    print("Tu attrapes un objet au hasard.")
    print("Zigomar ferme les yeux et se concentre.")

    # Simulation de la devinette avec probabilité équiprobable
    reussit = random.choice([True, False])

    if reussit:
        print(f"Zigomar : C'est le/la {objet_mystere}!")
        print("SUCCÈS : Elle a deviné juste! Zigomar saute de joie et te remercie.")
    else:
        # Construction d'une liste d'alternatives pour une réponse incorrecte
        autres_objets = []
        for objet in sac:
            if objet != objet_mystere:
                autres_objets.append(objet)

        # Génération d'une réponse incorrecte
        if len(autres_objets) > 0:
            mauvaise_reponse = random.choice(autres_objets)
            print(f"Zigomar : C'est le/la {mauvaise_reponse}?")
        else:
            print("Zigomar : C'est... euh... quelque chose d'autre?")

        print(f"ÉCHEC : La réponse était '{objet_mystere}'")
        print("Zigomar te lance un regard noir et grogne : 'Grrrr...")


# ============================================================================
# MODULE 5: TRI ALPHABÉTIQUE
# ============================================================================

def trier_alphabetique(sac):
    """
    Cette fonction trie tous les objets du sac par ordre alphabétique.
    """

    # Sauvegarde de l'ordre original pour comparaison
    sac_avant = []
    for objet in sac:
        sac_avant.append(objet)

    # Exécution du tri alphabétique
    sac.sort()

    # Vérification des changements
    ordre_change = False
    for i in range(len(sac)):
        if sac[i] != sac_avant[i]:
            ordre_change = True
            break

    # Rapport du résultat
    if ordre_change:
        print("\nTri alphabétique effectué avec succès.")
    else:
        print("Les objets étaient déjà correctement triés.")


# ============================================================================
# PROGRAMME PRINCIPAL
# ============================================================================

def main():

    # Initialisation du sac avec les objets de base
    sac = initialiser_sac()
    print("\nDébut de la chasse au trésor.")

    # PHASE D'EXPLORATION AUTOMATIQUE
    jour = 1
    print(f"{couleuretstyle.Rose}{couleuretstyle.Bold}\n{'=' * 60}")
    print("PHASE D'EXPLORATION AUTOMATIQUE")
    print(f"{couleuretstyle.Rose}{couleuretstyle.Bold}={couleuretstyle.Fin}" * 60)

    # Boucle d'exploration jusqu'à ce que le sac soit plein
    while not sac_plein(sac):
        print(f"\n--- JOUR {jour} - EXPLORATION ---")

        # Exploration automatique
        print("Zigomar part explorer de nouveaux lieux...")
        objets_trouves = partir_exploration()

        # Collecte des objets
        collecter_objets(sac, objets_trouves)

        jour += 1

    # PHASE DE TRI
    print(f"{couleuretstyle.Vert}{couleuretstyle.Bold}\n{"=" * 60}")
    print("PHASE DE TRI")
    print(f"{couleuretstyle.Vert}{couleuretstyle.Bold}={couleuretstyle.Fin}" * 60)
    print(f"{couleuretstyle.Underline}{couleuretstyle.Bold}\nÉTAPE 1 : Verification du nombre d'objets{couleuretstyle.Fin} ")
    print("\nLe sac contient plus que 15 objets!")

    faire_tri(sac)
    print("\nÉTAT DU SAC APRÈS LE TRI :")
    afficher_sac(sac)

    # PHASE DE QUIZ
    print(f"{couleuretstyle.Jaune}{couleuretstyle.Bold}\n{"=" * 60}")
    print("PHASE DE QUIZ")
    print(f"{couleuretstyle.Jaune}{couleuretstyle.Bold}{"=" * 60}{couleuretstyle.Fin}")

    mini_quiz(sac)

    # PHASE DE TRI FINAL
    print(f"{couleuretstyle.Cyan}{couleuretstyle.Bold}\n{'=' * 60}")
    print("PHASE DE TRI FINALE")
    print(f"{couleuretstyle.Cyan}{couleuretstyle.Bold}={couleuretstyle.Fin}" * 60)

    trier_alphabetique(sac)

    print("\nINVENTAIRE FINAL :")
    afficher_sac(sac)

# ============================================================================
# POINT D'ENTRÉE
# ============================================================================

if __name__ == "__main__":
    main()