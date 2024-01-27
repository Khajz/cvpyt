def gkontrol(gun):
    if len(gun)<2 or gun<='00' or gun>'31':
        return False
    else: return True
def akontrol(ay):
    if len(ay)<2 or ay<='00' or ay>'12':
        return False
    else: return True
def ykontrol(yil):
    if len(yil)<4 or yil<'1940' or yil>'2023':
        return False
    else: return True
def islemler(gun,ay,yil):
    toplam=int(gun[0])+int(gun[1])+int(ay[0])+int(ay[1])+int(yil[0])+int(yil[1])+int(yil[2])+int(yil[3])
    if toplam>9 and toplam!=11 or toplam>9 and toplam!=22:
        strtoplam=str(toplam)
        toplam=int(strtoplam[0])+int(strtoplam[1])
    return toplam
def aciklamayaz(aciklama):
    if toplam==1:
        aciklama==print("1: Numeroloji sisteminde 1 sayısının anlamı; Bağımsızlık, yaratıcılık, kendine düşkünlük, ego olarak ifade edilir. Kişi hem kendine yeterli hem de tam bir liderdir. Yani liderliği temsil eder. İş yaşamında acelecilik, aşırılık ve hükmedici davranışlardan kaçınması kişi adına fayda sağlayabilir.")
    elif toplam==2:
        aciklama==print("2: Kişilik özellikler; bağımlılık, aşırı duyarlılık, kavrama ve tasarım, iş birlik anlayışı ve sezgi yeteneği gelişmiştir. Kişi sevgi dolu, eleştirici ve barış yanlısı, ideal ortaktır. Detaylara takılmaktan ve yalnızlıktan kaçınmalıdır.")
    elif toplam==3:
        aciklama==print("3: Numerolojide 3 rakamı; sosyal, arkadaş canlısı, sanata yatkın, iyimser, ziyankarlık, yüzeysellik anlamlarına gelir. Dışa dönük bir kişidir. Yaşamı ve eğlenceyi sever. Oldukça yaratıcı ve duyarlıdır. Rutini sevmez. Kendine disiplin uygulamayı benimsemesi gerekir.")
    elif toplam==4:
        aciklama==print("4: Numerolojide 4 sayısı sağlam, pratik, uygulayıcı, bükülmez ve sıkı bir çalışan anlamına gelir. Her konuda başarıyı yakalamak ister. Candan ve iyi bir arkadaş olma konusunda yardıma ihtiyacı vardır. Aşırı güvenlik duygusuna kapılmamalıdır.")
    elif toplam==5:
        aciklama==print("5: Özgürlük, gezginlik, uyum kabiliyeti, değişkenlik gibi karakteristik özellikler numerolojide bu rakamın karşılığı olarak bilinmektedir. İkna edici bir kişiliğe sahiptir ve cesur bir kişiliktir. Can sıkıntısı olumsuz etkiler. Amacından kolayca sapması söz konusudur.")
    elif toplam==6:
        aciklama==print("6: Anlayış, aşk, sorumluluk, kıskançlık, her işe müdahale etmek gibi özelliklere sahiptir. Oldukça sıcak, koruyucu ve mutlu bir kişiliğe sahiptir. Sevdikleri için fedakarlık yapmaktan çekinmez. Sağlam ve güvenilir bir yapısı bulunur. Kendini kötümser bir ruh haline sokmaktan ve başkaları tarafından istismar edilen duygularından arınmış olmalıdır.")
    elif toplam==7:
        aciklama==print("7: Bu rakam; sır saklama, zeka, ruhsallık ve baskıcılığı ifade eder. Düşünür bir kişiliğe sahiptir. Değişken ve eksantriktir. Mesafeli ve soğuk olmaktan kaçınmalıdır. Ayrıca iyi şeylere sahip olmama duygusu ve yalnızlıktan kaçınmalıdır.")
    elif toplam==8:
        aciklama==print("8: Organizasyon yeteneğine sahip, güçlü, yönetici ruha sahip ve oldukça adildir. Sonuca giden bir kişiliğe sahiptir. Bu bağlamda her zaman kararlı ve güçlü yapısı ile ön plana çıkmaktadır. Özellikle maddi konularda başarılıdır. Hedefinin karşısında gördüğü kişilere karşı duygusuzca davranmaktan kaçınması gerekir.")
    elif toplam==9:
        aciklama==print("9: Hümanist, romantik, şefkatli, duygusal, sanatkar, sezgili, duyarlı, yaratıcı ve konforuna düşkündür. Kendini anlatmak adına tüm dünya ile savaşabilir. Kötü alışkanlıklarından arınmak ve yaşamın küçük detaylarından olumsuz etkilenmemek adına gayret göstermesi gerekir.")
    elif toplam==11:
        aciklama==print("11: Duyarlı, fanatik ve sezgi gücü yüksektir. Ayrıca keşif yeteneğine sahiptir. Öngörülü ve hayalci bir kişiliğe sahiptir. Bilinç üstü gelişmiştir ve sanatkardır. Aşırı duyarlılık ve gerginlik halinden uzak durmalıdır.")
    elif toplam==22:
        aciklama==print("22: Numerolojide 22 rakamının anlamı; maddi alanda üstün, zenginliğe kolay ulaşabilen, oldukça pratik bir idealist olarak tanımlanır. Amacına doğru ilerler ve eli çabuktur. Düşünce tarzı globaldir. Geleceğe fazla düşünmekten kaçınmalıdır.")
gun=input("Doğum gününüzü giriniz: ")
while gkontrol(gun)==False:
    gun=input("Doğum gününüzü yanlış girdiniz, tekrar giriniz: ")
ay=input("Doğum ayınızı giriniz: ")
while akontrol(ay)==False:
    ay=input("Doğum ayınızı yanlış girdiniz, tekrar giriniz: ")
yil=input("Doğum yılınızı giriniz: ")
while ykontrol(yil)==False:
    yil=input("Doğum yılınızı yanlış girdiniz, tekrar giriniz: ")
toplam=islemler(gun,ay,yil)
aciklama=aciklamayaz(toplam)

