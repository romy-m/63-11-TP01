"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Sandwich au poulet à 4.90
           - Chips paprika à 2.50
           - Barre chocolat à 2.00
           - Bonbons à 3.30
           - Ice Tea à 2.20
           - Limonade à 1.90
 Résultats : - Un message confirmant ou annulant la transaction
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant un bon appétit/santé
"""

### Déclaration et Initialisation des variables
nom_produit: str = ""
rendue: float = 0


nom_pUn: str = " Sandwich au poulet "
nom_pDeux: str = " Chips paprika"
nom_pTrois: str = " Barre chocolat "
nom_pQuatre: str = " Bonbons "
nom_pCinqu: str = " Ice Tea "
nom_pSix: str = " Limonade "

un : int = 1
deux : int = 2
trois : int = 3
quatre : int = 4
cinq : int = 5
six: int = 6

un_sandwichPolet : float = 4.90
deux_chiosPap : float = 2.50
trois_barreChoc : float = 2.00
quatre_bonbons : float = 3.30
cinque_iceTea : float = 2.20
six_limonade : float = 1.90
### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :") # choix de produit
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")

user_monnaie = input("Veillez introduire votre monnaie : ") # recolter donnée user monnaie introduite
user_produit= input("Veillez selectionner un produit : ")  #récolter donnée user choix produit

monnaie = float (user_monnaie) # conversation des donnée en float
num_produit = int (user_produit) # convertion des données en int

# choix de produit et calcule rendue monnaie ou pas si l'argent ne suffit pas

if monnaie < un_sandwichPolet or monnaie < deux_chiosPap or monnaie < trois_barreChoc or monnaie < quatre_bonbons or monnaie < cinque_iceTea or monnaie < six_limonade:
    print("La monnaie est insuffisante")
else:
    if num_produit == un and monnaie > un_sandwichPolet :
        nom_produit = nom_pUn
        rendue = monnaie - un_sandwichPolet
    elif num_produit == deux and monnaie > deux_chiosPap:
        nom_produit = nom_pDeux
        rendue = monnaie - deux_chiosPap
    elif num_produit == trois and monnaie > trois_barreChoc:
        nom_produit = nom_pTrois
        rendue = monnaie - trois_barreChoc
    elif num_produit == quatre and monnaie > quatre_bonbons:
        nom_produit = nom_pQuatre
        rendue = monnaie - quatre_bonbons
    elif num_produit == cinq and monnaie > cinque_iceTea:
        nom_produit = nom_pCinqu
        rendue = monnaie - cinque_iceTea
    elif num_produit == six and monnaie > six_limonade:
        nom_produit = nom_pSix
        rendue = monnaie - six_limonade

# message de sorti après interaction avec l'utilisateur
if nom_produit == nom_pCinqu :
    print("Monnaie à rendre : {:.2f} ".format(rendue))
    print("{} servie ! Santé}".format(nom_produit))
elif nom_produit == nom_pSix:
    print("Monnaie à rendre : {:.2f} ".format(rendue))
    print("{} servi ! Santé".format(nom_produit))
elif nom_produit == deux_chiosPap:
    print("Monnaie à rendre : {:.2f} ".format(rendue))
    print("{} servies ! Bon appétit}".format(nom_produit))
elif nom_produit == trois_barreChoc:
    print("Monnaie à rendre : {:.2f} ".format(rendue))
    print("{} servie ! Bon appétit}".format(nom_produit))
elif nom_produit == quatre_bonbons:
    print("Monnaie à rendre : {:.2f} ".format(rendue))
    print("{} servis ! Bon appétit}".format(nom_produit))
elif nom_produit == un_sandwichPolet:
    print("Monnaie à rendre : {:.2f} ".format(rendue))
    print("{} servis ! Bon appétit}".format(nom_produit))
else:
    print("Monnaie à rendre : {:.2f} ".format(rendue))
    print("{} servi ! Bonne appétit".format(nom_produit))





