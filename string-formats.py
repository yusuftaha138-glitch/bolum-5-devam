#string concat
ad = "Yusuf"
soyad = "Dirican"
yas = 25

msj = "My name is " + ad + " " + soyad + " and I am " + str(yas) + " years old."

# string format
msj2 = "My name is {} {} and I am {} years old.".format(ad, soyad, yas)
msj3 = "My name is {0} {1} and I am {2} years old.".format(ad, soyad, yas)
msj4 = "My name is {y} {s} and I am {y} years old.".format(a=ad, s=soyad, y=yas)

# f-string
msj5 = f"My name is {ad} {soyad} and I am {yas} years old."
print(msj)