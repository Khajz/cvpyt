def yeni_oyun():
    tahminler=[]
    dogru_tahminler=0
    soru_no=1
    for key in sorular:
        print("-----------------")
        print(key)
        for i in cevaplar[soru_no-1]:
            print(i)
        tahmin=input("Soruyu cevaplayın(A/B/C/D): ")
        tahmin=tahmin.upper()
        tahminler.append(tahmin)
    
        dogru_tahminler+=cvp_kontrol(sorular.get(key), tahmin)
        soru_no+=1
        
    skor_hesap(dogru_tahminler,tahminler)
    
def cvp_kontrol(cevaplar,tahmin):
    if cevaplar==tahmin:
        print("DOĞRU CEVAP")
        return 1
    else:
        print("Cevabınız Yanlış!")
        return 0

def skor_hesap(dogru_tahminler,tahminler):
    print("-----------------")
    print("SONUÇLAR")
    print("-----------------")
    
    print("Cevaplar:", end=" ")
    for i in sorular:
        print(sorular.get(i),end=" ")
    print()
    print("Tahminler:", end=" ")
    for i in tahminler:
        print(i,end=" ")
    print()
    
    skor=int((dogru_tahminler/len(sorular))*100)
    print("Skorunuz: %",str(skor))
def yeniden_oyna():
    yanit=input("Tekrar oynamak ister misin?(E/H): ")
    yanit=yanit.upper()
    if yanit=="E":
        return True
    else:
        return False
    

sorular = {
    "1.Türkiye'nin başkenti neresidir?":"A",
    "2.07 Plaka nolu şehrimiz hangisidir?":"D",
    "3.İlk darbe ne zaman olmuştur?":"C",
    "4.1994 Cumhurbaşkanımız kimdir?":"B"
    
}

cevaplar = [["A-Ankara B-İstabul C-Antalya D-Bayburt"],
            ["A-Balıkesir B-Kastamonu C-Afyon D-Antalya"],
            ["A-1980 B-1951 C-1960 D-2016"],
            ["A-Necmettin ERBAKAN B-Tansu ÇİLLER C-Bülent ECEVİT D-Muharrem İNCE"]]

yeni_oyun()

while yeniden_oyna():
    yeni_oyun()
print("Güle güle! :)")