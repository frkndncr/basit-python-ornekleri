başlık="""
####################################################
#                                                  #
#    HESAP MAKİNESİ UYGULAMASINA HOŞ GELDİNİZ!!!   #
#                                                  #
#                                                  #
#                                                  #
#       PROGRAMDA KULLANILAN DİL : PYTHON3.X       #
#                                                  #
####################################################
"""
print(başlık)

işlemler="""
(1) Toplama İşlemi\t +

(2) Çıkarma İşlemi\t -

(3) Çarpma İşlemi\t *

(4) Bölme İşlemi\t /

(5) Kuvvet Hesapmala\t **

(6) Karekök Hesaplama\t √
"""
print(işlemler)

while True:
    soru=input("Lütfen yapmak istediğiniz işlem numarasını giriniz(Çıkmak için X):\t")
    if soru=="X":
        print("Uygulamadan çıkılıyor...")
        break
    elif soru=="1":
        t1=input("İlk sayıyı giriniz:\t")
        t2=input("İkinci sayıyı giriniz:\t")
        try:
            t_1=int(t1)
            t_2=int(t2)
            print(t_1+t_2)
        except ValueError:
            print("Lütfen sadece sayı giriniz!!!")
    elif soru=="2":
        c1=input("İlk sayıyı giriniz:\t")
        c2=input("İkinci sayıyı giriniz:\t")
        try:
            c_1=int(c1)
            c_2=int(c2)
            print(c_1-c_2)
        except ValueError:
            print("Lütfen sadece sayı giriniz!!!")
    elif soru=="3":
        p1=input("İlk sayıyı giriniz:\t")
        p2=input("İkinci sayıyı giriniz:\t")
        try:
            p_1=int(p1)
            p_2=int(p2)
            print(p_1*p_2)
        except ValueError:
            print("Lütfen sadece sayı giriniz!!!")
    elif soru=="4":
        b1=input("Bölünen sayıyı giriniz:\t")
        b2=input("Bölen sayıyı giriniz:\t")
        try:
            b_1=int(b1)
            b_2=int(b2)
            print(b_1/b_2)
        except ValueError:
            print("Lütfen sadece sayı giriniz!!!")
        except ZeroDivisionError:
            print("Sıfır Bölüm Hatası : Sayıları sıfıra bölemezsiniz!!!")
    elif soru=="5":
        k1=input("Hesaplanılacak sayıyı giriniz:\t")
        k2=input("Hesaplanacak kuvveti giriniz:\t")
        try:
            k_1=int(k1)
            k_2=int(k2)
            print(k_1**k_2)
        except ValueError:
            print("Lütfen sadece sayı giriniz!!!")
    elif soru=="6":
        r1=input("Hesaplanacak sayıyı giriniz:\t")
        try:
            r_1=int(r1)
            print(r_1**0.5)
        except ValueError:
            print("Lütfen sadece sayı giriniz!!!")
