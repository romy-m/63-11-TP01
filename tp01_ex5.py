"""
Programme de calcul du prix d'un billet de cinéma selon plusieurs rabais possible.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais membre : 3chf
    Forfait famille : 1chf
    Carte mensuelle : L'entrée est gratuite

Indications :
    - Il est possible de bénéficier d'un rabais membre et étudiant en même temps
    - Il n'est pas possible de bénéficier d'un rabais famille et étudiant
    - Il est possible de bénéficier d'un rabais membre et famille
    - Il est possible d'avoir une carte mensuelle permettant
      l'accès gratuitement à ce film
    - Si une personne possède la carte membre et étudiante ainsi que le rabais famille,
      le rabais membre et étudiant s'applique (car le rabais étudiant est plus grand)

Contrainte : Si la personne possède la carte mensuelle,
             il ne faut pas lui demander d'autres informations."
"""
### Déclaration et Initialisation des variables
prix_base : int = 10
rabais_e : int = 2
rabais_m : int = 3
forfait_f : int = 1
prix_a_payer : int = 0

# input user
c_m = input("Possédez-vous la carte mensuelle ? (oui ou non ) ")



### Séquence d'opération

if c_m.upper() == "OUI":# test si user utilise une carte memebre
    prix_a_payer = 0
    print("Le prix à payer est : {} CHF".format(prix_a_payer))
else:# test si user n'as pas de carte membre
    c_membre = input("Possédez-vous la carte membre?  (oui ou non ) ")
    c_e = input("Possédez-vous la carte étudiante ? (oui ou non ) ")
    f_f = input("Bénéficiez-vous du forfait famille ? (oui ou non ) ")

    # transformation de saisie
    membre = c_membre.upper()
    ce = c_e.upper()
    ff = f_f.upper()

    # calcul le prix à payer
    if membre == "OUI" and ce == "OUI" or membre == "OUI" and ff == "OUI" and ce:
        prix_a_payer = prix_base - rabais_m - rabais_e
    elif membre == "OUI" and ff == "OUI":
        prix_a_payer = prix_base - rabais_m - forfait_f

    print("Le prix à payer est {} CHF ".format(prix_a_payer))
