# Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin : 39.35
# dizel :41.71
# lpg: 20.28

# benzinFiyat = 39.35
# dizelFiyat = 41.71
# lpgFiyat = 20.28

# toplamYakitUcreti = 0
# ortalamaTakitTuketimi = float(input("100 km'deki ortalama yakit tüketimi: "))
# gidilecekYol = float(input("Gidilen mesafe: "))
# yakitTipi = input("Yakıt tipi :")

# toplamYakitTuketimi = gidilecekYol * (ortalamaTakitTuketimi / 100)

# if(yakitTipi == "benzin"):
#     toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi
# elif(yakitTipi == "dizel"):
#     toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi
# elif(yakitTipi == "lpg"):
#     toplamYakitUcreti = lpgFiyat * toplamYakitTuketimi
# else:
#     print("yanlış yakıt tipi")

# if(toplamYakitUcreti != 0):
#     print(toplamYakitUcreti)

# Soru 2:
#Bir öğrencinnin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız. 

yazili1 = int(input("İlk yazılıyı giriniz: "))
yazii2 = int(input("2. yazılıyı giriniz: "))
sozlu = int(input("Sözlü notunu giriniz"))

ortalama =(yazili1 + yazii2 + sozlu) / 3

if(0 <= ortalama <= 24):
    print(f"ortalaman: {ortalama} ve değerlendrme notu:0")
elif(25 <= ortalama <= 44):
    print(f"ortalaman: {ortalama} ve değerlendrme notu: 1")
elif(45 <= ortalama <= 54):
    print(f"ortalaman: {ortalama} ve değerlendrme notu:2")
elif(55 <= ortalama <= 69):
    print(f"ortalamanız: {ortalama} ve değerlendrme notu: 3")
elif(70 <= ortalama <= 84):
    print(f"ortalamanız: {ortalama} ve değerlendrme notu: 4")
elif(85 <= ortalama <= 100):
    print(f"ortalamanız: {ortalama} ve değerlendrme notu: 5")
else:
    print("yanlış not girdiniz")