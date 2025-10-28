# 1- Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve değerler arasındaki tüm çift sayıları yazdırınız.

# baslangic = int(input("başlangıç"))
# bitis = int(input("bitiş: "))

# i= baslangic

# while(i< bitis):
#     if(i % 2 == 0):
#         print(i)
#     i += 1

# 2- (1 100) arasındaki değerleri azalan şekilde yazdırınız.

# x = 100
# while (x > 0):
#     print(x)
#     x -= 1


# Alınan 5 sayıyı ekranda sıralı bir şekilde yazdır.

# sayilar = []
# i= 0

# while (i < 5):
#     sayi = int(input("sayi: "))
#     sayilar.append(sayi)
#     i += 1

# sayilar.sort
# print(sayilar)

# 4- Klaveyden girişi istenen username bilgisi için boşluk girldiği süreve tekrar username girişi isteyiniz.

username = ""

while not username:
    username = input("kullanıcı adı")
print("girilen username" + username)


