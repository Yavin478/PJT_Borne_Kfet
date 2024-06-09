print("Demarrage 'LOG.py'")
from config import *

#### Script modifié par Yavin 4µ78, Secret'ss Rezal 222, alias Néo ####
def LOG_add(fichierName,contenu):
    _tmp=open(fichierName,"a")
    _tmp.write(str(contenu))
    _tmp.close()


def Entrer_log (nom_fichier_log,contenu):   # Toutes les variables en str
    os.makedirs(nom_fichier_log, exist_ok=True)
    now=ctime()
    LOG_add(setting.projet_path+config.repo+'/'+nom_fichier_log,"At: "+str(now)+":"+contenu+"\n")
