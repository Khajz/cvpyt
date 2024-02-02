def sayihata(x):
    try: int(x)
    except ValueError: return False
    else:
        if int(x)<=0: return False
        else: return True
def liste_olustur():
    x=input("""
Yapılacaklar listesine hoşgeldin!
Bugün kaç tane görevin var?: """)
    while sayihata(x)==False:
        x=input("Yanlış değer girdiniz, tekrar deneyin: ")
        
    for i in range(int(x)):
        sira=i+1
        gorev=input(f"{sira}.Görevinizi yazın: ")
        if gorev=="":
            break
        yapilacaklar.append(gorev)
    liste()
def liste_gorev_isaretle():
    if len(yapilacaklar)<1:
            print("İlk başta bir liste oluşturmalısınız!")
    else:
        liste()
        x=input("Hangi görevi yaptın?: ")
        while sayihata(x)==False or int(x)>len(yapilacaklar):
            x=input("Yanlış girdiniz tekrar deneyin: ")
        yapilanlar.append(yapilacaklar[int(x)-1]) 
        yapilacaklar.remove(yapilacaklar[int(x)-1])
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
        input("Ana menüye dönmek için bir tuşa bas")
def liste_gorev_ekle():
    if len(yapilacaklar)<1:
        print("İlk başta bir liste oluşturmalısınız!")
    else:
        x=input("Listeye kaç görev eklemek istiyorsun?: ")
        while sayihata(x)==False:
            x=input("Yanlış sayı girdiniz, tekrar deneyin: ")
        for i in range(int(x)):
            gorev=input("Görevinizi yazın: ")
            if gorev=="":
                break
            yapilacaklar.append(gorev)

        liste()
        input("Ana menüye dönmek için bir tuşa bas")
def liste_gorev_cikar():
        if len(yapilacaklar)<1:
            print("İlk başta bir liste oluşturmalısınız!")
        else:          
            x=input("Kaç tane görev çıkarmak istiyorsunuz?: ")
            while sayihata(x)==False or int(x)>len(yapilacaklar):
                x=input("Yanlış girdiniz tekrar deneyin: ")
            for i in range(int(x)):
                liste()
                y=input("Çıkarmak istediğiniz görevin numarasını giriniz: ")
                if y=="":
                    break
                while sayihata(y)==False or int(y)>len(yapilacaklar):
                    y=input("Yanlış girdiniz tekrar deneyin: ")
                yapilacaklar.remove(yapilacaklar[int(y)-1])
                liste()
            input("Ana menüye dönmek için bir tuşa bas")
def liste():
    sira=0
    print("--LİSTE---")
    for gorevler in yapilacaklar:
        sira=sira+1
        print(f"{sira}.{gorevler}")
    if len(yapilacaklar)<=0:
        print("Tebrikler tüm görevleri yaptınız!")
  
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
