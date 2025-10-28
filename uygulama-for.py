sayilar = [3,5,7,12,32,45]

# 1- sayilar listesindeki her bir elemanı yazdır

# for x in sayilar:
#     print(x)

# 2- "sayilar" listesinde hangi sayılar 3'ü katıdır

# for x in sayilar:
#     if x % 3 == 0:
#         print(x)

# 3- "sayilar" listesinde tüm saıların toplamı nedir ?

# toplam = 0
# for x in sayilar:
#     toplam += x
# print(toplam)

urunler = ["samsung s24","samsung s22","iphone 15","iphone 14 "]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz (find,index)

# for x in urunler:
#     index = x.find("iphone")
#     if index > -1:
#         print(x)
   


# 5- "urunler" listesinde kaç adet samsung ürünü vardır ?

# adet = 0
# for x in urunler:
#     index = x.find("samsung")
#     if index > -1:
#         adet += 1
# print(adet)

urunler = [
    {"urunAdi": "hp victus", "fiyat": 32999},
    {"urunAdi": "lenovo thinkpad", "fiyat": 25499},
    {"urunAdi": "Apple Macbook", "fiyat": 49999},
    {"urunAdi": "huawei matebook", "fiyat": 26999},
    {"urunAdi": "casper nirvana", "fiyat": 20000},
]

# Soru 1- 
# Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
    #"Hp victus marka ürünün fiyatı 32999 Türk Lirası"

# for urun in urunler:
#     print(f"{urun['urunAdi']} marka ürünün fiyatı {urun['fiyat']} Türk Lirası")

# # Soru 2-
# # Ürünlerin fiyat toplamı nedir ?

# toplam = 0
# for x in urunler:
#     toplam += x["fiyat"]
# print(f"ürün toplamı: {toplam}")

# Soru 2-
# 25000 ile 40000 arasındaki ürünleri listeleyiniz.

# for urun in urunler:
#     if (urun["fiyat"] >=25000 and urun["fiyat"] <= 40000):
#         print(f"{urun["urunAdi"]}")

# 4- Kullanıcıdan aınan anahtar kelimeye göre ürünleri listeyiniz.

kelime = input("aramak istediğiniz ürün: ")

for urun in urunler:
    if(urun["urunAdi"].lower().find(kelime.lower())> -1):
        print(f"{urun['urunAdi']}")