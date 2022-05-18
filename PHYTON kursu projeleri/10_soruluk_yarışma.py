import random

sorular=["Atatürk kaç yılında doğmuştur?","Atatürk kaç yılında vefat etmiştir?","Atatürk'e Kemal ismini kim vermiştir?","Atatürk kaç yılında Samsun'a çıkmıştır?","İlk Çağ uygarlıklarından hangisi yazıyı icat etmiştir?","Dünya Sağlık Örgütünün kısaltılmış ismi nedir?","Bir sebepten dolayı tek kulağına küpe takan Osmanlı padişahı kimdir?","Çanakkale Zaferi’nin dahil olduğu savaş hangisidir?","Türkiye’nin sahip olduğu uluslararası telefon kodu nedir?","İkinci Dünya Savaşında hangi ülkeye atom bombası atılmıştır?","Türkiye’nin en yüksek dağı hangisidir?","Kaç yılda bir Şubat ayı 29 çeker?","Voleybol nerede icat edildi?","Çin seddi nerededir?","LGS sınavı kaç sorudan oluşur?","Aspirinin ilk kez çıkış yılı nedir?","Romen rakamında hangi sayı yoktur?"," Aspirinin hammaddesi nedir?","“Sinekli Bakkal” romanının yazarı aşağıdakilerden hangisidir?","Dünya'nın en kalabalık ülkesi hangisidir?"]
şıklar=["A)1880 B)1881 C)1882 D)1883","A)1936 B)1937 C)1938 D)1939","A)matematik öğretmeni B)annesi C)babası D)arkadaşları","A)1916 B)1917 C)1918 D)1919","A)Sümerler B)babiller C)Hititler D)İyonlar","A)Uhw B)Unıcef C)Who D)Nato","A)Kanuni Sultan Süleyman B)Yavuz Sultan Selim C)Orhan Bey D)Fatih Sultan Mehmet","A)1.Dünya savaşı B)2.Dünya savaşı C)3.Dünya savaşı D)Balkan savaşları","A)+59 B)+219 C)+90 D)+61","A)Çin B)Amerika C)Mısır D)Japonya","A)Ağrı dağı B)Uludağ C)Toroslar D)Küre dağları","A)3 B)4 C)5 D)6","A)Amerika B)Türkiye C)Fransa D)İngiltere","A)Hindistan B)İtalya C)Çin D)Japonya","A)80 B)90 C)100 D)120","A)1889 B)2009 C)2019 D)1899","A)0 B)10 C)100 D)500","A)Söğüt B)Köknar C)Kavak D)Meşe","A)Reşat Nuri Güntekin B)Halide Edip Adıvar C)Ziya Gökalp D)Ömer Seyfettin","A)Hindistan B)Çin C)Rusya D)Amerika"]
cevaplar=["B","C","A","D","A","C","B","A","C","D","A","B","A","C","B","D","A","A","B","B"]
doğrular=[]
yanlışlar=[]
boşlar=[]
yapılanlar=[]
sayaç=0

isim=input("İsminizi giriniz:")
print(f"Hoşgeldiniz {isim}! Testimiz 10 sorudan oluşmakta ve her doğru cevap +10 puandır.")

while sayaç<10:
    soruno=random.randint(0,19)
    if soruno not in yapılanlar:
        print(sayaç+1, ")", sorular[soruno])
        print(şıklar[soruno])
        cevap=input("Cevabı giriniz:")
        yapılanlar.append(soruno)
        sayaç+=1
        cevap=cevap.upper()
        if cevap==cevaplar[soruno]:
            print(f"Tebrikler {isim} doğru yaptınız!")
            doğrular.append(sorular[soruno])
        elif cevap=="":
            boşlar.append(sorular[soruno])
        else:
            print(f"Maalesef {isim} yanlış yaptınız!")
            print(f"Doğru cevap {cevaplar[soruno]} !")
            yanlışlar.append(sorular[soruno])
        print()

toppuan=len(doğrular)*10

print(f"Toplam puanınız: {toppuan}")
print(f"Doğru yaptığınız sorular: {doğrular}")
print(f"yanlış yaptığınız sorular: {yanlışlar}")
print(f"Boş bıraktığınız sorular: {boşlar}")