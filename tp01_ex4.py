"""
Une compagnie d'assurance automobile propose à ses clients quatre familles
de tarifs identifiables par une couleur, du moins au plus onéreux :
    tarifs bleu, vert, orange et rouge.
Le tarif dépend de la situation du conducteur :
    - un conducteur de moins de 25 ans et titulaire du permis depuis moins
      de deux ans, se voit attribuer le tarif rouge, si toutefois
      il n'a jamais été responsable d'accident.
      Sinon, la compagnie refuse de l'assurer.
    - un conducteur de moins de 25 ans et titulaire du permis depuis
      plus de deux ans, ou de plus de 25 ans mais titulaire du permis
      depuis moins de deux ans a le droit au tarif orange s'il
      n'a jamais provoqué d'accident, au tarif rouge pour un accident,
      sinon il est refusé.
    - un conducteur de plus de 25 ans titulaire du permis depuis plus de
      deux ans bénéficie du tarif vert s'il n'est à l'origine d'aucun
      accident et du tarif orange pour un accident, du tarif rouge pour
      deux accidents, et refusé au-delà
    - De plus, pour encourager la fidélité des clients acceptés,
      la compagnie propose un contrat de la couleur immédiatement la plus
      avantageuse s'il est entré dans la maison depuis plus de cinq ans.
      Ainsi, s'il satisfait à cette exigence, un client normalement "vert"
      devient "bleu", un client normalement "orange" devient "vert",
      et le "rouge" devient "orange".

Ecrire l'algorithme permettant de saisir les données nécessaires
(sans contrôle de saisie) et de traiter ce problème.

  Données : - L'Age du conducteur
            - Le nombre d'année de permis
            - Le nombre d'accidents
            - Le nombre d'années d'assurance
  Résultats : Un message spécifiant la situation du client
"""

### Déclaration et Initialisation des variables

# Données
age_donnee: int = 25
permis_donnee: int = 2
pas_accident: int = 0
an_ass_max : int = 5
# user inpute
user_age: int = int(input("Entrez l'âge : "))  # damander à l'utilisateur son age
user_annee_permis: int = int(input(
    "Entrez le nombre d'année de permis : "))  # damander à l'utilisateur combien de temps qu'il a obtenu son permis
user_nb_accident: int = int(
    input("Entrez le nombre d'accident : "))  # damander à l'utilisateur s'il a déjà fait un accident
user_nb_annee_ass: int = int(
    input("Entrez le nombre d'année d'assurance : "))  # damander à l'utilisateur combien de temps qu'il est inscrit à l'assurance

situation: str = ""
attibution: str = ""

# initialisation des inputs
age = int(user_age)
annee_permis = int(user_annee_permis)
nb_accident = int(user_nb_accident)
nb_assurance = int(user_nb_annee_ass)

# type de tarifs
tarif_bleu: str = "Bleu"
tarif_vert: str = "Vert"
tarif_orange: str = "Orange"
tarif_rouge: str = "Rouge"

### Séquence d'opération

# première etape on test le npmbre d'ancienneté de l'assurré


if age < age_donnee and annee_permis < permis_donnee and nb_accident == pas_accident:
    attibution = tarif_rouge
if age < age_donnee and annee_permis >= permis_donnee or age >= age_donnee and nb_accident == pas_accident and annee_permis < permis_donnee:
    attibution = tarif_orange
if age < age_donnee and annee_permis >= permis_donnee or age >= age_donnee and nb_accident == 1 and annee_permis < permis_donnee:
    attibution = rouge
if age >= age_donnee and annee_permis >= permis_donnee and nb_accident == pas_accident :
    attibution = tarif_vert
if age >= age_donnee and annee_permis >= permis_donnee and nb_accident == 1 :
    attibution = tarif_orange
if age >= age_donnee and annee_permis >= permis_donnee and nb_accident > 1 :
    attibution = tarif_rouge


situation = attibution

# test si l'user est assuré depuis plus de 5 ans
if nb_assurance >= an_ass_max and attibution == tarif_vert:
    situation = tarif_bleu
elif nb_assurance >=  an_ass_max and attibution == tarif_orange:
    situation = tarif_vert
elif nb_assurance >=  an_ass_max and attibution == tarif_rouge:
    situation = tarif_orange



print("Votre situation : {} ".format(situation))
