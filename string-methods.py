mesaj = "BTK Akademi Python Kursu" 

sonuc = mesaj.upper()  # Tüm karakterleri büyük harfe çevirir   
sonuc = mesaj.lower()  # Tüm karakterleri küçük harfe çevirir
sonuc = mesaj.title()  # Her kelimenin ilk harfini büyük yapar
sonuc = mesaj.capitalize()  # Sadece ilk harfi büyük yapar
sonuc = "abc".isupper()

sonuc = mesaj.strip()
sonuc = mesaj.split()
sonuc = mesaj.index('akademi')  # 'akademi' kelimesinin başladığı indexi verir
sonuc = mesaj.find('Python')  # 'Python' kelimesinin başladığı index
sonuc = mesaj.replace('Python', 'Javasvript')  # 'Python' kelimesini 'Java' ile değiştirir

print(sonuc)  