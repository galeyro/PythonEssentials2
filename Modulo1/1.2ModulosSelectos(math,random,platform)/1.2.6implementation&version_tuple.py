#permite saber que version de python se está ejecutando

from platform import python_implementation, python_version_tuple

print(python_implementation())#devuelve una cadena que denota la implementacion de Python que se está ejecutando

for atr in python_version_tuple():#Devuelve una tupla de tres elementos la cual contiene: la versión principal, la versión secundaria y la versión de parche de Python.
    print(atr)