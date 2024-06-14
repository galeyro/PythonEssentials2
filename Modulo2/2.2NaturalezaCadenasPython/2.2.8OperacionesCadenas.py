"min()"

#Esta función encuentra el elemento mínimo de la secuencia pasada como argumento.
print("\nmin()-------------\n")
# Demonstración de min() - Ejemplo 1:
print(min("aAbByYzZ")) #El mínimo es A debido a que las mayúsculas tienen un valor menor que las minúsculas en la tabla ASCII.


# Demonstración de min() - Ejemplos 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(t) + ']') #El mínimo es un espacio en blanco.

t = [0, 1, 2]
print(min(t)) #El mínimo es 0.

"max()"
print("\nmax()-------------\n")
# encuentra el elemento máximo de la secuencia.

# Demostración de max() - Ejemplo 1:
print(max("aAbByYzZ"))


# Demostración de max() - Ejemplo 2 y 3:

t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + max(t) + ']') #el máximo es u
#print(ord(max(t)))

t = [0, 1, 2]
print(max(t))#El máximo es 2.

"index()"
#El método index() (es un método, no una función) busca la secuencia desde el principio, para encontrar el primer elemento del valor especificado en su argumento.

#Nota: el elemento buscado debe aparecer en la secuencia, su ausencia causará una excepción ValueError.

print("\nindex()-------------\n")
# Demonstración del método index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

"list()"
#La función list() toma su argumento (una cadena) y crea una nueva lista que contiene todos los caracteres de la cadena, uno por elemento de la lista.

#Nota: no es estrictamente una función de cadenas, list() es capaz de crear una nueva lista de muchas otras entidades (por ejemplo, de tuplas y diccionarios).
print("\nlist()-------------\n")
# Demostración de la función list():
print(list("abcabc"))

"count()"
#El método count() cuenta todas las apariciones del elemento dentro de la secuencia. La ausencia de tal elemento no causa ningún problema.
print("\ncount()-------------\n")
# Demostración del método count():
print("abcabc".count("b"))
print('abcabc'.count("d"))
