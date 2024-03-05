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
def hesapIslemleri():
    kadi=input("Kullanıcı adı seçin!: ")
    while kadi_olusturmaKontrol(kadi)==False:
        kadi=input("Kullanıcı adınız tamamen harflerden oluşmalı ve 3 ile 15 karakter arasında olmalıdır! Yeniden deneyin \n: ")
    sifre=input("Şifre oluşturun: ")
    while sifre_olusturmaKontrol(sifre)==False:
        sifre=input("Şifreniz 8-20 karakter arasında olmalı, içinde rakam ve büyük harf içermelidir!\n: ")

    print("Kullanıcı adınız ve şifreniz başarıyla oluşturuldu!")
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
            sifrekontrol(girissifre,sifre)
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
def sicilSistemi():
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
hesapIslemleri()
