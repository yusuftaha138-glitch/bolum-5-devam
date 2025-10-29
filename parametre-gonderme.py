# def selamlalama(isim):
#     return "Merhaba, " + isim

# print(selamlalama("Yusuf"))


def yasHesapla(dogumYili):
    return (2024 - dogumYili)

# print(yasHesapla(2001))

def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    kalanSure = 65 - yas

    if kalanSure > 0:
        return f"{isim}, emekliliğinize {kalanSure} yıl kaldı."
    else:
        return f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz. "
print(emekliligeKacYilKaldi(2001,"Yuduf Talha"))