programlama_dilleri = ["Python", "Java", "C++", "JavaScript", "Ruby"]

sonuc = programlama_dilleri
sonuc = type(programlama_dilleri)
sonuc = programlama_dilleri[:2]
sonuc = programlama_dilleri[:]
sonuc = programlama_dilleri[-3:-1]
sonuc = programlama_dilleri[-3:]

# güncelleme
programlama_dilleri[-1] = "Php"

sonuc = programlama_dilleri
sonuc = len(programlama_dilleri)
sonuc = programlama_dilleri + ["Go", "Delphi"]

sonuc = "Python" in programlama_dilleri
sonuc = "React" in programlama_dilleri

del programlama_dilleri[0]

for dil in programlama_dilleri:
    print(dil)

