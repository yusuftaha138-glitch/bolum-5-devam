my_list = [1,2,3]
my_tuple = (1,2,3) #değiştirilemez

print(type(my_list))
print(type(my_tuple))

my_list[0] = 2
# my_tuple[0] = 2 #hata verir

my_list.append(3)
# my_tuple.append(4) #hata verir

my_list.count(2)
print(my_list.count(2))

my_tuple2 = tuple([2,3,4])