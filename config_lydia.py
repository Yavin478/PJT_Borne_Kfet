print("Demarrage 'config_lydia.py'")
from setting import *
import mysql.connector
import json
from time import *
import requests

#from STRING import *

#### Fichier de définitions des TOKENS et numéro de téléphone utilisé pour les transactions ####
# Décommentez l'url adéquat selon l'utilisation de la borne #
# Décommentez le token adéquat selon l'utilisation de la borne #
# Le numéro de phone utilisé doit être le numéro d'un caissier du compte lydia d'encaissement #

class config_lydia :
    # L'URL de l'API pour initier une transaction (remplacer par l'URL de test ou de production selon le cas)
    #url = "https://lydia-app.com/api/payment/payment.json"   # Production
    url = "https://homologation.lydia-app.com/api/payment/payment.json"    # Test

    # TOKENS DE TEST pour le site Kfet
    token_public = "58ada276ab575970477137" #pour les appels
    #token_prive = "58ada276ad930951358751" #pour la signature

    # TOKENS DE PRODUCTION pour le site Kfet
    #token_public = "56b21e42103d7715736202" #pour les appels
    #token_prive = "56b21e4212e2b468320228" #pour la signature


    # Numéro de téléphone du caissier enregistré pour les rechargements Kfet
    #phone = '33782977418' # Phone d'un gripss O 223
    phone = '33632994795'  # Phone d'un gripss O 222

    #phone = '330648809845' # Phone de test d'un ancien gripss O
    #phone = '330648927501' # Phone d'un ancien gripss O
