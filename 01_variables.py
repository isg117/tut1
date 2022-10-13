# Variables en snake case
my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable) 
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_int_variable, my_bool_variable)
print( "Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema

print(len(my_string_variable))

# Variables en una sola linea ¡No abusar de esta syntaxis!
name, surname, alias, age = "Ivan", "Sandoval", "Sagi", 31
print("me llamo", name,"Mi aplellido", surname, "Tengo" "y mi alias es", alias )

# Inputs
"""
first_name = input('What is your name? ')
age = input("How old are you? ")
print(first_name)
print(age)
"""

# Cambiar tipo

name = 31
age = "Iván"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi direccion "
address = 32
print(address)
print(type(address))