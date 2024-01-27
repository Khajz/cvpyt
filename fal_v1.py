def kgun(gun):
    if len(gun)!=2 or gun=='00' or gun<'0':
        return False
    elif gun>'31':
        return False
    else:
        return True
def kay(ay):
    if len(ay)!=2 or ay=='00' or ay<'0':
        return False
    elif ay>'12':
        return False
    else:
        return True
def kyil(yil):
    if len(yil)!=4 or yil<'1950' or yil>'2023':
        return False
    else:
        return True
def stopla(gun,ay,yil):
    tyil=int(yil[0]+yil[1])+int(yil[2]+yil[3])
    thepsi=(int(gun)+int(ay)+int(tyil))%22
    sayi=thepsi
    return sayi
def aciklamayaz(aciklama):
    if sayi==0: aciklama="0 – Joker: Riskleri alma, açık fikirlilik, içindeki sesi dinleme."
    elif sayi==1: aciklama="I – Büyücü: Yetenek, özgüven, yaratıcı olma, beceri,"
    elif sayi==2: aciklama="II – Azize: Oluşuna bırakabilme ve sezgisel güç."
    elif sayi==3: aciklama="III – Kraliçe: Dişil güç ve bilgelik, yenilik, güzellik, doğanın gücü."
    elif sayi==4: aciklama="IV – Kral: Nizam, otorite, düzen, liderlik, maddi başarı, azim, irade, eril güç."
    elif sayi==5: aciklama="V – Aziz: Erdem, güven, maneviyat, anlamsal arayış."
    elif sayi==6: aciklama="VI – Aşıklar: Duygusal verilen karar, kendini sevme, yol ayrımı."
    elif sayi==7: aciklama="VII – Savaş Arabası: Bilinç kazanma, hedefe yönelme, deneyim kazanma, zorlukların ve çelişkilerin üstesinden gelme."
    elif sayi==8: aciklama="VIII – Güç: Arzu, tutku, öz farkındalık, hayvansal doğamızla uzlaşma."
    elif sayi==9: aciklama="IX – Ermiş: İç dönme, dış etkenlerden soyutlanma, içsel huzur, kendini bulma."
    elif sayi==10: aciklama="X – Kader Çarkı: Kendi hayatının sorumluluğunu üstlenme, büyüme, olgunlaşma, yolunda gitmeyen olaylar ve durumlar."
    elif sayi==11: aciklama="XI – Adalet: Denge, dürüstlük, objektif bakış, adalet."
    elif sayi==12: aciklama="XII – Asılmış Adam: Yeni bir görüş edinme, yeni görüşü kazanmak için eskisini feda etme, zorunlu dinlenme, yeniye teslim olma."
    elif sayi==13: aciklama="XIII – Ölüm: Eskinin sona ermesi ve yeninin doğuşu, yaşamın devamlılığı, ayrılık."
    elif sayi==14: aciklama="XIV – Denge: Denge, çevreyle uzlaşma, uyum, kişinin kendisiyle barışması, kararlılık."
    elif sayi==15: aciklama="XV – Şeytan: Kişinin kendisyle yüzleşmesi, bağımlılık, maddi güce bağımlı olma meyletme, iyi niyet yoksunluğu"
    elif sayi==16: aciklama="XVI – Yıkılan Kule: Eski güvendiğimiz şeylerin yıkılması ve yeni için yer açılması. Bilinir olandan özgürleşmek, öz farkındalık"
    elif sayi==17: aciklama="XVII – Yıldız: Beklenti, umut, öteyi kavrayış, kendine güven, yaşam enerjisi."
    elif sayi==18: aciklama="XVIII – Ay: Umutsuzluk, belirsizlik, endişe, korku, kabus, iç karartıcı öz seziler, bilinmeyenle yüzleşme."
    elif sayi==19: aciklama="XIX – Güneş: İyimserlik, sevecenlik, başarı, yaşama sevinci, yaratıcılık, öz güven."
    elif sayi==20: aciklama="XX – Mahkeme: Kendini bulma, özgürleşme, umut tohumlarının yeşermesi, kurtuluş, bilincin uyanışı, değişim sürecinin olumlu tamamlanması."
    elif sayi==21: aciklama="XXI – Dünya: Kendimizi bulma yolunda atacağımız önemli adımlara işaret eder. Kişinin kendisiyle ve evrenle bütünleşmesi. Hedefe ulaşma, uyum, mutluluk, başarı."
    return aciklama

gun=input("Doğum gününüzü giriniz: ")
while kgun(gun)==False:
    gun=input("Doğum gününüzü yanlış girdiniz, tekrar giriniz: ")
ay=input("Doğum ayınızı giriniz: ")
while kay(ay)==False:
    ay=input("Doğum ayınızı yanlış girdiniz, tekrar deneyiniz: ")
yil=input("Görmek istediğiniz yılı giriniz: ")
while kyil(yil)==False:
    yil=input("Yılı yanlış girdiniz, tekrar deneyiniz: ")

sayi=stopla(gun,ay,yil)
aciklama=aciklamayaz(sayi)
print(f"Sayınız: {sayi}, anlamı:")
print(aciklama)
input("Çıkmak için bir tuşa basınız.")

        