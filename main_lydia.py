print("Demarrage 'main_lydia.py'")
from API_lydia import *

#### Programme principale de la transaction lydia avec MAJ BDD ####
def Recharge_credit(users_id, montant_avant, montant):
    SQL_EXECUTE(QUERRY_setCredit(users_id, montant+montant_avant))

def Transaction_Lydia(users_id, montant, Qrcode, token_public, phone):

    # 1) Récupération de la date courrante et insertion de l'id de la transaction à effectuer
    current_date = SQL_SELECT(QUERRY_getTimeUnix())[0][0]
    SQL_EXECUTE(QUERRY_setIdLydia((-1)*montant, users_id, current_date))

    # 2) Récupération de l'id de cette transaction
    order_id = SQL_SELECT(QUERRY_getIdLydia(users_id, current_date))[0][0]

    # 3) Vérification de la transaction avec l'API lydia
    transaction_identifier = Lydia_check(token_public, montant, phone, order_id, Qrcode)
    #print("Transaction identifiant : ", transaction_identifier)

    # 4) Si paiement validé (check != None): MAJ montant de la carte BDD et table lydia
    if transaction_identifier:
        # MAJ credit user
        montant_avant = SQL_SELECT(QUERRY_getCredit(users_id))[0][0]
        Recharge_credit(users_id, montant_avant, montant)

        # Insertion de la conso dans la BDD
        date_consos = SQL_SELECT(QUERRY_getTimeUnix())[0][0]
        SQL_EXECUTE(QUERRY_setConsos(users_id, (-1)*montant, date_consos))

        # MAJ de la ligne consos lydia crée
        id_consos = SQL_SELECT(QUERRY_getIdConsos(users_id, date_consos))[0][0]
        SQL_EXECUTE(QUERRY_setConsosLydia(order_id,id_consos,transaction_identifier))

        # Insertion du log de MAJ du credit de l'user
        date_log= SQL_SELECT(QUERRY_getTime())[0][0]
        QUERRY_setLogCreditUpdate(date_log, users_id, montant_avant, montant_avant+montant)

        #Entrer_log(setting.projet_path, "Logs_prg", "Mise à jour de la BDD effectuée avec succès")
        return True

    # 5) Si paiement refusé
    else:
        #Entrer_log(setting.projet_path, "Logs_error", "Problème survenu lors de la transaction")
        return False


