print("Demarrage 'API_lydia.py'")
from Requetes import *

#### Script usiné par Yavin 4µ78, Secret'ss Rezal 222, alias Néo ####

#### Fonction de vérification d'une transaction lydia ####

def Lydia_check(token_public,montant,phone,order_id,Qrcode):

    #Convertit les données scannées du qrcode en un format comprehensible pour la requête Json
    paymentData = json.dumps(Qrcode)

    # Les données à envoyer à l'API
    data = {
        'vendor_token': token_public,
        'amount': montant,
        'phone': phone,
        'order_id': order_id,
        'paymentData': paymentData,
        'currency': 'EUR'
    }

    # En production, assurez-vous que SSL est activé et correctement configuré.
    requests.packages.urllib3.disable_warnings()

    # Effectuer la requête POST
    response = requests.post(config_lydia.url, data=data, verify=False)

    # Vérifier la réponse
    if response.status_code == 200:
        # Convertir la réponse en JSON
        response_data = response.json()

        try :
            if response_data['error'] == "0":
                #Entrer_log("Logs_prg","Transaction lydia réussie")
                #Entrer_log("Logs_prg", "Identifiant de la transaction :"+ str(response_data['transaction_identifier']))
                return response_data['transaction_identifier']
            else :
                #Entrer_log("Logs_error","Erreur lors de la transaction :" + str(response_data['error']) + " : " + str(response_data['message']))
                print(str(response_data['error']) + " : " + str(response_data['message']))
                return None

        except Exception as e:
            print("Exception détectée : ",e)
            #Entrer_log("Logs_error","Erreur lors de la transaction :" + str(e))
            return None

    else:
        #Entrer_log("Logs_error","Erreur de requête HTTP :" + str(response.status_code))
        return None

