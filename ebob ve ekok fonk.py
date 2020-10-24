def ekok_bulma(sayı1,sayı2):
    
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i


        elif (sayı1 % i ==  0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i


        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    return ekok

sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:",ekok_bulma(sayı1,sayı2))


#############################################
def ebob_bulma(sayı1,sayı2):
    
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2 ):

        if ( not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob
sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:",ebob_bulma(sayı1,sayı2))
