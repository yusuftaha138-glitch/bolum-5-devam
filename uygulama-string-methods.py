kursAdi = "Btk Akademi Python ile Programlama Dersleri"
website = "https://www.btkakademi.gov.tr/"

#  1- ' Btk Akademi ' ifadesinin başındaki ve sonundaki boşlukları silin
sonuc = kursAdi.strip()
print(sonuc)
# 2- kursAdi değişkenindeki tüm karakterleri küçük harfe çevirin 
souc = kursAdi.lower()
# 3- website değikeninde kaç tane '.' karakteri vardır ?
adet = website.count('.')
print(adet)
# 4- website değişkeni 'https' ile mi başlıyor ?
baslangic =website.startswith('https')
print(baslangic)

# 5- website değişkeni 'tr' ile mi bitiyor ?
bitis = website.endswith('tr')
print(bitis)
# 6- kursAdi değişkenindeki karakterlerin hepsi harf mi ?
sonuc = kursAdi.isalpha()
print(sonuc)
# 7- kursAdi değişkenindeki tüm boşlukları '-' ile değiştirin
sonuc = kursAdi.replace(' ', '-')
print(sonuc)
# 8- kursAdi değişkenindeki Python kelimesini ReactJs ile değiştirin
sonuc = kursAdi.replace('Python', 'ReactJs')
print(sonuc)
# 9- website değişkei 'www' içeriyor mu ?
iceritorMu = website.find('www') # karakteri bulamazsa -1 döner
iceritorMu = website.index('www') #karakteri bulamazsa hata gönderir
print(iceritorMu)
# 10- kursAdi değişkenini listeye çevirin
sonuc = kursAdi.split()
print(sonuc)