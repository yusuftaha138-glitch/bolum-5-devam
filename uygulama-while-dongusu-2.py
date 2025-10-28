# Klavyede girilen n sayıdaki öğrenci bilgisini liste içerisinde saklaynız.
# ** dictionary listesi yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyad) şeklinde olsun. 
# ** Ürün ekleme işlemi bittiğinde öğrencileri isteleyiniz.

devammi = "e"
ogrenciler = []

while (devammi != "h"):
    ogrenciNo = input("öğrenci no: ")
    ogrenciAdi = input("öğrenci adı: ")
    ogrenciSoyad = input("öğrenci soyad: ")

    ogrenciler.append({
        "ogrenciNo" : ogrenciNo,
        "ogrenciAd" : ogrenciAdi,
        "ogrenciSoyad" : ogrenciSoyad
    })

    devammi = input("devam mı? (e/h): ")

for ogrenci in ogrenciler:
    print(f"{ogrenci[ "ogrenciNo"]} numaralı öğrencinin adı {ogrenci["ogrenciAd"]} {ogrenci ["ogrenciSoyad"]}")

