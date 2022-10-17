### sets ###

from this import d


my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"ivan", "sandoval", 31}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("garcia")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("garcia")
print(my_other_set) # Un set solo accepta repetidos

print("ivan" in my_other_set)
print("iva" in my_other_set)

my_other_set.remove("ivan")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

my_set = {"ivan", "sg", "31"}
my_list = list(my_set)
print (my_list)
print(my_list[0])

my_other_set = {"ando", "1234"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"Java", "C#"}))

print(my_new)