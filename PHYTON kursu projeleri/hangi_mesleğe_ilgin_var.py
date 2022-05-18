import random

sorular=["Turistlerle konuşmaya çalışmak veya onlara rehberlik etmek","Yeni duyduğu yabancı kelime için sözlüğe bakmak","Dil öğrenmenin pratik yollarını araştırmak","Farklı dillerdeki ortak kelimeleri bulmaya çalışmak","Yabancı müzik ve filmlere ilgi duymak","Gazetelerden, internetten veya televizyondan günlük haberleri takip etmek","Söz söyleme ve ikna etme kabiliyetine sahip olma","Çeşitli toplulukların sosyal yapılarını incelemek","Çeşitli konularda düşüncelerini yazılı olarak ifade etmek","Münazaralara katılmak","Matematiksel hesaplara ilgi duymak","Bir binanın mimari özelliklerini incelemek","Programlama dillerini öğrenip bilgisayarda özel programlar yazmak","Elektronik cihazların aslında nasıl çalıştığını araştırmak","Evdeki eşyaların yerleştirilmesinde önerilerde bulunmak","İnsan vücudunun işleyişini incelemek","Diş sağlığına önem vermek","Alınan ilaçların prospektüsünü okumak","Hayvanlarla ilgilenmek","Laboratuvarda deney yapmak"]
puanlar=[1,1,1,1,1,10,10,10,10,10,100,100,100,100,100,1000,1000,1000,1000,1000]
sorular2=sorular
puanlar2=puanlar
yapılanlar=[]
sayaç=0
puan=0
sorusayı=19

print()
print("Testimiz 20 sorudan oluşmaktadır. Yazılan cümle sizi anlatıyorsa Evet(E) anlatmıyorsa Hayır(H) yazınız.")
print("Bu sunuçlara göre hangi alanlara ilginizin olduğunu öğreneceksiniz.")
print()

for i in range(20):
    soruno=random.randint(0,sorusayı)
    print(sorular[soruno])
    cevap=input("Cevabınızı giriniz(E/H):")
    print()
    cevap=cevap.upper()
    del sorular2[soruno]
    sorusayı-=1
    if cevap=="E":
        puan+=puanlar2[soruno]
    del puanlar2[soruno]

if puan==0:
    print("Sizin hiçbir alana ilginiz yoktur!")
elif puan<6:
    print("Sizin yabancı dil öğretmenliği veya mütercim tercümanlığı gibi alanlara ilginiz vardır!")
elif puan<51:
    print("Sizin hukuk, gazetecilik, yazarlık veya sosyoloji gibi alanlara ilginiz vardır!")
elif puan<501:
    print("Sizin mühendislik, mimarlık veya matematik gibi alanlara ilginiz vardır!")
elif puan<5001:
    print("Sizin tıp, eczacılık, diş hekimliği veya veterinerlik gibi alanlara ilginiz vardır!")
elif puan>5000:
    print("Sen aklına koyduğun her şeyi başarırsın. Çünkü senin inanılmaz bir gücün var!")
