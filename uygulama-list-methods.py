customers = ["sadikturan", "elif", "ahmet", "john", "doe"]
orders = [12000, 15000, 13000, 16000, 11000]

# orders.append(5000)
# orders.pop()
# name =input("username") + "isimli müşterinin sipariş toplamı " + input("sipariş tutarı") + "liradır"
# print(name)

# Soru 3 için diğer seçenek:

# sonuc = f"{customers[0]} isimli müşterinin sipariş toplamı {orders[4]} liradır."

customers.sort()
orders.sort()
print(customers)
print(orders)

min(orders)
print(min(orders))

sonuc = customers.count("sadikturan")

customers.remove("ahmet")

sonuc = customers.clear()
sonuc = orders.clear()
print(sonuc)

username = input("müsteri adı:")
toplam = input('toplam:')

customers.append(username)
orders.append((toplam))

print(customers)
print(orders)













