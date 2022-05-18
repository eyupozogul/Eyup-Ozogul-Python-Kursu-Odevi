import random

sayi = random.randint(1,1000)
sayac = 0

while True:

    tahmin1 = int(input("İlk tahmininizi giriniz:"))
    tahmin2 = int(input("İkinci tahmininizi giriniz:"))
    tahmin3 = int(input("Üçüncü tahmininizi giriniz:"))
    toptahmin = tahmin1 + tahmin2 + tahmin3

    sayac+=1

    if toptahmin > sayi:
        print("Daha küçük bir toplam giriniz!")
        print()
    elif toptahmin < sayi:
        print("Daha büyük bir toplam giriniz!")
        print()
    else:
        print("Tebrikler doğro bildiniz!")
        print(f"{sayac} tahminde bildiniz!")
        break