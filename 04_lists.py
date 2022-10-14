### Listas ###

from decimal import MIN_ETINY


my_list = list()
my_other_list = []

print(len(my_list))

my_list = [15, 24, 68, 30, 30, 31]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, 'Iván', "SG"]
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list.count("SG"))
print(my_list.count(30))

age, height, name, surname = my_other_list
print(surname)

height, age, name, surname = my_other_list[1], my_other_list[0], my_other_list[2], my_other_list[3]
print(name) 

print(my_list + my_other_list)
#print(my_list - my_other_list) Error


my_other_list.append('Infoblock')
print(my_other_list)

my_other_list.insert(1, 'Azul')
print(my_other_list)

my_other_list[1] = "verde"
print(my_other_list)

my_other_list.remove('verde')
print(my_other_list)

my_list.remove(30)
print(my_list)
# pop() desapila el ultimo elemento de una lista, y lo retorna
print(my_list.pop(1))
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)

my_new_list = my_list.copy()

my_list.clear()
print (my_list)
print (my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])