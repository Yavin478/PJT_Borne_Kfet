print("Demarrage 'Requetes.py'")
from SQL import *

#### Script usiné par Yavin 4µ78, Secret'ss Rezal 222, alias Néo ####

#### Définition des requêtes SQL ####

# Préparation BDD
def QUERRY_getIdLydia(users_id, date):
    return (("SELECT id FROM consos_lydia WHERE users_id='{}' AND date= '{}';").format(users_id, date))

def QUERRY_getUser(blairal):
    return (("SELECT * FROM users WHERE blairal= '{}' AND deleted=0;").format(blairal))

def QUERRY_setIdLydia(montant, users_id, date):
    return (("INSERT INTO consos_lydia (montant, users_id, date) VALUES ('{}','{}','{}');").format(montant, users_id, date))

# Récupère la date courante, mesurée en secondes depuis le début de l'époque UNIX, (1er janvier 1970 00:00:00 GMT)
def QUERRY_getTimeUnix():
    return (("SELECT UNIX_TIMESTAMP();"))

# Récupère la date courante de la BDD (ex : 2024-06-08 18:42:36)
def QUERRY_getTime():
    return (("SELECT Now();"))

# Finalisation BDD

def QUERRY_getCredit(users_id):
    return (("SELECT credit FROM users WHERE id= '{}' AND deleted=0;").format(users_id))
def QUERRY_setCredit(users_id, new_montant):
    return (("UPDATE users SET credit='{}'WHERE id='{}'").format(new_montant, users_id))
def QUERRY_setConsos(users_id, montant, date):
    return (("INSERT INTO consos (en_attente_de_livraison, users_id, consomateur_id, produits_id, date, admins_id, montant, quantite ) VALUES ('{}','{}',NULL,'{}','{}','{}','{}','{}');").format(0, users_id, 3222, date, 179, montant, 1))

def QUERRY_getIdConsos(users_id, date):
    return (("SELECT id FROM consos WHERE users_id='{}' AND date='{}';").format(users_id, date))

def QUERRY_setConsosLydia(order_id,id_consos,transaction_identifier):
    return (("UPDATE consos_lydia SET id_consos='{}', transaction_identifier='{}'WHERE id='{}'").format(id_consos,transaction_identifier,order_id))

def QUERRY_setLogCreditUpdate(date, users_id, montant_avant, montant_apres):
    return (("INSERT INTO log_credit_update (date, id_user, montant_avant, montant_apres) VALUES ('{}','{}','{}','{}');").format(date, users_id, montant_avant, montant_apres))