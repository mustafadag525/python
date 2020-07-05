import random
min_fark = 101
s2 = 201
while True:
    s1 = random.randint(1,100)
    print("{}    ".format(s1))
    gecici = s2 - s1
    if gecici < 0:
        gecici = gecici * -1
    if gecici <= min_fark:
        min_fark = gecici
        min1 = s1
        min2 = s2
    s2 = s1
    if (s1 >= 70 and s1 <= 75):
        break;
print("\nMinimum fark: {}" .format(min_fark))
print("\nSayi 1: {}, Sayi 2: {}".format(min1,min2))
