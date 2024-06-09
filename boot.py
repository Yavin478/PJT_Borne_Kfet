print("Démarrage 'boot.py'")

from Main_affichage import *

Entrer_log("Logs_prg", "Démarage Programe")

if config.debugging :
    print("Attente de 3s")
    sleep(3)

root=MainApp()
root.mainloop()
