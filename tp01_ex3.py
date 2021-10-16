"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1,
              le niveau de risque est faible. Sinon il est élevé.
"""
### Déclaration et Initialisation des variables

# user input variables
user_fumeur: str = input("Etes-vous fumeur ? (oui ou non ) ")  # demande utilisateur

user_sport: str = input("Faites-vous du sport ? (oui ou non ) ")  # demande utilisateur
user_sexe: str = (input("Quel est votre sexe ? "))
user_age: int = int(input("Quel est votre âge? "))
niveau_risque: int = 0

# Initialisation user input
fumeur = user_fumeur.upper()
sport = user_sport.upper()
sexe = user_sexe.upper()





### Séquence d'opération modif du niveau de risque

# test des risque
if fumeur == "OUI":
    niveau_risque += 2

if sport == "OUI":
    niveau_risque -= 1


if (user_age >= 50 and sexe == "H") or (user_age >= 60 and sexe == "F"):
    niveau_risque += 1



# résultat de niveau de risque
if niveau_risque <= 1:

    print("Le niveau de risque est faible ({})".format(niveau_risque))
else:
    print("Le niveau des risque est élevé ({})".format(niveau_risque))
