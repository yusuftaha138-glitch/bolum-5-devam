isim = "Yusuf Talha Dirican"

# for harf in isim:
#     if(harf == "i"):
#         continue
#     print(harf)   


i = 0
toplam = 0

while (i <= 100):
    i += 1
    if (i % 2 ==0):
        continue
    toplam += i

print(toplam)