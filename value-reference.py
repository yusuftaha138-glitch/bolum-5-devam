# value types
# x = 10
# y = 20
# x = y
# y = 30
# print(x,y)

a = ["elma", "armut"]
b = ["elma", "armut"]

a = b # adres kopyalandı.
a[0] = "çilek"
print(a,b)

# liste kopyalama
listeA = [10,20]
# listeB = listeA.copy() # birinci yöntem
# listeB = list(listeA) # ikinci yöntem
listeB = listeA[:] # üçüncü yöntem

listeB[0] = 30
print(listeA,listeB)