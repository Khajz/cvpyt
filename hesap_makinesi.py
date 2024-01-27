def toplama(x,y):
    print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
def cikarma(x,y):
    print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
def carpma(x,y):
    print(f"{sayi1} x {sayi2} = {sayi1 * sayi2}")
def bolme(x,y):
    print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
def karesi(x):
    print(f"{sayi} sayısının karesi = {sayi**2}")
def karekoku(x):
    print(f"{sayi} sayısının karekökü = {sayi**0.5}")
def istenenkuv(x,y):
    print(f"{sayi} sayısının {kuvvet} olan kuvveti = {sayi**kuvvet}")    
def faktoriyel():
    faktoriyel = 1
    for i in range(1,sayi+1):
        faktoriyel*=i
    print(f"{sayi}!={faktoriyel}")
        
    
    
    
    
    
print("""
    Hesap Makinesine Hoşgeldiniz
      --------------------------
    |                           |
    | 1.Toplama                 |
    |                           |
    | 2.Çıkarma                 |
    |                           |
    | 3.Çarpma                  |
    |                           |
    | 4.Bölme                   |
    |                           |
    | 5.Karesini Alma           |
    |                           |
    | 6.Karekökünü Alma         |
    |                           |
    | 7.İstenen Kuvveti Alma    |
    |                           |
    | 8.Faktoriyel              |
    |                           |
    | 9.Sıcaklık Dönüşümleri    |
     ---------------------------""")
while True:
    islem = input("İşlem Seçiniz(1,2,3,4,5,6,7,8,9):   ")
    if islem == '1':
        sayi1=float(input("1.Sayıyı Giriniz:    "))
        sayi2=float(input("2.Sayıyı Giriniz:    "))
        toplama(sayi1,sayi2)
    elif islem == '2':
        sayi1=float(input("1.Sayıyı Giriniz:    "))
        sayi2=float(input("2.Sayıyı Giriniz:    "))
        cikarma(sayi1,sayi2)
    elif islem == '3':
        sayi1=float(input("1.Sayıyı Giriniz:    "))
        sayi2=float(input("2.Sayıyı Giriniz:    "))
        carpma(sayi1,sayi2)
    elif islem == '4':
        sayi1=float(input("1.Sayıyı Giriniz:    "))
        sayi2=float(input("2.Sayıyı Giriniz:    "))
        bolme(sayi1,sayi2)
    elif islem == '5':
        sayi=float(input("Karesini almak istediğiniz sayıyı giriniz:    "))
        karesi(sayi)
    elif islem == '6':
        sayi=float(input("Karekökünü almak istediğiniz sayıyı giriniz:  "))
        karekoku(sayi)
    elif islem == '7':
        sayi=float(input("Kuvvetini almak istediğiniz sayıyı giriniz:   "))
        kuvvet=float(input("Kuvveti Giriniz:    "))
        istenenkuv(sayi,kuvvet)
    elif islem == '8':
        sayi=int(input("Faktöriyelini istediğiniz sayıyı giriniz: "))
        faktoriyel()
    elif islem == '9':
        def fahr_celc():
            f=int(input("Celciusa çevirmek istediğiniz Fahrenhayt derecesini giriniz: "))
            c=(f-32)/1.8
            print(f"{f} Fahrenhayt {round(c)} Celciusa eşittir!")
        def celc_fahr():
            c=int(input("Fahrenhayta çevirmek istediğiniz Celcius'u giriniz: "))
            f=(c*9/5)+32
            print(f"{c} Celcius {round(f)} Fahrenhayta eşittir!")
        def fahr_kelv():
            f=int(input("Kelvine çevirmek istediğiniz Fahrenhayt derecesini giriniz: "))
            c=(f-32)/1.8
            k=c+273.15
            print(f"{f} Fahrenhayt {k} Kelvine eşittir!")
        def celc_kelv():
            c=int(input("Kelvine çevirmek istediğiniz Celcius'u giriniz: "))
            k=c+273.15
            print(f"{c} Celcius {k} Kelvine eşittir!")

        secim=input("""
-----SICAKLIK DÖNÜŞÜM PROGRAMI-----
    1.Fahr-Celc
    2.Celc-Fahr
    3.Fahr-Kelv
    4.Celc-Kelv
-------SEÇİM YAPINIZ(1/2/3/4)------
""")

        while True:
            if secim=='1':
                fahr_celc()
                break
            elif secim=='2':
                celc_fahr()
                break
            elif secim=='3':
                fahr_kelv()
                break
            elif secim=='4':
                celc_kelv
                break
            else:
                secim=input("Yanlış seçtiniz, tekrar deneyin! (1/2/3/4): ")
    else: print("1,2,3,4,5,6,7,8 ya da 9u seçmeliydiniz!")
    devam = input("İşleme devam etmek ister misin? (E/H):   ")
    if devam.upper() == 'H':
        break