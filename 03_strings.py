### Strings ###

from platform import python_branch
from re import A


my_strings = "Mi string"
my_other_string = "Mi otro strings"

print(len (my_other_string))
print(len (my_strings))
print(my_strings + " " + my_other_string)

my_new_line_strings = "Esta es un String\ncon salto de linea"
print(my_new_line_strings)

my_new_new_line_strings = "\tEsta es un String con tabulacion"
print(my_new_new_line_strings)

# Formateo

name, surname, alias, age = "Ivan", "Sandoval", "Sagi", 31

print("mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("mi nombre es %s %s y mi edad es %d" %(name, surname, age))
#print(f"mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de datos 

languaje = "python"
a, b, c, d, e, f, = languaje
print(a)
print(b)

# Division 

languaje_slice = languaje[1:3]
print(languaje_slice)

languaje_slice = languaje[1:4]
print(languaje_slice)

languaje_slice = languaje[-2]
print(languaje_slice)

languaje_slice = languaje[0:6:4]
print(languaje_slice)

# Reverse 

reverse_lenguaje = languaje[::-1]
print(reverse_lenguaje)

# Fuciones del sistema

print(languaje.capitalize())
print(languaje.upper())
print(languaje.count("t"))
print("1".isnumeric())
print(languaje.lower())
print(languaje.upper().isupper())
print(languaje.startswith("py"))