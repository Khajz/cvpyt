def liste_olustur():
    x=input("""
Yapılacaklar listesine hoşgeldin!
Bugün kaç tane görevin var?: """)
    while x<='0':
        x=input("Hm çok az o, tekrar dene: ")

    for i in range(int(x)):
        sira=i+1
        gorev=input(f"{sira}.Görevinizi yazın: ")
        yapilacaklar.append(gorev)
    print("---GÖREVLER---")
    sira=0
    for gorevler in yapilacaklar:
        sira+=1
        print(f"{sira}.{gorevler}")
def liste_gorev_isaretle():
    if len(yapilacaklar)<1:
            print("İlk başta bir liste oluşturmalısınız!")
    else:
        sira=0
        print("---GÖREVLER---")
        for gorevler in yapilacaklar:
            sira=sira+1
            print(f"""{sira}.{gorevler}""")
        x=int(input("Hangi görevi yaptın?: "))
        while x>len(yapilacaklar):
            x=int(input("Yanlış girdiniz tekrar deneyin: "))
        yapilanlar.append(yapilacaklar[x-1]) 
        yapilacaklar.remove(yapilacaklar[x-1])
        sira=0
        print("---Kalan Görevler---")
        for gorevler in yapilacaklar:
            sira=sira+1
            print(f"""{sira}.{gorevler}""")
        sira=0
        print("---Yapılan Görevler---")
        for gorevler in yapilanlar:
            sira=sira+1
            print(f"""{sira}.{gorevler} YAPILDI""")
        if len(yapilacaklar)==0:
            print("TEBRİKLER! Tüm görevlerini yaptın!1")
        input("Ana menüye dönmek için bir tuşa bas")
def liste_gorev_ekle():
    if len(yapilacaklar)<1:
        print("İlk başta bir liste oluşturmalısınız!")
    else:
        x=int(input("Listeye kaç görev eklemek istiyorsun?: "))
        for i in range(x):
            gorev=input("Görevinizi yazın: ")
            yapilacaklar.append(gorev)
            sira=0
        print("---YENİ LİSTE---")
        for gorevler in yapilacaklar:
            sira=sira+1
            print(f"{sira}.{gorevler}")
        input("Ana menüye dönmek için bir tuşa bas")
def liste_gorev_cikar():
        if len(yapilacaklar)<1:
            print("İlk başta bir liste oluşturmalısınız!")
        else:          
            x=int(input("Kaç tane görev çıkarmak istiyorsunuz?: "))
            while x>len(yapilacaklar) or x<=0:
                x=int(input("Yanlış girdiniz tekrar deneyin: "))
            for i in range(x):
                sira=0
                print("---Kalan Görevler---")
                for gorevler in yapilacaklar:
                    sira=sira+1
                    print(f"{sira}.{gorevler}")
                y=int(input("Çıkarmak istediğiniz görevin numarasını giriniz: "))
                while y>len(yapilacaklar):
                    y=int(input("Yanlış girdiniz tekrar deneyin: "))
                yapilacaklar.remove(yapilacaklar[y-1])
                sira=0
                print("--YENİ LİSTE---")
                for gorevler in yapilacaklar:
                    sira=sira+1
                    print(f"{sira}.{gorevler}")
            input("Ana menüye dönmek için bir tuşa bas")

yapilacaklar=[]
yapilanlar=[]

while True:
    print("""
---YAPILAKACAKLAR LİSTESİ---
1.Yeni Liste Oluştur
2.Varolan listede bir görevi yapıldı işaretle
3.Varolan listeye görev eklemesi yap
4.Varolan listeden görev çıkar
5.Çıkış yap(Veriler kaybolur)
Seçim Yap(1/2/3/4/5) """)
    a=input("")

    if a=='1':
        liste_olustur()
    elif a=='2':
        liste_gorev_isaretle()
    elif a=='3':
        liste_gorev_ekle()
    elif a=='4':
        liste_gorev_cikar()
    elif a=='5':
        print("Çıkış yapılıyor! Bir tuşa basın")
        input("")
        break
    else:
        print("Yanlış seçim yaptınız(1/2/3/4/5): ")