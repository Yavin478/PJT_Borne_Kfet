print("Démarrage 'test.py'")

from main_lydia import *

Qrcode=["EHkA/Jg5u2AlGj4k8XPQswZNhvoGJCfK/N6I2VGsCarS9fZfMspyPfdUy1vzMSNhkcxGrFAUCOvw4ecV7t/rVKGNXzY7bFKbyeT0XRk03S2oVYdPdsiMGlbuPgRJUu9VAQXrzfYg4C5FRANBSQHVLZGodTI7WScszClgi9olzzQ=","3"]
blairal='0656683461'
montant=4

result=SQL_SELECT(QUERRY_getUser(blairal))
bucque=result[0][1]
users_id=result[0][0]
print("User : ",bucque, "Id : ", users_id)

if Transaction_Lydia(users_id, montant, Qrcode, config_lydia.token_public, config_lydia.phone) :
    print('Ok')
else:
    print('pas ok')


# print(Lydia_check(config_lydia.token_public,montant,config_lydia.phone,1,Qrcode))