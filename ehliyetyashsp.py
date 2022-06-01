yas = input('Yaşınızı Giriniz : ')
 
#Kullanıcıdan cinsiyeti isteniyor
cinsiyet = input('Cinsiyetini Giriniz : ')
 
#Yaşının en az 20 ve cinsiyetinin erkek olup olmadığını kontrol ediyoruz.
 
if(int(yas)>19 and (cinsiyet=="E" or cinsiyet=="e" or cinsiyet=="erkek" or cinsiyet=="Erkek" or cinsiyet=="ERKEK")):
     print("Ehliyet alma şartlarına sahipsiniz.")
else:
     print("Ehliyet alma şartlarına sahipsiniz değilsiniz.")