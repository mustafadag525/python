#BİR SAYININ TAM BÖLENLERİNİ BULMA 
def sayinintamboleni(gelensayi):
    tambolenler = []
    toplam=0
    sayac=0
    tumu=[]
    if(gelensayi==0):
        print("Sıfırın tam böleni yoktur")
    elif(gelensayi==1):
        print("1'in tam böleni kendisidir :)")
    else:
        for h in range (2,gelensayi):
            if(gelensayi%h==0):
                tambolenler.append(h)
                toplam+=h
                sayac+=1
                tumu=[tambolenler,toplam,sayac]
        return tumu
 
def asalmi(sayi):
    if(sayi==1):
        return False
    elif(sayi==2):
        return True
    else:
       for i in range(2,sayi):
           if(sayi%i==0):
               return False
       return True
 
while True:
    alinansayi=input("Tam Bölen İçin Sayi giriniz:")
 
    #Eğer sayı değilse except kısmı çalışır.
    try:
        alinansayi = int(alinansayi)
        parcala = sayinintamboleni(alinansayi)
        # BURADAN DİZİ DÖNÜYOR PYTHONDA BUNA LİSTE DENİYOR. BUNU PARÇALAYACAĞIZ
 
        if (alinansayi < 0):
            print("Negatif sayı girmeyiniz")
        elif (alinansayi == 1):
            print("1'in tam böleni kendisidir.")
        elif (asalmi(alinansayi) == True):
            print("Girilen sayı asaldır ve tam böleni 1 ve kendisidir.")
        else:
            tamboluneneler = parcala[0]
            tambolunentoplami = parcala[1]
            kactanetambolunen = parcala[2]
            print(
                "Tam bölen sayilar:{} 'dir.\nTam bölünen Sayilarin toplami:{} 'dir.\n{}'adet tam bölünen sayi vardır.".format(
                    tamboluneneler, tambolunentoplami, kactanetambolunen))
 
    except ValueError:
        print("LÜTFEN SAYI GİRİNİZ.")
