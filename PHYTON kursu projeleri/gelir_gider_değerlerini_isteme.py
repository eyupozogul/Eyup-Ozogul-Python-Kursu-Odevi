ocak=[]
şubat=[]
mart=[]
nisan=[]
mayıs=[]
haziran=[]
temmuz=[]
ağustos=[]
eylül=[]
ekim=[]
kasım=[]
aralık=[]

ocak1=input("Ocak ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
ocak1=ocak1.split()
ocak+=ocak1

şubat1=input("Şubat ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
şubat1=şubat1.split(" ")
şubat+=şubat1

mart1=input("Mart ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
mart1=mart1.split(" ")
mart+=mart1

nisan1=input("Nisan ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
nisan1=nisan1.split(" ")
nisan+=nisan1

mayıs1=input("Mayıs ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
mayıs1=mayıs1.split(" ")
mayıs+=mayıs1

haziran1=input("Haziran ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
haziran1=haziran1.split(" ")
haziran+=haziran1

temmuz1=input("Temmuz ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
tammuz1=temmuz1.split(" ")
temmuz+=temmuz1

ağustos1=input("Ağustos ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
ağustos1=ağustos1.split(" ")
ağustos+=ağustos1

eylül1=input("Eylül ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
eylül1=eylül1.split(" ")
eylül+=eylül1

ekim1=input("Ekim ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
ekim1=ekim1.split(" ")
ekim+=ekim1

kasım1=input("Kasım ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
kasım1=kasım1.split(" ")
kasım+=kasım1

aralık1=input("Aralık ayının elektrik su doğalgaz giderleri ve geliri boşluk bırakarak yazınız!")
aralık1=aralık1.split(" ")
aralık+=aralık1

ay=input("Hangi ayın verisini isterdiniz:")
ay=ay.lower()
veri=int(input("elektrik:1 su:2 doğalgaz:3 gelir:4 :"))

if ay=="ocak":
    print(ocak[veri-1])

elif ay=="şubat":
    print(şubat[veri-1])

elif ay == "mart":
    print(mart[veri - 1])

elif ay == "nisan":
    print(nisan[veri - 1])

elif ay == "mayıs":
    print(mayıs[veri - 1])

elif ay == "haziran":
    print(haziran[veri - 1])

elif ay == "temmuz":
    print(temmuz[veri - 1])

elif ay == "ağustos":
    print(ağustos[veri - 1])

elif ay == "eylül":
    print(eylül[veri - 1])

elif ay == "ekim":
    print(ekim[veri - 1])

elif ay == "kasım":
    print(kasım[veri - 1])

elif ay == "aralık":
    print(aralık[veri - 1])