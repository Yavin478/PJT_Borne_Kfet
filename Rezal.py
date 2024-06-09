print("Demarrage 'REZAL.py'")
from LOG import *

def REZAL_ping(IP):
    try:
        return int(os.system("ping -a -c 1 -W 1 "+str(IP))==0)
    except:
        return False

def REZAL_pingServeur():
    try:
        return REZAL_ping(setting.connection["host"])
    except:
        return False

def REZAL_pingInternet():
    try:
        return REZAL_ping(setting.serveurNet)
    except:
        return False

def REZAL_getIP():
    try:
        a = str(subprocess.check_output("hostname -I",shell=True).decode('utf-8')).split(" ")[0]
        if a == "\n":
            raise ValueError
        return a
    except:
        return '0.0.0.0'

def REZAL_connect(IP):
    env.host_string=IP
    env.user=setting.connection['user']
    env.password=setting.connection['password']
    env.sudo_user=setting.connection['user']
    env.sudo_password=setting.connection['password']

def REZAL_disconnect():
    disconnect_all()

def REZAL_download(chemin):
    get(chemin,chemin)

def REZAL_getMAC():
    for root,dirs,files in os.walk('/sys/class/net'):
        for dir in dirs:
            if dir[:3]=='enx' or dir[:3]=='eth':
                MAC=open('/sys/class/net/%s/address' %dir).read()[0:17]
    return MAC


def REZAL_restart():
    os.system("sudo python3"+setting.projet_path+config.repo+"/boot.py")
    sys.exit()

def REZAL_reboot():
    os.system("sudo reboot")
    sys.exit()

def REZAL_exit():
    sys.exit()

