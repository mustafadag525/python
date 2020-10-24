print ("KİŞİYE ÖZEL NOT TUTMA SİSTEMİ ")
print ("Sorulara evet veya hayır ile cevap veriniz!")
a = input("Kayıt olmak istiyor musunuz:")
while (a == "evet"):
   defkullanici = input ("Kullanıcı adını giriniz:")
   defparola = input ("Parolayı giriniz:")
   defparola1=input ("Parolayı tekrar giriniz:")
   if (defparola == defparola1):
       print ("Kayıt İşlemi Başarı İle Gerçekleştirildi.")
       tercih0 = input ("Giriş yapmak istiyor musunuz ? :")
       if (tercih0 == "evet"):
           girdi1 = input ("Kullanıcı adınızı giriniz:")
           girdi2 = input ("Şifrenizi giriniz:")
           if (girdi1 == defkullanici) and (girdi2 == defparola):
               print ("Giriş işleminiz başarı ile sonuçlandı")
               tercih1 =   input ("Not Sistemine girmek istiyor musunuz ? :")
               if (tercih1 == "evet"):
                   notlar = input("Eklemek istediğiniz notları giriniz:")
                   tercih2 =input ("Notları görüntülemek istiyor musunuz ? :")
                   if tercih2 == "evet":
                       print (notlar)
                       print ("Notlarınız bundan ibarettir.")
                       break
                   elif tercih2 == "hayır":
                       print ("Tercihiniz hayır olarak algılandı.")
                       print ("Programdan çıkılıyor....")
                       break
               elif (tercih1 != "evet") and tercih1=="hayır":
                   print ("Tercihiniz hayır olarak algılandı.")
                   print ("Programdan çıkılıyor....")
                   break
           else:
               print ("Parolanızı veya kullanıcı adınızı yanlış girdiniz.")
               print ("Programdan çıkılıyor....")
               break
       if (tercih0 == "hayır"):
           print("Tercihiniz hayır olarak algılandı.")
           print ("Programdan çıkılıyor...")
           break
       else:
           print ("Tanımlanamayan girdi alındı...")
           print ("İşlem sonlandırıldı...")
           break
   else:
       print("Uyuşmayan parola lütfen tekrar deneyiniz.")
if (a== "hayır"):
   print ("Programdan çıkış yapılıyor...")
else:
  print ("Kullandığınız için teşşekürler.")
  print ("Programdan çıkılıyor!...")

