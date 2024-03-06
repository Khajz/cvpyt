def kadi_olusturmaKontrol(kadi): #Kullanıcı adı oluşturma kriterleri
    if len(kadi)<3 or len(kadi)>15:
        return False
    try: int(kadi)
    except ValueError: return True
    else: return False
def sifre_olusturmaKontrol(sifre): #Şifre oluşturma kriterleri
    if len(sifre)<8 or len(sifre)>20:
        return False
    if sifre.lower()==sifre:
        return False
    return any(karakter.isdigit() for karakter in sifre)
def sifrekontrol(girissifre,sifre): #Girilen şifre ile mevcut şifrenin aynı olup olmamasına bakıyor
    for i in range(4):
        if girissifre!=sifre and i<4:
            girissifre=input(f"Şifrenizi yanlış girdiniz! Tekrar giriniz kalan hak {4-i}: ")
        if girissifre!=sifre and i==3:
            print("Giriş Başarısız, sistem kapanıyor!")
        if girissifre==sifre and i<4:
            print("Doğrulama başarılı!")
            return True
def secimkontrol(secim): #Seçim menüsünü kontrol ediyor
    if secim!="1" and secim!="2" and secim!="3" and secim!="4":
        return False
def hesapOlustur():
    global kadi
    global sifre
    kadi=input("Kullanıcı adı oluşturun!: ")
    while kadi_olusturmaKontrol(kadi)==False:
        kadi=input("Kullanıcı adınız tamamen harflerden oluşmalı ve 3 ile 15 karakter arasında olmalıdır! Yeniden deneyin \n: ")
    if kadi=="hile": sicilSistemi()
    sifre=input("Şifre oluşturun: ")
    while sifre_olusturmaKontrol(sifre)==False:
        sifre=input("Şifreniz 8-20 karakter arasında olmalı, içinde rakam ve büyük harf içermelidir!\n: ")

    print("Kullanıcı adınız ve şifreniz başarıyla oluşturuldu!")
    hesapIslemleri()
def hesapIslemleri():
    global kadi
    global sifre
    while True:
        print("1.Giriş Yap \n2.Kullanıcı Adını Değiştir\n3.Şifreni Değiştir\n4.Çıkış Yap(Veriler Kaybolur)")
        secim=str(input("Seçim Yapınız(1/2/3/4): "))
        while secimkontrol(secim)==False:
            secim=input("Yanlış seçim yaptınız tekrar deneyin(1/2/3/4): ")
        if secim=="1":
            giriskadi=input("Kullanıcı adınızı girin!: ")
            while giriskadi!=kadi:
                giriskadi=input("Kullanıcı adınızı yanlış girdiniz, tekrar girin!: ")
            girissifre=input("Şifrenizi girin!: ")

            if sifrekontrol(girissifre,sifre)==True:
                sicilSistemi()
            break
        elif secim=="2":
            girissifre=input("Şifrenizi doğrulayın!: ")
            if sifrekontrol(girissifre,sifre)==True:
                yenikadi=input("Yeni kullanıcı adınızı girin!: ")
                while kadi_olusturmaKontrol(yenikadi)==False or yenikadi==kadi:
                    yenikadi=input("Yeni kullanıcı adınız 3 ile 15 karakter arasında olmalıdır ve eskisiyle aynı olmamalıdır! Yeniden deneyin \n: ")
                kadi=yenikadi
                print(f"Yeni kullanıcı adınız başarıyla oluşturuldu! {kadi}")
        elif secim=="3":
            girissifre=input("Şuanki şifrenizi doğrulayın!: ")
            if sifrekontrol(girissifre,sifre)==True:
                yenisifre=input("Yeni şifrenizi girin: ")
                while sifre_olusturmaKontrol(yenisifre)==False or yenisifre==sifre:
                    yenisifre=input("Yeni şifreniz 8 ile 20 karakter arasında olmalı, büyük harf ve rakam içermeli, eskisi ile aynı olmamalıdır! Tekrar deneyin\n: ")
                sifre=yenisifre
                print("Yeni şifreniz başarıyla oluşturuldu!")
        elif secim=="4":
            break                
def sicilSistemieski():
    sicil=[]
    adlar=[]
    maaslar=[]
    for i in range(3):
        sira=i+1
        sicilno=input(f"{sira}. Kişinin sicilnosunu girin!: ")
        sicil.append(sicilno.upper())
        ad=input(f"{sira}. Kişinin ismini ve soyismini girin!: ")
        adlar.append(ad.capitalize())
        maas=input(f"{sira}. Kişinin maaşını giriniz!: ")
        maaslar.append(maas)
    print(sicil)
    secim=input("Kimin Sicilini görmek istiyorsun?: ")
    ysecim=secim.upper()
    while True:
        if ysecim not in sicil:
            ysecim=input("Yanlış girdiniz, tekrar deneyin!: ")
        else: break
    x=sicil.index(ysecim)
    print(f"Sicil no: {sicil[int(x)]}")
    print(f"İsim: {adlar[int(x)]}")
    print(f"Maaşı: {maaslar[int(x)]}")
    input()
def sicilSistemi():
    global hsecim

    sicilNo=[]
    isimList=[]
    maasList=[]

    def sayiKontrol(sayi):
        try: int(sayi)
        except ValueError: return False
        else: return True
    

    def sicilMenu():
        global hsecim
        print("\nSicil sistemine hoşgeldiniz! Yapmak istediğiniz işlemi seçiniz:\n1.Sicil Tablosu Ekle\n2.Varolan Tabloya Sicil Ekle\n3.Varolan Tablodaki Sicili Sil\n4.Sicillere Bak\n5.Hesap Ayarları")
        hsecim=input("")
        if hsecim=="1":
            sicilOlustur()
        elif hsecim=="2":
            sicilEkle()
        elif hsecim=="3":
            sicilSil()
        elif hsecim=="4":
            sicilBak()
        elif hsecim=="5":
            hesapIslemleri()
        else: 
            while hsecim!="1" and hsecim!="2" and hsecim!="3" and hsecim!="4" and hsecim!="5":
                hsecim=input("Yanlış seçtiniz! Tekrar deneyin (1/2/3/4)")
    def sicilOlustur():
        x=input("Kaç tane sicil ekleyeceksin?: ")
        while sayiKontrol(x)==False or int(x)<=0:
            x=input("Yanlış girdiniz: ")
        for i in range(1,int(x)+1):
            sira=i
            sicil=input(f"{sira}. Kişinin Sicil No'sunu giriniz: ")
            sicilNo.append(sicil.upper())
            if sicil=="":break
            
            isim=input(f"{sira}. Kişinin ismini giriniz: ")
            while sayiKontrol(isim)==True or len(isim)<3 or len(isim)>35:
                isim=input("İsim rakam içeremez!, tekrar deneyin: ")
            isimList.append(isim)
            maas=input(f"{sira}. Kişinin maaşını giriniz: ")
            while sayiKontrol(maas)==False or len(maas)<5:
                maas=input(f"Maaş harf içeremez!, tekrar deneyin:")
            maasList.append(maas)
    def sicilEkle():
        if len(sicilNo)<=0:
            print("Önce bir liste oluşturmalısın!")
        else:
            x=input("Kaç tane sicil ekleyeceksin?: ")
            while sayiKontrol(x)==False or int(x)<=0:
                x=input("Geçerli Bir Sayı giriniz: ")
            for i in range(1,int(x)+1):
                sira=i
                sicil=input(f"{sira}. Kişinin Sicil No'sunu giriniz: ")
                sicilNo.append(sicil)
                if sicil=="":break
            
                isim=input(f"{sira}. Kişinin ismini giriniz: ")
                while sayiKontrol(isim)==True or len(isim)<3 or len(isim)>35:
                    isim=input("İsim rakam içeremez!, tekrar deneyin: ")
                isimList.append(isim)
                maas=input(f"{sira}. Kişinin maaşını giriniz: ")
                while sayiKontrol(maas)==False or len(maas)<5:
                    maas=input(f"Maaş harf içeremez ve 5 harften uzun olmalıdır!, tekrar deneyin:")
                maasList.append(maas)
    def sicilSil():
        if len(sicilNo)<=0:print("Önce bir liste oluşturmalısın!")
        else:
            x=input("Kaç tane sicil sileceksin?: ")
            while sayiKontrol==False or int(x)<=0 or int(x)>len(sicilNo):
                x=input("Geçerli bir sayı giriniz!: ")
            
            for i in range(int(x)):
                print(sicilNo)
                secim=input("Silmek istediğiniz sicilNo'sunu girin: ")
                while secim not in sicilNo:
                    secim=input("Yanlış sicil girdiniz! Tekrar deneyin: ")
                isecim=sicilNo.index(secim)
                sicilNo.pop(isecim)
                isimList.pop(isecim)
                maasList.pop(isecim)
    def sicilBak():
        if len(sicilNo)<=0:print("Önce bir liste oluşturmalısın!: ")
        else:
            print("---SİCİL LİSTESİ---")
            sira=len(sicilNo)
            for sicil in sicilNo:
                print(f"Sicil:{sicil} -")
                print(f"İsim:{isimList[sira-1]}")
                print(f"Maaş:{maasList[sira-1]}")
                sira-=1
                if sira==0:break
                print("\n")
            print("------------------")
                
    while True:     
        sicilMenu()
        if hsecim=="5":break
hesapOlustur()
