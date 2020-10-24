def tam_bolen(sayı):
    tam_bolen=[]
    for i in range(1,sayı):
        if sayı%i==0:
            tam_bolen.append(i)
    return tam_bolen
while True:
    sayı=int(input("sayı gir:"))
    print("tam bölenleri:",tam_bolen(sayı))
