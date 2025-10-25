# sehirler = ["Istanbul", "Ankara", "Izmir", "Bursa"]
# plakalar = [34, 6, 35, 16]

# # key - value 

# print(plakalar[0], sehirler[0])
# print(plakalar[1], sehirler[1])

# print(plakalar[sehirler.index("Istanbul")])
# print(plakalar[sehirler.index("Ankara")])

# dictionary

plakalar = {
    "kocaeli": 41,
    "istanbul": 34, 
    "malatya": 44,
}
(plakalar["malatya"]) = 44

plakalar["ankara"] = 6

print(plakalar["kocaeli"])
print(plakalar["istanbul"])
print(plakalar["malatya"])