import random
import string
print("""
...............................
-----------ŞİFRE YARATICI-----------
...............................
      """)
def şifre_oluşturucu(length, level, output=[]):
    chars = string.ascii_letters
    if  level > 1:
        chars = "{}{}".format(chars, string.digits)
    if level > 2:
        chars = "{}{}".format(chars, string.punctuation)
    
    for i in range(length):
        output.append(random.choice(chars))
    
    return "".join(output)

print(("__" * 10) + "\n GÜVENLİ ŞİFRE OLUŞTURCU \n" + ("__" * 10))

şifre_uzunluk = int(input("UZUNLUK: "))
şifre_zorluk = int(input("ZORLUK: "))

şifre = şifre_oluşturucu(şifre_uzunluk, şifre_zorluk)
print("\n ŞİFRECİĞİN : {}".format(şifre))