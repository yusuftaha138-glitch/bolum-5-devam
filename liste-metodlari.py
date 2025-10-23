sayilar = [4,6,8,2,56,78,90]
isimler = ["ahmet","mehmet","ismet","saffet"]

sonuc =min(sayilar)
sonuc =max(isimler)
sonuc =min(isimler)
sonuc =max(sayilar)

# ekleme

sayilar.append(12)
isimler.append("zeynep")

sonuc = sayilar
sonuc = isimler
sayilar.insert(0,100)
sayilar.insert(-1,100)
sayilar.insert(-3,100)
sayilar.insert(len(sayilar), 200)

# silme
sayilar.pop()  
sayilar.pop(0)
isimler.remove("ismet")

# sıralama
sayilar.sort()
isimler.sort()
sayilar.reverse()

sonuc =sayilar.count(100)
sonuc =isimler.count("ahmet")

# arama
sonuc = sayilar.index(56)
sonuc = isimler.index("saffet")

sonuc = sayilar
sonuc = isimler


print(sonuc)
