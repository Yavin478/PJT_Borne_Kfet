print("Démarrage 'config.py'")
from setting import *

#### Script modifié par Yavin 4µ78, Secret'ss Rezal 222, alias Néo ####
class config:  # Définition des variables reliée à l'objet config définissant les paramètres de la borne

    # Montant en euros minimal à pouvoir mettre pendant une transaction
    minMontant = 1
    # Montant en euros max à pouvoir être rechargé en une opération
    maxTransaction = 99
    # Montant en euros maximal à pouvoir être mis sur un compte
    maxMontant = 150

    # Nom du repo utilisé
    repo="PJT_Borne_Kfet"

    # Périphérique USB
    name_scan="BF SCAN SCAN KEYBOARD"
    name_keyboard= "Barcode Reader"

    # pour avoir des affichages dans la console pour savoir à où le code en est
    debugging = False
