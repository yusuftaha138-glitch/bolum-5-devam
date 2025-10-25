meyveler = {"elma", "muz", "çilek", "portakal"}
meyveler2 = {"muz", "kivi", "karpuz", "çilek"}

#sonuc = meyveler[0]d #hata verir çünkü setlerde indexleme yoktur

#for x in meyveler:
#     print(x)

# sonuc = "elma" in meyveler

meyveler.add("ejder meyvesi")
meyveler.update(meyveler2)
meyveler.remove("elma")
meyveler.discard("vişne")  #hata verir
meyveler.discard("muz")
meyveler.pop()
meyveler.clear()

sonuc = meyveler
print(sonuc)


