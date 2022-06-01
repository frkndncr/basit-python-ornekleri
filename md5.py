import hashlib
import os
os.system("clear")
print("""
+++++++++++++++++++++++++++++++
+                             +
+                             +
+          1. MD5 OLUŞTUR     +
+                             +
+++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++
+                             +
+                             +
+          2. MD5 KIR         +
+                             +
+++++++++++++++++++++++++++++++
""")
veri = input("Islem Numarasini Girin : ")
if (veri =="1"):
        
    user = input("YAZIYI GİR :  ")
    h = hashlib.md5(user.encode())
    h2 = h.hexdigest()        
    print(h2)
                     
if (veri =="2"):
                            
    wlist = input("wordlist: ")
    hash2crack = input("hash: ")
    wlistlines = open(wlist, "r").readlines()
                
                                              
    for i in range(0, len(wlistlines)):
                                          
        hash2comp = hashlib.md5(wlistlines[i].replace(           
                "\n", "").encode()).hexdigest()        
                               
        if hash2crack == hash2comp:                                                       
            print("password found: "+wlistlines[i].replace("\n", ""))                               
            exit()                              
            print("password not found")