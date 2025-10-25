# Aşağıdaki öğrenci bilgilerini dictioonary listesinde saklayınız.    
    # 101 Yiğit Bilgi 2010 (40,80,90)
    # 102 Ada Bilgi 2012 (80,80,80)
    # 103 Çınar Turan 2017 (70,70,70)

ogrenciler = {
    101: {
        "ad": "Yiğit",
        "soyad": "Bilgi",
        "dogum_yili": 2010,
        "notlar": [40, 80, 90]
    },
    102: {
        "ad": "Ada",
        "soyad": "Bilgi",
        "dogum_yili": 2012,
        "notlar": [80, 80, 80]
    },
    103: {
        "ad": "Çınar",
        "soyad": "Turan",
        "dogum_yili": 2017,
        "notlar": [70, 70, 70]
    }
}     

# Klavyeden girilen öğrenci numarasına göre aşağıdaki cümleyi yazdırınız
  # 101 numaralı Yiğit Bilgi ismindeki öğrencini yaşı 14 ve not ortalaması 70.

ogrenciNo = int(input("Öğrenci no: ")) 
ogrenciler =ogrenciler[ogrenciNo]
ortalama = ogrenciler["notlar"][0] + ogrenciler["notlar"][1] + ogrenciler["notlar"][2]/ 3

print(f"{ogrenciNo} numaralı {ogrenciler['ad']} {ogrenciler['soyad']} ismindeki öğrencinin yaşı {2024 - ogrenciler['dogum_yili']} ve not ortalaması {ortalama}.")