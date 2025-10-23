markalar = ["Toyota", "Bmw", "Renault", "Mercedes"]

print(len(markalar))  

sonuc = markalar
print(sonuc [0]+ " " + sonuc [3])

markalar[2] = "Togg"
print(markalar)

"Togg" in markalar
print("Togg" in markalar)

markalar[:2]

sonuc = markalar + ["Ford", "Citroen"]
print(sonuc)

del markalar[-1]
print(markalar)

ogrenci1 = ["Yiğit","Bilgi", 2010 , [70,80,90]]
ogrenci2 = ["Sena","Turan", 2012 , [60,80,70]]
ogrenci3 = ["Ahmet","Sezer", 2009 , [80,90,70]]

ogrenciler = [ogrenci1, ogrenci2, ogrenci3]

yasYiğit = 2024 - ogrenciler[0][2]
yasSena = 2024 - ogrenciler[1][2]
yasAhmet = 2024 - ogrenciler[2][2]

print(yasYiğit, yasSena, yasAhmet)

notOrtYiğit = sum(ogrenciler[0][3]) / len(ogrenciler[0][3])
notOrtSena = sum(ogrenciler[1][3]) / len(ogrenciler[1][3])
notOrtAhmet = sum(ogrenciler[2][3]) / len(ogrenciler[2][3])
print(notOrtYiğit, notOrtSena, notOrtAhmet)



