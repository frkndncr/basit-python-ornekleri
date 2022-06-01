import time
from socket import *

def banner():
        print("""
###########################################################

#------------------PORT SCAN V 1.0-----------------------#

#--------------------------------------------------------#

###########################################################
""")
        
def scan():
        
        if __name__ == '__main__':
                hedef=input("Hedef: ")
                hedef_ip=gethostbyname(hedef)
                print("taranıyor:",hedef_ip)
                time.sleep(0.1)
                for i in range(655):#Mevcut 6555 ayarında tüm portları teker teker tarayacaktır.
#Değiştirmek  için taranmasını istediğiniz port aralığını yazınız örneğin 50.porttan 60.portun arasındaki 
#Portları tarayacaksanız for i in range(50,60) şeklinde düzenleyebilirsiniz.
                                time.sleep(0.5)
                                baglantı=socket(AF_INET,SOCK_STREAM)
                                port_tarama=baglantı.connect_ex((hedef_ip,i))
                                if(port_tarama==0):
                                        print("Açık port: %d " %(i))
                                baglantı.close()
        input("tarama sonlandırıldı.")

banner()
scan()
