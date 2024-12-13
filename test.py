"""Programme qui permet de tester si un nombre est porte-bonheur"""

# Déclaration des variables
nbr_utilisateur: int = None

# Demandez un nombre entier plus grand que 10
nbr_utilisateur = int(input("Veuillez un nombre plus grand que 10 : "))

# Si le nombre n'est pas plus grand que 10
if nbr_utilisateur <= 10:
    print("Veuillez entrer un nombre plus grand que 10.")
else:
    # Fonction pour calculer le carré de chaque chiffre
    def carre_chiffres(nbr_utilisateur: int) -> int:
        chiffres = [int(chiffre) for chiffre in str(nbr_utilisateur)]
        for chiffre in chiffres:
            print(f"{chiffre}^2={chiffre**2}")

    # Fonction pour afficher les étapes intermédiaires
    def afficher_etapes(nombre: int, carrés: list) -> None:
        chiffres = [int(chiffre) for chiffre in str(nombre)]
        for i in range(len(chiffres)):
            print(f"{chiffres[i]}^2={chiffres[i]**2}")
        print(f"Nouveau nombre : {' + '.join(map(str, carrés))} = {sum(carrés)}")

    # Fonction pour calculer la somme des carrés
    def somme_carres(nbr_utilisateur: int) -> int:
        carrés = [int(chiffre) ** 2 for chiffre in str(nbr_utilisateur)]
        afficher_etapes(nbr_utilisateur, carrés)
        return sum(carrés)

    # Vérifier si le nombre est un nombre porte-bonheur
    while nbr_utilisateur > 10:
        nbr_utilisateur = somme_carres(nbr_utilisateur)

    # Afficher le résultat final
    if nbr_utilisateur == 1:
        print("Le nombre est un nombre porte-bonheur !")
    else:
        print("Le nombre n'est pas un nombre porte-bonheur.")
