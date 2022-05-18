import random

KARAKTERLER=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0",".",",",":",";","!","#","+","$","%","/","^","&","/","{","\"","(","[",")","]","=","}","?","*","\\","_","@","<",">","|","'"]

sifre=random.sample(KARAKTERLER,16)

yenisifre=""
for i in sifre:
    yenisifre+=i

print(f"16 hanelik şifreniz {yenisifre} dir")