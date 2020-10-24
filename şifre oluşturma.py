# MUSTAFA DAĞ - 19010011042
print("****ŞİFRELEME METODU****")
deger=None
harfler="a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","ş","s","t","y","u","v","y","z"
şifre=input("şifrenizi giriniz:")
for i in range(10):

   if şifre.center(5):  #center() metodu bir karakter dizisini iki yana yaslamak için kullanılır.
           print(şifre)

   if şifre.startswith(str(i)):
            print("şifre rakam ile başlayamaz")
            print("!!!!!")
            break
   elif şifre.endswith(str(i)):
         print("şifre rakam ile bitemez")
         print("!!!!!")
         break
   if şifre.islower():
          print("şifre küçük harflerden oluşamaz!!!!")
          break
   elif şifre.isupper():
           print("şifre tamamen büyük harflerden oluşamaz!!!")
           print("lütfen dikkat edin")
           break
   if şifre.istitle() and şifre.endswith(str(i)):
            print("BÜY")




for i in şifre:
 if i.isalpha():
  print("%s alfabetik bir karakter dizisidir"%i)
 else:
  print("%s alfabetik bir karakter dizisi degildir"%i)
  break
