# Dictionary Metodları:

yemekTarifi ={
    "yemekAdi:" "Yağlama"
    "yemekTarifi:" "Tarif açıklaması"
    "resim:" "1.jpg"
}    

# access items
# sonuc = yemekTarifi["yemekAdi"]
# sonuc = yemekTarifi.get("yemekAdi")
# sonuc = yemekTarifi.keys()
# sonuc = yemekTarifi.values()
# sonuc = yemekTarifi.items()

# # update items
# yemekTarifi["yemekAdi"] = "Kısır"
# yemekTarifi.update({"yemekAdi": "Kısır"})
# yemekTarifi.update({"yemekAdi2": "Kısır"})

# #delete items
# yemekTarifi.pop("yemekAdi")
# yemekTarifi.popitem()
yemekTarifi.clear()


