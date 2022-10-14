### Tuplas conjunto de valores ###

from operator import index


my_tuple = tuple()
my_other_tuple = ()

my_other_tuple = (12, 32, 32, 45, 23, 42, 123, 32, 32)
my_tuple = (53, 1.75, 'ivan', 'SG')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('ivan')) # cuenta el numero de incidencias
print(my_tuple.index('ivan')) #regresa el numero de pocision 

# my_tuple[1] = 1.80 

my_sum_tuple = my_other_tuple + my_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)

del my_sum_tuple